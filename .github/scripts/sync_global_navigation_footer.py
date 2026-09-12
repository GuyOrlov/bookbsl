from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
PAGES = [
    "index.html",
    "awareness.html",
    "data.html",
    "law.html",
    "terms.html",
    "privacy.html",
    "cookies.html",
    "bsl-interpreter-cost.html",
    "bsl-interpreter-education.html",
    "bsl-interpreter-events.html",
    "bsl-interpreter-healthcare.html",
    "bsl-interpreter-work-meetings.html",
    "online-bsl-interpreter.html",
    "how-to-book-bsl-interpreter.html",
]
GUIDE_PAGES = {
    "bsl-interpreter-cost.html",
    "bsl-interpreter-education.html",
    "bsl-interpreter-events.html",
    "bsl-interpreter-healthcare.html",
    "bsl-interpreter-work-meetings.html",
    "online-bsl-interpreter.html",
    "how-to-book-bsl-interpreter.html",
}

STYLE_ID = "bookbsl-global-nav-footer-20260912"
STYLE = f'''<style id="{STYLE_ID}">
/* One BookBSL header and footer across all public pages */
.top .shell{{width:min(1160px,calc(100% - 32px))!important;margin:auto!important}}
.topin{{min-height:68px!important;height:auto!important;display:flex!important;align-items:center!important;justify-content:space-between!important;gap:18px!important;padding:0!important}}
.topnav{{display:flex!important;align-items:center!important;justify-content:flex-end!important;gap:20px!important;flex-wrap:nowrap!important}}
.topnav>a{{text-decoration:none!important;font-weight:800!important;font-size:.9rem!important;color:var(--ink,#092A35)!important;white-space:nowrap!important;line-height:1.1!important}}
.topnav>a[aria-current="page"]{{color:var(--blue,#2456B3)!important;text-decoration:underline!important;text-decoration-thickness:2px!important;text-underline-offset:6px!important}}
.topnav .header-cta{{display:inline-flex!important;align-items:center!important;justify-content:center!important;box-sizing:border-box!important;min-height:42px!important;height:42px!important;padding:0 18px!important;border:2px solid var(--ink,#092A35)!important;border-radius:999px!important;background:var(--ink,#092A35)!important;color:#fff!important;text-decoration:none!important;box-shadow:none!important}}
.topnav .header-cta:hover{{background:var(--blue,#2456B3)!important;border-color:var(--blue,#2456B3)!important}}
.mobileCtaText{{display:none}}

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
  .topin{{flex-wrap:wrap!important;padding:10px 0!important;gap:9px 14px!important}}
  .topnav{{width:100%!important;justify-content:space-between!important;gap:10px!important;order:2!important}}
  .bookbslFooterGrid{{grid-template-columns:1fr 1fr!important;gap:28px!important}}
  .bookbslFooterBrand{{grid-column:1/-1!important}}
}}
@media(max-width:680px){{
  .top .shell{{width:min(100% - 22px,1160px)!important}}
  .topnav>a{{font-size:.72rem!important}}
  .topnav .header-cta{{display:inline-flex!important;min-height:36px!important;height:36px!important;padding:0 10px!important;font-size:.72rem!important}}
  .desktopCtaText{{display:none!important}}
  .mobileCtaText{{display:inline!important}}
  .brandSub{{display:none!important}}
}}
@media(max-width:500px){{
  .topnav{{gap:6px!important}}
  .topnav>a{{font-size:.68rem!important}}
  .topnav .header-cta{{padding:0 8px!important;font-size:.68rem!important}}
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


for name in PAGES:
    path = ROOT / name
    if not path.exists():
        raise RuntimeError(f"Missing public page: {name}")
    text = path.read_text(encoding="utf-8")

    header_pattern = re.compile(r'<header class="top">.*?</header>', re.S)
    matches = header_pattern.findall(text)
    if len(matches) != 1:
        raise RuntimeError(f"Expected exactly one top header in {name}, found {len(matches)}")
    text = header_pattern.sub(header_for(name), text, count=1)

    footer_pattern = re.compile(r'<footer(?:\s[^>]*)?>.*?</footer>', re.S)
    matches = footer_pattern.findall(text)
    if len(matches) != 1:
        raise RuntimeError(f"Expected exactly one footer in {name}, found {len(matches)}")
    text = footer_pattern.sub(FOOTER, text, count=1)

    text = replace_style(text)
    path.write_text(text, encoding="utf-8")

print(f"Updated navigation and footer on {len(PAGES)} public BookBSL pages")
