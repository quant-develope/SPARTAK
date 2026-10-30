"""Shared blocks: header, hero, footer, quote form, pictures, schema."""
import html

DOMAIN = "https://spartak.unknwn-creation.workers.dev"
VER = "1030b"
IMG = {}  # photo name -> (width, height), filled by build.py

PHONE = "+30 212 104 8320"
PHONE_TEL = "+302121048320"
MOBILE = "+30 693 650 5824"
MOBILE_TEL = "+306936505824"
WA = "306936505824"
EMAIL = "pisina.gr@gmail.com"
MAPS = "https://maps.google.com/?cid=370785818317058797"
FB = "https://www.facebook.com/pisina.com.gr"
IG = "https://www.instagram.com/pisines.spartakos"
BIZ = {
    "name": {"el": "Πισίνες Σπάρτακος", "en": "Spartakos Pools"},
    "street": {"el": "Ξενοφώντος 112", "en": "Xenofontos 112"},
    "city": {"el": "Καλλιθέα", "en": "Kallithea"},
    "zip": "176 74",
}


def esc(s):
    return html.escape(s, quote=True)


def srcset(name):
    w = IMG.get(name, (1600, 1200))[0]
    return ", ".join("/img/%s-%d.webp %dw" % (name, s, s) for s in (480, 960, 1600) if s <= w or s == 480)


def pic(name, alt, sizes="(min-width: 960px) 50vw, 100vw", cls="", eager=False, zoom=False):
    w, h = IMG.get(name, (1600, 1200))
    big = 1600 if w >= 1600 else (960 if w >= 960 else 480)
    img = '<img src="/img/%s-960.webp" srcset="%s" sizes="%s" width="%d" height="%d" alt="%s"%s%s>' % (
        name if w >= 960 else name, srcset(name), sizes, w, h, esc(alt),
        ' loading="lazy" decoding="async"' if not eager else ' fetchpriority="high"',
        ' class="%s"' % cls if cls else "")
    if w < 960:
        img = img.replace("-960.webp\"", "-480.webp\"", 1)
    if zoom:
        return '<a class="zoom" href="/img/%s-%d.webp" data-cap="%s">%s</a>' % (name, big, esc(alt), img)
    return img


def figure(name, cap, sizes="(min-width: 960px) 50vw, 100vw", zoom=True):
    return '<figure class="fig">%s<figcaption>%s</figcaption></figure>' % (pic(name, cap, sizes, zoom=zoom), cap)


T = {
    "el": {
        "skip": "Μετάβαση στο περιεχόμενο", "menu": "Μενού", "quote": "Ζητήστε προσφορά", "call": "Κλήση",
        "home": "Αρχική", "faq": "Συχνές ερωτήσεις", "lang": "EN", "lang_label": "English version",
        "addr": "Ξενοφώντος 112, 176 74 Καλλιθέα, Αττική", "map": "Χάρτης", "tagline": "Πισίνες προκάτ · 28 χρόνια",
        "rights": "Πισίνες Σπάρτακος. Πισίνες προκάτ με γαλβανισμένα panels και liner.",
        "privacy": "Απόρρητο", "price": "Τιμή: κατόπιν επικοινωνίας, για κάθε πισίνα χωριστά.",
    },
    "en": {
        "skip": "Skip to content", "menu": "Menu", "quote": "Ask for a quote", "call": "Call",
        "home": "Home", "faq": "Questions", "lang": "ΕΛ", "lang_label": "Ελληνική έκδοση",
        "addr": "Xenofontos 112, 176 74 Kallithea, Attica, Greece", "map": "Map", "tagline": "Prefab pools · 28 years",
        "rights": "Spartakos Pools. Prefab pools with galvanised steel panels and PVC liner.",
        "privacy": "Privacy", "price": "Price: on request, worked out for each pool.",
    },
}

NAV = {
    "el": [("/pisina-prokat/", "Πισίνες προκάτ"), ("/liner-pisinas/", "Liner"), ("/erga/", "Έργα"),
           ("/perioxes/", "Περιοχές"), ("/odigos/", "Οδηγός"), ("/erotiseis/", "Ερωτήσεις")],
    "en": [("/en/prefab-pools/", "Prefab pools"), ("/en/pool-liner/", "Liner"), ("/en/projects/", "Projects"),
           ("/en/pools-on-islands/", "Islands"), ("/en/faq/", "Questions")],
}

MENU = {
    "el": [
        ("Πισίνες", [("/pisina-prokat/", "Πισίνα προκάτ: πώς είναι φτιαγμένη"), ("/pisina-skimmer/", "Πισίνα με skimmer"),
                     ("/pisina-yperxeilisis/", "Πισίνα υπερχείλισης"), ("/mikri-pisina/", "Μικρή πισίνα για αυλή"),
                     ("/yperypsomeni-pisina/", "Υπερυψωμένη πισίνα"), ("/diastaseis-pisinas/", "Διαστάσεις πισίνας"),
                     ("/pisina-gia-katalymata/", "Πισίνα για βίλα & κατάλυμα")]),
        ("Κατασκευή", [("/pos-kataskevazoume/", "Πώς κατασκευάζουμε"), ("/egkrisi-mikris-klimakas/", "Έγκριση μικρής κλίμακας"),
                       ("/liner-pisinas/", "Liner & χρώματα"), ("/michanostasio-pisinas/", "Μηχανοστάσιο & φίλτρο"),
                       ("/apolymansi-nerou/", "Αλάτι, χλώριο, pH"), ("/thermansi-pisinas/", "Θέρμανση πισίνας")]),
        ("Μετά την κατασκευή", [("/syntirisi-pisinas/", "Συντήρηση"), ("/anakainisi-pisinas/", "Ανακαίνιση & νέο liner"),
                                ("/odigos/", "Οδηγός πισίνας")]),
        ("Εταιρεία", [("/erga/", "Έργα"), ("/perioxes/", "Περιοχές"), ("/pisina-se-nisi/", "Πισίνα σε νησί"),
                      ("/erotiseis/", "Συχνές ερωτήσεις"), ("/epikoinonia/", "Επικοινωνία")]),
    ],
    "en": [
        ("Pools", [("/en/prefab-pools/", "Prefab pools"), ("/en/skimmer-pool/", "Skimmer pool"),
                   ("/en/overflow-pool/", "Overflow pool"), ("/en/pool-sizes/", "Pool sizes")]),
        ("Build", [("/en/pool-permit/", "Small-scale permit"), ("/en/pool-liner/", "Liner & colours"),
                   ("/en/pools-on-islands/", "Pools on the islands")]),
        ("Company", [("/en/projects/", "Projects"), ("/en/faq/", "Questions"), ("/en/contact/", "Contact")]),
    ],
}

LOGO = open(__file__.replace("parts.py", "static/logo.svg"), encoding="utf-8").read()
LOGO = LOGO.replace(' xmlns:c2pa="http://c2pa.org/manifest"', "").replace("<svg ", '<svg aria-hidden="true" ', 1)


def header(p):
    lang = p["lang"]
    t = T[lang]
    home = "/" if lang == "el" else "/en/"
    other = p.get("alt") or ("/en/" if lang == "el" else "/")
    nav = "".join('<a href="%s"%s>%s</a>' % (h, ' aria-current="page"' if h == p["path"] else "", n) for h, n in NAV[lang])
    groups = "".join('<div class="mgroup"><p>%s</p>%s</div>' % (g, "".join('<a href="%s">%s</a>' % (h, n) for h, n in links))
                     for g, links in MENU[lang])
    contact = "/epikoinonia/" if lang == "el" else "/en/contact/"
    return """<a class="skip" href="#main">{skip}</a>
<header class="top">
 <div class="wrap top-in">
  <a class="brand" href="{home}" aria-label="{name}">{logo}<span><b>ΣΠΑΡΤΑΚΟΣ</b><small>{tag}</small></span></a>
  <nav class="nav" aria-label="main">{nav}</nav>
  <div class="top-act">
   <a class="lang" href="{other}" hreflang="{olang}" title="{lang_label}">{lang_btn}</a>
   <a class="btn btn-sm hide-m" href="{contact}#quote">{quote}</a>
   <details class="menu"><summary aria-label="{menu}"><span></span><span></span><span></span></summary>
    <div class="menu-panel"><div class="wrap">{groups}
     <div class="mgroup mcontact"><a href="tel:{tel}">{phone}</a><a href="https://wa.me/{wa}">WhatsApp / Viber {mobile}</a><a href="mailto:{email}">{email}</a></div>
    </div></div>
   </details>
  </div>
 </div>
</header>
""".format(skip=t["skip"], home=home, name=BIZ["name"][lang], logo=LOGO, tag=t["tagline"], nav=nav, other=other,
           olang="en" if lang == "el" else "el", lang_label=t["lang_label"], lang_btn=t["lang"], contact=contact,
           quote=t["quote"], menu=t["menu"], groups=groups, tel=PHONE_TEL, phone=PHONE, wa=WA, mobile=MOBILE, email=EMAIL)


def crumbs(p):
    if p["path"] in ("/", "/en/"):
        return ""
    t = T[p["lang"]]
    home = "/" if p["lang"] == "el" else "/en/"
    items = [(t["home"], home)] + p.get("crumbs", []) + [(p.get("short", p["h1"]), None)]
    li = "".join('<li>%s</li>' % ('<a href="%s">%s</a>' % (h, esc(n)) if h else '<span aria-current="page">%s</span>' % esc(n))
                 for n, h in items)
    return '<nav class="crumbs" aria-label="breadcrumb"><ol>%s</ol></nav>' % li


def hero(p):
    if p.get("home_hero"):
        return p["home_hero"]
    facts = ""
    if p.get("facts"):
        facts = '<ul class="facts">%s</ul>' % "".join('<li><b>%s</b><span>%s</span></li>' % f for f in p["facts"])
    return """<section class="phero">
 <div class="wrap phero-in">
  <div class="phero-text">{crumbs}<p class="kicker">{kicker}</p><h1>{h1}</h1><p class="lead">{lead}</p>{facts}</div>
  <div class="phero-img">{img}</div>
 </div>
</section>
""".format(crumbs=crumbs(p), kicker=p.get("kicker", ""), h1=p["h1"], lead=p["lead"], facts=facts,
           img=pic(p["hero"], p["hero_alt"], "(min-width: 960px) 45vw, 100vw", eager=True))


def business_ld(lang):
    return {
        "@context": "https://schema.org", "@type": "HomeAndConstructionBusiness", "@id": DOMAIN + "/#business",
        "name": BIZ["name"][lang], "alternateName": "Spartakos Pisines" if lang == "el" else "Πισίνες Σπάρτακος",
        "url": DOMAIN + ("/" if lang == "el" else "/en/"), "logo": DOMAIN + "/icon-512.png",
        "image": DOMAIN + "/img/pisina-thea-thalassa-veranta-og.jpg",
        "telephone": PHONE_TEL, "email": EMAIL,
        "address": {"@type": "PostalAddress", "streetAddress": BIZ["street"][lang], "addressLocality": BIZ["city"][lang],
                    "postalCode": BIZ["zip"], "addressRegion": "Αττική" if lang == "el" else "Attica", "addressCountry": "GR"},
        "hasMap": MAPS, "areaServed": {"@type": "Country", "name": "Ελλάδα" if lang == "el" else "Greece"},
        "sameAs": [FB, IG, MAPS],
        "knowsAbout": ["πισίνες προκάτ", "liner πισίνας", "πισίνα υπερχείλισης", "πισίνα με skimmer"] if lang == "el"
        else ["prefab swimming pools", "pool liner", "overflow pools", "skimmer pools"],
        "contactPoint": [{"@type": "ContactPoint", "telephone": MOBILE_TEL, "contactType": "customer service",
                          "availableLanguage": ["el", "en"]}],
    }


def breadcrumb_ld(p):
    t = T[p["lang"]]
    home = "/" if p["lang"] == "el" else "/en/"
    items = [(t["home"], home)] + p.get("crumbs", []) + [(p.get("short", p["h1"]), p["path"])]
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": DOMAIN + h} for i, (n, h) in enumerate(items)]}


def faq_block(faq, lang, title=None):
    title = title or T[lang]["faq"]
    qs = "".join('<details class="qa"><summary>%s</summary><div>%s</div></details>' % (q, a if a.startswith("<") else "<p>%s</p>" % a)
                 for q, a in faq)
    return '<section class="sec"><div class="wrap narrow"><h2>%s</h2>%s</div></section>' % (title, qs)


def quote_block(lang):
    if lang == "el":
        f = dict(h="Πείτε μας για τον χώρο σας", p="Γράψτε περιοχή και περίπου διαστάσεις. Σας καλούμε πίσω, συνήθως την ίδια μέρα, με πρόταση και τιμή για τη δική σας πισίνα.",
                 name="Όνομα", phone="Τηλέφωνο", area="Περιοχή ή νησί", type="Τι σας ενδιαφέρει",
                 opts=["Πισίνα με skimmer", "Πισίνα υπερχείλισης", "Μικρή ή υπερυψωμένη πισίνα", "Ανακαίνιση / νέο liner", "Δεν ξέρω ακόμη"],
                 dims="Διαστάσεις (π.χ. 8 × 4 m)", msg="Κάτι ακόμη;", send="Αποστολή αιτήματος", alt="ή στείλτε το ίδιο μήνυμα:",
                 note="Τα στοιχεία σας χρησιμοποιούνται μόνο για να σας απαντήσουμε.", priv="/aporrito/", privt="Απόρρητο",
                 or_="ή καλέστε", hours="Δευτέρα–Σάββατο")
    else:
        f = dict(h="Tell us about your plot", p="Add the area and a rough size. We call you back, usually the same day, with a proposal and a price for your pool.",
                 name="Name", phone="Phone", area="Area or island", type="You are interested in",
                 opts=["Skimmer pool", "Overflow pool", "Small or raised pool", "Renovation / new liner", "Not sure yet"],
                 dims="Size (e.g. 8 × 4 m)", msg="Anything else?", send="Send request", alt="or send the same message by:",
                 note="Your details are used only to reply to you.", priv="/en/privacy/", privt="Privacy",
                 or_="or call", hours="Monday–Saturday")
    opts = "".join("<option>%s</option>" % o for o in f["opts"])
    return """<section class="quote" id="quote">
 <div class="wrap quote-in">
  <div class="quote-text">
   <h2>{h}</h2><p>{p}</p>
   <p class="quote-call">{or_}<br><a href="tel:{tel}">{phone}</a><br><a href="https://wa.me/{wa}">{mobile}</a> <small>WhatsApp · Viber</small></p>
   <p class="quote-addr">{addr}<br><a href="{maps}" rel="noopener">Google Maps →</a></p>
  </div>
  <form class="qform" novalidate>
   <label>{name}<input name="name" autocomplete="name" required></label>
   <label>{phonel}<input name="phone" type="tel" autocomplete="tel" required></label>
   <label>{area}<input name="area"></label>
   <label>{type}<select name="type">{opts}</select></label>
   <label>{dims}<input name="dims"></label>
   <label class="full">{msg}<textarea name="msg" rows="3"></textarea></label>
   <input class="hp" name="_honey" tabindex="-1" autocomplete="off" aria-hidden="true">
   <div class="full qbtns">
    <button class="btn" type="submit">{send}</button>
    <span class="qalt">{alt} <button class="lnk" type="button" data-via="wa">WhatsApp</button> · <button class="lnk" type="button" data-via="viber">Viber</button> · <button class="lnk" type="button" data-via="mail">Email</button></span>
   </div>
   <div class="full qres" hidden role="status"></div>
   <p class="full small">{note} <a href="{priv}">{privt}</a></p>
  </form>
 </div>
</section>
""".format(opts=opts, tel=PHONE_TEL, phone=PHONE, wa=WA, mobile=MOBILE, addr=T[lang]["addr"], maps=MAPS,
           phonel=f["phone"], **{k: v for k, v in f.items() if k not in ("phone", "opts")})


def footer(p):
    lang = p["lang"]
    t = T[lang]
    cols = "".join('<div><h3>%s</h3>%s</div>' % (g, "".join('<a href="%s">%s</a>' % (h, n) for h, n in links))
                   for g, links in MENU[lang][:3])
    return """<footer class="foot">
 <div class="wrap foot-grid">
  <div class="foot-biz"><a class="brand brand-foot" href="{home}">{logo}<span><b>ΣΠΑΡΤΑΚΟΣ</b><small>{tag}</small></span></a>
   <p>{addr}<br><a href="tel:{tel}">{phone}</a><br><a href="https://wa.me/{wa}">{mobile}</a> (WhatsApp, Viber)<br><a href="mailto:{email}">{email}</a></p>
   <p class="social"><a href="{maps}" rel="noopener">Google Maps</a> · <a href="{fb}" rel="noopener">Facebook</a> · <a href="{ig}" rel="noopener">Instagram</a></p>
   <p class="small">{price}</p>
  </div>
  {cols}
 </div>
 <div class="wrap foot-end"><span>© {year} {rights}</span><a href="{priv}">{privacy}</a></div>
</footer>
<nav class="mbar" aria-label="contact">
 <a href="tel:{tel}"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2c.3-.3.7-.4 1-.2 1.1.4 2.3.6 3.6.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1A17 17 0 0 1 3 4c0-.6.4-1 1-1h3.5c.6 0 1 .4 1 1 0 1.3.2 2.5.6 3.6.1.3 0 .7-.2 1z"/></svg>{call}</a>
 <a href="https://wa.me/{wa}"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15l-1.4 5 5.2-1.4A10 10 0 1 0 12 2zm5.3 14.1c-.2.6-1.3 1.2-1.8 1.2-.5.1-1 .2-3.3-.7-2.8-1.1-4.5-4-4.7-4.2-.1-.2-1.1-1.5-1.1-2.9s.7-2 1-2.3c.2-.3.5-.3.7-.3h.5c.2 0 .4 0 .6.5l.8 2c.1.2.1.3 0 .5l-.3.5-.4.4c-.1.1-.3.3-.1.6.2.3.7 1.2 1.6 1.9 1.1 1 2 1.3 2.3 1.4.3.1.5.1.6-.1l.9-1c.2-.3.4-.2.6-.1l1.9.9c.3.1.5.2.5.3.1.2.1.7-.1 1.4z"/></svg>WhatsApp</a>
 <a href="viber://chat?number=%2B{wa}"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M11.4 2C7 2 3.3 3.6 3.3 10.2c0 3.5 1 5.6 2.5 6.8V21l3-2.4c.8.2 1.7.3 2.6.3 4.4 0 8.2-1.6 8.2-8.4S15.8 2 11.4 2zm4.4 12.2c-.3.7-1.4 1.3-2 1.3-1.6.1-5-1.6-6.4-5.4-.3-.9.4-1.9 1-2.3.4-.2.8 0 1 .3l.9 1.3c.2.4.1.8-.3 1-.3.3-.3.7-.1 1 .6 1 1.4 1.7 2.4 2.2.4.2.8 0 1-.3.3-.4.7-.5 1.1-.2l1.2.9c.3.3.4.7.2 1.2z"/></svg>Viber</a>
 <a class="mbar-q" href="{contact}#quote">{quote}</a>
</nav>
<div class="lb" hidden><button class="lb-x" aria-label="close">×</button><button class="lb-p" aria-label="previous">‹</button><figure><img alt=""><figcaption></figcaption></figure><button class="lb-n" aria-label="next">›</button></div>
""".format(home="/" if lang == "el" else "/en/", logo=LOGO, tag=t["tagline"], addr=t["addr"], tel=PHONE_TEL,
           phone=PHONE, wa=WA, mobile=MOBILE, email=EMAIL, maps=MAPS, fb=FB, ig=IG, price=t["price"], cols=cols,
           year=2026, rights=t["rights"], priv="/aporrito/" if lang == "el" else "/en/privacy/", privacy=t["privacy"],
           call=t["call"], contact="/epikoinonia/" if lang == "el" else "/en/contact/", quote=t["quote"])


# ---------- content helpers ----------
def cards(items, cls="cards"):
    """items: (href, photo, title, text)"""
    out = []
    for href, photo, title, text in items:
        out.append('<a class="card" href="%s">%s<span class="card-b"><b>%s</b><span>%s</span></span></a>'
                   % (href, pic(photo, title, "(min-width: 960px) 30vw, (min-width: 600px) 45vw, 90vw"), title, text))
    return '<div class="%s">%s</div>' % (cls, "".join(out))


def gallery(items, cls="gallery"):
    """items: (photo, caption)"""
    return '<div class="%s">%s</div>' % (cls, "".join(
        '<figure>%s<figcaption>%s</figcaption></figure>' % (pic(n, c, "(min-width: 960px) 33vw, 50vw", zoom=True), c)
        for n, c in items))


def sec(title, body, cls="sec", narrow=True, kicker="", id_=""):
    k = '<p class="kicker">%s</p>' % kicker if kicker else ""
    h = "<h2>%s</h2>" % title if title else ""
    return '<section class="%s"%s><div class="wrap%s">%s%s%s</div></section>' % (
        cls, ' id="%s"' % id_ if id_ else "", " narrow" if narrow else "", k, h, body)


def split(img, alt, body, rev=False, cls=""):
    return '<div class="split%s%s"><div class="split-img">%s</div><div class="split-text">%s</div></div>' % (
        " split-rev" if rev else "", " " + cls if cls else "", pic(img, alt, "(min-width: 960px) 45vw, 100vw", zoom=True), body)


def steps(items):
    return '<ol class="steps">%s</ol>' % "".join('<li><b>%s</b><p>%s</p></li>' % i for i in items)


def table(head, rows, cls="tbl"):
    h = "".join("<th>%s</th>" % x for x in head)
    r = "".join("<tr>%s</tr>" % "".join("<td>%s</td>" % c for c in row) for row in rows)
    return '<div class="tbl-wrap"><table class="%s"><thead><tr>%s</tr></thead><tbody>%s</tbody></table></div>' % (cls, h, r)


def note(text, cls="note"):
    return '<aside class="%s">%s</aside>' % (cls, text)


def related(lang, items):
    title = "Συνεχίστε την ανάγνωση" if lang == "el" else "Read next"
    links = "".join('<a href="%s"><b>%s</b><span>%s</span></a>' % i for i in items)
    return '<section class="sec sec-tint"><div class="wrap"><h2>%s</h2><div class="rel">%s</div></div></section>' % (title, links)


def P(lang, path, title, desc, h1, lead, hero, hero_alt, body, **kw):
    d = dict(lang=lang, path=path, title=title, desc=desc, h1=h1, lead=lead, hero=hero, hero_alt=hero_alt, body=body)
    d.update(kw)
    return d
