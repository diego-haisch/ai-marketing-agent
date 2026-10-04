"""Exporta el histórico a CSV plano (Power BI) y HTML derivado (ADR-0001)."""

from __future__ import annotations

import csv
import html

from . import paths
from .store import load_catalog, load_observations


def _total(o: dict):
    parts = [o.get(f) for f in ("reactions", "comments", "reposts")]
    parts = [p for p in parts if isinstance(p, (int, float))]
    return sum(parts) if parts else None


def enrich(observations: list, catalog: dict) -> list[dict]:
    rows = []
    for o in observations:
        post = catalog.get(o.get("post_key"), {}) if isinstance(catalog.get(o.get("post_key")), dict) else {}
        total = _total(o)
        impressions = o.get("impressions")
        comments = o.get("comments")
        engagement = (total / impressions) if isinstance(total, (int, float)) and isinstance(impressions, (int, float)) and impressions else None
        comment_rate = (comments / total) if isinstance(comments, (int, float)) and isinstance(total, (int, float)) and total else None
        rows.append(
            {
                "post_key": o.get("post_key"),
                "post_urn": o.get("post_urn"),
                "source_post_id": o.get("source_post_id"),
                "published_at": o.get("published_at") or post.get("published_at"),
                "measured_at": o.get("measured_at"),
                "age_hours": o.get("age_hours"),
                "format": post.get("format"),
                "topic": post.get("topic"),
                "objective": post.get("objective"),
                "status": post.get("status"),
                "source": o.get("source"),
                "source_file": o.get("source_file"),
                "reactions": o.get("reactions"),
                "comments": o.get("comments"),
                "reposts": o.get("reposts"),
                "impressions": o.get("impressions"),
                "clicks": o.get("clicks"),
                "followers_gained": o.get("followers_gained"),
                "total_interactions": total,
                "engagement_rate": round(engagement, 4) if engagement is not None else None,
                "comment_rate": round(comment_rate, 4) if comment_rate is not None else None,
            }
        )
    rows.sort(key=lambda r: ((r.get("published_at") or ""), (r.get("measured_at") or "")))
    return rows


def _fmt(value) -> str:
    return "" if value is None else str(value)


def export_csv(rows: list[dict], dest=None) -> str:
    dest = dest or paths.MEASUREMENTS_CSV
    dest.parent.mkdir(parents=True, exist_ok=True)
    with open(dest, "w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=paths.CSV_COLUMNS)
        writer.writeheader()
        for row in rows:
            writer.writerow({col: _fmt(row.get(col)) for col in paths.CSV_COLUMNS})
    return str(dest)


def export_html(rows: list[dict], dest=None) -> str:
    dest = dest or paths.REPORT_HTML
    dest.parent.mkdir(parents=True, exist_ok=True)
    n_posts = len({r.get("post_key") for r in rows})
    cells = []
    for r in rows:
        cells.append(
            "<tr>"
            + "".join(f"<td>{html.escape(_fmt(r.get(c)))}</td>" for c in paths.CSV_COLUMNS)
            + "</tr>"
        )
    header = "".join(f"<th>{html.escape(c)}</th>" for c in paths.CSV_COLUMNS)
    page = f"""<!doctype html>
<html lang="es"><head><meta charset="utf-8">
<title>LinkedIn — histórico de publicaciones</title>
<style>
body{{font-family:system-ui,sans-serif;margin:2rem;color:#1c1c1c}}
table{{border-collapse:collapse;width:100%;font-size:12px}}
th,td{{border:1px solid #ddd;padding:4px 6px;text-align:left}}
th{{background:#f4f4f4;position:sticky;top:0}}
.meta{{color:#555;margin-bottom:1rem}}
</style></head>
<body>
<h1>LinkedIn — histórico de publicaciones</h1>
<p class="meta">Observaciones: {len(rows)} · Publicaciones: {n_posts} ·
Derivado regenerable desde el histórico YAML. Fuente para Power BI:
<code>measurements.csv</code>.</p>
<table><thead><tr>{header}</tr></thead>
<tbody>{''.join(cells)}</tbody></table>
</body></html>"""
    dest.write_text(page, encoding="utf-8")
    return str(dest)


def run_export() -> dict:
    catalog = load_catalog()
    observations = load_observations()
    rows = enrich(observations, catalog)
    csv_path = export_csv(rows)
    html_path = export_html(rows)
    return {"observations": len(rows), "posts": len({r.get("post_key") for r in rows}), "csv": csv_path, "html": html_path}
