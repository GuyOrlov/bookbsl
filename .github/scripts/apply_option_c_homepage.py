from pathlib import Path
import re

path = Path('index.html')
html = path.read_text(encoding='utf-8')

# 1) Use the full English name in the main visible headline.
old_h1 = '<h1>Book a BSL Interpreter in the UK <span>with confidence.</span></h1>'
new_h1 = '<h1>Book a British Sign Language interpreter in the UK <span>with confidence.</span></h1>'
if old_h1 in html:
    html = html.replace(old_h1, new_h1, 1)
elif new_h1 not in html:
    raise SystemExit('Homepage H1 pattern not found')

# 2) Make the direct commercial action clearer.
old_cta = 'I know what I need — email cSeeker'
new_cta = 'Already know what you need? Request availability &amp; a quote'
if old_cta in html:
    html = html.replace(old_cta, new_cta, 1)
elif new_cta not in html:
    raise SystemExit('Direct-enquiry CTA pattern not found')

# 3) Option C: keep the homepage conversion-first.
# Move proof, trust and preparation content out of the path between the hero and checklist.
# They remain on the page, immediately after the result/quote experience.
markers = {
    'proof': re.compile(r'<section class="proofStrip" aria-label="BookBSL facts">.*?</section>\n', re.S),
    'trust': re.compile(r'<section class="trust">.*?</section>\n', re.S),
    'prep': re.compile(r'<section class="section paper"><div class="shell"><div class="intro"><div class="eyebrow">Before you book</div>.*?</section>\n', re.S),
}

blocks = []
for name, pattern in markers.items():
    match = pattern.search(html)
    if not match:
        # Already moved is acceptable if it sits after results.
        continue
    blocks.append(match.group(0))
    html = html[:match.start()] + html[match.end():]

# Insert the supporting material after the results/quote block and before the next content section.
if blocks:
    anchor = '\n<section class="section paper faq" id="faq">'
    pos = html.find(anchor)
    if pos == -1:
        raise SystemExit('Could not locate post-results insertion point')
    html = html[:pos] + '\n' + ''.join(blocks) + html[pos:]

# Add a small conversion-order marker for future maintenance.
if '<!-- homepage-order: conversion-first -->' not in html:
    html = html.replace('<main id="main">', '<main id="main">\n<!-- homepage-order: conversion-first -->', 1)

path.write_text(html, encoding='utf-8')

# Verification
updated = path.read_text(encoding='utf-8')
assert new_h1 in updated
assert new_cta in updated
hero_pos = updated.find('<section class="hero">')
checker_pos = updated.find('<section class="checker" id="checker">')
proof_pos = updated.find('<section class="proofStrip"')
results_pos = updated.find('<section class="results" id="results"')
assert -1 not in (hero_pos, checker_pos, proof_pos, results_pos)
assert hero_pos < checker_pos < results_pos < proof_pos, (hero_pos, checker_pos, results_pos, proof_pos)
print('Applied conversion-first homepage order, full British Sign Language headline and clearer quote CTA.')
