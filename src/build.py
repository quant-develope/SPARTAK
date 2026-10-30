#!/usr/bin/env python3
"""Static site generator for the second Spartakos pools site, "Πισίνα Προκάτ Ελλάδα".

Run: python3 src/build.py   (writes ../site, which Cloudflare serves as-is)
Pages live in pages_el.py / pages_en.py, shared blocks in parts.py.
"""
import html
import json
import os
import re
import shutil
import sys
from datetime import date

from PIL import Image, ImageOps

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "site")
sys.path.insert(0, HERE)

import parts  # noqa: E402
from parts import DOMAIN, BIZ, esc  # noqa: E402
import pages_el  # noqa: E402
import pages_en  # noqa: E402

TODAY = date.today().isoformat()
SIZES = (480, 960, 1600)


# ---------- images ----------
def build_images():
    """Each src/photos/<name>.jpg becomes img/<name>-480.webp, -960.webp, -1600.webp and an og jpg."""
    src = os.path.join(HERE, "photos")
    dst = os.path.join(OUT, "img")
    os.makedirs(dst, exist_ok=True)
    for f in sorted(os.listdir(src)):
        if not f.endswith(".jpg"):
            continue
        name = f[:-4]
        im = ImageOps.exif_transpose(Image.open(os.path.join(src, f))).convert("RGB")
        parts.IMG[name] = im.size
        for w in SIZES:
            if w > im.width and w != SIZES[0]:
                continue
            out = os.path.join(dst, "%s-%d.webp" % (name, w))
            if not os.path.exists(out):
                r = im.copy()
                r.thumbnail((w, w * 2), Image.LANCZOS)
                r.save(out, "WEBP", quality=78, method=6)
        og = os.path.join(dst, name + "-og.jpg")
        if not os.path.exists(og) and not name.startswith("hg-"):
            r = ImageOps.fit(im, (1200, 630), Image.LANCZOS)
            r.save(og, quality=80, optimize=True, progressive=True)


# ---------- page shell ----------
def head(p):
    lang = p["lang"]
    url = DOMAIN + p["path"]
    alt = ""
    if p.get("alt"):
        el = p["path"] if lang == "el" else p["alt"]
        en = p["alt"] if lang == "el" else p["path"]
        alt = ('<link rel="alternate" hreflang="el" href="%s%s">'
               '<link rel="alternate" hreflang="en" href="%s%s">'
               '<link rel="alternate" hreflang="x-default" href="%s%s">') % (DOMAIN, el, DOMAIN, en, DOMAIN, el)
    og_img = "%s/img/%s-og.jpg" % (DOMAIN, p["hero"])
    ld = [parts.business_ld(lang)]
    if p["path"] not in ("/", "/en/"):
        ld.append(parts.breadcrumb_ld(p))
    ld += p.get("ld", [])
    if p.get("faq"):
        ld.append({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub("<[^>]+>", "", a)}}
            for q, a in p["faq"]]})
    if p.get("article"):
        ld.append({"@context": "https://schema.org", "@type": "Article", "headline": p["h1"],
                   "description": p["desc"], "image": og_img, "inLanguage": lang,
                   "datePublished": p["article"], "dateModified": p["article"],
                   "author": {"@type": "Organization", "name": BIZ["name"][lang]},
                   "publisher": {"@type": "Organization", "name": BIZ["name"][lang],
                                 "logo": {"@type": "ImageObject", "url": DOMAIN + "/icon-512.png"}},
                   "mainEntityOfPage": url})
    lds = "".join('<script type="application/ld+json">%s</script>' % json.dumps(x, ensure_ascii=False) for x in ld)
    return """<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">{alt}{robots}
<meta property="og:type" content="{ogtype}">
<meta property="og:site_name" content="{site}">
<meta property="og:locale" content="{locale}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{og}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0e4f5c">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Commissioner:wght@400;500;600;700&family=Noto+Serif:wght@600;700&display=swap">
<link rel="preload" as="image" href="/img/{hero}-960.webp" imagesrcset="{herosrcset}" imagesizes="100vw">
<link rel="stylesheet" href="/assets/style.css?v={ver}">
{lds}
</head>
""".format(lang=lang, title=esc(p["title"]), desc=esc(p["desc"]), url=url, alt=alt,
           ogtype="article" if p.get("article") else "website", site=esc(BIZ["name"][lang]),
           locale="el_GR" if lang == "el" else "en_GB", og=og_img, hero=p["hero"],
           herosrcset=parts.srcset(p["hero"]), ver=parts.VER, lds=lds,
           robots='\n<meta name="robots" content="noindex">' if p.get("noindex") else "")


def page(p):
    body = [head(p), '<body class="%s">' % p.get("cls", "inner"), parts.header(p), '<main id="main">']
    body.append(parts.hero(p))
    body.append(p["body"])
    if p.get("faq") and not p.get("faq_inline"):
        body.append(parts.faq_block(p["faq"], p["lang"]))
    if not p.get("no_quote"):
        body.append(parts.quote_block(p["lang"]))
    body.append("</main>")
    body.append(parts.footer(p))
    body.append('<script src="/assets/app.js?v=%s" defer></script></body></html>\n' % parts.VER)
    return "".join(body)


def write(path, text):
    full = os.path.join(OUT, path.lstrip("/"))
    if full.endswith("/"):
        full += "index.html"
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(text)


def sitemap(pages):
    rows = []
    for p in pages:
        if p.get("noindex"):
            continue
        alts = ""
        if p.get("alt"):
            el = p["path"] if p["lang"] == "el" else p["alt"]
            en = p["alt"] if p["lang"] == "el" else p["path"]
            alts = ('<xhtml:link rel="alternate" hreflang="el" href="%s%s"/>'
                    '<xhtml:link rel="alternate" hreflang="en" href="%s%s"/>') % (DOMAIN, el, DOMAIN, en)
        imgs = "".join("<image:image><image:loc>%s/img/%s-1600.webp</image:loc></image:image>" % (DOMAIN, n)
                       for n in sorted(set(re.findall(r'/img/([a-z0-9-]+?)-(?:480|960|1600)\.webp', p["html"])))[:12]
                       if parts.IMG.get(n, (0,))[0] >= 1600) if p["html"] else ""
        rows.append("<url><loc>%s%s</loc><lastmod>%s</lastmod>%s%s</url>" % (DOMAIN, p["path"], TODAY, alts, imgs))
    return ('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
            'xmlns:xhtml="http://www.w3.org/1999/xhtml" xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">\n'
            + "\n".join(rows) + "\n</urlset>\n")


def main():
    if os.path.isdir(OUT):
        for f in os.listdir(OUT):
            if f != "img":
                full = os.path.join(OUT, f)
                shutil.rmtree(full) if os.path.isdir(full) else os.remove(full)
    os.makedirs(OUT, exist_ok=True)
    build_images()
    static = os.path.join(HERE, "static")
    os.makedirs(os.path.join(OUT, "assets"), exist_ok=True)
    for f in os.listdir(static):
        target = "assets" if f.endswith((".css", ".js")) else ""
        shutil.copy(os.path.join(static, f), os.path.join(OUT, target, f))
    pages = pages_el.pages() + pages_en.pages()
    paths = {p["path"] for p in pages}
    for p in pages:
        p["html"] = page(p)
        write(p["path"], p["html"])
    # internal link check
    bad = set()
    for p in pages:
        for href in re.findall(r'href="(/[^"#?]*)', p["html"]):
            if href.startswith(("/assets/", "/img/")) or "." in href.rsplit("/", 1)[-1]:
                continue
            if href not in paths:
                bad.add((p["path"], href))
    for b in sorted(bad):
        print("BROKEN LINK", *b)
    nf = pages_el.not_found()
    write("/404.html", page(nf))
    write("/sitemap.xml", sitemap(pages))
    write("/robots.txt", "User-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n" % DOMAIN)
    write("/site.webmanifest", json.dumps({
        "name": BIZ["name"]["el"], "short_name": "Πισίνα Προκάτ", "start_url": "/", "display": "browser",
        "background_color": "#f6f1e8", "theme_color": "#0e4f5c",
        "icons": [{"src": "/icon-192.png", "sizes": "192x192", "type": "image/png"},
                  {"src": "/icon-512.png", "sizes": "512x512", "type": "image/png"}]}, ensure_ascii=False))
    # remove image variants no longer backed by a source photo
    names = set(parts.IMG)
    for f in os.listdir(os.path.join(OUT, "img")):
        if re.sub(r"-(480|960|1600|og)\.(webp|jpg)$", "", f) not in names:
            os.remove(os.path.join(OUT, "img", f))
    words = sum(len(re.sub("<[^>]+>", " ", p["body"]).split()) for p in pages)
    print("pages:", len(pages), "words in bodies:", words, "broken links:", len(bad))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
