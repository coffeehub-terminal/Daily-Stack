#!/usr/bin/env python3
"""Builds the menu in index.html plus /c/<slug>.html, /brands.html and /request.html.
Run from anywhere: python3 _build/build.py"""
import os, re, sys, html, urllib.parse
sys.path.insert(0, os.path.dirname(__file__))
from catalog import CATEGORIES, STACKS, TOP_BRANDS, ALL_BRANDS, STACK_LIST, STRIPE

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BY = {c["slug"]: c for c in CATEGORIES}
IN_STACK = {c["slug"] for c in CATEGORIES if c["pick"]}
PICK_BRANDS = {c["pick"][0] for c in CATEGORIES if c["pick"]}

def slug(s): return re.sub(r"[^a-z0-9]+", "-", html.unescape(s).lower().replace("ï", "i")).strip("-")
def q(s): return urllib.parse.quote(html.unescape(s))
def read(p): return open(os.path.join(ROOT, p), encoding="utf-8").read()
def write(p, s):
    full = os.path.join(ROOT, p); os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, "w", encoding="utf-8").write(s)

# ---------------- menu ----------------
def li_cat(s, label=None):
    c = BY[s]; cls = ' class="in"' if s in IN_STACK else ""
    return f'<li><a{cls} href="/c/{s}">{label or c["name"]}</a></li>'
def li_brand(b):
    cls = ' class="in"' if b in PICK_BRANDS else ""
    return f'<li><a{cls} href="/brands#{slug(b)}">{b}</a></li>'
def mcol(title, lis, cls=""): return f'<div class="mcol {cls}"><h4>{title}</h4><ul>{"".join(lis)}</ul></div>'
def group(g): return [li_cat(c["slug"]) for c in CATEGORIES if c["group"] == g]
def foot(t, href="/#boxes", label="See the stacks"):
    return f'<div class="mfoot"><p>{t}</p><a class="btn small green" href="{href}">{label}</a></div>'

panels = {
 "vit": ("Vitamins &amp; supplements", '<div class="mgrid g5">' + mcol("Vitamins", group("Vitamins")) + mcol("Minerals", group("Minerals"))
         + mcol("Supplements", group("Supplements"), "span2") + mcol("Herbs &amp; plants", group("Herbs &amp; plants")) + '</div>'
         + foot("We source every category from brands we trust. <b>Green</b> = already in one of our stacks.")),
 "sport": ("Sport", '<div class="mgrid g4">'
         + mcol("Type", [li_cat(s) for s in ["creatine","electrolytes","collagen","protein","protein-bars","energy-gels","pre-workout","post-workout","green-tea"]])
         + mcol("Activity", [li_cat("electrolytes","Endurance"), li_cat("creatine","Strength &amp; muscle")])
         + mcol("Amino acids", [li_cat(s) for s in ["bcaa","carnitine","glutamine"]])
         + mcol("Brands", [li_brand(b) for b in ["Mattisson Healthstyle","NOW Foods","Applied Nutrition","BioTechUSA","OstroVit","Vitakruid"]])
         + '</div>' + foot("Training? The <b>Energy Stack</b> already includes creatine and electrolytes.")),
 "brands": ("Brands", '<div class="mgrid gb">' + mcol("Our top picks", [li_brand(b) for b in TOP_BRANDS])
         + mcol(f"All brands ({len(ALL_BRANDS)})", [li_brand(b) for b in ALL_BRANDS], "cols4") + '</div>'
         + foot("We compare all of these brands and put our top pick for each supplement in your stack.", "/brands", "All brands")),
}
chev = '<svg width="12" height="12" viewBox="0 0 24 24" aria-hidden="true"><path d="M6 9l6 6 6-6" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"/></svg>'
items = "".join(f'<li class="mitem"><button type="button" class="mbtn" aria-expanded="false" aria-controls="mp-{k}">{t}{chev}</button>'
                f'<div class="mpanel" id="mp-{k}" hidden><div class="wrap">{c}</div></div></li>' for k, (t, c) in panels.items())
MENU = (f'<!--MENU--><div class="menubar"><div class="wrap"><ul class="mlist">{items}</ul>'
        '<ul class="mlinks"><li><a href="/#boxes">Our stacks</a></li><li><a href="/request">Request a product</a></li><li><a href="/#faq">FAQ</a></li></ul></div></div><!--/MENU-->')

idx = read("index.html")
idx = re.sub(r'(<!--MENU-->)?\s*<div class="menubar">.*?(<!--/MENU-->|</div></div>(?=\s*</header>))', "\n  " + MENU, idx, count=1, flags=re.S)
idx = idx.replace('<a class="logo" href="#" aria-label="Daily Stack home"', '<a class="logo" href="/" aria-label="Daily Stack home"')
for f in ["privacy", "terms", "impressum"]:
    idx = idx.replace(f'href="{f}.html"', f'href="/{f}"')
idx = idx.replace('<a class="btn small" href="#boxes">Subscribe</a>', '<a class="btn small" href="/#boxes">Subscribe</a>')

# homepage "browse everything" + request section (inserted once, before FAQ)
groups = ["Vitamins", "Minerals", "Supplements", "Herbs &amp; plants", "Sport"]
browse_cols = "".join(f'<div class="bcol"><h3>{g}</h3><div class="bchips">' + "".join(
    f'<a class="bchip{" in" if c["slug"] in IN_STACK else ""}" href="/c/{c["slug"]}">{c["name"]}</a>' for c in CATEGORIES if c["group"] == g) + '</div></div>' for g in groups)
BROWSE = f'''<!--BROWSE--><section id="browse" aria-labelledby="b-title">
  <div class="wrap">
    <div class="sec-head">
      <div class="eyebrow">Everything we source</div>
      <h2 class="display" id="b-title"><span class="bold">{len(CATEGORIES)} supplements.</span> <span class="thin">{len(ALL_BRANDS)} brands.</span></h2>
      <p>Our stacks cover the essentials. Want something else? Pick any product below and we'll add it to your box, from the brand we rate best. <b class="g">Green</b> = already in a stack.</p>
    </div>
    <div class="browse">{browse_cols}</div>
    <div class="browse-cta"><a class="btn green" href="/request">Request a product</a><a class="btn ghost" href="/brands">See all {len(ALL_BRANDS)} brands</a></div>
  </div>
</section><!--/BROWSE-->
'''
if "<!--BROWSE-->" in idx:
    idx = re.sub(r"<!--BROWSE-->.*?<!--/BROWSE-->\n", BROWSE, idx, flags=re.S)
else:
    idx = idx.replace("<!-- ============ FAQ ============ -->", BROWSE + "\n<!-- ============ FAQ ============ -->", 1)

EXTRA_CSS = '''
/*EXTRA*/
.mcol li a{color:var(--ink);font-weight:600;text-decoration:none}
.mcol li a.in{color:var(--green-dark);font-weight:800}
.mcol li a:hover{color:var(--green-dark);text-decoration:underline}
.btn.ghost{background:transparent;color:var(--ink);box-shadow:inset 0 0 0 2px var(--ink)}
.btn.ghost:hover{background:var(--ink);color:#fff}
.g{color:var(--green-dark)}
.browse{display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:22px}
.bcol h3{margin:0 0 12px;font:800 20px 'Inter',sans-serif;letter-spacing:-0.03em}
.bchips{display:flex;flex-wrap:wrap;gap:6px}
.bchip{font-size:13px;font-weight:700;border-radius:999px;padding:5px 11px;background:#fff;text-decoration:none;border:1px solid rgba(4,38,33,.12)}
.bchip.in{background:var(--green-dark);color:#fff;border-color:var(--green-dark)}
.bchip:hover{border-color:var(--ink)}
.browse-cta{margin-top:30px;display:flex;gap:12px;flex-wrap:wrap}
@media (max-width:980px){.browse{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (max-width:620px){.browse{grid-template-columns:1fr}}
.pshelf{display:flex;flex-wrap:wrap;gap:8px;margin:2px 0 0}
.pshelf img{width:68px;height:68px;object-fit:cover;border-radius:14px;background:#fff;border:1px solid rgba(4,38,33,.1)}
.box .pshelf img{width:78px;height:78px}
@media (max-width:620px){.box .pshelf{gap:6px}.box .pshelf img{width:calc((100% - 24px)/5);height:auto;aspect-ratio:1}}
.pimg{flex:0 0 96px}.pimg img{width:96px;height:96px;object-fit:cover;border-radius:16px;background:#fff;display:block}
.pick-img{width:100%;max-width:260px;aspect-ratio:1;object-fit:cover;border-radius:18px;background:#fff;border:1px solid rgba(4,38,33,.08);display:block;margin:0 0 16px;height:auto}
.stack-hero{display:grid;grid-template-columns:1.3fr 1fr;gap:30px;align-items:end}
.stack-hero h1{font-size:clamp(46px,7vw,88px);margin-top:12px}
.badge.static{position:static;display:inline-block}
.buy{background:#fff;border-radius:var(--radius);padding:24px;display:flex;flex-direction:column;gap:12px}
.btn.big{min-height:56px;font-size:17px}
.pgrid{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:18px}
.pcard{background:#fff;border-radius:var(--radius);overflow:hidden;display:flex;flex-direction:column}
.pphoto{position:relative;background:#fff;border-bottom:1px solid rgba(4,38,33,.06)}
.pphoto img{width:100%;height:auto;aspect-ratio:1;object-fit:cover;display:block}
.pmystery{aspect-ratio:1;display:flex;align-items:center;justify-content:center;background:var(--soft);font:800 96px 'Inter',sans-serif;color:var(--green)}
.pnum{position:absolute;top:12px;left:12px;width:30px;height:30px;border-radius:50%;background:var(--ink);color:#fff;font:800 14px 'Inter',sans-serif;display:flex;align-items:center;justify-content:center}
.pbody{padding:18px 20px 20px;display:flex;flex-direction:column;gap:4px;flex:1}
.pbody h3{margin:4px 0 0;font:800 21px 'Inter',sans-serif;letter-spacing:-0.03em;line-height:1.1}
.pprod{margin:0;font-weight:700}
.pwhy{margin:8px 0 0;font-size:14px;opacity:.85}
.pbody .more{margin-top:auto;padding-top:12px;font-weight:800;font-size:14px;color:var(--green-dark);text-decoration:none}
.stack-bottom{margin-top:22px;max-width:520px}
a.pshelf{text-decoration:none}a.pshelf img{transition:transform .15s}a.pshelf:hover img{transform:translateY(-2px)}
@media (max-width:980px){.stack-hero{grid-template-columns:1fr}.pgrid{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (max-width:620px){.pgrid{gap:12px}.pbody{padding:14px}.pbody h3{font-size:18px}.pwhy{display:none}}
.box details.peek{background:none;border-radius:0;padding:10px 0 0;margin:0;border-top:1px solid rgba(4,38,33,.1)}
.box .peek summary{padding:4px 0;font-size:15px;color:var(--green-dark);display:inline-flex;justify-content:flex-start;align-items:center;gap:8px}
.box .peek summary::after,.box details.peek[open] summary::after{content:"";width:7px;height:7px;border-right:2px solid currentColor;border-bottom:2px solid currentColor;transform:rotate(45deg) translateY(-3px);font-size:0;transition:transform .15s}
.box details.peek[open] summary::after{transform:rotate(-135deg) translate(-2px,-1px)}
.peek-grid{list-style:none;margin:12px 0 0;padding:0;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:10px}
.peek-grid li{display:flex;flex-direction:column;gap:4px;font-size:12px;font-weight:700;line-height:1.2;text-align:center}
.peek-grid img,.pmystery.small{width:100%;height:auto;aspect-ratio:1;object-fit:cover;border-radius:12px;background:#fff;border:1px solid rgba(4,38,33,.1)}
.pmystery.small{font-size:32px;display:flex}
.peek-more{display:inline-block;margin-top:12px;font-size:14px;font-weight:800;color:var(--green-dark);text-decoration:none}
/* inner pages */
.crumbs{font-size:14px;margin:28px 0 18px}.crumbs a{text-decoration:none;opacity:.75}.crumbs a:hover{opacity:1}
.page-hero{padding:0 0 40px}
.page-hero h1{font-size:clamp(42px,7vw,84px);margin-top:10px}
.page-hero .lead{font-size:20px;max-width:760px;margin:18px 0 0}
.page-grid{display:grid;grid-template-columns:1.4fr 1fr;gap:22px;align-items:start}
.card{background:#fff;border-radius:var(--radius);padding:28px}
.card h2{font:800 24px 'Inter',sans-serif;letter-spacing:-0.03em;margin:0 0 14px}
.claims{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:10px}
.claims li{padding-left:28px;position:relative}
.claims li:before{content:"";position:absolute;left:0;top:5px;width:16px;height:16px;border-radius:50%;background:var(--green) url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath d='M6 12.5l4 4 8-9' fill='none' stroke='white' stroke-width='3.5' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E") center/11px no-repeat}
.small-print{font-size:13px;opacity:.75;margin:14px 0 0}
.pick{border:2px solid var(--green)}
.pick .who{font:800 30px 'Inter',sans-serif;letter-spacing:-0.04em;line-height:1.05;margin:4px 0 6px}
.pick .actions{display:flex;flex-direction:column;gap:10px;margin-top:20px}
.stack-chips{display:flex;flex-wrap:wrap;gap:6px;margin-top:12px}
.stack-chips a{font-size:13px;font-weight:800;border-radius:999px;padding:4px 12px;background:var(--soft);text-decoration:none}
.info-note{background:var(--soft);border-radius:14px;padding:14px 16px;font-size:15px;margin-top:16px}
.brand-list{display:flex;flex-wrap:wrap;gap:8px}
.brand-list a{font-weight:800;font-size:15px;border-radius:999px;padding:8px 14px;background:var(--soft);text-decoration:none}
.related{margin-top:22px}
.brands-az{columns:4;column-gap:26px}
.brands-az .b{break-inside:avoid;background:#fff;border-radius:16px;padding:14px 16px;margin:0 0 12px;scroll-margin-top:140px}
.brands-az .b:target{outline:3px solid var(--green)}
.brands-az .b h3{margin:0;font:800 18px 'Inter',sans-serif;letter-spacing:-0.02em}
.brands-az .b p{margin:4px 0 0;font-size:14px}
.brands-az .b.top{border:2px solid var(--green)}
.form{display:grid;gap:14px;max-width:640px}
.form label{font-weight:800;font-size:15px;display:grid;gap:6px}
.form input,.form select,.form textarea{font:inherit;font-weight:500;font-size:17px;border:1px solid rgba(4,38,33,.2);border-radius:12px;padding:12px 14px;background:#fff;color:var(--ink)}
.form textarea{min-height:110px}
@media (max-width:980px){.page-grid{grid-template-columns:1fr}.brands-az{columns:2}}
@media (max-width:620px){.brands-az{columns:1}}
'''
idx = re.sub(r"\n/\*EXTRA\*/.*?(?=</style>)", "", idx, flags=re.S)
idx = idx.replace("</style>", EXTRA_CSS + "</style>", 1)
# Stripe links from catalog
idx = re.sub(r"CHECKOUT: \{.*?\}", "CHECKOUT: {\n" + ",\n".join(f'    {k}: "{v}"' for k, v in STRIPE.items()) + "\n  }", idx, count=1, flags=re.S)
# Boxes: remove photo row / big button, add a subtle "View products" dropdown under the list
idx = re.sub(r'\n\s*<(?:div|a) class="pshelf".*?</(?:div|a)>', '', idx, flags=re.S)
idx = re.sub(r'<a class="btn ghost" href="/stack/[a-z]+">See every product</a>\n\s*', '', idx)
idx = re.sub(r'\n\s*<details class="peek">.*?</details>', '', idx, flags=re.S)
for st in STACK_LIST:
    sid = st["id"]
    tiles = "".join(
        (f'<li><img src="/assets/products/{im}.webp" alt="{br} {pr}" width="640" height="640" loading="lazy"><span>{lab}</span></li>' if im
         else f'<li><div class="pmystery small" aria-hidden="true">?</div><span>{lab}</span></li>')
        for lab, br, pr, cs, im in st["items"])
    peek = (f'\n        <details class="peek"><summary>View products</summary><ul class="peek-grid">{tiles}</ul>'
            f'<a class="peek-more" href="/stack/{sid}">Full details per product →</a></details>')
    idx = re.sub(r'(id="%s">.*?<ul class="inside">.*?</ul>)' % sid, lambda m: m.group(1) + peek, idx, count=1, flags=re.S)
write("index.html", idx)

# ---------------- shared template ----------------
STYLE = re.search(r"<style>(.*?)</style>", idx, re.S).group(1)
HEADER = re.search(r'<header class="top">.*?</header>', idx, re.S).group(0)
FOOTER = re.search(r"<footer>.*?</footer>", idx, re.S).group(0).replace('href="#"', 'href="/"')
MENU_JS = re.search(r"// Mega menu.*?\}\)\(\);", idx, re.S).group(0)

def page(title, desc, body, extra_js=""):
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} · Daily Stack</title>
<meta name="description" content="{html.escape(html.unescape(desc), quote=True)}">
<link rel="icon" href="/assets/favicon.ico" sizes="any">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@200;300;800&family=Mulish:wght@400;600;700;800&display=swap">
<style>{STYLE}</style>
</head>
<body>
{HEADER}
<main>
{body}
</main>
{FOOTER}
<script>
{MENU_JS}
{extra_js}
</script>
</body>
</html>
'''

PICK_IMG = {"multivitamin":"thorne-basic-nutrients","vitamin-b-complex":"thorne-b-complex","vitamin-b12":"solgar-b12","vitamin-c":"pure-vitamin-c",
 "vitamin-d3":"sunday-d3-k2","vitamin-k2":"sunday-d3-k2","magnesium":"pure-magnesium","zinc":"solgar-zinc","selenium":"solgar-selenium","omega-3":"nordic-omega",
 "collagen":"now-collagen","creatine":"mattisson-creatine","electrolytes":"now-effer-hydrate"}
SAFETY = "Food supplements are not a substitute for a varied, balanced diet and a healthy lifestyle. Do not exceed the recommended daily dose. Pregnant, breastfeeding or taking medication? Check with your doctor or pharmacist first."

def brand_links(bs): return "".join(f'<a href="/brands#{slug(b)}">{b}</a>' for b in bs)

for c in CATEGORIES:
    name = c["name"]; plain = html.unescape(name)
    claims = ("<ul class=\"claims\">" + "".join(f"<li>{x}</li>" for x in c["claims"]) + "</ul><p class=\"small-print\">Approved EU health claims.</p>") if c["claims"] else \
             "<p>There are no approved EU health claims for this product, so we don't make any. We just help you get a quality product from a brand we trust.</p>"
    if c["pick"]:
        b, prod, stacks = c["pick"]
        side = f'''<div class="card pick">
        {f'<img class="pick-img" src="/assets/products/{PICK_IMG[c["slug"]]}.webp" alt="{b} {prod}" width="640" height="640">' if c["slug"] in PICK_IMG else ""}
        <div class="eyebrow">Our pick</div>
        <div class="who">{b}</div><p style="margin:0">{prod}</p>
        <div class="stack-chips">{"".join(f'<a href="/stack/{s}">In {STACKS[s]} Stack</a>' for s in stacks)}</div>
        <div class="actions"><a class="btn green" href="/#boxes">See the stacks</a><a class="btn ghost" href="/request?p={q(plain)}">Add it on its own</a></div>
      </div>'''
    else:
        side = f'''<div class="card">
        <div class="eyebrow">Not in a stack yet</div>
        <h2 style="margin-top:6px">Add it to your box</h2>
        <p style="margin:0">Tell us you want it and we'll add it to your next box, from the brand we rate best. No extra shipping.</p>
        <div style="margin-top:20px;display:flex;flex-direction:column;gap:10px"><a class="btn green" href="/request?p={q(plain)}">Request {plain}</a><a class="btn ghost" href="/#boxes">See the stacks</a></div>
      </div>'''
    note = f'<div class="info-note">{c["note"]}</div>' if c["note"] else ""
    related = "".join(f'<a class="bchip{" in" if r["slug"] in IN_STACK else ""}" href="/c/{r["slug"]}">{r["name"]}</a>' for r in CATEGORIES if r["group"] == c["group"] and r is not c)
    body = f'''<section class="page-hero"><div class="wrap">
    <nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a> / <a href="/#browse">{c["group"]}</a> / {name}</nav>
    <div class="eyebrow">{c["group"]}</div>
    <h1 class="display bold">{name}</h1>
    <p class="lead">{c["intro"]}</p>
  </div></section>
  <section style="padding-top:0"><div class="wrap">
    <div class="page-grid">
      <div class="card">
        <h2>What it does</h2>
        {claims}
        {note}
        <h2 style="margin-top:28px">Brands we compare</h2>
        <div class="brand-list">{brand_links(c["compare"])}</div>
        <p class="small-print">{SAFETY}</p>
      </div>
      {side}
    </div>
    <div class="related"><h2 class="display" style="font-size:28px;margin:30px 0 14px"><span class="bold">More {c["group"].lower()}</span></h2><div class="bchips">{related}</div></div>
  </div></section>'''
    write(f'c/{c["slug"]}.html', page(plain, c["intro"], body))

# ---------------- brands page ----------------
uses = {}
for c in CATEGORIES:
    for b in c["compare"]: uses.setdefault(b, []).append(c)
cards = ""
for b in ALL_BRANDS:
    top = b in TOP_BRANDS
    picks = [c for c in CATEGORIES if c["pick"] and c["pick"][0] == b]
    if picks: info = "Our pick for " + ", ".join(f'<a href="/c/{c["slug"]}">{c["name"]}</a>' for c in picks) + "."
    elif b in uses: info = "We compare it for " + ", ".join(f'<a href="/c/{c["slug"]}">{c["name"]}</a>' for c in uses[b][:4]) + "."
    else: info = f'<a href="/request?b={q(b)}">Request a product</a>'
    cards += f'<div class="b{" top" if top else ""}" id="{slug(b)}"><h3>{b}</h3><p>{info}</p></div>'
body = f'''<section class="page-hero"><div class="wrap">
    <nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a> / Brands</nav>
    <div class="eyebrow">Brands</div>
    <h1 class="display"><span class="bold">{len(ALL_BRANDS)} brands.</span> <span class="thin">One pick per supplement.</span></h1>
    <p class="lead">We compare these brands on form, dose, testing and price, and put the one we rate best in your stack. Want a specific product from any of them? <a href="/request">Request it</a>.</p>
  </div></section>
  <section style="padding-top:0"><div class="wrap"><div class="brands-az">{cards}</div>
  <p class="small-print">Daily Stack is an independent retailer. Brand names are trademarks of their owners; we are not affiliated with or endorsed by these brands.</p></div></section>'''
write("brands.html", page("Brands", "The supplement brands Daily Stack compares, and our pick for each supplement.", body))


# ---------------- stack (plan) pages ----------------
def why(item):
    label, brand, prod, cs, im = item
    if cs is None: return "Something new to try every month, picked by us from the brands we trust."
    c = BY[cs]
    if c["claims"]: return c["claims"][0]
    return "Paired with vitamin C in this box, which contributes to normal collagen formation for the normal function of skin."
for st in STACK_LIST:
    sid = st["id"]
    cards = ""
    for i, it in enumerate(st["items"], 1):
        label, brand, prod, cs, im = it
        pic = (f'<img src="/assets/products/{im}.webp" alt="{brand} {prod}" width="640" height="640" loading="lazy">' if im
               else '<div class="pmystery" aria-hidden="true">?</div>')
        more = f'<a class="more" href="/c/{cs}">More about {html.unescape(label).lower() if not label.startswith(("Vitamin","Omega","B-")) else label} →</a>' if cs else ""
        cards += f'''<article class="pcard"><div class="pphoto">{pic}<span class="pnum">{i}</span></div>
        <div class="pbody"><div class="eyebrow">{label}</div><h3>{brand}</h3><p class="pprod">{prod}</p><p class="pwhy">{why(it)}</p>{more}</div></article>'''
    extras = "".join(f"<li>{e}</li>" for e in st["extras"])
    others = "".join(f'<a class="bchip" href="/stack/{o["id"]}">{o["name"]} Stack · {o["price"]}</a>' for o in STACK_LIST if o is not st)
    buy = f'''<div class="buy"><div class="price"><span class="amount">{st["price"]}</span><span class="per">{st["per"]}</span></div>
      <a class="btn green big" href="{STRIPE[sid]}" data-box="{sid}">{st["cta"]}</a>
      <p class="small-print" style="margin:6px 0 0">{st.get("note") or "Monthly · pause or cancel anytime · original, sealed products"}</p></div>'''
    body = f'''<section class="page-hero"><div class="wrap">
    <nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a> / <a href="/#boxes">Stacks</a> / {st["name"]} Stack</nav>
    <div class="stack-hero"><div>
      {f'<span class="badge static">{st["badge"]}</span>' if st["badge"] else ""}
      <h1 class="display"><span class="bold">{st["name"]}</span> <span class="thin">Stack</span></h1>
      <p class="lead">{st["tagline"]}</p></div>
      {buy}
    </div>
  </div></section>
  <section style="padding-top:0"><div class="wrap">
    <h2 class="display" style="font-size:clamp(28px,4vw,40px);margin:0 0 20px"><span class="bold">What's in your box</span></h2>
    <div class="pgrid">{cards}</div>
    <div class="card" style="margin-top:22px"><h2>Also in the box</h2><ul class="claims">{extras}</ul></div>
    <div class="stack-bottom">{buy}</div>
    <p class="small-print">{SAFETY}</p>
    <div class="related"><h2 class="display" style="font-size:28px;margin:30px 0 14px"><span class="bold">Other stacks</span></h2><div class="bchips">{others}</div></div>
  </div></section>'''
    write(f"stack/{sid}.html", page(f'{st["name"]} Stack', st["tagline"], body))

# ---------------- request page ----------------
opts = "".join(f'<option value="{html.unescape(c["name"])}">' for c in CATEGORIES)
body = f'''<section class="page-hero"><div class="wrap">
    <nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a> / Request a product</nav>
    <div class="eyebrow">Request a product</div>
    <h1 class="display"><span class="bold">Want something extra?</span> <span class="thin">We'll add it.</span></h1>
    <p class="lead">Tell us what you'd like and we'll source it from the brand we rate best, add it to your next box, and send you the price first. No extra shipping.</p>
  </div></section>
  <section style="padding-top:0"><div class="wrap"><div class="card">
    <form class="form" id="req">
      <label>Product<input name="product" list="cats" required placeholder="e.g. Ashwagandha"></label>
      <datalist id="cats">{opts}</datalist>
      <label>Preferred brand (optional)<input name="brand" list="brands" placeholder="Leave empty and we'll pick"></label>
      <datalist id="brands">{"".join(f'<option value="{html.unescape(b)}">' for b in ALL_BRANDS)}</datalist>
      <label>Add it to
        <select name="stack"><option>My current stack</option><option>Foundation Stack</option><option>Her Stack</option><option>Energy Stack</option><option>Winter Stack</option><option>Just this product</option></select></label>
      <label>Your email<input name="email" type="email" required placeholder="you@example.com"></label>
      <label>Anything else? (optional)<textarea name="notes" placeholder="Size, flavour, dose…"></textarea></label>
      <button class="btn green" type="submit">Send request</button>
      <p class="small-print" id="req-note">We reply within one working day.</p>
    </form>
  </div></div></section>'''
REQ_JS = '''// Request form: prefill from ?p= / ?b=, then send by WhatsApp or email (set below)
const REQUEST = { whatsapp: "", email: "", instagram: "https://instagram.com/dailystack" };
(() => {
  const f=document.getElementById('req'); if(!f) return;
  const u=new URLSearchParams(location.search);
  if(u.get('p')) f.product.value=u.get('p'); if(u.get('b')) f.brand.value=u.get('b');
  f.addEventListener('submit',e=>{
    e.preventDefault();
    const t=`Daily Stack product request\\nProduct: ${f.product.value}\\nBrand: ${f.brand.value||'your pick'}\\nAdd to: ${f.stack.value}\\nEmail: ${f.email.value}\\nNotes: ${f.notes.value||'-'}`;
    if(REQUEST.whatsapp){location.href='https://wa.me/'+REQUEST.whatsapp.replace(/\\D/g,'')+'?text='+encodeURIComponent(t);return;}
    if(REQUEST.email){location.href='mailto:'+REQUEST.email+'?subject='+encodeURIComponent('Product request: '+f.product.value)+'&body='+encodeURIComponent(t);return;}
    navigator.clipboard&&navigator.clipboard.writeText(t).catch(()=>{});
    document.getElementById('req-note').innerHTML='Copied! Paste it in a DM to <a href="'+REQUEST.instagram+'" target="_blank" rel="noopener">@dailystack on Instagram</a>.';
    window.open(REQUEST.instagram,'_blank','noopener');
  });
})();'''
write("request.html", page("Request a product", "Ask Daily Stack to add any supplement to your monthly box.", body, REQ_JS))
print("built", len(CATEGORIES), "category pages,", len(ALL_BRANDS), "brands")
