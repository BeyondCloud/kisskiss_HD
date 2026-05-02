#!/usr/bin/env python3
"""Create a GIF from PNG files in a directory.

Example:
    python scripts/make_gif.py 720_body/vt -o vt.gif --duration-ms 50
"""
from __future__ import annotations

import argparse
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Create a GIF from PNG images in a folder")
    parser.add_argument(
        "input_dir",
        type=Path,
        help="Directory containing PNG files",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=Path("output.gif"),
        help="Output GIF file path (default: output.gif)",
    )
    parser.add_argument(
        "--duration-ms",
        type=int,
        default=50,
        help="Frame duration in milliseconds (default: 150)",
    )
    parser.add_argument(
        "--loop",
        type=int,
        default=0,
        help="GIF loop count (0 means infinite, default: 0)",
    )
    return parser.parse_args()


def collect_pngs(folder: Path) -> list[Path]:
    return sorted(p for p in folder.iterdir() if p.is_file() and p.suffix.lower() == ".png")


def main() -> None:
    args = parse_args()

    if args.duration_ms <= 0:
        raise SystemExit("--duration-ms must be a positive integer")
    if args.loop < 0:
        raise SystemExit("--loop must be >= 0")
    if not args.input_dir.exists() or not args.input_dir.is_dir():
        raise SystemExit(f"Input directory not found: {args.input_dir}")

    png_files = collect_pngs(args.input_dir)
    if not png_files:
        raise SystemExit(f"No PNG files found in: {args.input_dir}")

    try:
        from PIL import Image
    except ImportError as exc:
        raise SystemExit("Pillow is required. Install with: pip install Pillow") from exc

    frames = [Image.open(path).convert("RGBA") for path in png_files]

    args.output.parent.mkdir(parents=True, exist_ok=True)
    frames[0].save(
        args.output,
        format="GIF",
        save_all=True,
        append_images=frames[1:],
        duration=args.duration_ms,
        loop=args.loop,
        optimize=False,
        disposal=2,
    )

    for frame in frames:
        frame.close()

    print(f"Created GIF: {args.output}")
    print(f"Frames: {len(png_files)}")
    print(f"Duration per frame: {args.duration_ms} ms")


if __name__ == "__main__":
    main()
