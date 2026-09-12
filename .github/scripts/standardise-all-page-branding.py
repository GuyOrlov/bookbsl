from pathlib import Path
import re

BRAND = '<a class="brand" href="./"><span class="brandmark">BSL</span><span>Book<b>BSL</b><small class="brandSub">Clear booking. Clear communication.</small></span></a>'

H1_REPLACEMENTS = {
    'bsl-interpreter-events.html': ('<h1>Booking a BSL interpreter for events</h1>', '<h1>Booking a BSL interpreter for <span>events</span></h1>'),
    'bsl-interpreter-work-meetings.html': ('<h1>Booking a BSL interpreter for work and meetings</h1>', '<h1>Booking a BSL interpreter for <span>work and meetings</span></h1>'),
    'online-bsl-interpreter.html': ('<h1>Booking an online BSL interpreter</h1>', '<h1>Booking an online <span>BSL interpreter</span></h1>'),
    'bsl-interpreter-cost.html': ('<h1>How much does a BSL interpreter cost?</h1>', '<h1>How much does a <span>BSL interpreter cost?</span></h1>'),
    'how-to-book-bsl-interpreter.html': ('<h1>How to book a BSL interpreter in the UK</h1>', '<h1>How to book a <span>BSL interpreter in the UK</span></h1>'),
    'bsl-interpreter-healthcare.html': ('<h1>Arranging BSL interpreting for healthcare</h1>', '<h1>Arranging BSL interpreting <span>for healthcare</span></h1>'),
    'bsl-interpreter-education.html': ('<h1>Booking BSL interpreting for education and training</h1>', '<h1>Booking BSL interpreting for <span>education and training</span></h1>'),
    'stats.html': ('<h1 style="font-size:2.4rem">BookBSL site statistics</h1>', '<h1 style="font-size:2.4rem">BookBSL <span>site statistics</span></h1>'),
}

CONSISTENCY_CSS = '''
<style id="bookbsl-brand-consistency">
/* BookBSL brand consistency across every page */
:root{--bookbsl-blue:#2456B3;--bookbsl-ink:#092A35;--bookbsl-yellow:#FFD84D;--bookbsl-muted:#596970}
.top{position:sticky;top:0;z-index:40;background:rgba(244,247,245,.96);backdrop-filter:blur(14px);border-bottom:1px solid rgba(9,42,53,.12)}
.top .shell{width:min(1160px,calc(100% - 32px));margin:auto}
.topin{min-height:68px;display:flex;align-items:center;justify-content:space-between;gap:18px}
.brand{display:flex;align-items:center;gap:11px;text-decoration:none;font-weight:950;letter-spacing:-.04em;font-size:1.3rem;line-height:1;color:var(--ink,var(--bookbsl-ink));flex:0 0 auto}
.brandmark{width:42px;height:42px;border-radius:13px 13px 13px 5px;background:var(--ink,var(--bookbsl-ink));color:var(--yellow,var(--bookbsl-yellow));display:grid;place-items:center;font-size:.84rem;letter-spacing:-.03em;flex:0 0 auto}
.brand b{color:var(--blue,var(--bookbsl-blue))}
.brandSub{display:block;font-size:.65rem;letter-spacing:0;color:var(--muted,var(--bookbsl-muted));font-weight:750;margin-top:3px;line-height:1.15}
h1 span{color:var(--blue,var(--bookbsl-blue))}
@media(max-width:680px){
  .top .shell{width:min(100% - 22px,1160px)}
  .topin{min-height:62px;gap:10px}
  .brand{font-size:1rem;gap:8px}
  .brandmark{width:34px;height:34px;font-size:.72rem;border-radius:11px 11px 11px 4px}
  .brandSub{display:none!important}
}
</style>
'''

STATS_HEADER = '''<header class="top"><div class="shell topin">''' + BRAND + '''<nav class="topnav" aria-label="Main navigation"><a href="./#guides">Guides</a><a href="./#checker">Start checklist</a><a href="awareness.html">Awareness</a><a href="data.html">Data</a><a href="law.html">Laws</a></nav></div></header>'''

for path in sorted(Path('.').glob('*.html')):
    text = path.read_text(encoding='utf-8')

    # Upgrade simple BookBSL wordmark to the full branded mark + tagline.
    text = text.replace('<a class="brand" href="./">BookBSL</a>', BRAND)

    # Stats is intentionally noindex, but still gets the same visual header.
    if path.name == 'stats.html' and '<header class="top">' not in text:
        text = text.replace('<body>', '<body>' + STATS_HEADER, 1)

    # Add blue emphasis to guide titles / stats when not already applied.
    if path.name in H1_REPLACEMENTS:
        old, new = H1_REPLACEMENTS[path.name]
        if old in text:
            text = text.replace(old, new, 1)

    # Add one final consistency layer to every page without duplicating it.
    if 'id="bookbsl-brand-consistency"' not in text:
        text = text.replace('</head>', CONSISTENCY_CSS + '</head>', 1)

    path.write_text(text, encoding='utf-8')

# Verification: every HTML page should now carry the full BookBSL identity.
errors = []
for path in sorted(Path('.').glob('*.html')):
    text = path.read_text(encoding='utf-8')
    if 'Clear booking. Clear communication.' not in text:
        errors.append(f'{path}: missing tagline')
    if 'brandmark' not in text:
        errors.append(f'{path}: missing BSL brandmark')
    if 'bookbsl-brand-consistency' not in text:
        errors.append(f'{path}: missing consistency CSS')
    m = re.search(r'<h1\b[^>]*>(.*?)</h1>', text, re.S)
    if m and '<span' not in m.group(1):
        errors.append(f'{path}: H1 has no blue-highlight span')

if errors:
    raise SystemExit('\n'.join(errors))
