"""CLI para generar el CV de micro1.

Uso:
    python -m create_presentation [--format pdf|docx] [output.ext]
"""

import sys
from pathlib import Path

from .docx_render import save_docx
from .render import save_pdf

BASE = Path("2026-08-15_micro1_ai_expert_cv")
DEFAULT_DIR = Path(__file__).resolve().parents[2] / "comercial" / "contactos"


def main(argv=None) -> int:
    argv = sys.argv[1:] if argv is None else argv

    fmt = "pdf"
    paths = []
    i = 0
    while i < len(argv):
        arg = argv[i]
        if arg in ("--format", "-f"):
            i += 1
            fmt = argv[i] if i < len(argv) else "pdf"
        elif arg in ("--pdf", "--docx", "--word"):
            fmt = arg.lstrip("-")
        else:
            paths.append(arg)
        i += 1

    if fmt in ("word", "doc"):
        fmt = "docx"

    out = Path(paths[0]) if paths else DEFAULT_DIR / BASE.with_suffix(f".{fmt}")
    out.parent.mkdir(parents=True, exist_ok=True)

    if fmt == "docx":
        save_docx(str(out))
    else:
        save_pdf(str(out))

    print(f"{fmt.upper()} generado: {out}")
    print(f"Tamaño: {out.stat().st_size / 1024:.1f} KB")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
