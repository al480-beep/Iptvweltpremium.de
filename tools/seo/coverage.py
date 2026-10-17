#!/usr/bin/env python3
"""Keyword coverage report: which keyword from the keyword sheet is assigned to which page.

Usage: python3 tools/seo/coverage.py keywords.json   (JSON list of [keyword, volume, intent])
"""
import json, pathlib, sys, importlib.util

SEO = pathlib.Path(__file__).resolve().parent
# Keywords owned by the hand-written pages
STATIC_KW = {
    "": ["iptv"],
    "preise": ["iptv kosten", "ip tv kosten", "iptv packages", "iptv plans"],
    "kostenloser-test": ["iptv test", "iptv free trial", "iptv testline", "iptv 24h test", "iptv test 24", "iptv free test",
                         "iptv gratis testen", "iptv line test", "iptv premium test", "iptv test line", "iptv trial",
                         "testline iptv", "test ip tv"],
}
EXCLUDED = {"arabic iptv": "Tier 1 Arabic", "iptv arab": "Tier 1 Arabic", "iptv arabisch": "Tier 1 Arabic"}


def main():
    spec = importlib.util.spec_from_file_location("build", SEO / "build.py")
    build = importlib.util.module_from_spec(spec); spec.loader.exec_module(build)
    pages = build.load_pages()
    owner = {}
    for slug, kws in STATIC_KW.items():
        for k in kws:
            owner.setdefault(k, []).append(slug or "/")
    for slug, p in pages.items():
        for k in p.get("kw", []):
            owner.setdefault(k, []).append(slug)
    rows = json.load(open(sys.argv[1]))
    missing, dup = [], []
    for kw, vol, intent in rows:
        k = kw.strip().lower()
        if k in EXCLUDED:
            continue
        if k not in owner:
            missing.append((k, vol))
        elif len(owner[k]) > 1:
            dup.append((k, owner[k]))
    unknown = [k for k in owner if k not in {r[0].strip().lower() for r in rows}]
    print(f"keywords: {len(rows)}, excluded: {len(EXCLUDED)}, covered: {len(rows) - len(EXCLUDED) - len(missing)}")
    print("missing:", missing)
    print("assigned twice:", dup)
    print("not in sheet:", unknown)


if __name__ == "__main__":
    main()
