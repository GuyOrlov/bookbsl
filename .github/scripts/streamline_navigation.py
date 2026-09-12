from pathlib import Path
import re

ROOT = Path('.')
GUIDE_PAGES = {
    'bsl-interpreter-events.html',
    'bsl-interpreter-work-meetings.html',
    'online-bsl-interpreter.html',
    'bsl-interpreter-cost.html',
    'how-to-book-bsl-interpreter.html',
    'bsl-interpreter-healthcare.html',
    'bsl-interpreter-education.html',
    'awareness.html', 'data.html', 'law.html'
}

CSS = r'''
/* Streamlined BookBSL navigation */
.topnav{display:flex!important;align-items:center!important;gap:18px!important;flex-wrap:wrap!important}
.topnav>a{font-weight:800!important;text-decoration:none!important;color:var(--ink)!important;white-space:nowrap!important}
.topnav .header-cta{display:inline-flex!important;align-items:center!important;justify-content:center!important;min-height:42px!important;height:42px!important;padding:0 18px!important;border:2px solid var(--ink)!important;border-radius:999px!important;background:var(--ink)!important;color:#fff!important;line-height:1!important;box-shadow:none!important}
.topnav .header-cta:hover{background:var(--blue)!important;border-color:var(--blue)!important}
@media(max-width:680px){
  .topnav{gap:10px!important}
  .topnav>a:not(.header-cta){font-size:.76rem!important}
  .topnav .header-cta{display:none!important}
}
'''

RESOURCE_BLOCK = r'''
<div class="guideResourceBlock">
  <div class="eyebrow">BSL awareness & resources</div>
  <h3>Access guidance, UK evidence and BSL law.</h3>
  <p class="lead resourceLead">Explore practical Deaf awareness guidance, UK BSL data and the main laws connected with communication access.</p>
  <div class="resourceGrid">
    <a class="resourceCard" href="awareness.html"><strong>Awareness</strong><span>Prepare better Deaf access before someone arrives.</span></a>
    <a class="resourceCard" href="data.html"><strong>Data</strong><span>UK BSL, Deaf access and communication-professional evidence.</span></a>
    <a class="resourceCard" href="law.html"><strong>Laws</strong><span>A simple UK guide to BSL rights and reasonable adjustments.</span></a>
  </div>
</div>
'''

RESOURCE_CSS = r'''
.guideResourceBlock{margin-top:40px;padding-top:34px;border-top:1px solid var(--line)}
.guideResourceBlock h3{font-size:clamp(1.5rem,3vw,2.25rem);margin:0 0 10px;color:var(--ink)}
.resourceLead{max-width:760px}
.resourceGrid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px;margin-top:20px}
.resourceCard{display:flex;flex-direction:column;gap:7px;text-decoration:none;background:var(--mint,#DDF4EC);border:1.5px solid var(--ink);border-radius:20px;padding:18px;color:var(--ink)}
.resourceCard strong{font-size:1rem}.resourceCard span{color:var(--muted);font-size:.86rem}
@media(max-width:720px){.resourceGrid{grid-template-columns:1fr}}
'''

def nav_for(name: str) -> str:
    prefix = '' if name == 'index.html' else './'
    current = ' aria-current="page"' if name in GUIDE_PAGES else ''
    return (
        '<nav class="topnav" aria-label="Main navigation">'
        f'<a href="{prefix}#guides"{current}>Guides</a>'
        f'<a href="{prefix}#support">Support</a>'
        f'<a class="header-cta navCta" href="{prefix}#checker">Start checklist</a>'
        '</nav>'
    )

changed = []
for p in ROOT.glob('*.html'):
    if p.name == 'stats.html':
        continue
    text = p.read_text(encoding='utf-8')
    old = text
    text, n = re.subn(
        r'<nav class="topnav" aria-label="Main navigation">.*?</nav>',
        nav_for(p.name), text, count=1, flags=re.S
    )
    if n and 'Streamlined BookBSL navigation' not in text:
        text = text.replace('</style>', CSS + '\n</style>', 1)
    if p.name == 'index.html':
        if 'class="guideResourceBlock"' not in text:
            text, n2 = re.subn(r'(<div class="guideGrid">.*?</div>)', r'\1\n' + RESOURCE_BLOCK, text, count=1, flags=re.S)
            if n2 and '.guideResourceBlock{' not in text:
                text = text.replace('</style>', RESOURCE_CSS + '\n</style>', 1)
    if text != old:
        p.write_text(text, encoding='utf-8')
        changed.append(p.name)

if not changed:
    raise SystemExit('No navigation changes were needed')

print('Updated:', ', '.join(changed))
