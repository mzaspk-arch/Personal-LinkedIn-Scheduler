"""Render brand posters (1080 x 1350 PNG) from a JSON spec.

Usage:
    python3 designer/render.py designer/posts/<file>.json [--out posters]

Spec (one poster):
{
  "id": "53-UAE-Input-VAT-Verification",      # file name without .png; must start with the queue number
  "format": "Checklist",                       # MythVsFact | Checklist | LessonLearned | BuildInPublic | HotTake
  "pillar": "TAX • UAE",                        # TAX • UAE | TAX • PAKISTAN | FINANCE | ERP | SAAS | STRATEGY | DIGITAL TRANSFORMATION
  "source": "FTA Decision No. 13 of 2026 · Effective 1 October 2026",
  "headline": ["NEW INPUT VAT", "CHECKS FOR"],  # white lines, CAPITALS
  "highlight": "EVERY SUPPLIER",               # the ONE light-blue line
  "blocks": [
    {"type": "text", "text": "Plain text with **bold** parts."},
    {"type": "lead", "text": "What to do"},
    {"type": "list", "items": ["**Label:** text", "..."]},
    {"type": "myth", "text": "The myth in one sentence"},
    {"type": "metric", "value": "120", "label": "what the number means"},
    {"type": "closing", "text": "Agree or disagree?"}
  ],
  "disclaimer": true                            # true = "General information, not tax advice."; false = none; or custom text
}
A carousel is {"id": "...", "slides": [spec, spec, ...]}; shared fields (pillar, source, format) can sit at the top
and are copied into each slide. Slides are saved as <id>-Pg-1.png, <id>-Pg-2.png, ...

The script exits with an error if the text does not fit; shorten the text and try again.
"""
import json, os, sys, pathlib
from playwright.sync_api import sync_playwright

HERE = pathlib.Path(__file__).resolve().parent
TEMPLATE = HERE / "template.html"
SHARED = ("format", "pillar", "source", "disclaimer")


def slides_of(spec):
    if "slides" not in spec:
        return [(spec["id"], spec)]
    out = []
    n = len(spec["slides"])
    for i, s in enumerate(spec["slides"], 1):
        s = dict(s)
        for k in SHARED:
            if k in spec and k not in s:
                s[k] = spec[k]
        s.setdefault("slide", f"{i}/{n}")
        s["id"] = f'{spec["id"]}-Pg-{i}'
        out.append((s["id"], s))
    return out


def render(spec_path, out_dir):
    spec = json.loads(pathlib.Path(spec_path).read_text(encoding="utf-8"))
    out_dir = pathlib.Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    made = []
    exe = "/opt/pw-browsers/chromium" if os.path.exists("/opt/pw-browsers/chromium") and os.path.isfile("/opt/pw-browsers/chromium") else None
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path=exe) if exe else p.chromium.launch()
        page = browser.new_page(viewport={"width": 1080, "height": 1350}, device_scale_factor=1)
        for name, s in slides_of(spec):
            page.add_init_script(f"window.SPEC = {json.dumps(s)};")
            page.goto(TEMPLATE.as_uri())
            page.wait_for_function("window.READY === true", timeout=20000)
            fit = page.evaluate("window.FIT")
            if fit == "fail":
                browser.close()
                sys.exit(f"ERROR: text does not fit on {name}. Shorten the text and render again.")
            target = out_dir / f"{name}.png"
            page.locator("#canvas").screenshot(path=str(target))
            made.append((str(target), fit))
            page = browser.new_page(viewport={"width": 1080, "height": 1350}, device_scale_factor=1)
        browser.close()
    for path, fit in made:
        print(f"{path}  ({fit})")


if __name__ == "__main__":
    args = sys.argv[1:]
    out = "posters"
    if "--out" in args:
        i = args.index("--out")
        out = args[i + 1]
        args = args[:i] + args[i + 2:]
    if not args:
        sys.exit(__doc__)
    for a in args:
        render(a, out)
