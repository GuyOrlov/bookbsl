from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]

GUIDE_PAGES = {
    "access-to-work-bsl-interpreter.html",
    "bsl-interpreter-cost.html",
    "bsl-interpreter-education.html",
    "bsl-interpreter-events.html",
    "bsl-interpreter-healthcare.html",
    "bsl-interpreter-legal-official.html",
    "bsl-interpreter-work-meetings.html",
    "online-bsl-interpreter.html",
    "how-to-book-bsl-interpreter.html",
    "how-far-ahead-book-bsl-interpreter.html",
    "one-or-two-bsl-interpreters.html",
}

STYLE_ID = "bookbsl-global-nav-footer-20260912"
NAV_SCRIPT = '<script src="nav-polish.js?v=20260912-4"></script>'

STYLE = f'''<style id="{STYLE_ID}">
/* One BookBSL header and footer across every page with a BookBSL header */
.top .shell{{width:min(1160px,calc(100% - 32px))!important;margin:auto!important}}
.topin{{min-height:68px!important;height:auto!important;display:flex!important;align-items:center!important;justify-content:space-between!important;gap:32px!important;padding:0!important}}
.topnav{{display:flex!important;align-items:center!important;justify-content:flex-end!important;gap:14px!important;flex-wrap:nowrap!important}}
.mobileCtaText{{display:none}}

@media(min-width:681px){{
  .topnav>.bookbslMobilePanel{{display:contents!important}}
  .topnav>a:not(.header-cta),
  .topnav>.bookbslMobilePanel>a:not(.header-cta){{
    display:inline-flex!important;
    align-items:center!important;
    justify-content:center!important;
    min-height:42px!important;
    padding:0 14px!important;
    border-radius:999px!important;
    text-decoration:none!important;
    font-weight:800!important;
    font-size:.92rem!important;
    color:var(--ink,#092A35)!important;
    white-space:nowrap!important;
    line-height:1!important;
    transition:color .16s ease,background-color .16s ease,transform .08s ease!important;
  }}
  .topnav>a:not(.header-cta):hover,
  .topnav>a:not(.header-cta):focus-visible,
  .topnav>a:not(.header-cta):active,
  .topnav>.bookbslMobilePanel>a:not(.header-cta):hover,
  .topnav>.bookbslMobilePanel>a:not(.header-cta):focus-visible,
  .topnav>.bookbslMobilePanel>a:not(.header-cta):active{{
    color:var(--blue,#2456B3)!important;
    background:#fff!important;
    text-decoration:underline!important;
    text-decoration-thickness:2px!important;
    text-underline-offset:6px!important;
  }}
  .topnav>a:not(.header-cta):active,
  .topnav>.bookbslMobilePanel>a:not(.header-cta):active{{transform:translateY(1px)!important}}
  .topnav>a[aria-current="page"],
  .topnav>.bookbslMobilePanel>a[aria-current="page"]{{
    color:var(--blue,#2456B3)!important;
    text-decoration:underline!important;
    text-decoration-thickness:2px!important;
    text-underline-offset:6px!important;
  }}
  .topnav .header-cta{{
    display:inline-flex!important;
    align-items:center!important;
    justify-content:center!important;
    box-sizing:border-box!important;
    width:auto!important;
    min-width:0!important;
    max-width:none!important;
    min-height:42px!important;
    height:42px!important;
    padding:0 20px!important;
    margin-left:10px!important;
    border:2px solid var(--ink,#092A35)!important;
    border-radius:999px!important;
    background:var(--ink,#092A35)!important;
    color:#fff!important;
    text-decoration:none!important;
    box-shadow:none!important;
    font-size:.92rem!important;
    font-weight:800!important;
    line-height:1!important;
    letter-spacing:-.01em!important;
    white-space:nowrap!important;
    flex:0 0 auto!important;
    transition:background-color .16s ease,border-color .16s ease,transform .08s ease!important;
  }}
  .topnav .header-cta:hover,
  .topnav .header-cta:focus-visible,
  .topnav .header-cta:active{{background:var(--blue,#2456B3)!important;border-color:var(--blue,#2456B3)!important;color:#fff!important;text-decoration:none!important}}
  .topnav .header-cta:active{{transform:translateY(1px)!important}}
}}

.bookbslFooter{{background:#092A35!important;color:#fff!important;padding:46px 0!important;margin:0!important;font-size:.92rem!important}}
.bookbslFooter .shell{{width:min(1160px,calc(100% - 32px))!important;margin:auto!important}}
.bookbslFooterGrid{{display:grid!important;grid-template-columns:minmax(280px,1.35fr) repeat(3,minmax(135px,.55fr))!important;gap:34px!important;align-items:start!important}}
.bookbslFooterBrand strong{{display:block!important;font-size:1.2rem!important;color:#fff!important;margin-bottom:6px!important}}
.bookbslFooterTagline{{font-weight:800!important;color:#FFD84D!important;margin:0 0 12px!important}}
.bookbslFooterBrand p{{color:#C7D6DA!important;margin:6px 0!important;max-width:560px!important}}
.bookbslFooterGroup strong{{display:block!important;color:#FFD84D!important;font-size:.78rem!important;text-transform:uppercase!important;letter-spacing:.08em!important;margin-bottom:11px!important}}
.bookbslFooterGroup a{{display:block!important;color:#fff!important;text-decoration:none!important;margin:8px 0!important;font-weight:700!important}}
.bookbslFooterGroup a:hover{{text-decoration:underline!important;text-underline-offset:3px!important}}
.bookbslFooterBottom{{border-top:1px solid rgba(255,255,255,.2)!important;margin-top:30px!important;padding-top:18px!important;color:#B8CBCD!important;font-size:.82rem!important}}

@media(max-width:900px){{
  .bookbslFooterGrid{{grid-template-columns:1fr 1fr!important;gap:28px!important}}
  .bookbslFooterBrand{{grid-column:1/-1!important}}
}}
@media(max-width:680px){{
  .top .shell{{width:min(100% - 22px,1160px)!important}}
  .desktopCtaText{{display:none!important}}
  .mobileCtaText{{display:inline!important}}
  .brandSub{{display:none!important}}
}}
@media(max-width:500px){{
  .bookbslFooterGrid{{grid-template-columns:1fr!important}}
  .bookbslFooterBrand{{grid-column:auto!important}}
}}
</style>'''

FOOTER = '''<footer class="bookbslFooter"><div class="shell">
  <div class="bookbslFooterGrid">
    <div class="bookbslFooterBrand">
      <strong>BookBSL</strong>
      <p class="bookbslFooterTagline">Clear booking. Clear communication.</p>
      <p>A free UK booking-preparation resource by cSeeker Ltd, helping organisations prepare clearer British Sign Language interpreter enquiries.</p>
      <p>CSEEKER LIMITED · Company No. 08924049 · Registered in England and Wales.</p>
    </div>
    <nav class="bookbslFooterGroup" aria-label="Explore BookBSL">
      <strong>Explore</strong>
      <a href="./">Home</a>
      <a href="./#guides">Guides</a>
      <a href="awareness.html">Access preparation</a>
      <a href="data.html">Data</a>
      <a href="law.html">Laws</a>
    </nav>
    <nav class="bookbslFooterGroup" aria-label="Booking help">
      <strong>Booking help</strong>
      <a href="./#checker">Start checklist</a>
      <a href="how-to-book-bsl-interpreter.html">How to book</a>
      <a href="bsl-interpreter-cost.html">Interpreter costs</a>
      <a href="mailto:bookings@cseeker.co.uk">Contact cSeeker</a>
    </nav>
    <nav class="bookbslFooterGroup" aria-label="Legal information">
      <strong>Legal</strong>
      <a href="privacy.html">Privacy</a>
      <a href="terms.html">Terms</a>
      <a href="cookies.html">Cookies & analytics</a>
    </nav>
  </div>
  <div class="bookbslFooterBottom">© 2026 cSeeker Ltd. BookBSL is a service by cSeeker Ltd.</div>
</div></footer>'''


def header_for(name: str) -> str:
    guide_current = ' aria-current="page"' if name in GUIDE_PAGES else ''
    prep_current = ' aria-current="page"' if name == "awareness.html" else ''
    data_current = ' aria-current="page"' if name == "data.html" else ''
    return f'''<header class="top"><div class="shell topin"><a class="brand" href="./"><span class="brandmark">BSL</span><span>Book<b>BSL</b><small class="brandSub">Clear booking. Clear communication.</small></span></a><nav class="topnav" aria-label="Main navigation"><a href="./#guides"{guide_current}>Guides</a><a href="awareness.html"{prep_current}>Access preparation</a><a href="data.html"{data_current}>Data</a><a class="header-cta navCta" href="./#checker"><span class="desktopCtaText">Start checklist</span><span class="mobileCtaText">Checklist</span></a></nav></div></header>'''


def replace_style(text: str) -> str:
    existing = re.compile(rf'<style id="{re.escape(STYLE_ID)}">.*?</style>', re.S)
    if existing.search(text):
        return existing.sub(STYLE, text, count=1)
    if "</head>" not in text:
        raise RuntimeError("Missing </head>")
    return text.replace("</head>", STYLE + "\n</head>", 1)


def ensure_nav_script(text: str) -> str:
    text = re.sub(r'\s*<script src="nav-polish\.js(?:\?[^\"]*)?"></script>', '', text)
    ga4 = re.compile(r'(<script src="ga4-consent\.js(?:\?[^\"]*)?"></script>)')
    if ga4.search(text):
        return ga4.sub(r'\1\n' + NAV_SCRIPT, text, count=1)
    if "</body>" in text:
        return text.replace("</body>", NAV_SCRIPT + "\n</body>", 1)
    raise RuntimeError("Missing </body>")


pages = []
for path in sorted(ROOT.glob("*.html")):
    text = path.read_text(encoding="utf-8")
    if '<header class="top">' in text:
        pages.append(path)

if not pages:
    raise RuntimeError("No BookBSL HTML pages with a top header were found")

for path in pages:
    name = path.name
    text = path.read_text(encoding="utf-8")

    header_pattern = re.compile(r'<header class="top">.*?</header>', re.S)
    matches = header_pattern.findall(text)
    if len(matches) != 1:
        raise RuntimeError(f"Expected exactly one top header in {name}, found {len(matches)}")
    text = header_pattern.sub(header_for(name), text, count=1)

    footer_pattern = re.compile(r'<footer(?:\s[^>]*)?>.*?</footer>', re.S)
    footers = footer_pattern.findall(text)
    if len(footers) > 1:
        raise RuntimeError(f"Expected at most one footer in {name}, found {len(footers)}")
    if len(footers) == 1:
        text = footer_pattern.sub(FOOTER, text, count=1)

    text = replace_style(text)
    text = ensure_nav_script(text)
    path.write_text(text, encoding="utf-8")

print(f"Updated shared BookBSL navigation on {len(pages)} HTML pages")
