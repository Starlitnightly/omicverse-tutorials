#!/usr/bin/env python
"""Downscale embedded PNG outputs in notebooks before the Sphinx build.

Run this against the (ephemeral) docs checkout *before* Sphinx reads the
notebooks. It rewrites oversized ``image/png`` outputs in place to a
capped longest side, which shrinks what myst-nb has to parse and write to
``_images`` — the dominant cost of the HTML build. Source notebooks in
git are untouched; on Read the Docs the checkout is thrown away after the
build, so this only ever affects the rendered output.

Pure rendering optimisation: the figures are identical apart from
resolution, and no notebook is re-executed.

Usage
-----
    python downscale_notebook_images.py <root-dir> [--max-px 900]

Idempotent: a second pass is a no-op once every image is within the cap.
"""
from __future__ import annotations

import argparse
import base64
import io
import json
import os
import struct
import sys
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

SKIP_PARTS = {"_build", ".ipynb_checkpoints", "jupyter_execute"}


def _png_longest_side(raw: bytes) -> int:
    # IHDR width/height live at bytes 16:24 of a PNG.
    if raw[:8] != b"\x89PNG\r\n\x1a\n":
        return 0
    w, h = struct.unpack(">II", raw[16:24])
    return max(w, h)


def _shrink(b64: str, max_px: int, trigger_px: int | None = None):
    """Return (new_b64, saved_bytes) or (b64, 0) if no gain.

    Only images whose longest side exceeds ``trigger_px`` are touched; the
    rest are left bit-for-bit untouched. ``trigger_px`` defaults to
    ``max_px`` (cap everything above the cap). Set it higher than
    ``max_px`` to "only compress large images" — e.g. trigger=1900,
    max=1500 leaves ≤1900px figures alone and shrinks bigger ones to 1500.
    """
    from PIL import Image

    raw = base64.b64decode(b64)
    trigger = trigger_px if trigger_px is not None else max_px
    if _png_longest_side(raw) <= trigger:
        return b64, 0
    im = Image.open(io.BytesIO(raw))
    w, h = im.size
    scale = max_px / max(w, h)
    im = im.resize((max(1, round(w * scale)), max(1, round(h * scale))), Image.LANCZOS)
    if im.mode == "RGBA":
        bg = Image.new("RGB", im.size, (255, 255, 255))
        bg.paste(im, mask=im.split()[-1])
        im = bg
    buf = io.BytesIO()
    im.save(buf, format="PNG", optimize=True)
    new = buf.getvalue()
    if len(new) >= len(raw):
        return b64, 0
    return base64.b64encode(new).decode("ascii"), len(raw) - len(new)


def _iter_notebooks(root: Path):
    for p in root.rglob("*.ipynb"):
        if SKIP_PARTS & set(p.parts):
            continue
        yield p


def _process_one(args) -> tuple[int, int]:
    """Downscale a single notebook in place. Returns (images, bytes_saved)."""
    path, max_px, trigger_px = args
    try:
        nb = json.loads(Path(path).read_text())
    except (json.JSONDecodeError, OSError):
        return 0, 0
    imgs = saved = 0
    dirty = False
    for cell in nb.get("cells", []):
        if cell.get("cell_type") != "code":
            continue
        for out in cell.get("outputs", []):
            data = out.get("data")
            if not data or "image/png" not in data:
                continue
            img = data["image/png"]
            if isinstance(img, list):
                img = "".join(img)
            img = img.replace("\n", "")
            new_b64, gain = _shrink(img, max_px, trigger_px)
            if gain:
                data["image/png"] = new_b64
                imgs += 1
                saved += gain
                dirty = True
    if dirty:
        Path(path).write_text(json.dumps(nb, indent=1))
    return imgs, saved


def process(root: Path, max_px: int, workers: int | None = None,
            trigger_px: int | None = None) -> tuple[int, int, int]:
    paths = [str(p) for p in _iter_notebooks(root)]
    workers = workers or min(os.cpu_count() or 1, 8)
    nb_changed = imgs = saved = 0
    tasks = [(p, max_px, trigger_px) for p in paths]
    with ProcessPoolExecutor(max_workers=workers) as ex:
        for n_imgs, n_saved in ex.map(_process_one, tasks):
            if n_imgs:
                nb_changed += 1
            imgs += n_imgs
            saved += n_saved
    return nb_changed, imgs, saved


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("root", type=Path, help="docs root to scan for notebooks")
    ap.add_argument("--max-px", type=int, default=900,
                    help="cap the longest image side at this many pixels")
    ap.add_argument("--workers", type=int, default=None,
                    help="parallel worker processes (default: min(cpus, 8))")
    ap.add_argument("--min-trigger-px", type=int, default=None,
                    help="only downscale images whose longest side exceeds "
                         "this (default: --max-px). Set higher than --max-px "
                         "to compress only large figures and leave the rest "
                         "untouched.")
    args = ap.parse_args()
    if not args.root.exists():
        print(f"downscale: root {args.root} does not exist", file=sys.stderr)
        return 1
    nb_changed, imgs, saved = process(args.root, args.max_px, args.workers,
                                      args.min_trigger_px)
    trig = args.min_trigger_px or args.max_px
    print(f"downscale: {nb_changed} notebooks, {imgs} images, "
          f"{saved / 1048576:.1f} MB saved (cap {args.max_px}px, "
          f"trigger >{trig}px)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
