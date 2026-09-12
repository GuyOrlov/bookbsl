from pathlib import Path
import re

STYLE_ID = "bookbsl-equal-nav-tabs-20260912"
ROOT = Path('.')

STYLE = r'''
<style id="bookbsl-equal-nav-tabs-20260912">
/* Equal-size BookBSL top navigation tabs on every public page */
.topnav{
  display:grid!important;
  grid-template-columns:repeat(4,152px)!important;
  gap:10px!important;
  align-items:center!important;
  justify-content:end!important;
  flex-wrap:nowrap!important;
}
.topnav>a{
  box-sizing:border-box!important;
  width:152px!important;
  min-width:152px!important;
  height:42px!important;
  min-height:42px!important;
  padding:0 12px!important;
  display:inline-flex!important;
  align-items:center!important;
  justify-content:center!important;
  border:2px solid transparent!important;
  border-radius:999px!important;
  background:transparent!important;
  color:var(--ink,#092A35)!important;
  text-decoration:none!important;
  text-align:center!important;
  font-size:.86rem!important;
  font-weight:800!important;
  line-height:1!important;
  white-space:nowrap!important;
  box-shadow:none!important;
  transition:background-color .16s ease,border-color .16s ease,color .16s ease,transform .08s ease!important;
}
.topnav>a.header-cta,
.topnav>a.navCta{
  background:var(--ink,#092A35)!important;
  color:#fff!important;
  border-color:var(--ink,#092A35)!important;
}
.topnav>a:hover,
.topnav>a:focus-visible,
.topnav>a[aria-current="page"]{
  background:var(--blue,#2456B3)!important;
  border-color:var(--blue,#2456B3)!important;
  color:#fff!important;
  text-decoration:none!important;
}
.topnav>a:focus-visible{
  outline:3px solid #FFD84D!important;
  outline-offset:3px!important;
}
.topnav>a:active{
  background:var(--blue,#2456B3)!important;
  border-color:var(--blue,#2456B3)!important;
  color:#fff!important;
  transform:translateY(1px)!important;
}
.mobileNavLabel{display:none!important}

@media(max-width:980px){
  .topnav{
    width:100%!important;
    grid-template-columns:repeat(4,minmax(0,1fr))!important;
    gap:8px!important;
    justify-content:stretch!important;
  }
  .topnav>a{
    width:100%!important;
    min-width:0!important;
    padding:0 8px!important;
  }
}

@media(max-width:680px){
  .topnav{gap:6px!important}
  .topnav>a{
    height:38px!important;
    min-height:38px!important;
    padding:0 6px!important;
    font-size:.70rem!important;
  }
  .desktopNavLabel{display:none!important}
  .mobileNavLabel{display:inline!important}
}

@media(max-width:390px){
  .topnav{gap:4px!important}
  .topnav>a{font-size:.66rem!important;padding:0 4px!important}
}
</style>
'''

style_re = re.compile(r'\n?<style id="' + re.escape(STYLE_ID) + r'">.*?</style>\n?', re.S)
access_re = re.compile(r'(<a\b[^>]*href="awareness\.html"[^>]*>)(?:<span class="desktopNavLabel">Access preparation</span><span class="mobileNavLabel">Access</span>|Access preparation)(</a>)', re.I)

changed = []
checked = []
for path in sorted(ROOT.glob('*.html')):
    text = path.read_text(encoding='utf-8')
    if 'class="topnav"' not in text:
        continue

    checked.append(path.name)
    text = style_re.sub('\n', text)
    text = access_re.sub(r'\1<span class="desktopNavLabel">Access preparation</span><span class="mobileNavLabel">Access</span>\2', text)

    if '</head>' not in text:
        raise RuntimeError(f'{path}: missing </head>')
    text = text.replace('</head>', STYLE + '\n</head>', 1)

    nav_match = re.search(r'<nav class="topnav"[^>]*>(.*?)</nav>', text, re.S)
    if not nav_match:
        raise RuntimeError(f'{path}: topnav markup not found')
    anchor_count = len(re.findall(r'<a\b', nav_match.group(1)))
    if anchor_count != 4:
        raise RuntimeError(f'{path}: expected 4 top navigation links, found {anchor_count}')

    path.write_text(text, encoding='utf-8')
    changed.append(path.name)

if not checked:
    raise RuntimeError('No top navigation pages found')

for name in checked:
    check = (ROOT / name).read_text(encoding='utf-8')
    assert STYLE_ID in check, name
    assert 'grid-template-columns:repeat(4,152px)' in check, name
    assert 'background:var(--blue,#2456B3)!important' in check, name
    if 'awareness.html' in re.search(r'<nav class="topnav"[^>]*>(.*?)</nav>', check, re.S).group(1):
        assert 'mobileNavLabel">Access<' in check, name

print(f'Unified top navigation tabs on {len(changed)} pages: ' + ', '.join(changed))
