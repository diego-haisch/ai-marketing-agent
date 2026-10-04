"""Fuente MCP: snapshot vía el MCP server lanzado desde terminal (sin agente).

Flujo: CLI -> (stdio JSON-RPC) -> `npx @isteam/linkedin-mcp` -> API de LinkedIn.
Necesita `LINKEDIN_ACCESS_TOKEN` válido. `LINKEDIN_PERSON_ID` se resuelve
solo vía `/v2/userinfo` si falta.

Límites honestos: si LinkedIn deniega un permiso (p. ej. listar posts sin
`r_member_social`), el error 403 se propaga como MCPError con mensaje claro;
el CSV sigue siendo la vía alternativa para esos datos.
"""

from __future__ import annotations

import json
import os
import re
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

from . import paths
from .mcp_client import MCPClient, MCPError
from .store import load_catalog, load_observations, post_key_for, save_catalog, save_observations

SOURCE_MCP = "linkedin_mcp"
MCP_COMMAND = ["npx", "-y", "@isteam/linkedin-mcp"]
USERINFO_URL = "https://api.linkedin.com/v2/userinfo"

URN_RE = re.compile(r"urn:li:(?:share|ugcPost|activity):[A-Za-z0-9_-]+")

# Etiquetas habituales en respuestas de texto -> campo del modelo.
LABEL_MAP = {
    "reactions": ["reactions", "likes", "reacciones"],
    "comments": ["comments", "comentarios"],
    "reposts": ["reposts", "shares", "compartidos"],
    "impressions": ["impressions", "impresiones"],
    "clicks": ["clicks", "clics"],
    "followers_gained": ["followers", "seguidores"],
}


def load_env(repo_root: Path | None = None) -> dict[str, str]:
    """Variables de entorno con `.env` del repo como base (el entorno manda)."""
    env: dict[str, str] = {}
    dotenv = (repo_root or paths.REPO_ROOT) / ".env"
    if dotenv.exists():
        for line in dotenv.read_text(encoding="utf-8").splitlines():
            m = re.match(r"\s*(?:export\s+)?([A-Za-z_]+)=(.*)", line.strip())
            if m:
                env[m.group(1)] = m.group(2).strip().strip('"').strip("'")
    for key in ("LINKEDIN_ACCESS_TOKEN", "LINKEDIN_PERSON_ID", "LINKEDIN_MODE"):
        if os.environ.get(key):
            env[key] = os.environ[key]
    return env


def resolve_person_id(token: str, timeout: int = 30) -> str:
    """Obtiene el person id (`sub`) de `/v2/userinfo` con el token OAuth."""
    req = urllib.request.Request(USERINFO_URL, headers={"Authorization": f"Bearer {token}"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except Exception as exc:
        raise MCPError(f"No se pudo resolver LINKEDIN_PERSON_ID vía /v2/userinfo: {exc}") from exc
    sub = data.get("sub")
    if not sub:
        raise MCPError("userinfo no devolvió 'sub'; el token puede no tener scope openid/profile.")
    return str(sub)


def _to_number_or_none(value) -> int | float | None:
    if value is None:
        return None
    if isinstance(value, (int, float)):
        return value
    text = str(value).strip()
    if text == "" or text.lower() in {"n/a", "na", "null", "none", "-"}:
        return None
    text = text.replace(",", "")
    try:
        return int(text)
    except ValueError:
        try:
            num = float(text)
        except ValueError:
            return None
        return int(num) if num.is_integer() else num


def _numbers_from_text(text: str) -> dict:
    """Extrae métricas de una respuesta en texto ("likes: 69", ...)."""
    found: dict = {}
    for field, labels in LABEL_MAP.items():
        for label in labels:
            m = re.search(rf"{label}\D{{0,12}}([\d][\d.,]*)", text, re.IGNORECASE)
            if m:
                found[field] = _to_number_or_none(m.group(1))
                break
    return found


def _first(obj, keys: list[str]):
    if not isinstance(obj, dict):
        return None
    for key in keys:
        if obj.get(key) is not None:
            return obj.get(key)
    lowered = {str(k).lower(): v for k, v in obj.items()}
    for key in keys:
        if lowered.get(key.lower()) is not None:
            return lowered[key.lower()]
    return None


def parse_post_dict(obj: dict) -> dict:
    """Normaliza un dict de post (forma tolerante: varias formas de API)."""
    blob = json.dumps(obj)
    urns = URN_RE.findall(blob)
    urn = _first(obj, ["post_urn", "urn", "id"]) or (urns[0] if urns else None)
    if urn and not str(urn).startswith("urn:li:"):
        urn = None
    metrics: dict = {}
    stats = obj.get("stats") if isinstance(obj.get("stats"), dict) else obj
    for field in ("reactions", "comments", "reposts", "impressions", "clicks", "followers_gained"):
        metrics[field] = _to_number_or_none(_first(stats, [field, field.capitalize()]))
    if all(v is None for v in metrics.values()):
        metrics.update(_numbers_from_text(blob))
    return {
        "post_urn": str(urn) if urn else None,
        "source_post_id": None,
        "published_at": _first(obj, ["published_at", "publishedAt", "published", "created_at", "createdAt", "date", "created"]),
        "format": _first(obj, ["format", "type"]),
        "topic": None,
        "objective": None,
        "metrics": metrics,
        "raw_text": None,
    }


def parse_posts_payload(text: str) -> list[dict]:
    """Convierte la respuesta de get_own_posts en lista de posts normalizados."""
    text = text.strip()
    try:
        data = json.loads(text)
    except json.JSONDecodeError:
        data = None
    if isinstance(data, dict):
        for key in ("posts", "data", "elements", "results"):
            if isinstance(data.get(key), list):
                data = data[key]
                break
    if isinstance(data, list):
        posts = [parse_post_dict(o) for o in data if isinstance(o, dict)]
        return [p for p in posts if p["post_urn"]]
    # Respuesta en texto humano: extraer URNs y métricas por bloque.
    posts = []
    for urn in dict.fromkeys(URN_RE.findall(text)):
        posts.append({
            "post_urn": urn,
            "source_post_id": None,
            "published_at": None,
            "format": None,
            "topic": None,
            "objective": None,
            "metrics": _numbers_from_text(text),
            "raw_text": text[:2000],
        })
    return posts


def _parse_age_hours(published_at: str | None, measured_at: str) -> float | None:
    if not published_at:
        return None
    try:
        pub = datetime.fromisoformat(str(published_at).replace("Z", "+00:00"))
        meas = datetime.fromisoformat(measured_at.replace("Z", "+00:00"))
    except ValueError:
        return None
    if pub.tzinfo is None:
        pub = pub.replace(tzinfo=timezone.utc)
    if meas.tzinfo is None:
        meas = meas.replace(tzinfo=timezone.utc)
    return round((meas - pub).total_seconds() / 3600, 1)


def snapshot_mcp(
    *,
    days: int = 90,
    count: int = 50,
    dry_run: bool = False,
    timeout: int = 120,
) -> dict:
    """Snapshot vía MCP server. Devuelve resumen como `import_csv`."""
    env = load_env()
    token = env.get("LINKEDIN_ACCESS_TOKEN", "")
    if not token:
        raise MCPError("Falta LINKEDIN_ACCESS_TOKEN (ni entorno ni .env). Completa el OAuth primero.")
    person_id = env.get("LINKEDIN_PERSON_ID", "")
    if not person_id:
        person_id = resolve_person_id(token)

    # El server necesita el entorno completo (PATH, HOME para npx/node, ...).
    server_env = dict(os.environ)
    server_env["LINKEDIN_ACCESS_TOKEN"] = token
    server_env["LINKEDIN_PERSON_ID"] = person_id
    server_env["LINKEDIN_MODE"] = env.get("LINKEDIN_MODE", os.environ.get("LINKEDIN_MODE", "member"))

    measured_at = datetime.now(timezone.utc).isoformat(timespec="seconds")
    with MCPClient(MCP_COMMAND, server_env, timeout=timeout) as client:
        posts = parse_posts_payload(client.call_tool("get_own_posts", {"count": count}))
        enriched = []
        for post in posts:
            metrics = dict(post["metrics"])
            if all(v is None for v in metrics.values()) and post["post_urn"]:
                try:
                    stats_text = client.call_tool("get_post_stats", {"post_urn": post["post_urn"]})
                    try:
                        stats_data = json.loads(stats_text)
                        parsed = parse_post_dict(stats_data if isinstance(stats_data, dict) else {})
                        for k, v in parsed["metrics"].items():
                            if v is not None:
                                metrics[k] = v
                    except json.JSONDecodeError:
                        for k, v in _numbers_from_text(stats_text).items():
                            if v is not None:
                                metrics[k] = v
                except MCPError as exc:
                    post["stats_error"] = str(exc)[:200]
            post["metrics"] = metrics
            enriched.append(post)

    catalog = load_catalog()
    observations = load_observations()
    existing = {(o.get("post_key"), o.get("measured_at"), o.get("source")) for o in observations}
    evergreen = {k for k, p in catalog.items() if isinstance(p, dict) and p.get("status") == "evergreen"}
    now = datetime.now(timezone.utc)

    added, skipped_dup, skipped_scope = 0, 0, 0
    for post in enriched:
        key = post_key_for(post["post_urn"], post["source_post_id"], post["published_at"])
        if key not in evergreen and post["published_at"]:
            try:
                pub = datetime.fromisoformat(str(post["published_at"]).replace("Z", "+00:00"))
                if pub.tzinfo is None:
                    pub = pub.replace(tzinfo=timezone.utc)
                if (now - pub).days > days:
                    skipped_scope += 1
                    continue
            except ValueError:
                pass
        dedup = (key, measured_at, SOURCE_MCP)
        if dedup in existing:
            skipped_dup += 1
            continue
        obs = {
            "post_key": key,
            "post_urn": post["post_urn"],
            "source_post_id": post["source_post_id"],
            "published_at": post["published_at"],
            "measured_at": measured_at,
            "age_hours": _parse_age_hours(post["published_at"], measured_at),
            "source": SOURCE_MCP,
            "source_file": None,
            **{f: post["metrics"].get(f) for f in ("reactions", "comments", "reposts", "impressions", "clicks", "followers_gained")},
        }
        if key not in catalog:
            catalog[key] = {
                "post_urn": post["post_urn"],
                "source_post_id": post["source_post_id"],
                "published_at": post["published_at"],
                "format": post["format"],
                "topic": post["topic"],
                "objective": post["objective"],
                "duration_seconds": None,
                "status": "active",
            }
        observations.append(obs)
        existing.add(dedup)
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
        "source": SOURCE_MCP,
    }
