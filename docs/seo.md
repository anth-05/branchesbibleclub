# BBC: SEO and metadata plan

Base URL (one value, swap when the custom domain goes live): `BASE = https://anth-05.github.io/branchesbibleclub/`
Every URL below starts with `https://anth-05.github.io/branchesbibleclub/`. To change the domain, find and replace that string in both `<head>` blocks, both JSON-LD graphs and `sitemap.xml`.

Pages: NL at `BASE` (x-default), EN at `BASE + en/`.

---

## 1. Keyword map

Research: Dutch searchers use **"bijbelstudie voor vrouwen"** and **"bijbelkring / vrouwenkring"**, and the established networks use phrasing like "groep vrouwen", "Bijbelstudie-avond" and "samen de Bijbel lezen" (Bijbelgenootschap *Zij Lacht*, Leger des Heils, EO "kringavond"). The SERP is mostly study material, with very few listings for real groups, so a group page can rank on a specific phrase.

| | NL (/) | EN (/en/) |
|---|---|---|
| **Primary** | bijbelstudie voor vrouwen | women's bible study |
| Secondary | bijbelkring vrouwen / vrouwenkring | bible study group for women |
| | samen de Bijbel lezen | christian women's group |
| | christelijke vrouwengroep | bible study every other Thursday |
| | bijbelstudie donderdag(avond) | (English-speaking) women's bible study Netherlands *(only once a location is confirmed)* |
| | intimiteit met Christus / Johannes 15 de wijnstok en de ranken | intimacy with Christ / John 15 vine and branches |
| Brand | Branches Bible Club | Branches Bible Club |

Note: "BBC" cannot rank on its own because the broadcaster owns that term. Always write the full name "Branches Bible Club" in metadata, and use "BBC" only after the full name.
Local modifier: once the city is known, add "in [stad]" to the title, the description and the FAQ. The local modifier is the biggest ranking lever this site has.

---

## 2. Title and meta description

| | Text | Chars |
|---|---|---|
| NL title | `Bijbelstudie voor vrouwen op donderdag \| Branches Bible Club` | **60** |
| NL description | `Bijbelstudie voor vrouwen: om de week op donderdag samen de Bijbel lezen, praten en bidden bij koffie en kaarslicht. Kom dichter bij Christus. Schuif aan!` | **154** |
| EN title | `Women's Bible Study Group, Thursdays \| Branches Bible Club` | **58** |
| EN description | `Women's Bible study every other Thursday: read Scripture, talk and pray together over coffee and candlelight. Grow closer to Christ. Pull up a chair!` | **149** |

Once the location is known, the title becomes, for example, `Bijbelstudie voor vrouwen in [Stad] | Branches Bible Club`. Keep it at 60 characters or fewer.
Remove the `document.title` swap from the JS, because each page now has its own static title.

---

## 3. `<head>` blocks

### NL: `/index.html` (`<html lang="nl">`)
```html
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Bijbelstudie voor vrouwen op donderdag | Branches Bible Club</title>
<meta name="description" content="Bijbelstudie voor vrouwen: om de week op donderdag samen de Bijbel lezen, praten en bidden bij koffie en kaarslicht. Kom dichter bij Christus. Schuif aan!">
<meta name="robots" content="index, follow, max-image-preview:large">
<link rel="canonical" href="https://anth-05.github.io/branchesbibleclub/">
<link rel="alternate" hreflang="nl" href="https://anth-05.github.io/branchesbibleclub/">
<link rel="alternate" hreflang="en" href="https://anth-05.github.io/branchesbibleclub/en/">
<link rel="alternate" hreflang="x-default" href="https://anth-05.github.io/branchesbibleclub/">
<meta name="author" content="Branches Bible Club">
<meta name="application-name" content="Branches Bible Club">
<meta name="apple-mobile-web-app-title" content="BBC">
<meta name="theme-color" content="#F4DFC0">
<!-- <meta name="google-site-verification" content="OWNER_TOKEN"> -->

<meta property="og:type" content="website">
<meta property="og:site_name" content="Branches Bible Club">
<meta property="og:locale" content="nl_NL">
<meta property="og:locale:alternate" content="en_GB">
<meta property="og:url" content="https://anth-05.github.io/branchesbibleclub/">
<meta property="og:title" content="Bijbelstudie voor vrouwen, om de week op donderdag">
<meta property="og:description" content="Samen de Bijbel lezen, praten en bidden bij koffie en kaarslicht. Een kring van vrouwen die dichter bij Christus wil komen. Schuif aan!">
<meta property="og:image" content="https://anth-05.github.io/branchesbibleclub/assets/og.jpg">
<meta property="og:image:type" content="image/jpeg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Illustratie van vier vrouwen op een kleed met opengeslagen Bijbels, koffie en kaarsjes, met het logo van Branches Bible Club">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Bijbelstudie voor vrouwen, om de week op donderdag">
<meta name="twitter:description" content="Samen de Bijbel lezen, praten en bidden bij koffie en kaarslicht. Schuif aan bij Branches Bible Club.">
<meta name="twitter:image" content="https://anth-05.github.io/branchesbibleclub/assets/og.jpg">
<meta name="twitter:image:alt" content="Illustratie van vier vrouwen op een kleed met opengeslagen Bijbels, koffie en kaarsjes">

<link rel="icon" href="assets/favicon.ico" sizes="32x32">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="assets/apple-touch-icon.png">
<link rel="manifest" href="assets/site.webmanifest">
```

### EN: `/en/index.html` (`<html lang="en">`)
```html
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Women's Bible Study Group, Thursdays | Branches Bible Club</title>
<meta name="description" content="Women's Bible study every other Thursday: read Scripture, talk and pray together over coffee and candlelight. Grow closer to Christ. Pull up a chair!">
<meta name="robots" content="index, follow, max-image-preview:large">
<link rel="canonical" href="https://anth-05.github.io/branchesbibleclub/en/">
<link rel="alternate" hreflang="nl" href="https://anth-05.github.io/branchesbibleclub/">
<link rel="alternate" hreflang="en" href="https://anth-05.github.io/branchesbibleclub/en/">
<link rel="alternate" hreflang="x-default" href="https://anth-05.github.io/branchesbibleclub/">
<meta name="author" content="Branches Bible Club">
<meta name="application-name" content="Branches Bible Club">
<meta name="apple-mobile-web-app-title" content="BBC">
<meta name="theme-color" content="#F4DFC0">

<meta property="og:type" content="website">
<meta property="og:site_name" content="Branches Bible Club">
<meta property="og:locale" content="en_GB">
<meta property="og:locale:alternate" content="nl_NL">
<meta property="og:url" content="https://anth-05.github.io/branchesbibleclub/en/">
<meta property="og:title" content="Women's Bible study, every other Thursday">
<meta property="og:description" content="Read Scripture, talk and pray together over coffee and candlelight. A circle of women pursuing a stronger intimacy with Christ. Pull up a chair!">
<meta property="og:image" content="https://anth-05.github.io/branchesbibleclub/assets/og.jpg">
<meta property="og:image:type" content="image/jpeg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Illustration of four women on a rug with open Bibles, coffee and candles, with the Branches Bible Club logo">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Women's Bible study, every other Thursday">
<meta name="twitter:description" content="Read Scripture, talk and pray together over coffee and candlelight. Pull up a chair at Branches Bible Club.">
<meta name="twitter:image" content="https://anth-05.github.io/branchesbibleclub/assets/og.jpg">
<meta name="twitter:image:alt" content="Illustration of four women on a rug with open Bibles, coffee and candles">

<link rel="icon" href="../assets/favicon.ico" sizes="32x32">
<link rel="icon" href="../assets/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="../assets/apple-touch-icon.png">
<link rel="manifest" href="../assets/site.webmanifest">
```
Path note: this is a project site served under `/branchesbibleclub/`, so a root-absolute path such as `/assets/...` breaks. Use relative paths: `assets/` on NL and `../assets/` on EN. Metadata URLs (canonical, og, hreflang) must be absolute.
The `google-site-verification` meta goes on the NL page only, and only if the owner picks the HTML-tag verification method.

`site.webmanifest`: `{"name":"Branches Bible Club","short_name":"BBC","start_url":"../","scope":"../","display":"browser","background_color":"#F4DFC0","theme_color":"#F4DFC0","icons":[{"src":"icon-192.png","sizes":"192x192","type":"image/png"},{"src":"icon-512.png","sizes":"512x512","type":"image/png"}]}`. The manifest lives in `/assets/`, so `start_url` and `scope` are relative to it. Generate icon-192 and icon-512 from the badge as well.

---

## 4. JSON-LD (`@graph`)

Decisions:
- **Event: leave it out for now.** Google requires `startDate` and `location` (a Place with an address, or a VirtualLocation), and both are still placeholders. Partial Event markup triggers Search Console errors. Section 4c lists what to add later.
- **Lessons (ItemList/Article): leave them out for now.** Article markup only pays off when each lesson has its own URL and a date. When there are 3 or more lessons, give each one a page (for example `/lessen/01-het-najagen-van-intimiteit/` and `/en/lessons/01-the-pursuit-of-intimacy/`) with `BlogPosting` (headline, datePublished, author = Organization, inLanguage, about). The homepage can then carry an `ItemList` that links to them.
- **FAQPage: optional.** Google has shown FAQ rich results only for government and health sites since 2023, so this markup will not produce a snippet. It still helps AI answers and does no harm. Add it only once the visible FAQ in section 5 is live, and keep the text identical to the visible copy. The snippets are in 4b.
- No `sameAs` (there are no profiles yet), no reviews or ratings, and no `address`.
- `logo` must be a raster image of at least 112x112 px. Add `/assets/logo.png` (512x512, the BBC badge on a solid background).

### 4a. NL graph (in the `<head>` of `/`)
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Organization",
      "@id": "https://anth-05.github.io/branchesbibleclub/#org",
      "name": "Branches Bible Club",
      "alternateName": "BBC",
      "url": "https://anth-05.github.io/branchesbibleclub/",
      "logo": {
        "@type": "ImageObject",
        "@id": "https://anth-05.github.io/branchesbibleclub/#logo",
        "url": "https://anth-05.github.io/branchesbibleclub/assets/logo.png",
        "width": 512,
        "height": 512,
        "caption": "Branches Bible Club"
      },
      "image": { "@id": "https://anth-05.github.io/branchesbibleclub/#logo" },
      "slogan": "Fostering a stronger intimacy with Christ",
      "description": "Een kring van vrouwen die om de week op donderdag samen de Bijbel leest, praat en bidt, om dichter bij Christus te komen.",
      "knowsAbout": ["Bijbelstudie", "Johannes 15", "Johannes 14:22-23"]
    },
    {
      "@type": "WebSite",
      "@id": "https://anth-05.github.io/branchesbibleclub/#website",
      "url": "https://anth-05.github.io/branchesbibleclub/",
      "name": "Branches Bible Club",
      "publisher": { "@id": "https://anth-05.github.io/branchesbibleclub/#org" },
      "inLanguage": ["nl-NL", "en"]
    },
    {
      "@type": "WebPage",
      "@id": "https://anth-05.github.io/branchesbibleclub/#webpage",
      "url": "https://anth-05.github.io/branchesbibleclub/",
      "name": "Bijbelstudie voor vrouwen op donderdag | Branches Bible Club",
      "description": "Bijbelstudie voor vrouwen: om de week op donderdag samen de Bijbel lezen, praten en bidden bij koffie en kaarslicht. Kom dichter bij Christus. Schuif aan!",
      "inLanguage": "nl-NL",
      "isPartOf": { "@id": "https://anth-05.github.io/branchesbibleclub/#website" },
      "about": { "@id": "https://anth-05.github.io/branchesbibleclub/#org" },
      "primaryImageOfPage": {
        "@type": "ImageObject",
        "url": "https://anth-05.github.io/branchesbibleclub/assets/og.jpg",
        "width": 1200,
        "height": 630
      },
      "workTranslation": { "@id": "https://anth-05.github.io/branchesbibleclub/en/#webpage" }
    }
  ]
}
</script>
```

### 4a. EN graph (in the `<head>` of `/en/`)
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Organization",
      "@id": "https://anth-05.github.io/branchesbibleclub/#org",
      "name": "Branches Bible Club",
      "alternateName": "BBC",
      "url": "https://anth-05.github.io/branchesbibleclub/",
      "logo": {
        "@type": "ImageObject",
        "@id": "https://anth-05.github.io/branchesbibleclub/#logo",
        "url": "https://anth-05.github.io/branchesbibleclub/assets/logo.png",
        "width": 512,
        "height": 512,
        "caption": "Branches Bible Club"
      },
      "image": { "@id": "https://anth-05.github.io/branchesbibleclub/#logo" },
      "slogan": "Fostering a stronger intimacy with Christ",
      "description": "A circle of women who read the Bible, talk and pray together every other Thursday, pursuing a stronger intimacy with Christ."
    },
    {
      "@type": "WebSite",
      "@id": "https://anth-05.github.io/branchesbibleclub/#website",
      "url": "https://anth-05.github.io/branchesbibleclub/",
      "name": "Branches Bible Club",
      "publisher": { "@id": "https://anth-05.github.io/branchesbibleclub/#org" },
      "inLanguage": ["nl-NL", "en"]
    },
    {
      "@type": "WebPage",
      "@id": "https://anth-05.github.io/branchesbibleclub/en/#webpage",
      "url": "https://anth-05.github.io/branchesbibleclub/en/",
      "name": "Women's Bible Study Group, Thursdays | Branches Bible Club",
      "description": "Women's Bible study every other Thursday: read Scripture, talk and pray together over coffee and candlelight. Grow closer to Christ. Pull up a chair!",
      "inLanguage": "en",
      "isPartOf": { "@id": "https://anth-05.github.io/branchesbibleclub/#website" },
      "about": { "@id": "https://anth-05.github.io/branchesbibleclub/#org" },
      "primaryImageOfPage": {
        "@type": "ImageObject",
        "url": "https://anth-05.github.io/branchesbibleclub/assets/og.jpg",
        "width": 1200,
        "height": 630
      },
      "translationOfWork": { "@id": "https://anth-05.github.io/branchesbibleclub/#webpage" }
    }
  ]
}
</script>
```

### 4b. Optional FAQPage node (append to the `@graph` once the visible FAQ exists)
Build each `Question` from the visible FAQ copy in section 5, word for word: `{"@type":"Question","name":"<vraag>","acceptedAnswer":{"@type":"Answer","text":"<antwoord>"}}`. Wrap them in `{"@type":"FAQPage","@id":"<page url>#faq","mainEntity":[...],"inLanguage":"nl-NL"|"en"}`. Mark up only the questions that are visible on the page.

### 4c. Add later (once the time and location are confirmed)
One `Event` per upcoming meeting, generated for the next 6 to 8 Thursdays. Google wants individual dated events; schema.org `eventSchedule` alone is not enough for Google.
```json
{"@type":"Event","name":"Branches Bible Club: bijbelstudie voor vrouwen",
 "startDate":"YYYY-MM-DDTHH:MM+01:00","endDate":"…",
 "eventStatus":"https://schema.org/EventScheduled",
 "eventAttendanceMode":"https://schema.org/OfflineEventAttendanceMode",
 "location":{"@type":"Place","name":"…","address":{"@type":"PostalAddress","addressLocality":"…","addressCountry":"NL"}},
 "organizer":{"@id":"…#org"},"image":"…/assets/og.jpg","description":"…",
 "inLanguage":"nl-NL"}
```
If meetings are online, use `OnlineEventAttendanceMode` with a `VirtualLocation` instead. Add `"isAccessibleForFree": true` or `offers` only once the owner confirms the cost. If meetings happen in a private home, give only the city (`addressLocality`) and no street. Keep a single source for the dates so the page and the JSON-LD always agree, and remove past events.

---

## 5. On-page fixes

### Headings (identical structure on both pages)
```
H1  Dichter bij Christus, samen aan tafel. / Closer to Christ, together at the table.   (keep: brand voice)
 H2 Johannes 14:22–23 / John 14:22–23
  H3 Liefhebben · Zijn woord bewaren · Hij woont bij ons / Love Him · Keep His word · He makes His home
 H2 Waarom we Branches heten / Why we're called Branches      ← FIX: this is a <p class="label"> now; make it <h2 class="label"> (keep the styling) so the section has a heading
 H2 Wat we leerden / What we learned
  H3 per lesson: Het najagen van intimiteit / The pursuit of intimacy   (static HTML, as planned)
 H2 Een plek om te blijven. / A place to remain.
 H2 Veelgestelde vragen / Questions you might have             ← NEW
  H3 each question (or <details><summary> with the question inside an <h3>)
 H2 Kom erbij / Come and join us
```
- Only one H1 per page. With the language split, each page carries only its own language's span.
- The H1 has no keyword, which is acceptable. The keyword goes in the title, the description, the `.when` pill and the first sentence of the lead (below). If the owner prefers it in the H1 itself, use: NL `Bijbelstudie voor vrouwen: dichter bij <em>Christus</em>, samen aan tafel.` / EN `A women's Bible study: closer to <em>Christ</em>, together at the table.`
- Section labels and aria-labels are hard-coded in Dutch. Localise them per page: nav `aria-label` Hoofdmenu / Main menu; `.vcard` Kernvers / Anchor verse; band `aria-label` Waarom Branches / Why Branches; to-top button Naar boven / Back to top; language group Taal / Language; brand link "naar het begin" / "back to top".
- The language switcher becomes real links instead of JS buttons. NL: `<a href="en/" hreflang="en" lang="en">EN</a>`. EN: `<a href="../" hreflang="nl" lang="nl">NL</a>`. Mark the current language with `aria-current="page"`. Remove the `?lang=` and localStorage auto-switch logic.

### Copy tweaks (natural, one mention each)
| Spot | NL | EN |
|---|---|---|
| `.when` pill | `Bijbelstudie voor vrouwen · om de week op donderdag` | `Women's Bible study · every other Thursday` |
| Lead, first sentence | `Branches Bible Club is een bijbelstudie voor vrouwen: een kring die om de week op donderdag samen de Bijbel openslaat.` (rest unchanged) | `Branches Bible Club is a women's Bible study: a circle of women who open the Bible together every other Thursday.` (rest unchanged) |
| Lessons intro | `Na elke bijbelstudie zetten we de belangrijkste lessen hier, …` | `After each Bible study we post the main lessons here, …` |
| About paragraph | Remove the `[Raé, …]` placeholder before indexing. When the real story goes in, mention "vrouwenkring" or "bijbelkring" once and, if known, the city. | Same; mention "Bible study group" once. |
| Lesson H3 + ref | Keep the Bible reference visible next to each H3 (`Hooglied 1:1–4`). Book names are long-tail queries in their own right. | `Song of Songs 1:1–4` |

### New visible FAQ (true statements only, based on what the page says)
**NL: Veelgestelde vragen**
1. **Wanneer komen jullie samen?** Om de week op donderdag. De precieze tijd zetten we binnenkort op deze pagina. *(Once confirmed: "Om de week op donderdag om [tijd].")*
2. **Wat moet ik meenemen?** Je Bijbel, een notitieboekje en jezelf. Er staat een kop koffie voor je klaar.
3. **Wat doen jullie op zo'n avond?** We lezen samen een gedeelte uit de Bijbel, delen wat het met ons doet en bidden voor elkaar.
4. **Ik heb een donderdag gemist. Kan ik bijlezen?** Ja. Na elke bijeenkomst zetten we de belangrijkste lessen op deze pagina, onder "Wat we leerden".
5. **Welke Bijbelvertaling gebruiken jullie?** Op deze site citeren we de Statenvertaling (Nederlands) en de World English Bible (Engels).

**EN: Questions you might have**
1. **When do you meet?** Every other Thursday. We'll post the exact time on this page soon.
2. **What should I bring?** Your Bible, a notebook and yourself. There's a cup of coffee with your name on it.
3. **What happens at a gathering?** We read a Bible passage together, share what it stirs in us and pray for one another.
4. **I missed a Thursday. Can I catch up?** Yes. After each gathering we post the main lessons on this page, under "What we learned".
5. **Which Bible translation do you use?** On this site we quote the Statenvertaling (Dutch) and the World English Bible (English).

The owner must confirm these before they go on the page. Do not publish answers to the following until confirmed:
- "Moet ik ervaring hebben met de Bijbel?" / "Do I need to know the Bible already?" (likely "no", but the page doesn't say)
- "Kost het iets?" / "Does it cost anything?" (unknown: never claim "free")
- "Waar komen jullie samen?" / "Where do you meet?" (placeholder)
- Whether the circle uses the Statenvertaling in the meetings themselves (the page only shows that the site quotes it)

### Images
| Image | File | alt NL | alt EN |
|---|---|---|---|
| Hero illustration | `assets/bijbelstudie-vrouwen-branches-bible-club.jpg` (also make a WebP) | `Illustratie: vier vrouwen op een kleed met opengeslagen Bijbels, koffie, croissants en kaarsjes, met het BBC-logo` (current, good) | `Illustration: four women on a rug with open Bibles, coffee, croissants and candles, with the BBC logo` |
| About crop (same artwork) | reuse the same file | `alt=""` (decorative duplicate, fine as it is) | `alt=""` |
| Logo badge SVG | inline | Keep `aria-hidden`; the link's label carries the name | |
| og.jpg | `assets/og.jpg` 1200x630 | see `og:image:alt` | see `og:image:alt` |

Keep `width` and `height` on the images, `fetchpriority="high"` on the hero and `loading="lazy"` on the about image. Inline base64 images are gone with the move to `/assets/`, which is the largest performance gain for LCP.

### Other
- The sign-up form is a non-working preview. Connect it (Formspree, Netlify Forms, or a `mailto:`) or replace it with a contact link before promoting the site. A form that only says "dit is een voorbeeld" is bad for trust.
- "Powered by Branch" (branch.nu): add `rel="noopener"` (already present). That is fine as it is.
- `404.html`: add `<meta name="robots" content="noindex">`, a bilingual message, and links to `/branchesbibleclub/` and `/branchesbibleclub/en/`. Use absolute paths here, because the 404 is served at any depth.

---

## 6. robots.txt and sitemap.xml

**Important:** crawlers only read `robots.txt` at the **host root** (`https://anth-05.github.io/robots.txt`). A file at `/branchesbibleclub/robots.txt` is ignored. Add the file anyway so it works the moment a custom domain is mapped, and submit the sitemap directly in Search Console in the meantime.

`robots.txt`
```
User-agent: *
Allow: /

Sitemap: https://anth-05.github.io/branchesbibleclub/sitemap.xml
```

`sitemap.xml`
```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:xhtml="http://www.w3.org/1999/xhtml">
  <url>
    <loc>https://anth-05.github.io/branchesbibleclub/</loc>
    <lastmod>2026-11-25</lastmod>
    <xhtml:link rel="alternate" hreflang="nl" href="https://anth-05.github.io/branchesbibleclub/"/>
    <xhtml:link rel="alternate" hreflang="en" href="https://anth-05.github.io/branchesbibleclub/en/"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="https://anth-05.github.io/branchesbibleclub/"/>
  </url>
  <url>
    <loc>https://anth-05.github.io/branchesbibleclub/en/</loc>
    <lastmod>2026-11-25</lastmod>
    <xhtml:link rel="alternate" hreflang="nl" href="https://anth-05.github.io/branchesbibleclub/"/>
    <xhtml:link rel="alternate" hreflang="en" href="https://anth-05.github.io/branchesbibleclub/en/"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="https://anth-05.github.io/branchesbibleclub/"/>
  </url>
</urlset>
```
Update `lastmod` whenever a lesson is added. Leave out `changefreq` and `priority`, because Google ignores them.

---

## 7. Owner tasks (in order)

1. **Fill the placeholders first:** time, location (or "online"), the about-us story (`[Raé, …]`), and the cost and experience answers for the FAQ. Then connect the sign-up form. Do this before steps 3 and 4, so Google's first crawl sees a finished page.
2. **Custom domain (recommended):** for example `branchesbibleclub.nl` (a .nl domain signals a Dutch audience and builds trust), with `www` or the bare domain as canonical. Set it in GitHub Pages, add the `CNAME` file, enable "Enforce HTTPS", then swap `BASE` everywhere. `robots.txt` starts working after this step.
3. **Google Search Console:** add a URL-prefix property for `BASE` (HTML-tag verification via the commented meta), submit `sitemap.xml`, and request indexing for `/` and `/en/`. After a domain move, add a Domain property (DNS TXT) and resubmit.
4. **Bing Webmaster Tools:** import from Search Console. Bing also powers DuckDuckGo and Ecosia.
5. **Validate:** run the Rich Results Test and validator.schema.org on both URLs, and check the share previews (the opengraph.xyz debugger, a WhatsApp test message).
6. **Local listings (once the location is known):** add the group to the Bijbelgenootschap/*Zij Lacht* group overview and to your church's website or newsletter, with a link to the site. These are the best realistic backlinks for this niche. Use a Google Business Profile only if there is a public, staffed meeting place; skip it for a private home.
7. **Content cadence:** add each Thursday's lesson within a few days; this fresh content is what keeps the page alive in search. Once there are 3 or more lessons, move to one page per lesson with `BlogPosting` markup (section 4).
8. **Social profiles:** if an Instagram or WhatsApp community is created, add its URL to `sameAs` in the Organization node. Until then, leave `sameAs` out.

Sources consulted for phrasing: [Bijbelgenootschap: Zij Lacht](https://mautic.bijbelgenootschap.nl/asset/63:zij-lacht--guide-nieuw-in-geloof), [Leger des Heils: Bijbelstudies vrouwen](https://www.salvationarmy.org/sites/default/files/2023-06/bd72edf0-9191-4566-b84e-d9cf3ff7dcc8_BijbelstudiesVrouwenDocument.pdf), [EO: tips voor een kringavond](https://www.eo.nl/artikel/10-tips-voor-een-originele-kringavond).
