"""Importador de CSV de LinkedIn Analytics al modelo común (ADR-0001).

- Flexible con los nombres de columna (mayúsculas, espacios, alias en ES/EN).
- Celda vacía -> None (desconocido), nunca 0.
- Idempotente por (post_key, measured_at, source): repetir el mismo
  fichero no duplica observaciones.
"""

from __future__ import annotations

import csv
from datetime import datetime, timezone
from pathlib import Path

from . import paths
from .store import load_catalog, load_observations, post_key_for, save_catalog, save_observations

SOURCE_DEFAULT = "linkedin_analytics_csv"

# Alias de columnas: nombre normalizado -> campo del modelo.
ALIASES = {
    "post_urn": ["post_urn", "urn", "post urn"],
    "source_post_id": ["source_post_id", "post_id", "post id", "id", "url", "post_url", "post url", "link", "permalink"],
    "published_at": ["published_at", "published", "created", "created_at", "date", "fecha", "fecha_publicacion"],
    "format": ["format", "formato", "type", "tipo"],
    "topic": ["topic", "tema"],
    "objective": ["objective", "objetivo"],
    "status": ["status", "estado"],
    "duration_seconds": ["duration_seconds", "duration", "duracion", "duración"],
    "reactions": ["reactions", "likes", "reacciones", "me_gusta"],
    "comments": ["comments", "comentarios"],
    "reposts": ["reposts", "repost", "shares", "compartidos"],
    "impressions": ["impressions", "impresiones"],
    "clicks": ["clicks", "clics"],
    "followers_gained": ["followers_gained", "followers", "seguidores", "new_followers"],
}

METRIC_FIELDS = ["reactions", "comments", "reposts", "impressions", "clicks", "followers_gained"]


def _norm_header(name: str) -> str:
    return " ".join((name or "").strip().lower().replace("_", " ").split())


def _build_index(headers: list[str]) -> dict[str, int]:
    normed = {_norm_header(h): i for i, h in enumerate(headers)}
    index: dict[str, int] = {}
    for field, aliases in ALIASES.items():
        for alias in aliases:
            key = _norm_header(alias)
            if key in normed:
                index[field] = normed[key]
                break
    return index


def _to_number(raw: str | None):
    if raw is None:
        return None
    text = raw.strip().replace("\u202f", "").replace(" ", "")
    if text == "" or text.lower() in {"n/a", "na", "null", "none", "-"}:
        return None
    text = text.replace(",", ".") if text.count(",") == 1 and "." not in text else text.replace(",", "")
    try:
        return int(text)
    except ValueError:
        pass
    try:
        value = float(text)
    except ValueError:
        return None
    return int(value) if value.is_integer() else value


def _to_text(raw: str | None):
    if raw is None:
        return None
    text = raw.strip()
    return text if text != "" else None


def _parse_age_hours(published_at: str | None, measured_at: str) -> float | None:
    if not published_at:
        return None
    try:
        pub = datetime.fromisoformat(published_at.replace("Z", "+00:00"))
        meas = datetime.fromisoformat(measured_at.replace("Z", "+00:00"))
    except ValueError:
        return None
    if pub.tzinfo is None:
        pub = pub.replace(tzinfo=timezone.utc)
    if meas.tzinfo is None:
        meas = meas.replace(tzinfo=timezone.utc)
    return round((meas - pub).total_seconds() / 3600, 1)


def import_csv(
    csv_path: str | Path,
    *,
    measured_at: str | None = None,
    source: str = SOURCE_DEFAULT,
    only_recent_days: int | None = None,
    dry_run: bool = False,
) -> dict:
    """Importa un CSV y devuelve resumen {added, skipped_duplicate, skipped_out_of_scope, posts}."""
    csv_path = Path(csv_path)
    if not csv_path.exists():
        raise FileNotFoundError(f"No existe el fichero: {csv_path}")

    if measured_at is None:
        measured_at = datetime.now(timezone.utc).isoformat(timespec="seconds")

    with open(csv_path, newline="", encoding="utf-8-sig") as fh:
        reader = csv.DictReader(fh)
        if not reader.fieldnames:
            raise ValueError("El CSV no tiene cabecera.")
        index = _build_index(reader.fieldnames)
        rows = list(reader)
        headers = reader.fieldnames

    def cell(row: dict, field: str):
        if field not in index:
            return None
        return row.get(headers[index[field]])

    catalog = load_catalog()
    observations = load_observations()
    existing_keys = {(o.get("post_key"), o.get("measured_at"), o.get("source")) for o in observations}

    # Publicaciones evergreen ya conocidas (para la ventana de 90 días).
    evergreen = {k for k, p in catalog.items() if isinstance(p, dict) and p.get("status") == "evergreen"}

    added, skipped_dup, skipped_scope = 0, 0, 0
    now = datetime.now(timezone.utc)

    for row in rows:
        post_urn = _to_text(cell(row, "post_urn"))
        source_post_id = _to_text(cell(row, "source_post_id"))
        published_at = _to_text(cell(row, "published_at"))
        key = post_key_for(post_urn, source_post_id, published_at)
        if key in (None, ""):
            skipped_scope += 1
            continue

        if only_recent_days is not None and key not in evergreen:
            try:
                pub = datetime.fromisoformat((published_at or "").replace("Z", "+00:00"))
                if pub.tzinfo is None:
                    pub = pub.replace(tzinfo=timezone.utc)
                if (now - pub).days > only_recent_days:
                    skipped_scope += 1
                    continue
            except ValueError:
                pass  # Sin fecha válida no se excluye: se importa y se revisa a mano.

        dedup = (key, measured_at, source)
        if dedup in existing_keys:
            skipped_dup += 1
            continue

        obs: dict = {
            "post_key": key,
            "post_urn": post_urn,
            "source_post_id": source_post_id,
            "published_at": published_at,
            "measured_at": measured_at,
            "age_hours": _parse_age_hours(published_at, measured_at),
            "source": source,
            "source_file": csv_path.name,
        }
        for field in METRIC_FIELDS:
            obs[field] = _to_number(cell(row, field))

        if key not in catalog:
            catalog[key] = {
                "post_urn": post_urn,
                "source_post_id": source_post_id,
                "published_at": published_at,
                "format": _to_text(cell(row, "format")),
                "topic": _to_text(cell(row, "topic")),
                "objective": _to_text(cell(row, "objective")),
                "duration_seconds": _to_number(cell(row, "duration_seconds")),
                "status": _to_text(cell(row, "status")) or "active",
            }

        observations.append(obs)
        existing_keys.add(dedup)
        added += 1

    if not dry_run and added:
        paths.ensure_dirs()
        save_catalog(catalog)
        save_observations(observations)

    return {
        "added": added,
        "skipped_duplicate": skipped_dup,
        "skipped_out_of_scope": skipped_scope,
        "posts": len(catalog),
        "measured_at": measured_at,
        "source": source,
    }
