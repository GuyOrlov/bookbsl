from pathlib import Path
import re

ROOT = Path('.')
INDEX = ROOT / 'index.html'
AWARE = ROOT / 'awareness.html'


def find_section_by_id(text: str, section_id: str):
    m = re.search(r'<section\b[^>]*\bid=["\']' + re.escape(section_id) + r'["\'][^>]*>', text, re.I)
    if not m:
        return None
    start = m.start()
    pos = m.end()
    depth = 1
    tag_re = re.compile(r'<section\b[^>]*>|</section\s*>', re.I)
    for tag in tag_re.finditer(text, pos):
        t = tag.group(0).lower()
        if t.startswith('<section'):
            depth += 1
        else:
            depth -= 1
            if depth == 0:
                return start, tag.end(), text[start:tag.end()]
    raise RuntimeError(f'Unclosed section #{section_id}')


def find_first_main_section_end(text: str):
    main = re.search(r'<main\b[^>]*>', text, re.I)
    if not main:
        raise RuntimeError('No <main> found')
    first = re.search(r'<section\b[^>]*>', text[main.end():], re.I)
    if not first:
        raise RuntimeError('No section inside <main>')
    start = main.end() + first.start()
    pos = main.end() + first.end()
    depth = 1
    tag_re = re.compile(r'<section\b[^>]*>|</section\s*>', re.I)
    for tag in tag_re.finditer(text, pos):
        if tag.group(0).lower().startswith('<section'):
            depth += 1
        else:
            depth -= 1
            if depth == 0:
                return tag.end()
    raise RuntimeError('Could not find end of first main section')

support_css = r'''
<style id="bookbsl-awareness-support-styles">
#support{scroll-margin-top:82px;background:#fff;border-block:1px solid var(--line);padding:58px 0}
#support .supportIntro{max-width:880px}
#support .supportGrid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px;margin-top:28px}
#support .supportCard{border:1.5px solid var(--ink);border-radius:24px;padding:22px;background:#fff;min-height:210px}
#support .supportCard:nth-child(1){background:var(--mint)}
#support .supportCard:nth-child(2){background:var(--yellow)}
#support .supportNo{width:38px;height:38px;border-radius:50%;background:var(--ink);color:var(--yellow);display:grid;place-items:center;font-weight:800;margin-bottom:24px}
#support .supportCard h3{margin-bottom:8px;font-size:1.18rem}
#support .supportCard p{color:var(--muted);margin-bottom:0;font-size:.92rem}
#support .supportNote{margin-top:22px;padding:18px 20px;border-left:6px solid var(--blue);background:#EDF3FF;border-radius:0 18px 18px 0;color:#33465B}
#support .supportNote strong{color:var(--ink)}
@media(max-width:900px){#support .supportGrid{grid-template-columns:1fr 1fr}}
@media(max-width:680px){#support{padding:44px 0}#support .supportGrid{grid-template-columns:1fr}#support .supportCard{min-height:0}}
</style>
'''

support_section = r'''
<section id="support" aria-labelledby="support-title">
  <div class="shell">
    <div class="supportIntro">
      <div class="eyebrow">Communication support</div>
      <h2 id="support-title">Different Deaf people may need <span style="color:var(--blue)">different support.</span></h2>
      <p class="lead">Do not assume that every Deaf person needs the same adjustment. Ask the person what communication support they prefer, then arrange the right professional or access option for the situation.</p>
    </div>
    <div class="supportGrid">
      <article class="supportCard"><div class="supportNo">1</div><h3>BSL interpreter</h3><p>Supports communication between a British Sign Language user and people using spoken English. The booking should include enough context, timings and preparation material.</p></article>
      <article class="supportCard"><div class="supportNo">2</div><h3>Deaf Relay / intralingual support</h3><p>Some Deaf people may benefit from a Deaf relay or intralingual professional who can adapt language and communication between different signing styles, language levels or contexts.</p></article>
      <article class="supportCard"><div class="supportNo">3</div><h3>Lipspeaker</h3><p>A lipspeaker silently and clearly reproduces a speaker’s words with visible lip patterns and appropriate facial expression for people who lipread.</p></article>
      <article class="supportCard"><div class="supportNo">4</div><h3>Speech-to-text / live captions</h3><p>Real-time speech-to-text support turns spoken information into readable text. This can be useful for meetings, events, training and other spoken communication.</p></article>
      <article class="supportCard"><div class="supportNo">5</div><h3>Deafblind communication support</h3><p>A Deafblind person may use tactile signing, hands-on communication or another preferred method. The individual should confirm what works best for them.</p></article>
      <article class="supportCard"><div class="supportNo">6</div><h3>Other adjustments</h3><p>Captions, written information, visual alerts, hearing technology, room layout and other adjustments may also be part of accessible communication, depending on the person and setting.</p></article>
    </div>
    <div class="supportNote"><strong>Best practice:</strong> ask the Deaf person first. Communication preference should guide the booking rather than assumptions about hearing level, language or identity.</div>
  </div>
</section>
'''

# 1) Remove the old Support section from the homepage.
index = INDEX.read_text(encoding='utf-8')
old = find_section_by_id(index, 'support')
if old:
    start, end, _ = old
    index = index[:start] + index[end:]

# Homepage Support menu should now go to Awareness.
index = re.sub(r'<a\s+href=["\'](?:\./)?#support["\']([^>]*)>Support</a>',
               r'<a href="awareness.html#support"\1>Support</a>', index, flags=re.I)
INDEX.write_text(index, encoding='utf-8')

# 2) Add the communication-support section to Awareness, directly after its hero.
aware = AWARE.read_text(encoding='utf-8')
existing = find_section_by_id(aware, 'support')
if existing:
    s, e, _ = existing
    aware = aware[:s] + aware[e:]

if 'id="bookbsl-awareness-support-styles"' not in aware:
    aware = aware.replace('</head>', support_css + '\n</head>', 1)

insert_at = find_first_main_section_end(aware)
aware = aware[:insert_at] + '\n' + support_section + aware[insert_at:]

# Strengthen the Awareness search snippet now that it also explains support types.
aware = re.sub(
    r'<meta name="description" content="[^"]*">',
    '<meta name="description" content="Deaf awareness and communication support guidance for UK organisations, including BSL interpreters, Deaf Relay, lipspeakers, speech-to-text and practical access preparation.">',
    aware,
    count=1,
    flags=re.I,
)

# On the Awareness page, Support is the current top-level destination.
aware = re.sub(r'<a\s+href=["\'](?:\./)?#support["\']([^>]*)>Support</a>',
               r'<a href="#support" aria-current="page"\1>Support</a>', aware, flags=re.I)
aware = re.sub(r'<a\s+href=["\']awareness\.html#support["\']([^>]*)>Support</a>',
               r'<a href="#support" aria-current="page"\1>Support</a>', aware, flags=re.I)
AWARE.write_text(aware, encoding='utf-8')

# 3) Point Support in every other public page header to the Awareness support section.
for p in ROOT.glob('*.html'):
    if p.name in {'index.html', 'awareness.html', 'stats.html'}:
        continue
    text = p.read_text(encoding='utf-8')
    text = re.sub(r'<a\s+href=["\'](?:\./)?#support["\']([^>]*)>Support</a>',
                  r'<a href="awareness.html#support"\1>Support</a>', text, flags=re.I)
    text = re.sub(r'<a\s+href=["\']awareness\.html#support["\']([^>]*)>Support</a>',
                  r'<a href="awareness.html#support"\1>Support</a>', text, flags=re.I)
    p.write_text(text, encoding='utf-8')

# Verification.
index_now = INDEX.read_text(encoding='utf-8')
aware_now = AWARE.read_text(encoding='utf-8')
assert 'id="support"' not in index_now, 'Support section still exists on homepage'
assert 'href="awareness.html#support"' in index_now, 'Homepage Support nav does not point to Awareness'
assert aware_now.count('id="support"') == 1, 'Awareness must contain exactly one support section'
assert 'BSL interpreter' in aware_now and 'Speech-to-text / live captions' in aware_now and 'Deaf Relay / intralingual support' in aware_now
assert 'href="#support" aria-current="page"' in aware_now, 'Awareness Support nav is not active'
print('Moved communication support from homepage to awareness.html and updated navigation.')
