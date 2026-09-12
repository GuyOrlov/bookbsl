from pathlib import Path
import re

ROOT = Path('.')

for path in ROOT.glob('*.html'):
    text = path.read_text(encoding='utf-8')
    if 'class="topnav"' not in text:
        continue
    if 'href="#guides"' in text or 'href="./#guides"' in text:
        continue

    # Add Guides as the first item in the main navigation on subpages.
    updated, count = re.subn(
        r'(<nav\s+class="topnav"[^>]*>)',
        r'\1<a href="./#guides">Guides</a>',
        text,
        count=1,
    )
    if count:
        path.write_text(updated, encoding='utf-8')
        print(f'Added Guides menu item to {path.name}')
