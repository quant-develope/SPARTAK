"""English pages (/en/): the main topics for foreign owners of homes and villas in Greece."""
from parts import P, pic, cards, gallery, sec, split, steps, table, note, related, faq_block, quote_block, PHONE, PHONE_TEL, WA, MOBILE, EMAIL, MAPS
from el_main import SIZES
from el_build import SERIES, nice


def N(*a, **kw):
    return P("en", *a, **kw)


POOLS = [("Prefab pools", "/en/prefab-pools/")]

PROJECTS = [
    ("pisina-thea-thalassa-veranta", "Terrace pool with a view", "Steps, decking and the sea on the horizon"),
    ("pisina-yperxeilisi-skouro-liner", "Overflow with a dark liner", "Water spills over along the whole length"),
    ("pisina-xylini-stefani-gazon", "Timber coping pool", "Turquoise water, artificial lawn, open view"),
    ("pisina-yperypsomeni-nychta", "Raised pool at night", "Lifted above ground and wrapped in decking"),
    ("pisina-limnos-petrino-spiti", "Limnos, 2023", "Skimmer pool next to a stone guesthouse"),
    ("pisina-psifida-deck-vrady", "Mosaic-pattern liner", "LED lights and a full-length deck"),
]


def home():
    hero = """<section class="hero">
 %s
 <div class="wrap hero-in">
  <p class="kicker">Pisina Prokat Greece · Athens</p>
  <h1>Prefab pools for homes and villas across Greece</h1>
  <p class="lead">Galvanised steel walls, a watertight liner with a 10-year written warranty, and one team from the site visit to the first swim. Athens, the islands and the mainland.</p>
  <div class="hero-cta"><a class="btn" href="#quote">Ask for a quote</a><a class="btn btn-light" href="/en/projects/">See our projects</a></div>
 </div>
</section>
<section class="stats"><div class="wrap"><ul>
 <li><b>28+</b><span>years building prefab pools</span></li>
 <li><b>10 years</b><span>written liner warranty</span></li>
 <li><b>2 mm</b><span>galvanised steel panels</span></li>
 <li><b>&lt; 50 m²</b><span>no full building permit</span></li>
</ul></div></section>
""" % pic("pisina-thea-thalassa-veranta", "Prefab pool on a terrace overlooking the sea", "100vw", eager=True)
    body = sec("Three ways to have a pool", """<p style="max-width:60ch">Every pool we build is prefabricated: the same steel frame and the same liner. What changes is how the water circulates and how the pool sits on your plot.</p>""" + cards([
        ("/en/skimmer-pool/", "pisina-xylini-stefani-gazon", "Skimmer pool", "The simple, popular choice for family homes and holiday houses."),
        ("/en/overflow-pool/", "pisina-yperxeilisi-skouro-liner", "Overflow pool", "Water level with the deck, like a mirror. For villas and rentals."),
        ("/en/pool-sizes/", "pisina-yperypsomeni-kanapes", "Small or raised", "For town gardens and sloping plots. Less digging, same quality."),
    ], "cards-big"), narrow=False, kicker="Pool types")
    body += sec("", split("panels-trigona-antistirixis", "Galvanised panels and braces of a prefab pool",
        """<p class="kicker">Behind the liner</p><h2>A steel frame and a watertight skin</h2>
<p>A prefab pool is not a temporary pool. It is a permanent structure whose walls arrive as factory-made panels and are bolted together on site.</p>
<ul class="ticks"><li><b>2 mm galvanised steel panels</b>, 1.10 or 1.50 m high.</li><li><b>Adjustable braces</b> at every joint keep the walls perfectly vertical.</li><li><b>1.5 mm reinforced PVC liner</b>, welded on site, 10-year written warranty.</li><li><b>Flexible, so it does not crack</b> when the ground moves, a real advantage in Greece.</li></ul>
<p><a href="/en/prefab-pools/">How a prefab pool is built →</a></p>"""), cls="sec sec-tint", narrow=False)
    body += quote_block("en")
    body += sec("", '<div class="sec-head"><div><p class="kicker">Our work</p><h2>Pools people already swim in</h2></div><a href="/en/projects/">All projects →</a></div><div class="scroller">%s</div>' % "".join(
        '<figure class="proj">%s<figcaption><b>%s</b>%s</figcaption></figure>' % (pic(n, t, "(min-width: 900px) 360px, 80vw", zoom=True), t, c) for n, t, c in PROJECTS), narrow=False)
    body += sec("Building from abroad?", """<div class="cols cols-2"><div><p>Many of our clients live outside Greece and visit their house a few times a year. We are used to working that way: photos and short videos at every stage on WhatsApp, a written proposal in English, and a pool that is ready and clean when you arrive.</p>
<p>The engineer who signs the small-scale works approval is part of the process, so you do not need to find one yourself. <a href="/en/pool-permit/">How the permit works →</a></p></div>
<ul class="ticks"><li>Proposal and updates in English</li><li>Site visit before any price is given</li><li>Materials shipped to the islands by ferry</li><li>Automatic dosing for pools that are often unattended</li><li>Seasonal opening and closing on request</li></ul></div>""", cls="sec sec-sea", narrow=False, kicker="For foreign owners")
    body += sec("What clients say", """<div class="revs">
<figure class="rev"><blockquote>Mr. Spartakos is very professional, provides great service! Best contractor in Greece! We have the best pool and jacuzzis in Limnos.</blockquote><figcaption class="small">Elysian Limnos · Google review</figcaption></figure>
<figure class="rev"><blockquote>From the first meeting he explained the small-scale approval and the order of the works, and advised us not to overdo it.</blockquote><figcaption class="small">Google review, translated from Greek</figcaption></figure>
<figure class="rev"><blockquote>Very professional!</blockquote><figcaption class="small">Helena · Google review</figcaption></figure>
</div>""", narrow=False, kicker="Reviews")
    faq = [
        ("How long does a prefab pool last?", "The panels are galvanised steel made to live in damp ground, and the liner carries a 10-year written warranty. With well-kept water it usually lasts longer, and when it is finally worn, only the liner is replaced."),
        ("Do I need a building permit?", 'For a water surface under 50 m² a small-scale works approval is usually enough. See <a href="/en/pool-permit/">the conditions</a>.'),
        ("How much does it cost?", "Every pool is priced on its own, depending on size, system, liner, equipment and site access. Ask us and we will send a free written quote."),
        ("Do you build on the islands?", 'Yes, from Mykonos and Rhodes to Corfu and Limnos. See <a href="/en/pools-on-islands/">how island projects work</a>.'),
    ]
    body += faq_block(faq, "en")
    return N("/en/", "Prefab Swimming Pools in Greece | Pisina Prokat Greece",
             "Prefab swimming pools in Athens, the Greek islands and mainland Greece: galvanised steel panels, PVC liner with a 10-year warranty, skimmer or overflow. Free quote.",
             "Prefab pools", "", "pisina-thea-thalassa-veranta", "", body, alt="/", home_hero=hero, cls="home", faq=faq, faq_inline=True, no_quote=True)


def prefab():
    body = sec("", """<div class="prose"><h2>Five layers, two jobs</h2>
<p>Cut a prefab pool in half and you find the ground, a level base, a steel frame, the pipework running behind it and, on the inside, a PVC membrane that holds the water. The frame gives shape and strength. The liner gives watertightness. Neither depends on the other, which is why the system is so forgiving.</p></div>""" + table(["Part", "What it is", "Why it matters"], [
        ["Panels", "2 mm galvanised steel, 1.10 or 1.50 m high", "Set the shape and depth, resist damp soil"],
        ["Anchoring", "Four expansion bolts per panel", "Nothing moves when the pool is filled"],
        ["Braces", "4 mm hot-dip galvanised steel, adjustable", "Keep the walls vertical, carry the backfill"],
        ["Liner", "1.5 mm fibre-reinforced PVC, or 1.8 mm textured membrane", "Watertight, any colour, 10-year warranty"],
    ]) + split("panels-galvanismena-seira", "Row of galvanised panels in the excavation", """<h3>It does not crack</h3>
<p>Rigid pools are sealed with renders that can open when the ground settles or after an earthquake. A liner is flexible: it follows small movements instead of breaking.</p>
<h3>It goes up fast</h3>
<p>Panels come ready from the factory. There is no formwork and nothing to wait for to cure, so the work on your plot takes days rather than weeks.</p>
<h3>It reaches awkward plots</h3>
<p>Two people can carry a panel. Narrow side passages, steps, terraces and ferries are not a problem.</p>""") + split("vasi-pisinas-prokat", "Base of a prefab pool with the first panels", """<h3>What to keep in mind</h3>
<ul><li>Sharp objects can damage a liner: use soft brushes and pool-safe cleaners.</li><li>A liner pool is not emptied in winter. The water holds the liner in place.</li><li>Balanced water chemistry (pH 7.0–7.4) adds years to the liner.</li></ul>
<p>Next: <a href="/en/skimmer-pool/">skimmer pool</a> or <a href="/en/overflow-pool/">overflow pool</a>.</p>""", rev=True), narrow=False)
    return N("/en/prefab-pools/", "Prefab Pools: How They Are Built | Pisina Prokat Greece",
             "How a prefab swimming pool is built: 2 mm galvanised steel panels, adjustable braces, 1.5 mm PVC liner with a 10-year warranty. Why it does not crack and installs fast.",
             "Prefab pools: a steel frame that holds water for decades",
             "Before choosing a colour or a size, it helps to know what sits behind the liner. Here is every part of the pool, as we build it.",
             "panels-trigona-antistirixis", "Galvanised steel panels of a prefab pool", body, short="Prefab pools", kicker="The technology",
             alt="/pisina-prokat/", facts=[("2 mm", "steel panels"), ("1.10 / 1.50 m", "panel height"), ("1.5 mm", "PVC liner"), ("10 yrs", "liner warranty")])


def skimmer():
    body = sec("", """<div class="prose"><h2>How it works</h2>
<p>Openings in the pool wall just below the coping, the skimmers, draw in the surface water with whatever floats on it: leaves, insects, dust. The pump sends it through the filter and back into the pool through return jets on the opposite side, so the whole pool keeps moving.</p>
<p>The water stays 10–15 cm below the top of the wall, which is the visible difference from an overflow pool.</p>
<h2>Why most families choose it</h2>
<ul class="ticks"><li>No perimeter channel and no balance tank.</li><li>A compact filter unit is enough for small and medium pools.</li><li>Simple care: empty the skimmer basket and the surface stays clean.</li><li>The most economical of the systems we build.</li></ul>
<h2>How many skimmers?</h2>
<p>Roughly one per 25 m² of water: one for a 4 × 3 m pool, two for 8 × 4 m. We place them downwind, so the breeze pushes leaves towards them.</p></div>""" + gallery([
        ("pisina-xylini-stefani-gazon", "Timber coping and lawn"), ("pisina-skala-inox", "Stainless steel ladder"),
        ("pisina-limnos-petrino-spiti", "Limnos guesthouse pool")]))
    return N("/en/skimmer-pool/", "Skimmer Pool: Simple and Economical | Pisina Prokat Greece",
             "Prefab skimmer pool: how the water circulates, how many skimmers you need, and why it is the simplest and most economical choice for a family home in Greece.",
             "Skimmer pool: the simple system that just works",
             "Most of our family projects are skimmer pools. Little equipment, a small filter unit, easy care and clear water all summer.",
             "pisina-xylini-stefani-gazon", "Skimmer pool with timber coping", body, short="Skimmer pool", kicker="Pool type", crumbs=POOLS, alt="/pisina-skimmer/")


def overflow():
    body = sec("", """<div class="prose"><h2>What happens at the edge</h2>
<p>In an overflow pool the water rises to the very top and spills gently into a channel around the pool. A grating about 25 cm wide, in plastic or marble, covers the channel and can be walked on. The water collects in a balance tank, is filtered and returns to the pool.</p>
<p>The surface sits level with the deck, with no visible wall. At night, with the lights on, it turns into a mirror.</p>
<h2>When it is worth it</h2>
<ul class="ticks"><li>Larger pools, from around 60 m², where skimmers cannot keep up.</li><li>Rentals and villas with many swimmers: the surface cleans itself continuously.</li><li>Architect-designed houses where the pool must sit flush with the floor.</li><li>Plots with a view, where the water seems to merge with the horizon.</li></ul></div>"""
        + note("<p>The balance tank needs space close to the plant room. We plan it from day one, so it does not take room from the garden.</p>")
        + gallery([("pisina-yperxeilisi-skouro-liner", "Dark liner, full-length overflow"), ("pisina-yperxeilisi-thea", "Overflow with a sea view"),
                   ("kanali-yperxeilisis-schara", "Channel and grating")]))
    return N("/en/overflow-pool/", "Overflow Pool: Water Level with the Deck | Pisina Prokat Greece",
             "Prefab overflow pool with a perimeter channel, 25 cm grating and balance tank. A mirror-like surface for villas, holiday rentals and large pools in Greece.",
             "Overflow pool: water level with the deck",
             "The water rises to the edge and spills into a channel all around. The surface stays clean even with many swimmers.",
             "pisina-yperxeilisi-thea", "Overflow prefab pool with a view", body, short="Overflow pool", kicker="Pool type", crumbs=POOLS, alt="/pisina-yperxeilisis/")


def sizes():
    rows = []
    for L, W in SIZES:
        a = L * W
        rows.append(["%g × %g m" % (L, W), "%g m²" % a, "~%d m³" % round(a * 0.98), "~%d m³" % round(a * 1.38),
                     "Small-scale approval" if a < 50 else "<b>Building permit</b>"])
    body = quote_block("en") + sec("", table(["Size", "Water area", "Water, 1.10 m panels", "Water, 1.50 m panels", "Approval"], rows) + """<div class="prose">
<h2>Choosing a size</h2>
<p><b>Who will swim?</b> For laps, aim for at least 8 m of length. For children playing, 4 m of width or more. For cooling off with a drink, 4 × 3 m with a bench is plenty.</p>
<p><b>How much space is left?</b> Keep at least 1–1.5 m of deck around the pool, room for two loungers and a spot for the plant room.</p>
<p><b>Where does the water come from?</b> On dry islands, every cubic metre counts: an 8 × 4 m pool with 1.10 m panels needs about 13 m³ less than with 1.50 m panels.</p>
<p><b>Under 50 m²?</b> A long, narrow 12 × 4 m pool (48 m²) gives real swimming length and stays under the limit.</p></div>""")
    return N("/en/pool-sizes/", "Pool Sizes: Water Area, Volume, Permit | Pisina Prokat Greece",
             "Prefab pool sizes from 4 × 3 to 12 × 6 m: water area, volume with 1.10 or 1.50 m panels, and when a small-scale approval is enough, and how to choose.",
             "Pool sizes: how much water, how much space, which approval",
             "Find your size in the table or send us the size of your space: water area, volume to fill and whether the pool stays under 50 m².",
             "pisina-makria-foinikes", "Long narrow prefab pool between palm trees", body, short="Sizes", kicker="Sizes", crumbs=POOLS, alt="/diastaseis-pisinas/", no_quote=True)


def permit():
    body = sec("", """<div class="prose"><h2>The small-scale works approval</h2>
<p>In Greece, a private pool with a water surface under 50 m² usually does not need a full building permit. It needs a <b>small-scale works approval</b> (έγκριση εργασιών μικρής κλίμακας): faster, cheaper and without a full set of engineering studies. Before work starts, a licensed engineer signs a declaration covering the structure and the electrics.</p>
<h2>The conditions in plain words</h2></div>""" + table(["Condition", "What it means"], [
        ["Water surface under 50 m²", "Only the water counts, not the deck around it"],
        ["Depth up to 1.5 m", "Prefab panels are 1.10 or 1.50 m high"],
        ["Up to 1 m above natural ground", "Also applies to raised pools"],
        ["Excavation or fill up to 1 m", "The terrain is not reshaped dramatically"],
        ["Compact filter unit", "Filter and pump in a single unit"],
        ["Planting of the open area kept", "The plot's mandatory greenery stays"],
        ["Engineer's declaration", "Signed before work starts; we coordinate it"],
    ]) + note("<p>Rules change and depend on each plot (outside town plans, traditional settlements, archaeological zones). The engineer confirms your case before any work. This is general information, not legal advice.</p>", "note note-coral") + """<div class="prose">
<h2>Over 50 m²?</h2><p>Then a building permit is needed. It is perfectly possible, it just takes longer. If you are a few square metres over, a long narrow pool often solves it.</p>
<h2>After the build</h2><p>A private pool is declared on the E9 property form and affects property tax (ENFIA) and income presumptions. Your accountant will give you the current figures.</p></div>""")
    return N("/en/pool-permit/", "Pool Permit in Greece: Small-Scale Approval | Pisina Prokat Greece",
             "Do you need a building permit for a pool in Greece? Under 50 m² of water a small-scale works approval is usually enough. The conditions explained in plain English.",
             "Pool permit in Greece: the small-scale works approval",
             "A pool with under 50 m² of water usually needs a simple approval, not a full building permit. Here are the conditions, in plain English.",
             "pisina-prin-to-gemisma", "Prefab pool just before filling", body, short="Pool permit", kicker="Permits", alt="/egkrisi-mikris-klimakas/")


EN_SERIES = {"Classic": "Smooth plain-colour PVC", "3D-Uni": "Plain colour with a fine 3D texture", "StoneFlex": "Reinforced 3D, natural stone texture",
             "StoneTile": "Reinforced 3D, stone tile look", "Matrix": "Glass mosaic look with a pearl sheen", "Larch": "Larch wood look with relief",
             "Printed NG": "Printed patterns under a protective lacquer"}


def liner():
    sw = ""
    for s, d, slip, n, photos in SERIES:
        sw += '<h3>%s <span class="small">· %s</span></h3><div class="swatches">%s</div>' % (s, EN_SERIES[s], "".join(
            '<figure>%s<figcaption>%s</figcaption></figure>' % (pic(p, "Haogenplast liner " + nice(p), "160px", zoom=True), nice(p)) for p in photos))
    body = sec("", """<div class="prose"><p>The liner is the pool you actually see and touch: a PVC membrane that lines the floor, walls and steps as one watertight shell. We use 1.5 mm fibre-reinforced liner with a 10-year written warranty, or 1.8 mm reinforced membranes with a textured, anti-slip surface.</p>
<h2>Colour first</h2></div>""" + table(["Liner", "Water looks", "Goes with"], [
        ["White", "Bright, Cycladic turquoise", "White walls, marble"], ["Light blue", "Classic pool blue", "Any garden"],
        ["Sand", "Green-turquoise, like a shallow beach", "Stone, timber"], ["Light grey", "Natural blue-green", "Modern houses"],
        ["Dark grey, anthracite", "Deep blue-green, mirror-like", "Overflow pools, minimal design"],
    ]) + """<div class="prose"><h2>Haogenplast ranges</h2><p>We use Haogenplast membranes, certified to EN 15836-2, and SOPREMAPOOL anti-slip membranes.</p></div>""" + table(
        ["Range", "Type", "Anti-slip", "Colours"], [[s, EN_SERIES[s], slip.replace("Ναι, κατ.", "Yes, class").replace("Λεία", "Smooth"), n] for s, d, slip, n, _ in SERIES])
        + sw + '<p class="small" style="margin-top:14px">Manufacturer photos. Screen colours differ from the real material: ask us for a sample.</p>')
    return N("/en/pool-liner/", "Pool Liner Colours & Haogenplast Ranges | Pisina Prokat Greece",
             "Pool liner for prefab pools: 1.5 mm PVC with a 10-year warranty and Haogenplast ranges Classic, 3D-Uni, StoneFlex, StoneTile, Matrix, Larch. How each colour changes the water.",
             "Pool liner: colour, texture and watertightness in one membrane",
             "The liner decides how your pool looks and how the steps feel underfoot. See colours, textures and the ranges we use.",
             "pisina-liner-psifida", "Pool with a mosaic-pattern liner", body, short="Liner", kicker="Finish", alt="/liner-pisinas/")


def projects():
    body = sec("", gallery([
        ("pisina-thea-thalassa-veranta", "Terrace pool with a sea view"), ("pisina-xylini-stefani-gazon", "Timber coping and lawn"),
        ("pisina-yperxeilisi-skouro-liner", "Overflow with a dark liner"), ("pisina-yperxeilisi-thea", "Overflow facing the sea"),
        ("pisina-skouro-liner-deck", "Dark liner and deck"), ("pisina-yperypsomeni-nychta", "Raised pool at night"),
        ("pisina-deck-xaplostres", "Deck for loungers"), ("pisina-psifida-deck-vrady", "Mosaic liner at dusk"),
        ("pisina-yperypsomeni-kanapes", "Raised pool with built-in seating"), ("pisina-vila-katarraktis", "Villa pool with a waterfall"),
        ("pisina-limnos-petrino-spiti", "Limnos guesthouse pool"), ("jacuzzi-limnos", "Limnos jacuzzi"),
    ]), narrow=False)
    body += sec("Selected projects", table(["Place", "Year", "Project"], [
        ["Villa Christy, Mykonos", "2024", "Villa pool"], ["Kleopatra estate, Koropi", "2024", "Estate pool"], ["Limnos", "2023", "Guesthouse pool and jacuzzi"],
        ["Trikala", "2022–2023", "Skimmer pools"], ["Glyfada", "2014, 2022", "Prefab pools"], ["Rhodes", "2020", "Prefab pool"],
        ["Lagonisi", "2019", "Overflow pool"], ["Kifisia", "2016", "Skimmer pool"], ["Corfu", "2014", "Prefab pool"]]))
    return N("/en/projects/", "Projects: Prefab Pools We Built | Pisina Prokat Greece",
             "Photos of prefab pools we built in Greece: overflow, skimmer and raised pools, villa pools. Mykonos, Limnos, Rhodes, Corfu, Glyfada, Koropi and more.",
             "Projects: pools people already swim in", "From town gardens to island villas. Tap a photo to see it large.",
             "pisina-xylini-stefani-gazon", "Prefab pool with timber coping", body, short="Projects", kicker="Portfolio", alt="/erga/")


def islands():
    body = sec("", steps([
        ("Transport", "Panels, braces, liner and equipment fit on one truck, travel on the regular ferry and reach the plot without special vehicles. Where a road ends, they are carried by hand."),
        ("Water", "On dry islands we suggest 1.10 m panels where they suit, which cuts the volume noticeably, and we organise filling by water truck."),
        ("Time on site", "The crew arrives once all materials are on the island. The build itself is short, so fewer nights away and lower costs for you."),
        ("Salt and wind", "Suitable stainless steel, a sheltered plant room and a pool position protected from the north wind."),
        ("When you are away", "Automatic pH and chlorine dosing and, if you wish, a local partner for regular visits."),
    ]) + """<div class="prose" style="margin-top:22px"><h2>When to start</h2>
<p>For a pool ready in June, start talking in winter: the approval, the liner order and ferry bookings all take time. In July and August ports are busy and many islands restrict building work.</p></div>""" + gallery([
        ("pisina-limnos-petrino-spiti", "Limnos"), ("pisina-limnos-vrady", "Limnos at dusk"), ("mini-pisina-kataskevi-thea", "Building with a sea view")]))
    return N("/en/pools-on-islands/", "Building a Pool on a Greek Island | Pisina Prokat Greece",
             "Prefab pools on the Greek islands: shipping materials by ferry, filling with little water, salt and wind, timing. Cyclades, Dodecanese, Ionian, North Aegean.",
             "Pools on the Greek islands: the pool that travels by ferry",
             "Transport, water, salt and crew time make island projects different. Here is how we organise them so your pool is ready for summer.",
             "pisina-limnos-petrino-spiti", "Prefab pool in Limnos next to a stone house", body, short="Islands", kicker="Islands", alt="/pisina-se-nisi/")


def faq_page():
    qs = [
        ("What is a prefab pool?", 'A permanent pool with walls made of factory-made galvanised steel panels, anchored to a base and lined with a watertight PVC membrane. <a href="/en/prefab-pools/">How it is built</a>.'),
        ("How deep is it?", "Panels are 1.10 or 1.50 m high, giving a water depth of about 1.0 or 1.4 m."),
        ("Do I need a permit?", 'Under 50 m² of water, usually a small-scale works approval. Over 50 m², a building permit. <a href="/en/pool-permit/">Details</a>.'),
        ("How much does it cost?", "Prices are given on request and agreed for each pool, depending on size, depth, system, liner, equipment and access. The quote is free."),
        ("Is the liner guaranteed?", "Yes, with a 10-year written warranty."),
        ("Do I empty the pool in winter?", "No. The water keeps the liner in place. The pool is cleaned, treated with a winter product and covered."),
        ("Salt or chlorine?", "Both disinfect with chlorine. A salt system makes it automatically from a low dose of salt, and feels softer on the skin."),
        ("Can you work while I am abroad?", "Yes. We send photos and videos on WhatsApp at every stage."),
    ]
    return N("/en/faq/", "Prefab Pool FAQ | Pisina Prokat Greece",
             "Answers about prefab pools in Greece: depth, permits, price, liner warranty, winter care, salt or chlorine, building while you are abroad.",
             "Questions about prefab pools", "Short answers to what clients ask us most. Missing something? Message us on WhatsApp.",
             "pisina-skala-inox", "Prefab pool with stainless ladder", "", short="Questions", kicker="FAQ", alt="/erotiseis/", faq=qs)


def contact():
    body = sec("", """<div class="cols"><div><h3>Phone</h3><p><a href="tel:%s">%s</a></p><h3>Mobile, WhatsApp, Viber</h3><p><a href="https://wa.me/%s">%s</a></p></div>
<div><h3>Email</h3><p><a href="mailto:%s">%s</a></p><h3>Address</h3><p>Xenofontos 112<br>176 74 Kallithea, Attica, Greece<br><a href="%s" rel="noopener">Open in Google Maps →</a></p></div>
<div><h3>What to send us</h3><ul class="ticks"><li>Location of the property</li><li>Size of the space or the pool</li><li>Skimmer or overflow, if you know</li><li>A few photos of the plot on WhatsApp</li></ul></div></div>"""
               % (PHONE_TEL, PHONE, WA, MOBILE, EMAIL, EMAIL, MAPS), narrow=False)
    return N("/en/contact/", "Contact & Free Quote | Pisina Prokat Greece",
             "Contact Pisina Prokat Greece, Xenofontos 112, Kallithea, Athens. Phone +30 212 104 8320, WhatsApp/Viber +30 693 650 5824. Free quote for a prefab pool in Greece.",
             "Tell us about your pool", "A call or a message with two photos is enough to start. The quote is free.",
             "pisina-me-deck-spiti", "Prefab pool with deck next to the house", body, short="Contact", kicker="Contact", alt="/epikoinonia/")


def privacy():
    body = sec("", """<div class="prose"><p>The website “Pisina Prokat Greece” belongs to Spartakos Pools (Πισίνες Σπάρτακος), Xenofontos 112, 176 74 Kallithea, Greece (pisina.gr@gmail.com).</p>
<h2>What we receive</h2><p>When you send the quote form, we receive by email the details you entered: name, phone, area, size and message. If you write to us on WhatsApp, Viber or email, we receive what you send there.</p>
<h2>Why</h2><p>Only to reply and send you a quote. We do not sell or share your details for advertising, and we send no newsletters.</p>
<h2>Cookies</h2><p>No tracking or advertising cookies. Fonts are loaded from Google Fonts.</p>
<h2>Your rights</h2><p>Ask for access, correction or deletion at pisina.gr@gmail.com. You may also complain to the Hellenic Data Protection Authority.</p></div>""")
    return N("/en/privacy/", "Privacy Policy | Pisina Prokat Greece", "How we use the details you send through the quote form.",
             "Privacy policy", "Short and clear: what we receive, why, and how to delete it.",
             "pisina-tirkouaz-nero", "Pool with turquoise water", body, short="Privacy", alt="/aporrito/", no_quote=True)


def pages():
    return [home(), prefab(), skimmer(), overflow(), sizes(), permit(), liner(), projects(), islands(), faq_page(), contact(), privacy()]
