"""CLI `linkedin-stats` — ingesta e histórico de LinkedIn (ADR-0001)."""

from __future__ import annotations

import argparse
import sys

from . import paths
from .exporter import run_export
from .importer import SOURCE_DEFAULT, import_csv
from .mcp_source import SOURCE_MCP, snapshot_mcp
from .mcp_client import MCPError
from .reporter import run_report
from .store import load_catalog, save_catalog


def _cmd_import(args) -> int:
    result = import_csv(
        args.file,
        measured_at=args.measured_at,
        source=args.source,
        only_recent_days=None,
        dry_run=args.dry_run,
    )
    print(
        f"[{result['source']}] añadidas={result['added']} "
        f"duplicadas={result['skipped_duplicate']} "
        f"fuera_de_alcance={result['skipped_out_of_scope']} "
        f"posts={result['posts']} measured_at={result['measured_at']}"
        + (" (dry-run, sin cambios)" if args.dry_run else "")
    )
    return 0


def _cmd_snapshot(args) -> int:
    source = (args.source or "mcp").lower()
    if source in ("mcp", SOURCE_MCP):
        # Vía principal: el CLI lanza el MCP server por stdio (sin agente).
        try:
            result = snapshot_mcp(days=args.days, count=args.count, dry_run=args.dry_run)
        except MCPError as exc:
            print(f"snapshot MCP fallido: {exc}", file=sys.stderr)
            return 3
        print(
            f"[snapshot MCP {args.days}d] añadidas={result['added']} "
            f"duplicadas={result['skipped_duplicate']} "
            f"omitidas_antiguas={result['skipped_out_of_scope']}"
            + (" (dry-run, sin cambios)" if args.dry_run else "")
        )
        return 0
    if not args.file:
        print(
            f"snapshot con fuente '{args.source}' necesita --file. "
            f"Ejemplos: 'snapshot --file export.csv' o 'snapshot --source mcp'.",
            file=sys.stderr,
        )
        return 2
    result = import_csv(
        args.file,
        measured_at=args.measured_at,
        source=args.source,
        only_recent_days=args.days,
        dry_run=args.dry_run,
    )
    print(
        f"[snapshot {args.days}d] añadidas={result['added']} "
        f"duplicadas={result['skipped_duplicate']} "
        f"omitidas_antiguas={result['skipped_out_of_scope']}"
        + (" (dry-run, sin cambios)" if args.dry_run else "")
    )
    return 0


def _cmd_export(args) -> int:
    if not args.csv and not args.html:
        args.csv = args.html = True
    if args.dry_run:
        print("dry-run: se regenerarían measurements.csv y/o report.html desde el YAML (sin cambios).")
        return 0
    result = run_export()
    out = []
    if args.csv:
        out.append(f"csv={result['csv']}")
    if args.html:
        out.append(f"html={result['html']}")
    print(f"observaciones={result['observations']} posts={result['posts']} " + " ".join(out))
    return 0


def _cmd_report(args) -> int:
    print(run_report(args.window))
    return 0


def _cmd_evergreen(args) -> int:
    catalog = load_catalog()
    if args.list or (not args.add and not args.remove):
        flagged = sorted(k for k, p in catalog.items() if isinstance(p, dict) and p.get("status") == "evergreen")
        print("evergreen:" if flagged else "sin publicaciones evergreen")
        for k in flagged:
            print(f"  {k}")
        return 0
    key = args.add or args.remove
    post = catalog.get(key)
    if not isinstance(post, dict):
        print(f"post no encontrado en el catálogo: {key}", file=sys.stderr)
        return 1
    if args.dry_run:
        print(f"dry-run: {'marcar' if args.add else 'desmarcar'} evergreen {key} (sin cambios)")
        return 0
    post["status"] = "evergreen" if args.add else "active"
    paths.ensure_dirs()
    save_catalog(catalog)
    print(f"{key} -> {post['status']}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="linkedin-stats",
        description="Histórico de métricas de LinkedIn (ADR-0001). Vía principal: MCP server por terminal; alternativa: CSV de LinkedIn Analytics.",
    )
    parser.add_argument("--dry-run", action="store_true", help="No escribe cambios, solo muestra lo que haría.")
    sub = parser.add_subparsers(dest="command", required=False)

    p_import = sub.add_parser("import", help="Carga completa inicial desde un CSV.")
    p_import.add_argument("--file", required=True, help="CSV exportado de LinkedIn Analytics.")
    p_import.add_argument("--measured-at", default=None, help="Fecha de medición ISO 8601 (por defecto: ahora UTC).")
    p_import.add_argument("--source", default=SOURCE_DEFAULT, help="Fuente de la observación.")
    p_import.set_defaults(func=_cmd_import)

    p_snap = sub.add_parser("snapshot", help="Seguimiento habitual vía MCP (ventana de N días + evergreen).")
    p_snap.add_argument("--days", type=int, default=90, help="Ventana de días (por defecto 90).")
    p_snap.add_argument("--count", type=int, default=50, help="Posts recientes a pedir al MCP (máx. 50).")
    p_snap.add_argument("--file", default=None, help="Solo para fuente CSV: CSV a importar de forma selectiva.")
    p_snap.add_argument("--measured-at", default=None, help="Solo para fuente CSV.")
    p_snap.add_argument("--source", default="mcp", help="'mcp' (por defecto) o 'linkedin_analytics_csv'.")
    p_snap.set_defaults(func=_cmd_snapshot)

    p_exp = sub.add_parser("export", help="Regenera measurements.csv y report.html desde el YAML.")
    p_exp.add_argument("--csv", action="store_true")
    p_exp.add_argument("--html", action="store_true")
    p_exp.set_defaults(func=_cmd_export)

    p_rep = sub.add_parser("report", help="Muestra crecimiento y velocidad en terminal.")
    p_rep.add_argument("--window", default="7d")
    p_rep.set_defaults(func=_cmd_report)

    p_evg = sub.add_parser("evergreen", help="Marca o lista publicaciones con seguimiento permanente.")
    p_evg.add_argument("--add", default=None, metavar="POST_KEY")
    p_evg.add_argument("--remove", default=None, metavar="POST_KEY")
    p_evg.add_argument("--list", action="store_true")
    p_evg.set_defaults(func=_cmd_evergreen)

    return parser


def main(argv=None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if not args.command:
        parser.print_help()
        return 0
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
