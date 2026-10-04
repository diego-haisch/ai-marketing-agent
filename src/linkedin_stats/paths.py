"""Rutas del almacén local (ver ADR-0001)."""

from __future__ import annotations

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
BASE = REPO_ROOT / "data" / "social" / "linkedin"
RAW_DIR = BASE / "raw"
CURATED_DIR = BASE / "curated"
EXPORTS_DIR = BASE / "exports"

CATALOG_FILE = CURATED_DIR / "catalog.yaml"
OBSERVATIONS_FILE = CURATED_DIR / "observations.yaml"
MEASUREMENTS_CSV = EXPORTS_DIR / "measurements.csv"
REPORT_HTML = EXPORTS_DIR / "report.html"

CSV_COLUMNS = [
    "post_key",
    "post_urn",
    "source_post_id",
    "published_at",
    "measured_at",
    "age_hours",
    "format",
    "topic",
    "objective",
    "status",
    "source",
    "source_file",
    "reactions",
    "comments",
    "reposts",
    "impressions",
    "clicks",
    "followers_gained",
    "total_interactions",
    "engagement_rate",
    "comment_rate",
]


def ensure_dirs() -> None:
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    CURATED_DIR.mkdir(parents=True, exist_ok=True)
    EXPORTS_DIR.mkdir(parents=True, exist_ok=True)
