# Stay Awake — Website

Startseite (en + de), sieben Anleitungen je Sprache, dazu die Datenschutzerklärung, die
Google Play verlangt, und das Impressum.

**Live:** <https://allradmuelleimer.github.io/stay-awake/> – **Englisch ist die Hauptseite**
(Wurzel `/`, Anleitungen `/guides/`), jede weitere Sprache liegt unter `/<code>/` (Deutsch:
`/de/`, `/de/anleitungen/`). Entscheidung des Inhabers vom 21.11.2026. Die Rechtsseiten bleiben,
wo sie sind (`/datenschutz/` ist bei Google Play eingetragen). Die am 21.11. kurz gültigen
Adressen (`/en/…`, `/anleitungen/…`) leiten per Meta-Refresh weiter.

Seit 21.11.2026 erzeugt ein kleines Python-Skript Startseiten, Anleitungen, Sitemap und robots.txt
(kein Framework, keine Abhängigkeiten). Texte stehen in `tools/content_de.py` und
`tools/content_en.py`, Aufbau in `tools/build.py`, Gestaltung in `css/site.css`:

```
python -I tools/build.py        # baut alle erzeugten Seiten neu
python -I tools/check_site.py   # Links, Bilder, JSON-LD, hreflang, Titel-/Beschreibungslänge
```

Die erzeugten `index.html` nie direkt ändern. Startseiten und Anleitungen sind **indexierbar**
und stehen in `sitemap.xml`; Datenschutz, Impressum, Privacy, Imprint und 404 bleiben
handgeschrieben und `noindex` (Name und Anschrift). Bilder in `img/` sind echte App-Aufnahmen
vom Emulator. Verboten in allen Texten: Autofahren/Straßenverkehr (außer dem Grenzen-Satz aus dem
Play-Eintrag), Arbeitsschutz-Versprechen, „verhindert Einschlafen“, medizinische Ratschläge.

```
index.html              Startseite DE (inkl. Hinweis "kein Sicherheitssystem")
datenschutz/            Datenschutzerklärung DE   <- diese URL geht zu Google Play
impressum/              Impressum DE (§ 5 DDG)
privacy/                Privacy policy EN
imprint/                Imprint EN
404.html
css/site.css            Das einzige Stylesheet, Palette wie in der App (ui/theme/Color.kt)
.nojekyll               Verhindert, dass GitHub Pages die Dateien durch Jekyll schickt
robots.txt / sitemap.xml  erzeugt von tools/build.py
```

---

## Gehostet auf GitHub Pages

Kein dritter Dienst: Das Repository *ist* der Server. Pages liefert aus, was im Branch `main`
im Wurzelverzeichnis liegt — ein `git push` genügt, eine Minute später ist die Änderung online.

Einmalige Einrichtung (vom Auftraggeber auszuführen):

```bash
gh repo create allradmuelleimer/stay-awake --public \
  --description "Stay Awake – Datenschutzerklärung und Impressum" \
  --source . --remote origin --push
gh api -X POST repos/allradmuelleimer/stay-awake/pages \
  -f 'source[branch]=main' -f 'source[path]=/'
```

Status jederzeit nachsehen:

```bash
gh api repos/allradmuelleimer/stay-awake/pages --jq '.status, .html_url'
```

---

## Wichtig: die Pfade hängen am Repository-Namen

Pages liefert Projektseiten unter `/<repo-name>/` aus, nicht unter `/`. Deshalb stehen alle
internen Verweise als `/stay-awake/…` im Quelltext. **Wird das Repository umbenannt,
bricht jede CSS- und Navigationsverknüpfung**, bis alles mitgezogen ist:

```bash
grep -rl "stay-awake" . --exclude-dir=.git \
  | xargs sed -i 's|stay-awake|NEUER-NAME|g'
```

Die Adresse der Datenschutzerklärung wird bei Google Play im Feld „Datenschutzerklärung"
eingetragen (siehe `../docs/play-console.md`).

---

## Änderungen an der Datenschutzerklärung

Die Quelle ist `../docs/datenschutzerklaerung.md`. Wer sie ändert, muss
`datenschutz/index.html` **und** `privacy/index.html` nachziehen und oben das Datum
hochsetzen — sonst weichen App-Text (`settings_privacy_text`), Store-Angabe (Datensicherheit)
und Wahrheit voneinander ab.
