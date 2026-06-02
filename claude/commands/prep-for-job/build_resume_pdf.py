#!/usr/bin/env python3
"""
build_resume_pdf.py - Convert a RESUME.md into a print-ready PDF that fills
1.9-2.0 pages (never less, never more), with comfortable, readable spacing.

Pipeline:  pandoc (markdown -> HTML)  ->  print CSS  ->  headless Chrome (-> PDF)

It AUTO-CALIBRATES line-height so the last page is ~88-95% full: no wasted
whitespace (the "1.5 page" failure) and no overflow to a 3rd page. If the
content cannot hit the target at any reasonable spacing, it tells you whether
to ADD or TRIM content (spacing alone cannot fix a content problem).

Usage:
    python3 build_resume_pdf.py <RESUME.md> <output.pdf> [--pages N]

Defaults: Arial 10pt, margins 0.55in vertical / 0.7in horizontal, US Letter.

Requirements: pandoc, "Google Chrome", poppler (pdfinfo + pdftoppm), Pillow.
"""

import argparse
import subprocess
import sys
import tempfile
from pathlib import Path

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
PAGE_HEIGHT_IN = 11.0  # US Letter

# Acceptable fill of the LAST page (as a fraction of the printable area).
FILL_LO = 0.88
FILL_HI = 0.97

# Line-height sweep (primary calibration knob). Ascending = looser = more fill.
LH_MIN, LH_MAX, LH_STEP = 1.18, 1.55, 0.02


def build_html(md_path: str, lh: float, pv: str, ph: str, body_size: str) -> str:
    body = subprocess.check_output(
        ["pandoc", md_path, "-t", "html5", "-f", "markdown-smart"], text=True
    )
    css = f"""
@page {{ margin: {pv} {ph}; }}
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
body {{ font-family: Arial, Helvetica, sans-serif; font-size: {body_size};
       line-height: {lh}; color: #111; }}
h1 {{ font-size: 19pt; font-weight: bold; margin-bottom: 3px; }}
h1 + p {{ font-size: 9pt; color: #444; margin-bottom: 6px; }}
h2 {{ font-size: 12pt; font-weight: bold; border-bottom: 1.5px solid #222;
      padding-bottom: 2px; margin-top: 11px; margin-bottom: 4px; }}
h2 + p {{ font-size: 9.5pt; color: #555; margin-bottom: 4px; }}
h3 {{ font-size: 11pt; font-weight: bold; margin-top: 9px; margin-bottom: 2px; }}
h3 + p {{ font-size: 9.5pt; color: #333; margin-bottom: 3px; }}
p {{ margin-bottom: 3px; }}
ul {{ margin-left: 16px; margin-top: 3px; margin-bottom: 4px; padding: 0; }}
li {{ margin-bottom: 2px; }}
"""
    return f"""<!DOCTYPE html>
<html><head><meta charset="utf-8"><style>{css}</style></head>
<body>
{body}
</body></html>"""


def render_pdf(html: str, pdf_path: str) -> None:
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False) as f:
        f.write(html)
        html_path = f.name
    subprocess.run(
        [CHROME, "--headless", "--disable-gpu", f"--print-to-pdf={pdf_path}",
         "--no-pdf-header-footer", "--print-to-pdf-no-header",
         "--virtual-time-budget=5000", f"file://{html_path}"],
        capture_output=True,
    )


def page_count(pdf_path: str) -> int:
    out = subprocess.check_output(["pdfinfo", pdf_path], text=True)
    for line in out.splitlines():
        if line.startswith("Pages:"):
            return int(line.split()[1])
    return 0


def last_page_fill(pdf_path: str, pages: int, pv_in: float) -> float:
    """Fraction of the last page's printable area that contains ink (0..1)."""
    from PIL import Image
    prefix = tempfile.mktemp()
    subprocess.run(
        ["pdftoppm", "-png", "-r", "150", "-f", str(pages), "-l", str(pages),
         pdf_path, prefix],
        capture_output=True,
    )
    img = next(Path(tempfile.gettempdir()).glob(Path(prefix).name + "*"))
    im = Image.open(img).convert("L")
    w, h = im.size
    px = im.load()
    last_ink = 0
    for y in range(h):
        if any(px[x, y] < 200 for x in range(0, w, 3)):
            last_ink = y
    top = pv_in / PAGE_HEIGHT_IN
    bottom = 1.0 - pv_in / PAGE_HEIGHT_IN
    return max(0.0, (last_ink / h - top) / (bottom - top))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("md")
    ap.add_argument("pdf")
    ap.add_argument("--pages", type=int, default=2, help="target page count")
    ap.add_argument("--pv", default="0.55in")
    ap.add_argument("--ph", default="0.7in")
    ap.add_argument("--body", default="10pt")
    args = ap.parse_args()

    pv_in = float(args.pv.replace("in", ""))
    target = args.pages

    best = None  # (fill, lh) for configs that land on exactly `target` pages
    lh = LH_MIN
    while lh <= LH_MAX + 1e-9:
        html = build_html(args.md, lh, args.pv, args.ph, args.body)
        render_pdf(html, args.pdf)
        pages = page_count(args.pdf)
        if pages == target:
            fill = last_page_fill(args.pdf, pages, pv_in)
            print(f"  lh={lh:.2f}  pages={pages}  last-page fill={fill*100:.1f}%")
            if FILL_LO <= fill <= FILL_HI:
                best = (fill, lh)  # in-range: keep the loosest (most readable)
            elif fill < FILL_LO and best is None:
                best = (fill, lh)  # remember under-filled as fallback
        else:
            print(f"  lh={lh:.2f}  pages={pages}")
        lh += LH_STEP

    if best is None:
        print(f"\nFAIL: could not reach exactly {target} pages at any spacing.")
        print("This is a CONTENT problem, not a spacing one:")
        print(f"  - If it never reaches {target} pages -> ADD detail (restore "
              "trimmed bullets, expand achievements). Do NOT inflate spacing.")
        print(f"  - If it always exceeds {target} pages -> TRIM the least "
              "relevant bullets. Do NOT crush bullets into run-on sentences.")
        return 1

    fill, lh = best
    html = build_html(args.md, lh, args.pv, args.ph, args.body)
    render_pdf(html, args.pdf)
    pages = page_count(args.pdf)
    status = "OK" if fill >= FILL_LO else "UNDER-FILLED (add content to reach 1.9-2.0 pages)"
    print(f"\n{status}: {pages} pages, last page {fill*100:.1f}% full "
          f"(line-height {lh:.2f})")
    print(f"Saved: {args.pdf}")
    return 0 if fill >= FILL_LO else 2


if __name__ == "__main__":
    sys.exit(main())
