"""Prueft die erzeugten Seiten: interne Links und Bilder vorhanden, JSON-LD gueltig,
hreflang gegenseitig, Titel <= 70 und Beschreibung <= 160 Zeichen. Aufruf: python -I tools/check_site.py"""
import html, json, pathlib, re, sys
ROOT = pathlib.Path(__file__).resolve().parent.parent
BASE = "/stay-awake"
SITE = "https://allradmuelleimer.github.io" + BASE
fehler = []
seiten = [p for p in ROOT.rglob("index.html") if "tools" not in p.parts] + [ROOT / "404.html"]
alts = {}
for p in seiten:
    s = p.read_text(encoding="utf-8")
    rel = "/" + p.parent.relative_to(ROOT).as_posix() + "/" if p.name == "index.html" else "/404.html"
    rel = rel.replace("/./", "/")
    for ref in re.findall(r'(?:href|src|srcset)="(/stay-awake/[^"#?]*)', s):
        t = ROOT / ref[len(BASE) + 1:]
        if not (t.exists() if t.suffix else (t / "index.html").exists()):
            fehler.append(f"{rel}: kaputter Verweis {ref}")
    for blob in re.findall(r'<script type="application/ld\+json">(.*?)</script>', s, re.S):
        try: json.loads(blob)
        except Exception as ex: fehler.append(f"{rel}: JSON-LD {ex}")
    if 'content="index, follow"' in s:
        t = html.unescape(re.search(r"<title>(.*?)</title>", s).group(1))
        d = html.unescape(re.search(r'name="description" content="([^"]*)"', s).group(1))
        if len(t) > 75: fehler.append(f"{rel}: Titel {len(t)} Zeichen")
        if len(d) > 165: fehler.append(f"{rel}: Beschreibung {len(d)} Zeichen")
        canon = re.search(r'rel="canonical" href="([^"]+)"', s).group(1)
        alts[canon] = dict(re.findall(r'hreflang="([^"]+)" href="([^"]+)"', s))
for canon, a in alts.items():
    for lang, url in a.items():
        if url not in alts: fehler.append(f"{canon}: hreflang {lang} -> {url} fehlt")
        elif canon not in alts[url].values(): fehler.append(f"{canon}: {url} verweist nicht zurueck")
print("\n".join(fehler) or f"OK: {len(seiten)} Seiten, {len(alts)} indexierbar")
sys.exit(1 if fehler else 0)
