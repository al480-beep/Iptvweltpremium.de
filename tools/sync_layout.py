#!/usr/bin/env python3
"""Copy the shared header and footer from index.html into every other page.

index.html holds the master copy between the markers
  <!-- layout:top --> ... <!-- /layout:top -->        (icon sprite, background, header)
  <!-- layout:bottom --> ... <!-- /layout:bottom -->  (footer, WhatsApp button, privacy notice)
Run from the repository root after changing the header or footer:  python3 tools/sync_layout.py
Pass a version number to also bump the ?v= cache buster on CSS/JS:  python3 tools/sync_layout.py 6
"""
import pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
PAGES = ["preise/index.html", "kostenloser-test/index.html", "impressum.html", "datenschutz.html", "404.html"]
BLOCKS = ("top", "bottom")


def block(text, name):
    m = re.search(rf"<!-- layout:{name} -->.*?<!-- /layout:{name} -->", text, re.S)
    if not m:
        sys.exit(f"index.html is missing the layout:{name} markers")
    return m.group(0)


def main():
    master = (ROOT / "index.html").read_text(encoding="utf-8")
    parts = {n: block(master, n) for n in BLOCKS}
    version = sys.argv[1] if len(sys.argv) > 1 else None
    for rel in ["index.html"] + PAGES:
        path = ROOT / rel
        text = path.read_text(encoding="utf-8")
        if rel != "index.html":
            for n in BLOCKS:
                text = re.sub(rf"<!-- layout:{n} -->.*?<!-- /layout:{n} -->", lambda _: parts[n], text, count=1, flags=re.S)
        if version:
            text = re.sub(r"(/assets/(?:css/style\.css|js/main\.js))(\?v=[^\"']*)?", rf"\1?v={version}", text)
        path.write_text(text, encoding="utf-8")
        print("updated", rel)


if __name__ == "__main__":
    main()
