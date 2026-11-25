# Branches Bible Club

Static site for GitHub Pages: Dutch at `/`, English at `/en/`.

## How to edit

Don't edit `index.html` or `en/index.html` by hand. They are generated.

- **Text and layout:** `src/site.html`. Write every text twice, as `<span lang="nl">…</span><span lang="en">…</span>`.
- **New lesson after a Thursday:** add it at the **top** of `src/lessons.json`.
- **Sign-up form:** paste your form-service URL (Formspree, for example) into `FORM_ENDPOINT` at the bottom of `src/site.html`.
- **Custom domain:** change `BASE` at the top of `build.py`.

Then run:

```sh
python3 build.py
```

The build writes `index.html`, `en/index.html`, `404.html`, `sitemap.xml`, `robots.txt` and `site.webmanifest`. Commit those files together with your source changes.

## Before launch (owner)

1. Fill in the privacy contact (`[naam contactpersoon]`, `[e-mail]`, `[contact name]`, `[email]`) in `src/site.html`.
2. Connect the form (`FORM_ENDPOINT`). If you use a non-EU service, name it in the privacy text.
3. Raé confirms the "every member is called a Branch" line and adds the club's story, with the city if possible. Look for `TODO(Raé)` in `src/site.html`.
4. Once the time and place are fixed: add them to the hero pill and the FAQ, and add Event schema (see `docs/seo.md` §4c).
5. Google Search Console: verify the site and submit `sitemap.xml`. Then set up Bing Webmaster Tools.
6. Recommended: a custom domain (for example `branchesbibleclub.nl`). `robots.txt` only takes effect at a domain root.

The SEO rationale, keywords and schema decisions are in `docs/seo.md`. The site files are the final version where the two differ.

Fonts are self-hosted (SIL OFL), so no visitor data goes to Google. The site has no cookies and no tracking.
