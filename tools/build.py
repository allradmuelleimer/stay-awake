"""
Baut Startseiten (de + en), Anleitungen, Sitemap und robots.txt der Stay-Awake-Website.

Kein Framework, keine Abhaengigkeiten: Python schreibt HTML. Die erzeugten Seiten nie direkt
aendern - Texte stehen in tools/content_<sprache>.py, Aufbau hier:

    python -I tools/build.py
    python -I tools/check_site.py

Handgeschrieben und NICHT erzeugt (bleiben noindex, weil Name und Anschrift darin stehen):
datenschutz/, impressum/, privacy/, imprint/, 404.html.

Faktenregel: In den Texten steht nur, was die App wirklich kann (Quellen: ../CLAUDE.md,
../PRODUCT_SPEC.md, ../docs/abweichungen.md, ../docs/store-eintrag.md, Code). Verboten:
Autofahren/Strassenverkehr, Arbeitsschutz-Versprechen, "verhindert Einschlafen", medizinische
Ratschlaege.

Bildschirmfotos in img/: echte Aufnahmen vom Emulator (Debug-Build, Werbung per Testschalter aus),
Statusleiste abgeschnitten, 540 x 1145 WebP.
"""

from __future__ import annotations

import hashlib
import html
import importlib
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))

SITE = "https://allradmuelleimer.github.io"
BASE = "/stay-awake"
PLAY_ID = "com.nicedevelopments.stayawake"
PLAY_HL = {"de": "de", "en": "en"}
SHOT_W, SHOT_H = 540, 1145

LOCALES = ["en", "de"]
C = {code: importlib.import_module(f"content_{code}").C for code in LOCALES}
LEGAL = {
    "de": {"privacy": "/datenschutz/", "imprint": "/impressum/"},
    "en": {"privacy": "/privacy/", "imprint": "/imprint/"},
}

e = html.escape


# Englisch ist die Hauptsprache und liegt an der Wurzel (Entscheidung des Inhabers, 21.11.2026);
# jede weitere Sprache bekommt ein eigenes Verzeichnis /<code>/.
GUIDES_DIR = {"en": "guides", "de": "anleitungen"}

# Adressen, die am 21.11.2026 kurz online waren (de an der Wurzel, en unter /en/). Sie leiten auf
# die neuen Adressen weiter, falls Google oder jemand sie schon kennt.
OLD = {"de": ("/", "/anleitungen/"), "en": ("/en/", "/en/guides/")}


def home_path(code: str) -> str:
    return "/" if code == "en" else f"/{code}/"


def guides_path(code: str) -> str:
    return home_path(code) + GUIDES_DIR[code] + "/"


def guide_path(code: str, g: dict) -> str:
    return guides_path(code) + g["slug"] + "/"


def abs_url(path: str) -> str:
    return SITE + BASE + path


def href(path: str) -> str:
    return BASE + path


def guide_by_id(code: str, gid: str) -> dict | None:
    return next((g for g in C[code]["guides"] if g["id"] == gid), None)


def play_url(code: str) -> str:
    return f"https://play.google.com/store/apps/details?id={PLAY_ID}&hl={PLAY_HL[code]}"


# ---------------------------------------------------------------- Bausteine

def inline(s: str) -> str:
    """Text mit **fett**, *betont* und [Text](/pfad/) (interne Pfade ohne /stay-awake)."""
    s = e(s, quote=False)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<![*\w])\*(?=\S)([^*\n]+?)(?<=\S)\*(?![*\w])", r"<em>\1</em>", s)
    return re.sub(r"\[([^\]]+)\]\((/[^)\s]*)\)", lambda m: f'<a href="{BASE}{m.group(2)}">{m.group(1)}</a>', s)


def ld(data: dict) -> str:
    return f'<script type="application/ld+json">{json.dumps(data, ensure_ascii=False)}</script>\n'


def head(code: str, path: str, title: str, desc: str, alts: dict[str, str], extra: str = "",
         og_type: str = "website", og_image: str = "/img/icon-512.png") -> str:
    canon = abs_url(path)
    links = "".join(f'<link rel="alternate" hreflang="{c}" href="{abs_url(p)}">\n' for c, p in alts.items())
    if "en" in alts:
        links += f'<link rel="alternate" hreflang="x-default" href="{abs_url(alts["en"])}">\n'
    return f"""<!doctype html>
<html lang="{code}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<meta name="robots" content="index, follow">
<link rel="canonical" href="{canon}">
{links}<meta name="color-scheme" content="dark light">
<!-- Hintergrund sofort setzen, sonst blitzt beim Seitenwechsel kurz Weiss auf -->
<style>html{{background:#080B14;color:#E8ECF7}}@media (prefers-color-scheme:light){{html{{background:#F3F4FA;color:#12162A}}}}</style>
<meta name="theme-color" content="#E7E9F5" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#141B33" media="(prefers-color-scheme: dark)">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="{e(C[code]['app_name'])}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{abs_url(og_image)}">
<meta property="og:locale" content="{C[code]['og_locale']}">
<link rel="icon" href="{href('/img/icon-48.png')}" sizes="48x48" type="image/png">
<link rel="apple-touch-icon" href="{href('/img/icon-180.png')}">
<link rel="stylesheet" href="{href('/css/site.css')}?v={STAMP}">
{extra}</head>
<body>
<a class="skip" href="#main">{e(C[code]['ui']['skip'])}</a>"""


def header(code: str, alts: dict[str, str], current: str = "") -> str:
    u = C[code]["ui"]
    other = [c for c in LOCALES if c != code]
    lang_links = "".join(
        f'<a href="{href(alts.get(c, home_path(c)))}" hreflang="{c}" lang="{c}">{e(C[c]["lang_name"])}</a>'
        for c in other)
    cur = ' aria-current="page"' if current == "guides" else ""
    return f"""
<header class="site">
  <div class="wrap wide">
    <a class="brand" href="{href(home_path(code))}"><img src="{href('/img/icon-48.png')}" width="30" height="30" alt="">Stay <span>Awake</span></a>
    <nav class="site" aria-label="{e(u['nav'])}">
      <a href="{href(guides_path(code))}"{cur}>{e(u['guides'])}</a>
      {lang_links}
    </nav>
  </div>
</header>"""


def footer(code: str) -> str:
    u = C[code]["ui"]
    lg = LEGAL[code]
    return f"""
<footer class="site">
  <div class="wrap wide foot">
    <p><strong>{e(C[code]['app_name'])}</strong> · {e(u['footer_tag'])}</p>
    <p><a href="{href(guides_path(code))}">{e(u['guides'])}</a> · <a href="{href(lg['privacy'])}">{e(u['privacy'])}</a> · <a href="{href(lg['imprint'])}" rel="nofollow">{e(u['imprint'])}</a> · <a href="{e(play_url(code))}">Google Play</a></p>
    <p class="fine">Nice Developments · {e(u['trademark'])}</p>
  </div>
</footer>
</body>
</html>
"""


def play_badge(code: str) -> str:
    u = C[code]["ui"]
    return (f'<p class="cta"><a class="btn" href="{e(play_url(code))}">{e(u["play_cta"])}</a>'
            f'<span class="cta__note">{e(u["play_note"])}</span></p>')


def phone(src: str, alt: str, *, eager: bool = False, w: int = 270) -> str:
    load = 'fetchpriority="high"' if eager else 'loading="lazy"'
    return (f'<figure class="phone"><img src="{href("/img/" + src)}" width="{w}" height="{w * SHOT_H // SHOT_W}" '
            f'alt="{e(alt)}" decoding="async" {load}></figure>')


def faq_block(items) -> str:
    return '<div class="faq">' + "".join(
        f'<details><summary>{e(q)}</summary><div class="answer">{"".join(f"<p>{inline(p)}</p>" for p in a)}</div></details>'
        for q, a in items) + "</div>"


def faq_ld(items) -> str:
    strip = lambda s: re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", s).replace("**", "").replace("*", "")
    return ld({"@context": "https://schema.org", "@type": "FAQPage",
               "mainEntity": [{"@type": "Question", "name": q,
                               "acceptedAnswer": {"@type": "Answer", "text": " ".join(strip(x) for x in a)}}
                              for q, a in items]})


def app_ld(code: str) -> dict:
    c = C[code]
    return {
        "@type": "MobileApplication",
        "name": c["app_name"],
        "operatingSystem": "Android",
        "applicationCategory": "UtilitiesApplication",
        "description": c["home"]["desc"],
        "url": abs_url(home_path(code)),
        "image": abs_url("/img/icon-512.png"),
        "inLanguage": code,
        "screenshot": [abs_url("/img/" + s) for s in c["home"]["shots"]],
        "installUrl": f"https://play.google.com/store/apps/details?id={PLAY_ID}",
        "offers": {"@type": "Offer", "price": "0", "priceCurrency": "EUR"},
        "publisher": {"@type": "Organization", "name": "Nice Developments"},
    }


def escalation(code: str) -> str:
    """Die vier Stufen eines Checks als Zeitleiste - das Erkennungszeichen der Seite."""
    h = C[code]["home"]
    items = "".join(
        f'<li class="esc__step esc__step--{i}"><span class="esc__t">{e(t)}</span>'
        f'<b>{e(name)}</b><span class="esc__d">{e(d)}</span></li>'
        for i, (t, name, d) in enumerate(h["steps"]))
    return f'<ol class="esc">{items}</ol>'


# ---------------------------------------------------------------- Startseite

LIVE = {
    "en": ("SESSION RUNNING", "until next check", "Unlimited", "Every 30 minutes · Tap or shake", "I am awake", "End session"),
    "de": ("SITZUNG LÄUFT", "bis zum nächsten Check", "Unbegrenzt", "Alle 30 Minuten · Tippen oder Schütteln", "Ich bin wach", "Sitzung beenden"),
}


def live_session(code: str) -> str:
    """Der Sitzungsbildschirm der App, nachgebaut in HTML: Der Countdown laeuft wirklich herunter
    und der Ring schrumpft mit (Werte und Farben wie ui/session/ActiveSessionScreen). Ohne
    JavaScript bleibt er bei 29:50 stehen - genau wie das Bildschirmfoto."""
    title, until, mode, every, awake, end = LIVE[code]
    alt = C[code]["home"]["shots"][C[code]["home"]["hero_shot"]]
    r = 44
    circ = 2 * 3.14159265 * r
    return f"""<figure class="phone live" role="img" aria-label="{e(alt)}">
      <div class="live__screen" aria-hidden="true">
        <span class="live__title">{e(title)}</span>
        <svg class="live__ring" viewBox="0 0 100 100"><circle class="live__glow" cx="50" cy="50" r="{r}"/><circle class="live__track" cx="50" cy="50" r="{r}"/><circle class="live__arc" cx="50" cy="50" r="{r}" stroke-dasharray="{circ:.2f}" stroke-dashoffset="{circ * 10 / 1800:.2f}" data-circ="{circ:.2f}"/></svg>
        <span class="live__time" data-left="1790">29:50</span>
        <span class="live__until">{e(until)}</span>
        <span class="live__mode">{e(mode)}</span>
        <span class="live__every">{e(every)}</span>
        <span class="live__btn">{e(awake)}</span>
        <span class="live__end">{e(end)}</span>
        <span class="live__bar"></span>
      </div>
    </figure>
    <script>
    (function () {{
      var t = document.querySelector(".live__time"), arc = document.querySelector(".live__arc");
      if (!t || !arc) return;
      var full = 1800, left = +t.dataset.left, circ = +arc.dataset.circ;
      function show() {{
        var m = Math.floor(left / 60), s = left % 60;
        t.textContent = m + ":" + (s < 10 ? "0" : "") + s;
        arc.style.strokeDashoffset = (circ * (full - left) / full).toFixed(2);
      }}
      setInterval(function () {{ left = left > 0 ? left - 1 : full; show(); }}, 1000);
    }})();
    </script>"""


def home(code: str) -> str:
    c = C[code]
    h = c["home"]
    u = c["ui"]
    alts = {x: home_path(x) for x in LOCALES}
    shots = h["shots"]
    feats = "".join(
        f"""<li class="feature">{phone(f['shot'], shots[f['shot']], w=230)}
      <div class="feature__text"><p class="kicker">{e(f['kicker'])}</p><h3>{e(f['h2'])}</h3>{''.join(f'<p>{inline(p)}</p>' for p in f['body'])}</div></li>"""
        for f in h["features"])
    nots = "".join(f"<li>{inline(x)}</li>" for x in h["nots"])
    why_cols = "".join(
        f'<div class="why__col why__col--{i}"><h3>{e(t)}</h3><ul>'
        + "".join(f"<li>{inline(x)}</li>" for x in items) + "</ul></div>"
        for i, (t, items) in enumerate(h["why"]))
    guide_cards = "".join(
        f'<li><a href="{href(guide_path(code, g))}"><b>{e(g["h1"])}</b><em>{e(g["teaser"])}</em></a></li>'
        for g in c["guides"])
    graph = {"@context": "https://schema.org", "@graph": [app_ld(code), {
        "@type": "WebSite", "name": c["app_name"], "url": abs_url(home_path(code)), "inLanguage": code}]}
    body = f"""{header(code, alts)}
<main id="main">
  <section class="hero"><div class="wrap wide hero__grid">
    <div class="hero__text">
      <p class="kicker">{e(h['kicker'])}</p>
      <h1>{e(h['h1'])}</h1>
      <p class="lead">{inline(h['lead'])}</p>
      <p class="who">{e(h['who'])}</p>
      {play_badge(code)}
    </div>
    <div class="hero__shot"><div class="halo" aria-hidden="true"></div>{live_session(code)}</div>
  </div></section>

  <section class="why"><div class="wrap wide">
    <h2>{e(h['why_h2'])}</h2>
    <p class="lead">{e(h['why_lead'])}</p>
    <div class="why__grid">{why_cols}</div>
  </div></section>

  <section class="steps-band"><div class="wrap wide">
    <h2>{e(h['steps_h2'])}</h2>
    <p class="lead">{e(h['steps_lead'])}</p>
    {escalation(code)}
  </div></section>

  <section class="features"><div class="wrap wide">
    <h2>{e(h['features_h2'])}</h2>
    <ul class="feature-grid">{feats}</ul>
  </div></section>

  <section class="band"><div class="wrap wide band__grid">
    <div>
      <h2>{e(h['nots_h2'])}</h2>
      <ul class="ticks">{nots}</ul>
      <p><a href="{href(LEGAL[code]['privacy'])}">{e(h['privacy_link'])}</a></p>
    </div>
    <div class="limits">
      <h2>{e(h['limits_h2'])}</h2>
      <p>{e(h['limits'])}</p>
    </div>
  </div></section>

  <section><div class="wrap wide">
    <h2>{e(h['guides_h2'])}</h2>
    <p class="lead">{e(h['guides_lead'])}</p>
    <ul class="tiles cols">{guide_cards}</ul>
  </div></section>

  <section><div class="wrap">
    <h2>{e(u['faq'])}</h2>
    {faq_block(h['faq'])}
  </div></section>

  <section class="final"><div class="wrap">
    <h2>{e(h['final_h2'])}</h2>
    <p class="lead">{e(h['final_body'])}</p>
    {play_badge(code)}
  </div></section>
</main>
{footer(code)}"""
    return head(code, home_path(code), h["title"], h["desc"], alts, extra=ld(graph) + faq_ld(h["faq"])) + body


# ---------------------------------------------------------------- Anleitungen

def block(code: str, b) -> str:
    if isinstance(b, str):
        return f"<p>{inline(b)}</p>"
    if "steps" in b:
        return '<ol class="steps">' + "".join(f"<li>{inline(x)}</li>" for x in b["steps"]) + "</ol>"
    if "list" in b:
        return "<ul>" + "".join(f"<li>{inline(x)}</li>" for x in b["list"]) + "</ul>"
    if "note" in b:
        return f'<p class="note">{inline(b["note"])}</p>'
    if "table" in b:
        head_, *rows = b["table"]
        th = "".join(f'<th scope="col">{e(x)}</th>' for x in head_)
        trs = "".join("<tr>" + "".join(
            (f'<th scope="row">{inline(x)}</th>' if j == 0 and not head_[0] else f"<td>{inline(x)}</td>")
            for j, x in enumerate(r)) + "</tr>" for r in rows)
        return f'<div class="table-scroll"><table><thead><tr>{th}</tr></thead><tbody>{trs}</tbody></table></div>'
    raise ValueError(f"Unbekannter Block: {b}")


def guide_alts(gid: str) -> dict[str, str]:
    return {c: guide_path(c, g) for c in LOCALES if (g := guide_by_id(c, gid))}


def guide_page(code: str, g: dict) -> str:
    c = C[code]
    u = c["ui"]
    alts = guide_alts(g["id"])
    path = guide_path(code, g)
    toc = "".join(f'<li><a href="#{sid}">{e(h)}</a></li>' for sid, h, _ in g["sections"])
    secs = "".join(f'<h2 id="{sid}">{e(h)}</h2>' + "".join(block(code, b) for b in blocks)
                   for sid, h, blocks in g["sections"])
    app = g["app"]
    app_html = (f'<section class="app-box" aria-labelledby="app-h"><div class="app-box__text">'
                f'<p class="kicker">{e(u["with_app"])}</p><h2 id="app-h">{e(app["h2"])}</h2>'
                + "".join(block(code, b) for b in app["body"])
                + f'{play_badge(code)}</div>'
                + f'<div class="app-box__shot">{phone(app["shot"], app["alt"], w=220)}</div>'
                + "</section>")
    others = "".join(f'<li><a href="{href(guide_path(code, o))}">{e(o["h1"])}</a></li>'
                     for o in c["guides"] if o["id"] != g["id"])
    crumbs = ld({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": c["app_name"], "item": abs_url(home_path(code))},
        {"@type": "ListItem", "position": 2, "name": u["guides"], "item": abs_url(guides_path(code))},
        {"@type": "ListItem", "position": 3, "name": g["h1"], "item": abs_url(path)}]})
    article = ld({"@context": "https://schema.org", "@type": "Article", "headline": g["h1"],
                  "description": g["desc"], "inLanguage": code, "dateModified": g["updated"],
                  "datePublished": g["updated"], "url": abs_url(path), "mainEntityOfPage": abs_url(path),
                  "image": abs_url("/img/" + app["shot"]),
                  "author": {"@type": "Organization", "name": "Nice Developments"},
                  "publisher": {"@type": "Organization", "name": "Nice Developments",
                                "logo": {"@type": "ImageObject", "url": abs_url("/img/icon-512.png")}}})
    body = f"""{header(code, alts, 'guides')}
<main id="main">
  <article class="guide">
    <div class="wrap">
      <nav class="crumbs" aria-label="{e(u['crumbs'])}"><a href="{href(home_path(code))}">{e(c['app_name'])}</a> / <a href="{href(guides_path(code))}">{e(u['guides'])}</a></nav>
      <h1>{e(g['h1'])}</h1>
      <p class="lead answer">{inline(g['answer'])}</p>
      <p class="stand">{e(u['updated'])} {e(g['updated_label'])}</p>
      <nav class="toc" aria-label="{e(u['toc'])}"><p>{e(u['toc'])}</p><ol>{toc}<li><a href="#faq">{e(u['faq'])}</a></li></ol></nav>
      {secs}
      {app_html}
      <h2 id="faq">{e(u['faq'])}</h2>
      {faq_block(g['faq'])}
      <h2>{e(u['more_guides'])}</h2>
      <ul class="related">{others}</ul>
    </div>
  </article>
</main>
{footer(code)}"""
    return head(code, path, g["title"], g["desc"], alts, extra=article + crumbs + faq_ld(g["faq"]),
                og_type="article") + body


def guides_index(code: str) -> str:
    c = C[code]
    u = c["ui"]
    gi = c["guides_index"]
    alts = {x: guides_path(x) for x in LOCALES}
    cards = "".join(
        f'<li><a href="{href(guide_path(code, g))}"><b>{e(g["h1"])}</b><em>{e(g["teaser"])}</em></a></li>'
        for g in c["guides"])
    items = ld({"@context": "https://schema.org", "@type": "ItemList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "url": abs_url(guide_path(code, g)), "name": g["h1"]}
        for i, g in enumerate(c["guides"])]})
    body = f"""{header(code, alts, 'guides')}
<main id="main">
  <div class="wrap">
    <h1>{e(gi['h1'])}</h1>
    <p class="lead">{e(gi['lead'])}</p>
    <ul class="tiles">{cards}</ul>
    <div class="app-box slim"><div class="app-box__text"><p class="kicker">{e(u['with_app'])}</p><p>{inline(gi['app'])}</p>{play_badge(code)}</div></div>
  </div>
</main>
{footer(code)}"""
    return head(code, guides_path(code), gi["title"], gi["desc"], alts, extra=items) + body


# ---------------------------------------------------------------- Schreiben

STAMP = "dev"

# Chrome unter Windows trennt Deutsch nicht selbst: weiche Trennstellen fuer lange Woerter,
# nur im sichtbaren Teil ausserhalb von h1 und script.
WEICH = {"de": [("Verlässlichkeitsprüfung", "Verlässlichkeits&shy;prüfung"),
                ("Benachrichtigungen", "Benach&shy;richtigungen"), ("Sperrbildschirm", "Sperr&shy;bildschirm"),
                ("Akku-Optimierung", "Akku-Opti&shy;mierung")]}


def trennen(code: str, page: str) -> str:
    regeln = WEICH.get(code)
    if not regeln:
        return page
    kopf, rumpf = page.split("<body>", 1)
    teile = re.split(r"(<h1[^>]*>.*?</h1>|<script[^>]*>.*?</script>|<[^>]+>)", rumpf, flags=re.S)
    for i in range(0, len(teile), 2):
        for alt, neu in regeln:
            teile[i] = teile[i].replace(alt, neu)
    return kopf + "<body>" + "".join(teile)


def write(path: str, content: str) -> None:
    target = ROOT / path.lstrip("/") / "index.html"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding="utf-8", newline="\n")


def redirect_page(target: str) -> str:
    url = href(target)
    return (f'<!doctype html><html><head><meta charset="utf-8"><title>Stay Awake</title>'
            f'<meta name="color-scheme" content="dark light"><style>html{{background:#080B14;color:#E8ECF7}}@media (prefers-color-scheme:light){{html{{background:#F3F4FA;color:#12162A}}}}</style>'
            f'<meta name="robots" content="noindex"><link rel="canonical" href="{abs_url(target)}">'
            f'<meta http-equiv="refresh" content="0; url={url}"></head>'
            f'<body><p><a href="{url}">{abs_url(target)}</a></p></body></html>\n')


def write_redirects() -> int:
    """Alte Adressen -> neue. Die Wurzel "/" ist jetzt die englische Startseite und bleibt."""
    n = 0
    for code, (old_home, old_guides) in OLD.items():
        moves = [(old_home, home_path(code)), (old_guides, guides_path(code))]
        moves += [(old_guides + g["slug"] + "/", guide_path(code, g)) for g in C[code]["guides"]]
        for old, new in moves:
            if old == new or old == "/":
                continue
            write(old, redirect_page(new))
            n += 1
    return n


def main() -> None:
    global STAMP
    STAMP = hashlib.sha1((ROOT / "css/site.css").read_bytes()).hexdigest()[:8]
    pages: list[tuple[str, dict[str, str]]] = []
    for code in LOCALES:
        write(home_path(code), trennen(code, home(code)))
        pages.append((home_path(code), {x: home_path(x) for x in LOCALES}))
        write(guides_path(code), trennen(code, guides_index(code)))
        pages.append((guides_path(code), {x: guides_path(x) for x in LOCALES}))
        for g in C[code]["guides"]:
            write(guide_path(code, g), trennen(code, guide_page(code, g)))
            pages.append((guide_path(code, g), guide_alts(g["id"])))

    urls = []
    for path, alts in pages:
        x = "".join(f'\n    <xhtml:link rel="alternate" hreflang="{c}" href="{abs_url(p)}"/>' for c, p in alts.items())
        if "en" in alts:
            x += f'\n    <xhtml:link rel="alternate" hreflang="x-default" href="{abs_url(alts["en"])}"/>'
        urls.append(f"  <url>\n    <loc>{abs_url(path)}</loc>{x}\n  </url>")
    (ROOT / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
        + "\n".join(urls) + "\n</urlset>\n", encoding="utf-8", newline="\n")
    (ROOT / "robots.txt").write_text(
        "# Startseiten und Anleitungen sind indexierbar und stehen in der Sitemap.\n"
        "# Datenschutz, Impressum, Privacy und Imprint tragen weiter noindex (Name und Anschrift).\n"
        f"User-agent: *\nAllow: /\nDisallow: {BASE}/tools/\n\nSitemap: {abs_url('/sitemap.xml')}\n",
        encoding="utf-8", newline="\n")
    print(f"{len(urls)} Seiten gebaut, {write_redirects()} Weiterleitungen, Stempel {STAMP}")


if __name__ == "__main__":
    main()
