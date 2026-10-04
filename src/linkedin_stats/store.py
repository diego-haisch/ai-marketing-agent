"""Carga/guardado del catálogo y las observaciones (YAML)."""

from __future__ import annotations

from datetime import datetime, timezone

import yaml

from . import paths


def _utcnow_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def load_yaml(path, default):
    if not path.exists():
        return default
    with open(path, encoding="utf-8") as fh:
        data = yaml.safe_load(fh)
    return default if data is None else data


def save_yaml(path, data) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        yaml.safe_dump(data, fh, allow_unicode=True, sort_keys=False)


def load_catalog() -> dict:
    data = load_yaml(paths.CATALOG_FILE, {})
    posts = data.get("posts", {}) if isinstance(data, dict) else {}
    return posts if isinstance(posts, dict) else {}


def save_catalog(posts: dict) -> None:
    save_yaml(paths.CATALOG_FILE, {"version": 1, "posts": posts})


def load_observations() -> list:
    data = load_yaml(paths.OBSERVATIONS_FILE, {})
    obs = data.get("observations", []) if isinstance(data, dict) else []
    return obs if isinstance(obs, list) else []


def save_observations(observations: list) -> None:
    save_yaml(paths.OBSERVATIONS_FILE, {"version": 1, "observations": observations})


def post_key_for(post_urn: str | None, source_post_id: str | None, published_at: str | None) -> str:
    if post_urn:
        return post_urn.strip()
    if source_post_id:
        return source_post_id.strip()
    return f"unknown:{(published_at or 'nodate').strip()}"


def utcnow_iso() -> str:
    return _utcnow_iso()
