# Kleines Hilfsmodul für handgeschriebene Seiten: baut das page-dict aus Abschnitten.
def table(head, rows):
    h = "".join(f'<th scope="col">{c}</th>' for c in head)
    r = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in row) + "</tr>" for row in rows)
    return f'<div class="matrix"><div class="matrix-scroll"><table><thead><tr>{h}</tr></thead><tbody>{r}</tbody></table></div></div>'


def steps(items):
    return '<ol class="howto">' + "".join(f"<li><b>{a}</b> {b}</li>" for a, b in items) + "</ol>"


def tip(t):
    return f'<div class="tip"><p><strong>Tipp:</strong> {t}</p></div>'


def page(slug, parent, nav, title, desc, h1, eyebrow, lead, answer, secs, faq, related, kw, card, priority="0.7", app=None, about=None, cta=None):
    body = "\n\n".join(f'<h2 id="{i}">{h}</h2>\n{t}' for i, h, t in secs)
    d = dict(slug=slug, parent=parent, nav=nav, priority=priority, card=card, kw=kw, title=title, desc=desc, eyebrow=eyebrow,
             h1=h1, lead=lead, answer=answer, body="\n" + body + "\n", faq=faq, related=related)
    if app:
        d["app"] = app
    if about:
        d["about"] = about
    if cta:
        d["cta"] = cta
    return d
