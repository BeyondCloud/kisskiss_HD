#!/usr/bin/env python3
"""Regenerate the image gallery sections inside PNG/README.md and GIF/README.md.

Each target README must contain a `<!-- gallery:start -->` ... `<!-- gallery:end -->`
block; everything between the markers is replaced.
"""
from __future__ import annotations

import hashlib
from pathlib import Path
from urllib.parse import quote

REPO_ROOT = Path(__file__).resolve().parent.parent
START = "<!-- gallery:start -->"
END = "<!-- gallery:end -->"
COLS = 4
THUMB_WIDTH = 160
PNG_EXTS = {".png"}
GIF_EXTS = {".gif"}


def gallery_table(prefix: str, files: list[Path]) -> str:
    if not files:
        return "_(empty)_"
    header = "|" + "|".join([" "] * COLS) + "|"
    sep = "|" + "|".join([" --- "] * COLS) + "|"
    rows = [header, sep]
    for i in range(0, len(files), COLS):
        chunk = files[i : i + COLS]
        cells = []
        for f in chunk:
            src = quote(f"{prefix}{f.name}") if prefix else quote(f.name)
            digest = hashlib.md5(f.read_bytes()).hexdigest()[:8]
            cells.append(f'<img src="{src}?v={digest}" width="{THUMB_WIDTH}"><br>{f.stem}')
        cells.extend([""] * (COLS - len(cells)))
        rows.append("| " + " | ".join(cells) + " |")
    return "\n".join(rows)


def grouped_png_gallery(root: Path) -> str:
    sections = []
    for sub in sorted(p for p in root.iterdir() if p.is_dir()):
        files = sorted(p for p in sub.iterdir() if p.suffix.lower() in PNG_EXTS)
        table = gallery_table(f"{sub.name}/", files)
        sections.append(f"### {sub.name} ({len(files)})\n\n{table}")
    return "\n\n".join(sections)


def gif_gallery() -> str:
    gif_dir = REPO_ROOT / "GIF"
    files = sorted(p for p in gif_dir.iterdir() if p.suffix.lower() in GIF_EXTS)
    return gallery_table("", files)


def splice(path: Path, body: str) -> bool:
    text = path.read_text(encoding="utf-8")
    if START not in text or END not in text:
        raise SystemExit(f"{path} is missing gallery markers ({START} / {END})")
    before, _, rest = text.partition(START)
    _, _, after = rest.partition(END)
    new = f"{before}{START}\n\n{body}\n\n{END}{after}"
    if new == text:
        return False
    path.write_text(new, encoding="utf-8")
    return True


def main() -> None:
    changed = []
    targets = [
        ("PNG/README.md", lambda: grouped_png_gallery(REPO_ROOT / "PNG")),
        ("GIF/README.md", gif_gallery),
        ("720_body/README.md", lambda: grouped_png_gallery(REPO_ROOT / "720_body")),
    ]
    for rel, builder in targets:
        if splice(REPO_ROOT / rel, builder()):
            changed.append(rel)
    if changed:
        print("Updated:", ", ".join(changed))
    else:
        print("No changes")


if __name__ == "__main__":
    main()
