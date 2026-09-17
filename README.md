# Stay Awake — Website

Die öffentliche Datenschutzerklärung, die Google Play verlangt, dazu Impressum und eine
kleine Startseite. Deutsch und englisch.

Reines HTML und ein Stylesheet. **Kein Build-Schritt, kein Framework, keine Abhängigkeiten.**

**Künftig live unter:** <https://allradmuelleimer.github.io/stay-awake-website/>
(noch nicht veröffentlicht — Befehle unten)

```
index.html              Startseite DE (inkl. Hinweis "kein Sicherheitssystem")
datenschutz/            Datenschutzerklärung DE   <- diese URL geht zu Google Play
impressum/              Impressum DE (§ 5 DDG)
privacy/                Privacy policy EN
imprint/                Imprint EN
404.html
css/site.css            Das einzige Stylesheet, Palette wie in der App (ui/theme/Color.kt)
.nojekyll               Verhindert, dass GitHub Pages die Dateien durch Jekyll schickt
robots.txt  sitemap.xml
```

---

## Gehostet auf GitHub Pages

Kein dritter Dienst: Das Repository *ist* der Server. Pages liefert aus, was im Branch `main`
im Wurzelverzeichnis liegt — ein `git push` genügt, eine Minute später ist die Änderung online.

Einmalige Einrichtung (vom Auftraggeber auszuführen):

```bash
gh repo create allradmuelleimer/stay-awake-website --public \
  --description "Stay Awake – Datenschutzerklärung und Impressum" \
  --source . --remote origin --push
gh api -X POST repos/allradmuelleimer/stay-awake-website/pages \
  -f 'source[branch]=main' -f 'source[path]=/'
```

Status jederzeit nachsehen:

```bash
gh api repos/allradmuelleimer/stay-awake-website/pages --jq '.status, .html_url'
```

---

## Wichtig: die Pfade hängen am Repository-Namen

Pages liefert Projektseiten unter `/<repo-name>/` aus, nicht unter `/`. Deshalb stehen alle
internen Verweise als `/stay-awake-website/…` im Quelltext. **Wird das Repository umbenannt,
bricht jede CSS- und Navigationsverknüpfung**, bis alles mitgezogen ist:

```bash
grep -rl "stay-awake-website" . --exclude-dir=.git \
  | xargs sed -i 's|stay-awake-website|NEUER-NAME|g'
```

Die Adresse der Datenschutzerklärung wird bei Google Play im Feld „Datenschutzerklärung"
eingetragen (siehe `../docs/play-console.md`).

---

## Änderungen an der Datenschutzerklärung

Die Quelle ist `../docs/datenschutzerklaerung.md`. Wer sie ändert, muss
`datenschutz/index.html` **und** `privacy/index.html` nachziehen und oben das Datum
hochsetzen — sonst weichen App-Text (`settings_privacy_text`), Store-Angabe (Datensicherheit)
und Wahrheit voneinander ab.
