"""Informe de evolución en terminal: crecimiento y velocidad (ADR-0001)."""

from __future__ import annotations

from datetime import datetime, timezone

from .exporter import enrich
from .store import load_catalog, load_observations


def _parse_window(window: str) -> int:
    text = window.strip().lower().replace("días", "").replace("dias", "").replace("d", "")
    return max(int(text), 1)


def run_report(window: str = "7d") -> str:
    days = _parse_window(window)
    catalog = load_catalog()
    observations = load_observations()
    rows = enrich(observations, catalog)
    now = datetime.now(timezone.utc)

    by_post: dict[str, list] = {}
    for r in rows:
        try:
            meas = datetime.fromisoformat((r.get("measured_at") or "").replace("Z", "+00:00"))
            if meas.tzinfo is None:
                meas = meas.replace(tzinfo=timezone.utc)
        except ValueError:
            continue
        if (now - meas).days <= days + 4000:  # ventana amplia si las mediciones son históricas
            by_post.setdefault(r.get("post_key") or "?", []).append((meas, r))

    lines = [f"Ventana: últimos {days}d (+histórico) · publicaciones con datos: {len(by_post)}", ""]
    header = f"{'post':34} {'obs':>3} {'reacc':>12} {'coment':>12} {'total':>12} {'veloc/h':>8}"
    lines.append(header)
    lines.append("-" * len(header))
    for key in sorted(by_post):
        obs = sorted(by_post[key], key=lambda t: t[0])
        first, last = obs[0][1], obs[-1][1]

        def num(v):
            return v if isinstance(v, (int, float)) else 0

        d_react = num(last.get("reactions")) - num(first.get("reactions"))
        d_comm = num(last.get("comments")) - num(first.get("comments"))
        d_total = num(last.get("total_interactions")) - num(first.get("total_interactions"))
        age = last.get("age_hours") or 0
        velocity = (num(last.get("total_interactions")) / age) if age else 0
        short = (key or "?")[:34]
        lines.append(f"{short:34} {len(obs):>3} {d_react:>+12} {d_comm:>+12} {d_total:>+12} {velocity:>8.2f}")
    lines += ["", "reacc/coment/total = crecimiento entre primera y última observación de la ventana.",
              "veloc/h = interacciones totales / horas desde publicación."]
    return "\n".join(lines)
