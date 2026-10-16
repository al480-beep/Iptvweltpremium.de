#!/usr/bin/env python3
"""Regenerate the plan cards (between <!-- plans:start --> and <!-- plans:end -->) in index.html and preise/index.html.

Prices for 1 device are written into the HTML; main.js swaps them when another device count is chosen.
Run from the repository root:  python3 tools/plans_block.py
"""
import pathlib, re

ROOT = pathlib.Path(__file__).resolve().parent.parent
PRICES_1 = {1: 9, 3: 29, 6: 39, 12: 49}
LABEL = {1: "1 Monat", 3: "3 Monate", 6: "6 Monate", 12: "1 Jahr"}
FEATURES = [
    "+50.000 Live-Kanäle",
    "+300.000 Filme &amp; Serien (VOD)",
    "4K Ultra HD Qualität",
    "Bundesliga · Sky · Dazn",
    "PPV Events inklusive",
    "EPG &amp; Catch-Up TV",
    "VPN-freundlich",
    "24/7 Deutscher Support",
]


def euro(n):
    return (f"{n:.2f}".replace(".", ",")) if n != int(n) else str(int(n))


def card(months, delay):
    featured = months == 12
    price = PRICES_1[months]
    if months == 1:
        per, save = "einmalig, ohne Verlängerung", ""
    else:
        per = f"nur {euro(round(price / months, 2))} € pro Monat"
        s = round((1 - price / (PRICES_1[1] * months)) * 100)
        save = f"Sie sparen {s} %" if s > 0 else ""
    feats = "".join(f'\n            <li><svg><use href="#i-check"/></svg>{f}</li>' for f in FEATURES)
    bonus = ('''
          <div class="plan-bonus"><svg><use href="#i-star"/></svg><div><b>IBO Player Pro Premium Abo</b><span>kostenlos inklusive</span></div></div>'''
             if featured else "")
    tag = '\n          <span class="plan-tag">★ Bester Preis</span>' if featured else ""
    d = f" d{delay}" if delay else ""
    return f'''        <article class="plan{' featured' if featured else ''} reveal{d}" data-months="{months}">{tag}
          <div class="plan-name">{LABEL[months]}</div>
          <div class="plan-devices">1 Gerät</div>
          <div class="plan-price price-anim"><b>{price}</b><span>€</span></div>
          <div class="plan-monthly">{per}</div>
          <div class="plan-save-wrap"><span class="plan-save">{save}</span></div>{bonus}
          <ul class="plan-features">{feats}
          </ul>
          <a class="btn btn-primary btn-block plan-btn" href="/checkout/?geraete=1&amp;laufzeit={months}">Jetzt starten <svg><use href="#i-arrow"/></svg></a>
        </article>'''


def block():
    switch = '''      <div class="device-switch reveal" role="tablist" aria-label="Anzahl der Geräte">
        <span class="switch-glider" aria-hidden="true"></span>
        <button class="active" role="tab" aria-selected="true" data-devices="1"><svg><use href="#i-user"/></svg>1 Gerät</button>
        <button role="tab" aria-selected="false" data-devices="2"><svg><use href="#i-users"/></svg>2 Geräte</button>
        <button role="tab" aria-selected="false" data-devices="3"><svg><use href="#i-users"/></svg>3 Geräte</button>
        <button role="tab" aria-selected="false" data-devices="4"><svg><use href="#i-users"/></svg>4 Geräte</button>
        <button role="tab" aria-selected="false" data-devices="5"><svg><use href="#i-users"/></svg>5 Geräte</button>
      </div>
      <p class="device-hint reveal">Wählen Sie, auf wie vielen Geräten gleichzeitig geschaut wird. Ideal für Familien.</p>
'''
    cards = "\n\n".join(card(m, i) for i, m in enumerate((1, 3, 6, 12)))
    return f"<!-- plans:start -->\n{switch}\n      <div class=\"plans\" data-plans>\n{cards}\n      </div>\n      <div class=\"plans-dots\" aria-hidden=\"true\"><i class=\"active\"></i><i></i><i></i><i></i></div>\n      <!-- plans:end -->"


def main():
    for rel in ("index.html", "preise/index.html"):
        p = ROOT / rel
        t = p.read_text(encoding="utf-8")
        t, n = re.subn(r"<!-- plans:start -->.*?<!-- plans:end -->", lambda _: block(), t, flags=re.S)
        if n != 1:
            raise SystemExit(f"{rel}: plans markers not found")
        p.write_text(t, encoding="utf-8")
        print("updated", rel)


if __name__ == "__main__":
    main()
