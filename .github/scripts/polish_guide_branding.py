from pathlib import Path

GUIDES = {
    "bsl-interpreter-events.html": ("Booking a BSL interpreter ", "for events"),
    "bsl-interpreter-work-meetings.html": ("Booking a BSL interpreter for ", "work and meetings"),
    "online-bsl-interpreter.html": ("Booking an ", "online BSL interpreter"),
    "bsl-interpreter-cost.html": ("How much does a ", "BSL interpreter cost?"),
    "how-to-book-bsl-interpreter.html": ("How to book a ", "BSL interpreter in the UK"),
    "bsl-interpreter-healthcare.html": ("Arranging BSL interpreting ", "for healthcare"),
    "bsl-interpreter-education.html": ("Booking BSL interpreting for ", "education and training"),
}

BRAND_OLD = '<a class="brand" href="./">BookBSL</a>'
BRAND_NEW = (
    '<a class="brand" href="./">'
    '<span class="brandmark">BSL</span>'
    '<span>Book<b>BSL</b><small class="brandSub">Clear booking. Clear communication.</small></span>'
    '</a>'
)

POLISH = r'''
/* BookBSL guide brand polish */
.top{position:sticky;top:0;z-index:40;background:rgba(244,247,245,.96);backdrop-filter:blur(14px)}
.top .shell{width:min(1160px,calc(100% - 32px))}
.brand{display:flex;align-items:center;gap:11px;text-decoration:none;font-weight:950;letter-spacing:-.04em;font-size:1.3rem;line-height:1;color:var(--ink)}
.brandmark{width:42px;height:42px;border-radius:13px 13px 13px 5px;background:var(--ink);color:var(--yellow);display:grid;place-items:center;font-size:.84rem;letter-spacing:-.03em;flex:0 0 auto}
.brand b{color:var(--blue)}
.brandSub{display:block;font-size:.65rem;letter-spacing:0;color:var(--muted);font-weight:750;margin-top:3px;line-height:1.15}
h1 span{color:var(--blue)}
@media(max-width:680px){
  .top .shell{width:min(100% - 22px,1160px)}
  .brand{font-size:1rem;gap:8px}
  .brandmark{width:34px;height:34px;font-size:.72rem;border-radius:11px 11px 11px 4px}
  .brandSub{display:none}
}
'''.strip()

for filename, (prefix, accent) in GUIDES.items():
    path = Path(filename)
    if not path.exists():
        raise SystemExit(f"Missing guide: {filename}")
    text = path.read_text(encoding="utf-8")

    if BRAND_NEW not in text:
        if BRAND_OLD not in text:
            raise SystemExit(f"Brand marker not found in {filename}")
        text = text.replace(BRAND_OLD, BRAND_NEW, 1)

    plain_h1 = f'<h1>{prefix}{accent}</h1>'
    styled_h1 = f'<h1>{prefix}<span>{accent}</span></h1>'
    if styled_h1 not in text:
        if plain_h1 not in text:
            raise SystemExit(f"H1 marker not found in {filename}: {plain_h1}")
        text = text.replace(plain_h1, styled_h1, 1)

    if '/* BookBSL guide brand polish */' not in text:
        if '</style>' not in text:
            raise SystemExit(f"Style end marker not found in {filename}")
        text = text.replace('</style>', '\n' + POLISH + '\n</style>', 1)

    path.write_text(text, encoding="utf-8")
