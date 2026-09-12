from pathlib import Path
import re

ROOT = Path('.')
GUIDE_PAGES = {
    'bsl-interpreter-cost.html',
    'online-bsl-interpreter.html',
    'bsl-interpreter-events.html',
    'bsl-interpreter-education.html',
    'bsl-interpreter-healthcare.html',
    'how-to-book-bsl-interpreter.html',
    'bsl-interpreter-work-meetings.html',
}


def nav_for(name: str) -> str:
    guides_current = ' aria-current="page"' if name in GUIDE_PAGES else ''
    access_current = ' aria-current="page"' if name == 'awareness.html' else ''
    data_current = ' aria-current="page"' if name == 'data.html' else ''
    return (
        '<nav class="topnav" aria-label="Main navigation">'
        f'<a href="./#guides"{guides_current}>Guides</a>'
        f'<a href="awareness.html"{access_current}>Access preparation</a>'
        f'<a href="data.html"{data_current}>Data</a>'
        '<a class="header-cta navCta" href="./#checker">Start checklist</a>'
        '</nav>'
    )

changed = []
for path in sorted(ROOT.glob('*.html')):
    text = path.read_text(encoding='utf-8')
    if '<nav class="topnav"' not in text:
        continue
    new_text, count = re.subn(
        r'<nav class="topnav" aria-label="Main navigation">.*?</nav>',
        nav_for(path.name),
        text,
        count=1,
        flags=re.S,
    )
    if count != 1:
        raise SystemExit(f'Expected exactly one top navigation in {path.name}, found {count}')
    if new_text != text:
        path.write_text(new_text, encoding='utf-8')
        changed.append(path.name)

print('Updated navigation:', ', '.join(changed) if changed else 'no files needed changes')
