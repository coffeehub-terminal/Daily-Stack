#!/usr/bin/env python3
"""Builds the menu in index.html plus /c/<slug>.html, /brands.html and /request.html.
Run from anywhere: python3 _build/build.py"""
import os, re, sys, html, urllib.parse
sys.path.insert(0, os.path.dirname(__file__))
from catalog import GRADE_B, GRADE_A_NOTE, grade, NOT_IN_OUR_BOX, ADDON, ADDON_EXTRA, ADDON_PRICE, SUGGEST, CATEGORIES, STACKS, TOP_BRANDS, ALL_BRANDS, STACK_LIST, STRIPE, BRAND_LOGO, SPORT_BRANDS

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


def visual(brand, product, photo, cls="pv"):
    """Product photo if we have one, else a clean brand tile marked as a 30-day pack."""
    if photo:
        return f'<img src="/assets/products/{photo}.webp" alt="{brand} {product}" width="640" height="640" loading="lazy">'
    if brand == "Daily Stack":
        return f'<div class="{cls} mystery" aria-hidden="true"><b>?</b><span>New every month</span></div>'
    logo = BRAND_LOGO.get(brand)
    inner = f'<img src="/assets/brands/{logo}.png" alt="{brand}">' if logo else f'<b>{brand}</b>'
    return f'<div class="{cls}">{inner}<em>{product}</em><span>30-day pack</span></div>'

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
         + foot("We only list what's backed by approved EU claims or solid human trials. <b>Green</b> = already in one of our stacks.")),
 "sport": ("Sport", '<div class="mgrid g4">'
         + mcol("Type", [li_cat(s) for s in ["creatine","electrolytes","protein","protein-bars","energy-gels","post-workout"] if s in BY])
         + mcol("Activity", [li_cat("electrolytes","Endurance"), li_cat("creatine","Strength &amp; muscle")])
         + mcol("Brands", [li_brand(b) for b in SPORT_BRANDS])
         + '</div>' + foot("Training? The <b>Energy Stack</b> already includes creatine and magnesium.")),
 "brands": ("Brands", '<div class="mgrid gb">' + mcol("Popular brands", [li_brand(b) for b in TOP_BRANDS])
         + mcol(f"All brands ({len(ALL_BRANDS)})", [li_brand(b) for b in ALL_BRANDS], "cols4") + '</div>'
         + foot("Want a product from any of these brands? Request it and we'll add it to your next box.", "/brands", "All brands")),
}
chev = '<svg width="12" height="12" viewBox="0 0 24 24" aria-hidden="true"><path d="M6 9l6 6 6-6" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"/></svg>'
items = "".join(f'<li class="mitem"><button type="button" class="mbtn" aria-expanded="false" aria-controls="mp-{k}">{t}{chev}</button>'
                f'<div class="mpanel" id="mp-{k}" hidden><div class="wrap">{c}</div></div></li>' for k, (t, c) in panels.items())
MENU = (f'<!--MENU--><div class="menubar"><div class="wrap"><ul class="mlist">{items}</ul>'
        '<ul class="mlinks"><li><a href="/#boxes">Our stacks</a></li><li><a href="/add-ons">Add-ons</a></li><li><a href="/evidence">Our standard</a></li><li><a href="/#faq">FAQ</a></li></ul></div></div><!--/MENU-->')

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
      <p>Our stacks cover the essentials. Want something else? Pick any product below and we'll add it to your box, from a brand we trust. <b class="g">Green</b> = already in a stack.</p>
    </div>
    <div class="browse">{browse_cols}</div>
    <div class="browse-cta"><a class="btn green" href="/request">Request a product</a><a class="btn ghost" href="/brands">See all {len(ALL_BRANDS)} brands</a></div>
  </div>
</section><!--/BROWSE-->
'''
if "<!--BROWSE-->" in idx:
    idx = re.sub(r"<!--BROWSE-->.*?<!--/BROWSE-->\n", "", idx, flags=re.S)
# (the browse grid is no longer shown on the homepage)

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
.pack{display:block;font-size:12.5px;opacity:.65;font-weight:600}
.month-tag{margin:-6px 0 0;font-size:14px;font-weight:800;color:var(--green-dark);display:flex;align-items:center;gap:6px}
.month-note{display:flex;gap:16px;align-items:center;background:#fff;border-radius:18px;padding:16px 20px;margin:0 0 22px;font-size:16px;line-height:1.45;border-left:5px solid var(--green)}
.mn-icon{flex:0 0 52px;height:52px;border-radius:14px;background:var(--green-dark);color:#fff;font:800 22px 'Inter',sans-serif;display:flex;align-items:center;justify-content:center;letter-spacing:-0.03em}
.pv{aspect-ratio:1;width:100%;background:linear-gradient(160deg,#fff,#f1f4f2);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:10px;padding:14%;box-sizing:border-box;text-align:center;border-radius:inherit}
.pv img{max-width:80%;max-height:34%;object-fit:contain;border:0!important;background:none!important;width:auto!important;height:auto!important;aspect-ratio:auto!important}
.pv b{font:800 20px 'Inter',sans-serif;letter-spacing:-0.03em}
.pv em{font-style:normal;font-weight:700;font-size:15px;line-height:1.2}
.pv span{font-size:11px;font-weight:800;letter-spacing:.1em;text-transform:uppercase;color:#fff;background:var(--green-dark);padding:4px 9px;border-radius:999px}
.pv.mystery b{font-size:72px;color:var(--green)}.pv.mystery span{background:var(--ink)}
.pv.small{padding:10%;gap:4px;border:1px solid rgba(4,38,33,.1);border-radius:12px}.pv.small em{display:none}.pv.small span{font-size:7px;padding:2px 5px;letter-spacing:.05em}.pv.small b{font-size:12px}.pv.small.mystery b{font-size:30px}
.pv.tiny{width:96px;border-radius:16px;padding:10px;gap:5px}.pv.tiny em{display:none}.pv.tiny span{font-size:8px;padding:2px 6px}.pv.tiny b{font-size:13px}
.pick-vis{max-width:260px;margin:0 0 16px;border-radius:18px;overflow:hidden;border:1px solid rgba(4,38,33,.08)}.pick-vis>img{display:block;width:100%!important;height:auto!important;aspect-ratio:1;object-fit:contain;background:#fff}
.ppack{margin:2px 0 0;font-size:13px;font-weight:800;color:var(--green-dark)}
.product .pk{margin:4px 0 0;font-size:13px;font-weight:800;color:var(--green-dark)}
.hero-photo{margin:0 0 22px;border-radius:var(--radius);overflow:hidden;aspect-ratio:21/9;background:#e9d6cc}.hero-photo img{width:100%;height:100%;object-fit:cover;object-position:center 40%;display:block}
@media (max-width:620px){.hero-photo{aspect-ratio:4/5}}

/* USP bar + footer */
.usp{background:var(--ink);color:#fff;font-size:14px;font-weight:600}
.usp ul{list-style:none;margin:0 auto;padding:10px 24px;max-width:1240px;display:flex;justify-content:space-between;gap:24px}
.usp li{display:flex;align-items:center;gap:9px;white-space:nowrap}
.usp svg{flex:0 0 auto;opacity:.95}
@media (max-width:980px){.usp ul{justify-content:center}.usp li:nth-child(n+3){display:none}}
@media (max-width:560px){.usp li:nth-child(n+2){display:none}}
footer.big .wrap{display:block}
footer.big{background:var(--ink);color:#fff;padding:64px 0 34px;font-size:15px;margin-top:0}
footer.big a{color:#fff;text-decoration:none;opacity:.85}
footer.big a:hover{opacity:1;text-decoration:underline}
footer.big .fgrid{display:grid;grid-template-columns:1.2fr 1fr 1fr 1.6fr;gap:34px;align-items:start}
footer.big h4{margin:0 0 14px;font:800 16px 'Inter',sans-serif;letter-spacing:-0.01em}
footer.big ul{list-style:none;margin:0;padding:0;display:grid;gap:9px}
footer.big .logo{color:#fff}
footer.big .flead{opacity:.8;margin:14px 0 0;max-width:260px;line-height:1.5}
.pays{display:flex;flex-wrap:wrap;gap:8px}
.pay{width:62px;height:40px;border-radius:7px;background:#fff;color:#111;display:flex;align-items:center;justify-content:center;font:800 12px 'Inter',sans-serif;letter-spacing:-0.02em}
.pay.ideal{color:#CC0066;font-size:13px}.pay.visa{color:#1A1F71;font-style:italic;font-size:16px}
.pay.amex{background:#2E77BC;color:#fff;font-size:11px}.pay.bc{color:#005498;font-size:9.5px}
.pay.mc span{width:18px;height:18px;border-radius:50%;display:block}.pay.mc span:first-child{background:#EB001B}.pay.mc span:last-child{background:#F79E1B;margin-left:-7px;mix-blend-mode:multiply}
.pay.apple,.pay.gpay{font-size:11px}
.fslogan{margin:56px 0 0;font:300 clamp(48px,8vw,112px)/0.98 'Inter',sans-serif;letter-spacing:-0.055em}
.fslogan b{font-weight:800}
.fbottom{margin-top:44px;padding-top:20px;border-top:1px solid rgba(255,255,255,.15);display:flex;flex-wrap:wrap;justify-content:space-between;gap:16px;font-size:14px;opacity:.85}
.fbottom nav{display:flex;flex-wrap:wrap;gap:20px}
@media (max-width:980px){footer.big .fgrid{grid-template-columns:1fr 1fr}}
@media (max-width:560px){footer.big .fgrid{grid-template-columns:1fr}}
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
# Boxes: rebuilt from the catalog (30-day packs)
idx = re.sub(r'\n\s*<(?:div|a) class="pshelf".*?</(?:div|a)>', '', idx, flags=re.S)
idx = re.sub(r'<a class="btn ghost" href="/stack/[a-z]+">See every product</a>\n\s*', '', idx)
CHECK = '<svg width="18" height="18" viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12.5l4.5 4.5L19 7.5" fill="none" stroke="#1F7A50" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></svg>'
for st in STACK_LIST:
    sid = st["id"]
    m = re.search(r'id="%s">.*?</article>' % sid, idx, re.S)
    art = m.group(0); a2 = art
    a2 = re.sub(r'<p class="for">.*?</p>', f'<p class="for">{st["tagline"]}</p>', a2, count=1, flags=re.S)
    seen = []
    for it in st["items"]:
        if it[1] != "Daily Stack" and it[1] not in seen: seen.append(it[1])
    row = '<div class="brand-row" aria-label="Brands in this box">' + "".join(
        f'<span class="brand-chip" data-logo="assets/brands/{BRAND_LOGO.get(b) or slug(b)}.png">{b}</span>' for b in seen) + '</div>'
    a2 = re.sub(r'<div class="brand-row"[^>]*>.*?</div>', row, a2, count=1, flags=re.S)
    lis = "".join((f'<li><b>{lab}</b> · {br} {pr}<span class="pack">{pk}</span></li>' if br != "Daily Stack"
                   else '<li><b>Monthly discovery</b> · a new product to try every month</li>') for lab, br, pr, pk, cs, im in st["items"])
    tiles = "".join(f'<li>{visual(br, pr, im, "pv small")}<span>{lab}</span></li>' for lab, br, pr, pk, cs, im in st["items"])
    peek = (f'\n        <details class="peek"><summary>View products</summary><ul class="peek-grid">{tiles}</ul>'
            f'<a class="peek-more" href="/stack/{sid}">Full details per product →</a></details>')
    a2 = re.sub(r'\n\s*<details class="peek">.*?</details>', '', a2, flags=re.S)
    a2 = re.sub(r'<ul class="inside">.*?</ul>', lambda mm: f'<ul class="inside">{lis}</ul>' + peek, a2, count=1, flags=re.S)
    ex = ", ".join(e[0].lower() + e[1:] if not e.startswith("Dutch") else e for e in st["extras"])
    ex = ex.replace("your daily", "your daily")
    a2 = re.sub(r'<div class="extras">.*?</div>', f'<div class="extras">+ {ex}</div>', a2, count=1, flags=re.S)
    a2 = re.sub(r'\n\s*<p class="month-tag">.*?</p>', '', a2, flags=re.S)
    a2 = re.sub(r'<span class="amount">[^<]*</span>', f'<span class="amount">{st["price"]}</span>', a2, count=1)
    a2 = re.sub(r'(<div class="price">.*?</div>)', lambda mm: mm.group(1) + f'\n        <p class="month-tag">{CHECK}Every product is a 30-day pack</p>', a2, count=1, flags=re.S)
    idx = idx.replace(art, a2)

# Brand carousel: local brands. Drop a logo at assets/brands/<slug>.png and it shows automatically.
_logo = lambda br: BRAND_LOGO.get(br) or slug(br)
_items = "".join(f'<li class="logo-item"><span data-logo="assets/brands/{_logo(br)}.png">{br}</span></li>' for br in TOP_BRANDS + [x for x in ALL_BRANDS if x not in TOP_BRANDS])
_dupe = _items.replace('<li class="logo-item">', '<li class="logo-item" aria-hidden="true">')
idx = re.sub(r'<ul class="marquee-track">.*?</ul>', lambda mm: f'<ul class="marquee-track">{_items}{_dupe}</ul>', idx, count=1, flags=re.S)

# Honest line above the boxes
NOTE = ('<!--MONTH--><div class="month-note"><div class="mn-icon" aria-hidden="true">30</div><div><b>One box, one month.</b> '
        'Every product is a 30-day pack, so nothing runs out early and nothing piles up in the cupboard.</div></div><!--/MONTH-->\n    ')
idx = re.sub(r'<!--MONTH-->.*?<!--/MONTH-->\n\s*', '', idx, flags=re.S)
idx = idx.replace('<div class="boxes">', NOTE + '<div class="boxes">', 1)
# Products section, rebuilt
from catalog import OMEGA, MAG, VITC, MULTI, FLORA, CREA
FEAT = [(OMEGA, "Fish oil rich in DHA from a Dutch practitioner brand, one softgel a day. DHA contributes to the maintenance of normal brain function (250 mg DHA per day)."),
        (MAG, "Four forms of magnesium in one tablet a day. Magnesium contributes to the reduction of tiredness and fatigue."),
        (VITC, "1000 mg of vitamin C in one tablet a day. Vitamin C contributes to the normal function of the immune system."),
        (MULTI, "A Dutch multivitamin with 21 vitamins and minerals in well-absorbed forms. Just one tablet a day."),
        (FLORA, "A Dutch daily bacterial blend with nine strains. One capsule a day, from one of the best-known Dutch brands."),
        (CREA, "Creapure® creatine made in Germany, in easy capsules. Creatine increases physical performance in successive bursts of short-term, high-intensity exercise (3 g daily).")]
cards = ""
for (lab, br, pr, pk, cs, im), desc in FEAT:
    ins = [s2["name"] for s2 in STACK_LIST if any(x[1] == br and x[2] == pr for x in s2["items"])]
    cards += (f'\n      <article class="product">\n        <div class="pimg">{visual(br, pr, im, "pv tiny")}</div>\n        <div>\n          <div class="brand">{br}</div>\n'
              f'          <h3>{pr}</h3>\n          <p class="pk">30-day pack · {pk}</p>\n          <p>{desc}</p>\n          <div class="in">' + "".join(f'<span class="chip">{n}</span>' for n in ins) + '</div>\n        </div>\n      </article>')
idx = re.sub(r'(id="products".*?<div class="products">).*?(\n    </div>\n  </div>\n</section>)', lambda mm: mm.group(1) + cards + mm.group(2), idx, count=1, flags=re.S)
idx = idx.replace("No white-label mystery pills. Every product is an original, sealed product from a brand we chose for its form, dose and reputation. Here's why.",
                  "No white-label mystery pills. Every product is an original, sealed 30-day pack from a brand we chose for its form, dose and reputation. Here's why.")


# ---------------- USP bar + footer (shared) ----------------
_ic = lambda d: f'<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{d}</svg>'
USP = ('<!--USP--><div class="usp"><ul>'
  f'<li>{_ic("<path d=\'M3 7h11v9H3z\'/><path d=\'M14 10h4l3 3v3h-7\'/><circle cx=\'7\' cy=\'17.5\' r=\'1.7\'/><circle cx=\'17\' cy=\'17.5\' r=\'1.7\'/>")}Free shipping across the EU</li>'
  f'<li>{_ic("<rect x=\'3\' y=\'5\' width=\'18\' height=\'16\' rx=\'2\'/><path d=\'M3 10h18M8 3v4M16 3v4\'/>")}Every product a 30-day pack</li>'
  f'<li>{_ic("<rect x=\'2.5\' y=\'5\' width=\'19\' height=\'14\' rx=\'2\'/><path d=\'M2.5 10h19M6 15h4\'/>")}Pay with iDEAL</li>'
  f'<li>{_ic("<path d=\'M3 12a9 9 0 1 0 3-6.7L3 8\'/><path d=\'M3 3v5h5\'/>")}Pause or cancel anytime</li>'
  '</ul></div><!--/USP-->\n')
idx = re.sub(r'<!--USP-->.*?<!--/USP-->\n?', '', idx, flags=re.S)
idx = idx.replace('<header class="top">', USP + '<header class="top">', 1)
PAYS = ('<div class="pays" aria-label="Payment methods">'
  '<span class="pay ideal">iDEAL</span><span class="pay bc">Bancontact</span><span class="pay visa">VISA</span>'
  '<span class="pay mc" aria-label="Mastercard"><span></span><span></span></span><span class="pay amex">AMEX</span>'
  '<span class="pay apple">Apple Pay</span><span class="pay gpay">G Pay</span></div>')
NEWFOOT = f'''<footer class="big">
  <div class="wrap">
    <div class="fgrid">
      <div><a class="logo" href="/" aria-label="Daily Stack home" style="font-size:26px"><b>Daily</b><span>stack</span></a>
        <p class="flead">Your vitamins in perfect 30-day packs, from trusted Dutch and European brands. Shipping to all 27 EU countries.</p></div>
      <div><h4>Shop</h4><ul><li><a href="/#boxes">Our stacks</a></li><li><a href="/add-ons">Add-ons</a></li><li><a href="/evidence">Our standard</a></li><li><a href="/brands">Brands</a></li></ul></div>
      <div><h4>Help</h4><ul><li><a href="/#faq">FAQ</a></li><li><a href="https://www.instagram.com/dailystack_vitamins/" rel="noopener">Instagram</a></li><li><a href="/request">Contact</a></li></ul></div>
      <div><h4>Payment methods</h4>{PAYS}</div>
    </div>
    <p class="fslogan"><b>Never run out.</b><br>Never pile up.</p>
    <div class="fbottom"><span>© 2026 Daily Stack. All rights reserved.</span>
      <nav aria-label="Legal"><a href="/terms">Terms &amp; conditions</a><a href="/privacy">Privacy policy</a><a href="/impressum">Legal notice / Impressum</a></nav></div>
  </div>
</footer>'''
idx = re.sub(r'<footer[^>]*>.*?</footer>', lambda mm: NEWFOOT, idx, count=1, flags=re.S)

CART_TAGS = '<!--CART--><link rel="stylesheet" href="/assets/cart.css"><script src="/assets/cart-data.js" defer></script><script src="/assets/cart.js" defer></script><!--/CART-->'
idx = re.sub(r"<!--CART-->.*?<!--/CART-->", "", idx, flags=re.S).replace("</head>", CART_TAGS + "\n</head>", 1)
idx = re.sub(r"\n// Every Subscribe button goes straight to Stripe checkout\n.*?\n\}\);\n", "\n", idx, count=1, flags=re.S)
write("index.html", idx)
# ---------------- shared template ----------------
STYLE = re.search(r"<style>(.*?)</style>", idx, re.S).group(1)
HEADER = re.search(r'<header class="top">.*?</header>', idx, re.S).group(0)
FOOTER = re.search(r"<footer[^>]*>.*?</footer>", idx, re.S).group(0).replace('href="#"', 'href="/"')
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
{CART_TAGS}
</head>
<body>
{USP}{HEADER}
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

PICK_VIS = {}
for _st in STACK_LIST:
    for _lab, _br, _pr, _pk, _cs, _im in _st["items"]:
        if _cs and _cs not in PICK_VIS: PICK_VIS[_cs] = (_br, _pr, _im)
PICK_VIS["vitamin-d3"] = PICK_VIS.get("multivitamin")
SAFETY = "Food supplements are not a substitute for a varied, balanced diet and a healthy lifestyle. Do not exceed the recommended daily dose. Pregnant, breastfeeding or taking medication? Check with your doctor or pharmacist first."

def brand_links(bs): return "".join(f'<a href="/brands#{slug(b)}">{b}</a>' for b in bs)

for c in CATEGORIES:
    name = c["name"]; plain = html.unescape(name)
    claims = ("<ul class=\"claims\">" + "".join(f"<li>{x}</li>" for x in c["claims"]) + "</ul><p class=\"small-print\">Approved EU health claims.</p>") if c["claims"] else \
             "<p>No approved EU health claims, so we don't make any.</p>"
    if c["pick"]:
        b, prod, stacks = c["pick"]
        side = f'''<div class="card pick">
        {f'<div class="pick-vis">{visual(*PICK_VIS[c["slug"]], cls="pv")}</div>' if c["slug"] in PICK_VIS else ""}
        <div class="eyebrow">Our pick</div>
        <div class="who">{b}</div><p style="margin:0">{prod}</p>
        <div class="stack-chips">{"".join(f'<a href="/stack/{s}">In {STACKS[s]} Stack</a>' for s in stacks)}</div>
        <div class="actions"><a class="btn green" href="/#boxes">See the stacks</a><a class="btn ghost" href="/request?p={q(plain)}">Add it on its own</a></div>
      </div>'''
    elif c["slug"] in ADDON:
        ab, ap, aimg = ADDON[c["slug"]]
        side = f'''<div class="card pick">
        <div class="pick-vis">{visual(ab, ap, aimg, cls="pv")}</div>
        <div class="eyebrow">Add-on</div>
        <div class="who">{ab}</div><p style="margin:0">{ap}</p>
        <p class="small-print" style="margin-top:10px">Add it to any stack. It ships in the same box every month, no extra shipping.</p>
        <div class="actions"><button type="button" class="btn green" data-addon="{c["slug"]}">Add to my box · €{ADDON_PRICE[c["slug"]]/100:.2f}/month</button><a class="btn ghost" href="/add-ons">See all add-ons</a></div>
      </div>'''
    else:
        side = f'''<div class="card">
        <div class="eyebrow">Not in a stack yet</div>
        <h2 style="margin-top:6px">Add it to your box</h2>
        <p style="margin:0">Tell us you want it and we'll add it to your next box, from a brand we trust. No extra shipping.</p>
        <div style="margin-top:20px;display:flex;flex-direction:column;gap:10px"><a class="btn green" href="/request?p={q(plain)}">Request {plain}</a><a class="btn ghost" href="/#boxes">See the stacks</a></div>
      </div>'''
    note = f'<div class="info-note">{c["note"]}</div>' if c["note"] else ""
    related = "".join(f'<a class="bchip{" in" if r["slug"] in IN_STACK else ""}" href="/c/{r["slug"]}">{r["name"]}</a>' for r in CATEGORIES if r["group"] == c["group"] and r is not c)
    body = f'''<section class="page-hero"><div class="wrap">
    <nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a> / <a href="/#browse">{c["group"]}</a> / {name}</nav>
    <div class="eyebrow">{c["group"]}</div>
    <h1 class="display bold">{name}</h1>
    <p class="grade-line"><span class="grade g{grade(c["slug"])}">Grade {grade(c["slug"])}</span> <a href="/evidence">How we grade</a></p>
    <p class="lead">{c["intro"]}</p>
  </div></section>
  <section style="padding-top:0"><div class="wrap">
    <div class="page-grid">
      <div class="card">
        <div class="grade-box g{grade(c["slug"])}"><b>Grade {grade(c["slug"])}.</b> {GRADE_B.get(c["slug"], GRADE_A_NOTE)}</div>
        <h2>What it does</h2>
        {claims}
        {note}
        <h2 style="margin-top:28px">Other brands you can request</h2>
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
    picks = [c for c in CATEGORIES if c["pick"] and c["pick"][0] == b]
    if picks: info = "In our stacks for " + ", ".join(f'<a href="/c/{c["slug"]}">{c["name"]}</a>' for c in picks) + "."
    elif b in uses: info = "Available on request for " + ", ".join(f'<a href="/c/{c["slug"]}">{c["name"]}</a>' for c in uses[b][:4]) + "."
    else: info = f'<a href="/request?b={q(b)}">Request a product</a>'
    cards += f'<div class="b{" top" if picks else ""}" id="{slug(b)}"><h3>{b}</h3><p>{info}</p></div>'
body = f'''<section class="page-hero"><div class="wrap">
    <nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a> / Brands</nav>
    <div class="eyebrow">Brands</div>
    <h1 class="display"><span class="bold">{len(ALL_BRANDS)} brands.</span> <span class="thin">Any of them in your box.</span></h1>
    <p class="lead">Mostly Dutch brands, all sold in Dutch drugstores and pharmacies, and the same brands people already trust here. Our stacks use Vitakruid, Bonusan, Orthica, Solgar and Mattisson Healthstyle. We only list products backed by an approved EU health claim or solid human trials. Want one of them in your box? <a href="/request">Request it</a> and we'll add it to your next box.</p>
  </div></section>
  <section style="padding-top:0"><div class="wrap"><div class="brands-az">{cards}</div>
  <p class="small-print">Daily Stack is an independent retailer. Brand names are trademarks of their owners; we are not affiliated with or endorsed by these brands.</p></div></section>'''
write("brands.html", page("Brands", "The supplement brands you can get in your Daily Stack box.", body))


# ---------------- stack (plan) pages ----------------
def why(item):
    label, brand, prod, pk, cs, im = item
    if cs is None: return "Something new to try every month, picked by us from the brands we trust."
    c = BY[cs]
    if c["claims"]: return c["claims"][0]
    return c["intro"]
for st in STACK_LIST:
    sid = st["id"]
    cards = ""
    for i, it in enumerate(st["items"], 1):
        label, brand, prod, pk, cs, im = it
        pic = visual(brand, prod, im, "pv big")
        more = f'<a class="more" href="/c/{cs}">More about {html.unescape(label).lower() if not label.startswith(("Vitamin","Omega","B-")) else label} →</a>' if cs else ""
        cards += f'''<article class="pcard"><div class="pphoto">{pic}<span class="pnum">{i}</span></div>
        <div class="pbody"><div class="eyebrow">{label}</div><h3>{brand}</h3><p class="pprod">{prod}</p><p class="ppack">{"30-day pack · " + pk if brand != "Daily Stack" else pk}</p><p class="pwhy">{why(it)}</p>{more}</div></article>'''
    extras = "".join(f"<li>{e}</li>" for e in st["extras"])
    others = "".join(f'<a class="bchip" href="/stack/{o["id"]}">{o["name"]} Stack · {o["price"]}</a>' for o in STACK_LIST if o is not st)
    buy = f'''<div class="buy"><div class="price"><span class="amount">{st["price"]}</span><span class="per">{st["per"]}</span></div>
      <a class="btn green big" href="{STRIPE[sid]}" data-box="{sid}">{st["cta"]}</a>
      <p class="small-print" style="margin:6px 0 0">{st.get("note") or "Monthly · pay with iDEAL · pause or cancel anytime"}</p></div>'''
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
    <div class="month-note" style="margin-bottom:20px"><div class="mn-icon" aria-hidden="true">30</div><div><b>One box, one month.</b> Every product in this box is a 30-day pack, so it runs out right when the next box lands on your doormat.</div></div>
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
    <p class="lead">Tell us what you'd like and we'll source it from a brand we trust, add it to your next box, and send you the price first. No extra shipping.</p>
  </div></section>
  <section style="padding-top:0"><div class="wrap"><div class="card">
    <form class="form" id="req">
      <label>Product<input name="product" list="cats" required placeholder="e.g. Vitamin D3"></label>
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
const REQUEST = { whatsapp: "", email: "", instagram: "https://ig.me/m/dailystack_vitamins" };
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
    document.getElementById('req-note').innerHTML='Copied! Paste it in a DM to <a href="'+REQUEST.instagram+'" target="_blank" rel="noopener">@dailystack_vitamins on Instagram</a>.';
    window.open(REQUEST.instagram,'_blank','noopener');
  });
})();'''
write("request.html", page("Request a product", "Ask Daily Stack to add any supplement to your monthly box.", body, REQ_JS))
# ---------------- box drawer data (browser + checkout function) ----------------
import json
NAMES = {c["slug"]: html.unescape(c["name"]) for c in CATEGORIES}
ADDONS = {}
for k, (br, pr, img) in ADDON.items():
    if k in NAMES: ADDONS[k] = dict(name=NAMES[k], brand=html.unescape(br), product=html.unescape(pr), photo=img, price=ADDON_PRICE[k], url=f"/c/{k}", grade=grade(k))
for k, (br, pr, img, nm) in ADDON_EXTRA.items():
    ADDONS[k] = dict(name=nm, brand=br, product=pr, photo=img, price=ADDON_PRICE[k], url=None, grade="A")
CART_STACKS = {}
for st in STACK_LIST:
    CART_STACKS[st["id"]] = dict(name=f'{st["name"]} Stack', price=int(st["price"].replace("€", "")) * 100,
        recurring=st["id"] != "winter", count=len(st["items"]), link=STRIPE[st["id"]],
        photos=[i[5] for i in st["items"] if i[5]][:4], suggest=[s for s in SUGGEST[st["id"]] if s in ADDONS])
CART = dict(stacks=CART_STACKS, addons=ADDONS)
write("assets/cart-data.js", "window.DS_CART = " + json.dumps(CART, ensure_ascii=False) + ";\n")
os.makedirs(os.path.join(ROOT, "api"), exist_ok=True)
write("api/_catalog.json", json.dumps(CART, ensure_ascii=False, indent=1))

cards = ""
for k, a in ADDONS.items():
    link = f'<a href="{a["url"]}">{a["name"]}</a>' if a["url"] else a["name"]
    cards += f'''<article class="acard"><div class="aphoto"><img src="/assets/products/{a["photo"]}.webp" alt="{a["brand"]} {a["product"]}" loading="lazy"></div>
      <div class="abody"><div class="eyebrow">{link} <span class="grade g{a["grade"]}">Grade {a["grade"]}</span></div><h3>{a["brand"]}</h3><p>{a["product"]}</p>{f'<p class="bnote">{GRADE_B[k]}</p>' if a["grade"] == "B" else ""}
      <div class="aprice">€{a["price"]/100:.2f} <span>/ month</span></div>
      <button type="button" class="btn green small" data-addon="{k}">Add to my box</button></div></article>'''
body = f'''<section class="page-hero"><div class="wrap">
    <nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a> / Add-ons</nav>
    <div class="eyebrow">Custom box</div>
    <h1 class="display"><span class="bold">Start with a stack.</span> <span class="thin">Make it yours.</span></h1>
    <p class="lead">Every box starts with one of our four stacks. Add what you need on top. It comes in the same box, no extra shipping. Every extra has a grade, so you know what the science says before you pay.</p>
    <ol class="asteps"><li><b>1</b> Pick your stack</li><li><b>2</b> Add your extras</li><li><b>3</b> One box, every month</li></ol>
  </div></section>
  <section style="padding-top:0"><div class="wrap"><div class="agrid">{cards}</div>
  <p class="small-print">We only list products with an approved EU health claim or solid human trials. Food supplements are not a substitute for a varied, balanced diet and a healthy lifestyle.</p></div></section>'''
write("add-ons.html", page("Add-ons", "Start with a stack, then add the extras you need. One box, every month.", body))

# ---------------- Our standard (evidence) page ----------------
rows = "".join(f'<tr><td><a href="/c/{c["slug"]}">{c["name"]}</a></td><td><span class="grade g{grade(c["slug"])}">{grade(c["slug"])}</span></td><td>{GRADE_B.get(c["slug"], (c["claims"][0] if c["claims"] else GRADE_A_NOTE))}</td></tr>'
               for c in sorted(CATEGORIES, key=lambda c: (grade(c["slug"]), html.unescape(c["name"]))))
NAMES_ALL = {"amino-acids": "Amino acids", "bcaa": "BCAA", "glutamine": "Glutamine", "carnitine": "Carnitine", "pre-workout": "Pre-workout",
             "green-tea": "Green tea extract", "5-htp": "5-HTP", "msm": "MSM", "milk-thistle": "Milk thistle", "enzymes": "Digestive enzymes"}
nob = "".join(f'<li><b>{NAMES_ALL.get(k, k.replace("-", " ").capitalize())}</b><span>{why}</span></li>' for k, why in NOT_IN_OUR_BOX.items())
body = f'''<section class="page-hero"><div class="wrap">
    <nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a> / Our standard</nav>
    <div class="eyebrow">Our standard</div>
    <h1 class="display"><span class="bold">Only what holds up.</span> <span class="thin">The truth about the rest.</span></h1>
    <p class="lead">The supplement aisle is full of promises. We only sell what has an approved EU health claim or solid human research behind it, and we give every product a grade so you can see that for yourself.</p>
  </div></section>
  <section style="padding-top:0"><div class="wrap">
    <div class="grades3">
      <div class="gcard gA"><span class="grade gA">A</span><h3>Proven</h3><p>An approved EU health claim and solid human research. Think vitamin D, magnesium, omega-3 and creatine for training.</p></div>
      <div class="gcard gB"><span class="grade gB">B</span><h3>Promising</h3><p>No approved claim yet, or the trials are small and early. We sell these as extras and say so plainly. When the evidence changes, we tell you.</p></div>
      <div class="gcard gX"><span class="grade gX">✕</span><h3>Not in our box</h3><p>Weak evidence, industry-funded results or safety concerns. We don't sell it, and we tell you why.</p></div>
    </div>
    <h2 class="display" style="font-size:clamp(28px,3.5vw,40px);margin:48px 0 14px"><span class="bold">Every product,</span> <span class="thin">graded.</span></h2>
    <div class="gtable-wrap"><table class="gtable"><thead><tr><th>Product</th><th>Grade</th><th>Why</th></tr></thead><tbody>{rows}</tbody></table></div>
    <h2 class="display" id="not-in-our-box" style="font-size:clamp(28px,3.5vw,40px);margin:48px 0 14px"><span class="bold">Not in our box.</span> <span class="thin">And why.</span></h2>
    <ul class="nob">{nob}</ul>
    <p class="small-print">Grades are our own reading of the EU register of health claims and published human trials. Food supplements are not a substitute for a varied, balanced diet and a healthy lifestyle. Pregnant, breastfeeding or on medication? Check with your doctor or pharmacist first.</p>
  </div></section>'''
write("evidence.html", page("Our standard", "We only sell what holds up, and grade every product A or B. Here's what's not in our box, and why.", body))

print("built", len(CATEGORIES), "category pages,", len(ALL_BRANDS), "brands")
