#!/usr/bin/env python3
"""Build the Branches Bible Club site.

    python3 build.py

Reads  src/site.html   (one bilingual template: every text exists as
                        <span lang="nl">…</span><span lang="en">…</span>)
       src/lessons.json (the lessons; add a new session at the TOP)
Writes index.html       (Dutch, the default page)
       en/index.html    (English)
       404.html, sitemap.xml

Template tokens: {{root}} relative path to the site root, {{url}} absolute
URL of this page, {{alt_url}} the other language, {{base}} site base URL,
{{lessons}} the rendered lessons, {{updated}} build date.
Head-only snippets live in <template data-lang="nl|en">…</template> blocks.
"""
import html, json, re, datetime
from html.parser import HTMLParser
from pathlib import Path

BASE = "https://anth-05.github.io/branchesbibleclub/"  # change when a custom domain is connected
HERE = Path(__file__).parent
VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "source", "track", "wbr", "use", "path", "circle", "rect"}
SVG_CASE = {"textpath": "textPath", "lineargradient": "linearGradient", "radialgradient": "radialGradient", "clippath": "clipPath", "foreignobject": "foreignObject"}
LABELS = {
    "nl": {"{{navlabel}}": "Hoofdmenu", "{{brandlabel}}": "Branches Bible Club, naar het begin", "{{langlabel}}": "Taal",
           "{{vcardlabel}}": "Kernvers", "{{totoplabel}}": "Naar boven",
           "{{heroalt}}": "Illustratie: vier vrouwen op een kleed met opengeslagen Bijbels, koffie, croissants en kaarsjes, met het logo van Branches Bible Club"},
    "en": {"{{navlabel}}": "Main menu", "{{brandlabel}}": "Branches Bible Club, back to top", "{{langlabel}}": "Language",
           "{{vcardlabel}}": "Anchor verse", "{{totoplabel}}": "Back to top",
           "{{heroalt}}": "Illustration: four women on a rug with open Bibles, coffee, croissants and candles, with the Branches Bible Club logo"},
}
NUMERALS = ["i", "ii", "iii", "iv", "v", "vi"]


class LangFilter(HTMLParser):
    """Drops every element whose lang= is the other language (with its children)."""

    def __init__(self, keep):
        super().__init__(convert_charrefs=False)
        self.keep, self.out, self.skip = keep, [], 0

    def _drop(self, attrs, tag=""):
        d = dict(attrs)
        if "hreflang" in d:  # language-switch links keep their lang attribute on both pages
            return False
        lang = d.get("lang") if tag != "template" else d.get("data-lang")
        return lang in ("nl", "en") and lang != self.keep

    def handle_starttag(self, tag, attrs):
        selfclosing = self.get_starttag_text().rstrip().endswith("/>")
        if self.skip:
            if tag not in VOID and not selfclosing:
                self.skip += 1
            return
        if self._drop(attrs, tag):
            if tag not in VOID and not selfclosing:
                self.skip = 1
            return
        text = self.get_starttag_text()
        # the kept language no longer needs its marker on inline spans
        if tag == "span" and dict(attrs).get("lang") == self.keep and len(attrs) == 1:
            self.out.append("\x00")  # unwrap marker
            return
        if tag == "template" and dict(attrs).get("data-lang") == self.keep:
            self.out.append("\x01")
            return
        self.out.append(text)

    def handle_startendtag(self, tag, attrs):
        if not self.skip and not self._drop(attrs, tag):
            self.out.append(self.get_starttag_text())

    def handle_endtag(self, tag):
        if self.skip:
            if tag not in VOID:
                self.skip -= 1
            return
        self.out.append(f"</{SVG_CASE.get(tag, tag)}>")

    def handle_data(self, d):
        if not self.skip:
            self.out.append(d)

    def handle_entityref(self, n):
        self.handle_data(f"&{n};")

    def handle_charref(self, n):
        self.handle_data(f"&#{n};")

    def handle_comment(self, d):
        if not self.skip and not d.strip().startswith("src:"):
            self.out.append(f"<!--{d}-->")

    def handle_decl(self, d):
        self.out.append(f"<!{d}>")

    def result(self):
        # re-balance unwrapped spans / templates: drop the matching close tags
        s, stack, res = "".join(self.out), [], []
        for tok in re.split(r"(\x00|\x01|<span\b[^>]*>|</span>|<template\b[^>]*>|</template>)", s):
            if tok in ("\x00", "\x01"):
                stack.append(None)
            elif tok.startswith("<span") or tok.startswith("<template"):
                stack.append(tok)
                res.append(tok)
            elif tok in ("</span>", "</template>"):
                if stack and stack.pop() is None:
                    continue
                res.append(tok)
            else:
                res.append(tok)
        return "".join(res)


def esc(s):
    return html.escape(s, quote=False)


def render_lessons(lessons, lang):
    out = []
    for l in lessons:
        keys = "".join(
            f'<li><i aria-hidden="true">{NUMERALS[i]}</i><span><strong>{esc(k[lang][0])}</strong> {esc(k[lang][1])}</span></li>'
            for i, k in enumerate(l["keys"]))
        asks = "".join(f"<p>{esc(q)}</p>" for q in l["ask"][lang])
        summary = "Om over na te denken &amp; gebed" if lang == "nl" else "To reflect on &amp; pray"
        pray = "Gebed" if lang == "nl" else "Prayer"
        out.append(
            f'<article class="entry" id="sessie-{l["n"]}" aria-labelledby="les-{l["n"]}">'
            f'<p class="date"><b>{l["n"]}</b>{esc(l["date"][lang])}</p><div>'
            f'<p class="label">{esc(l["ref"][lang])}</p><h3 id="les-{l["n"]}">{esc(l["title"][lang])}</h3>'
            f'<ol class="keys">{keys}</ol>'
            f'<details><summary>{summary}</summary><div class="in">{asks}'
            f'<p class="pray"><span class="label">{pray}</span>{esc(l["pray"][lang])}</p></div></details>'
            f'</div></article>')
    return "\n".join(out)


def build():
    src = (HERE / "src/site.html").read_text()
    lessons = json.loads((HERE / "src/lessons.json").read_text())
    today = datetime.date.today().isoformat()
    pages = {"nl": ("index.html", BASE, BASE + "en/", ""), "en": ("en/index.html", BASE + "en/", BASE, "../")}
    for lang, (out, url, alt, root) in pages.items():
        p = LangFilter(lang)
        p.feed(src.replace("{{lessons}}", render_lessons(lessons, lang)))
        page = p.result()
        for k, v in {"{{lang}}": lang, "{{root}}": root, "{{url}}": url, "{{alt_url}}": alt, "{{base}}": BASE, "{{updated}}": today, **LABELS[lang]}.items():
            page = page.replace(k, v)
        page = re.sub(r"\n\s*\n+", "\n", page)
        assert "{{" not in page, "unreplaced token"
        (HERE / out).parent.mkdir(exist_ok=True)
        (HERE / out).write_text(page)
        print("wrote", out, len(page), "bytes")

    (HERE / "sitemap.xml").write_text(f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">
  <url>
    <loc>{BASE}</loc>
    <lastmod>{today}</lastmod>
    <xhtml:link rel="alternate" hreflang="nl" href="{BASE}"/>
    <xhtml:link rel="alternate" hreflang="en" href="{BASE}en/"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="{BASE}"/>
  </url>
  <url>
    <loc>{BASE}en/</loc>
    <lastmod>{today}</lastmod>
    <xhtml:link rel="alternate" hreflang="nl" href="{BASE}"/>
    <xhtml:link rel="alternate" hreflang="en" href="{BASE}en/"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="{BASE}"/>
  </url>
</urlset>
""")
    (HERE / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {BASE}sitemap.xml\n")
    (HERE / "site.webmanifest").write_text(json.dumps({
        "name": "Branches Bible Club", "short_name": "BBC", "lang": "nl", "start_url": "./", "scope": "./",
        "display": "browser", "background_color": "#F4DFC0", "theme_color": "#F4DFC0",
        "icons": [{"src": "assets/icon-192.png", "sizes": "192x192", "type": "image/png"},
                  {"src": "assets/icon-512.png", "sizes": "512x512", "type": "image/png"},
                  {"src": "assets/icon-maskable-512.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable"}]}, indent=2) + "\n")
    path = BASE.split("github.io", 1)[-1] if "github.io" in BASE else "/"
    (HERE / "404.html").write_text(f"""<!doctype html>
<html lang="nl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Pagina niet gevonden · Branches Bible Club</title><meta name="robots" content="noindex">
<link rel="icon" href="{path}favicon.svg?v=2" type="image/svg+xml"><link rel="icon" href="{path}favicon.ico?v=2" sizes="32x32">
<link rel="stylesheet" href="{path}assets/fonts.css">
<style>body{{margin:0;min-height:100svh;display:grid;place-items:center;background:#F4DFC0;color:#3E2A1F;font:17px/1.6 Figtree,system-ui,sans-serif;padding:24px}}
main{{max-width:34rem}}h1{{font:400 clamp(40px,8vw,64px)/1 Newsreader,Georgia,serif;margin:16px 0}}p{{margin:0 0 12px;color:#5A4334}}
a{{display:inline-flex;align-items:center;min-height:48px;padding:0 22px;margin:12px 12px 0 0;border-radius:18px 22px 16px 24px;background:#B4402A;color:#FFF6EA;text-decoration:none;font-weight:600}}
a.l{{background:transparent;color:#3E2A1F;box-shadow:inset 0 0 0 2px #3E2A1F}}a:focus-visible{{outline:2.5px solid #9E3522;outline-offset:3px}}</style></head>
<body><main><img src="{path}favicon.svg" width="56" height="56" alt="">
<h1>Deze pagina is er niet.</h1><p>De link klopt niet meer, of de pagina is verhuisd.</p><p lang="en">This page doesn’t exist. The link may be out of date.</p>
<a href="{path}">Naar de homepage</a><a class="l" href="{path}en/" lang="en" hreflang="en">English homepage</a></main></body></html>
""")
    print("wrote sitemap.xml, robots.txt, site.webmanifest, 404.html")


if __name__ == "__main__":
    build()
