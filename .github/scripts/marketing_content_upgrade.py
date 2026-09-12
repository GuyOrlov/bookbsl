from pathlib import Path
import re
import json

ROOT = Path('.')
TODAY = '2026-09-12'


def read(name):
    return (ROOT / name).read_text(encoding='utf-8')


def write(name, text):
    (ROOT / name).write_text(text, encoding='utf-8')


def sub_once(pattern, replacement, text, label, flags=re.S):
    out, n = re.subn(pattern, replacement, text, count=1, flags=flags)
    if n != 1:
        raise RuntimeError(f'Could not update {label}: expected 1 match, found {n}')
    return out


# -----------------------------------------------------------------------------
# 1) Homepage: conversion-focused guide hierarchy and consistent naming.
# -----------------------------------------------------------------------------
index = read('index.html')

popular_guides = [
    ('how-to-book-bsl-interpreter.html', 'How to book a British Sign Language interpreter', 'A step-by-step UK booking guide for first-time and occasional bookers.'),
    ('bsl-interpreter-cost.html', 'How much does a British Sign Language interpreter cost?', 'Understand the factors that affect a quote before you enquire.'),
    ('bsl-interpreter-work-meetings.html', 'British Sign Language interpreters for work and meetings', 'Prepare workplace meetings, interviews, training and business bookings.'),
]
more_guides = [
    ('bsl-interpreter-events.html', 'Events, conferences & exhibitions', 'Plan timings, stage access, breaks, cameras and livestreams.'),
    ('access-to-work-bsl-interpreter.html', 'Access to Work & interpreter bookings', 'Organise workplace support while keeping funding and booking responsibilities clear.'),
    ('one-or-two-bsl-interpreters.html', 'Do I need one or two interpreters?', 'Understand the factors that can make a team more appropriate.'),
    ('bsl-interpreter-legal-official.html', 'Legal & official appointments', 'Prepare clearer enquiries for legal, public-sector and official settings.'),
    ('how-far-ahead-book-bsl-interpreter.html', 'How far ahead should I book?', 'Plan early for fixed dates, specialist work, events and busy periods.'),
    ('bsl-interpreter-healthcare.html', 'Healthcare appointments', 'Prepare communication access, appointment details and privacy information.'),
    ('online-bsl-interpreter.html', 'Online & remote interpreting', 'Prepare Zoom, Teams, hybrid and other remote bookings.'),
    ('bsl-interpreter-education.html', 'Education & training', 'Prepare courses, workshops, assessments and learning sessions.'),
]

popular_html = ''.join(
    f'<a class="popularGuideCard" href="{href}"><span class="popularLabel">Popular guide</span><strong>{title}</strong><span>{desc}</span></a>'
    for href, title, desc in popular_guides
)
more_html = ''.join(
    f'<a class="guideCard" href="{href}"><strong>{title}</strong><span>{desc}</span></a>'
    for href, title, desc in more_guides
)

guide_section = f'''<section class="section paper" id="guides">
  <div class="shell">
    <div class="eyebrow">British Sign Language booking guides</div>
    <h2>Start with the questions people ask before they book.</h2>
    <p class="lead">Use BookBSL guides to understand the booking, prepare the right information and then use the checklist to request availability and a quote.</p>

    <h3 class="guideGroupTitle">Popular guides</h3>
    <div class="popularGuideGrid">{popular_html}</div>

    <h3 class="guideGroupTitle moreTitle">More practical guides</h3>
    <div class="guideGrid">{more_html}</div>

    <div class="guideResourceBlock">
      <div class="eyebrow">Access, evidence & rights</div>
      <h3>Prepare access, understand the evidence and check the law.</h3>
      <p class="lead resourceLead">Use these supporting pages when you need practical Deaf access guidance, UK data or a simple overview of British Sign Language rights and reasonable adjustments.</p>
      <div class="resourceGrid">
        <a class="resourceCard" href="awareness.html"><strong>Access preparation</strong><span>Prepare communication access, rooms, lighting and support before the meeting, appointment or event.</span></a>
        <a class="resourceCard" href="data.html"><strong>Data</strong><span>UK British Sign Language, Deaf access and registered communication-professional evidence.</span></a>
        <a class="resourceCard" href="law.html"><strong>Laws</strong><span>A simple UK guide to British Sign Language rights and reasonable adjustments.</span></a>
      </div>
    </div>
  </div>
</section>
<style id="bookbsl-marketing-guide-layout">
.guideGroupTitle{{font-size:1.15rem;margin:30px 0 12px;color:var(--ink)}}
.popularGuideGrid{{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px;margin-top:12px}}
.popularGuideCard{{display:flex;flex-direction:column;gap:9px;text-decoration:none;background:var(--ink);color:#fff;border:2px solid var(--ink);border-radius:26px;padding:24px;min-height:210px;box-shadow:6px 6px 0 var(--yellow)}}
.popularGuideCard strong{{font-size:1.22rem;line-height:1.18;color:#fff}}
.popularGuideCard>span:last-child{{color:#D4E1E4;font-size:.9rem}}
.popularLabel{{width:max-content;background:var(--yellow);color:var(--ink);border-radius:999px;padding:5px 9px;font-size:.72rem;font-weight:900;text-transform:uppercase;letter-spacing:.06em}}
.moreTitle{{margin-top:40px}}
.guideGrid{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px;margin-top:12px}}
.guideCard{{display:flex;flex-direction:column;gap:7px;text-decoration:none;background:#fff;border:1.5px solid var(--ink);border-radius:22px;padding:20px}}
.guideCard:hover,.resourceCard:hover{{box-shadow:4px 4px 0 var(--yellow);transform:translate(-1px,-1px)}}
.guideCard strong{{color:var(--ink);font-size:1rem}}.guideCard span{{color:var(--muted);font-size:.86rem}}
@media(max-width:900px){{.popularGuideGrid{{grid-template-columns:1fr}}.popularGuideCard{{min-height:0}}}}
@media(max-width:720px){{.guideGrid{{grid-template-columns:1fr}}}}
</style>'''

# Replace the existing guides section and its local guide-grid style block.
index = sub_once(
    r'<section class="section paper" id="guides">.*?</section>\s*<style>\s*\.guideGrid\{.*?</style>',
    guide_section,
    index,
    'homepage guide section',
)
index = index.replace('<strong>Awareness</strong>', '<strong>Access preparation</strong>')
write('index.html', index)


# -----------------------------------------------------------------------------
# 2) Four substantial, high-intent guides. Use an existing live guide as the
#    visual/layout base so the new pages inherit the current BookBSL design.
# -----------------------------------------------------------------------------
base = read('bsl-interpreter-work-meetings.html')

GUIDES = [
    {
        'file': 'access-to-work-bsl-interpreter.html',
        'title': 'Access to Work BSL Interpreter Guide UK | BookBSL',
        'desc': 'Prepare an Access to Work British Sign Language interpreter booking in the UK. Check communication preference, funding responsibility, dates, workplace details and preparation.',
        'h1': 'Access to Work and <span>British Sign Language interpreter bookings</span>',
        'headline': 'Access to Work and British Sign Language interpreter bookings',
        'kicker': 'Workplace communication support',
        'intro': 'Access to Work can support eligible workplace communication needs, but the funding arrangement and the interpreter booking are not the same thing. Prepare both clearly so the employee, employer, provider and communication professional know what has been agreed.',
        'sections': [
            ('Start with the Deaf person’s communication preference', 'Do not start with the funding scheme and assume the support type. Confirm what communication support the Deaf employee wants for the meeting, training, interview, supervision, conference or other workplace activity.'),
            ('Check the Access to Work award and responsibilities', 'Confirm what the current award covers, any limits or conditions, and who is expected to arrange the support and handle payment or reimbursement. BookBSL does not decide Access to Work eligibility or funding. Use the employee’s award information and current GOV.UK guidance.'),
            ('Give the complete workplace booking', 'Include the date, exact start and finish times, venue or online platform, purpose, number of participants, format and a named workplace contact. Recurring support should include every known date rather than only the first session.'),
            ('Share preparation material early', 'Agendas, slides, policies, technical vocabulary, names and background documents help the interpreter prepare. Workplace terminology can be specialist even when the meeting itself is short.'),
            ('Keep funding and booking records separate and clear', 'Keep the booking confirmation, agreed rate, cancellation terms and invoice information together. Keep any Access to Work claim or reimbursement paperwork in the organisation’s normal finance process so the booking details are not lost.'),
            ('If the award or support need changes', 'Do not assume an old arrangement automatically applies to a new role, new type of assignment or different communication need. Check the current award and ask the relevant parties before confirming the booking.'),
        ],
        'extra': '<p><strong>Official information:</strong> <a href="https://www.gov.uk/access-to-work" target="_blank" rel="noopener">Access to Work on GOV.UK ↗</a></p>',
    },
    {
        'file': 'one-or-two-bsl-interpreters.html',
        'title': 'One or Two BSL Interpreters? UK Booking Guide | BookBSL',
        'desc': 'Do you need one or two British Sign Language interpreters? Understand how duration, intensity, breaks, stage work, recording and specialist content can affect the team.',
        'h1': 'Do I need <span>one or two British Sign Language interpreters?</span>',
        'headline': 'Do I need one or two British Sign Language interpreters?',
        'kicker': 'Planning the right interpreting team',
        'intro': 'There is no single time limit that automatically decides whether a booking needs one interpreter or a team. The right arrangement depends on the duration, intensity, subject, format, breaks, audience, recording plans and working conditions.',
        'sections': [
            ('Duration matters, but it is not the only factor', 'A longer assignment can increase fatigue and make a team more appropriate, but a short and highly intensive assignment can also need additional support. Give the full start and finish times rather than only the speaking time.'),
            ('Intensity and specialist content matter', 'Fast discussion, technical vocabulary, multiple speakers, legal or medical content, stage work and audience interaction can increase cognitive demand. Tell the provider what will actually happen during the session.'),
            ('Events, stages and livestreams need extra planning', 'An interpreter who is continuously visible on stage or camera may have fewer natural breaks. Recording, broadcasting, rehearsals and sound checks should be declared before the team is confirmed.'),
            ('Breaks and working conditions affect the recommendation', 'A timetable with genuine breaks is different from a continuous programme. Room layout, travel between rooms, online switching and whether the interpreter must remain available during breaks can all affect the plan.'),
            ('Do not treat “90 minutes” as a universal rule', 'BookBSL may flag a longer booking as a prompt to check the team, but that is not a national rule. The interpreter or agency should assess the actual assignment and recommend the appropriate number of professionals.'),
            ('Ask before confirming a quote', 'Send the complete booking details and ask whether one interpreter is suitable or whether a team is recommended. If two professionals are required, make sure the quote, timetable and access arrangements reflect both.'),
        ],
        'extra': '<p><strong>Useful next step:</strong> use the BookBSL checklist and include the duration, format, recording plans and preparation material so the provider can assess the team.</p>',
    },
    {
        'file': 'bsl-interpreter-legal-official.html',
        'title': 'BSL Interpreter for Legal & Official Appointments UK | BookBSL',
        'desc': 'Prepare a British Sign Language interpreter enquiry for legal or official appointments in the UK. Check communication preference, setting, qualifications, security, timing and documents.',
        'h1': 'British Sign Language interpreters for <span>legal and official appointments</span>',
        'headline': 'British Sign Language interpreters for legal and official appointments',
        'kicker': 'Legal, public-sector & official settings',
        'intro': 'Legal and official settings can have specific professional, procedural, security or independence requirements. Prepare the booking carefully and confirm the organisation’s requirements before choosing a communication professional.',
        'sections': [
            ('Confirm the Deaf person’s communication preference', 'Ask what communication support is required rather than assuming British Sign Language interpreting is automatically the right adjustment. Some people may need Deaf Relay, speech-to-text, deafblind communication support or another arrangement.'),
            ('Describe the exact setting', 'Say whether the booking is for a court, tribunal, police matter, solicitor meeting, immigration appointment, local authority meeting, disciplinary process or another official setting. Different environments can have different requirements.'),
            ('Check qualification or registration requirements', 'Ask the responsible organisation whether a particular registration, qualification, security clearance or specialist experience is required. Do not assume that every interpreter is suitable for every legal or official assignment.'),
            ('Protect independence and confidentiality', 'Use appropriate professional arrangements and only share information needed to prepare for the assignment. Avoid using family members, friends or unqualified helpers where an independent professional is required.'),
            ('Give accurate timing and access information', 'Include arrival time, expected finish time, waiting time, security procedures, room details, breaks, remote-platform information and a named contact who can resolve access problems on the day.'),
            ('Send documents safely and early', 'Where appropriate and permitted, provide relevant names, terminology, case or meeting context and documents through the organisation’s approved information-sharing process. Sensitive information should follow the organisation’s normal security and privacy rules.'),
        ],
        'extra': '<p><strong>Important:</strong> this page is general booking guidance, not legal advice. The court, tribunal, police force, solicitor, public body or other responsible organisation should confirm any specific professional or procedural requirements.</p>',
    },
    {
        'file': 'how-far-ahead-book-bsl-interpreter.html',
        'title': 'How Far Ahead Should I Book a BSL Interpreter? UK | BookBSL',
        'desc': 'How early should you book a British Sign Language interpreter in the UK? Plan ahead for fixed dates, specialist assignments, events, evenings, weekends and interpreter teams.',
        'h1': 'How far ahead should I book a <span>British Sign Language interpreter?</span>',
        'headline': 'How far ahead should I book a British Sign Language interpreter?',
        'kicker': 'Availability & early planning',
        'intro': 'There is no single UK booking deadline that guarantees availability. The safest approach is to enquire as soon as the date and core details are known, especially for fixed-date events, specialist work, evenings, weekends or bookings that may need a team.',
        'sections': [
            ('Book as early as the booking allows', 'If the date is fixed, start the enquiry when you know the date, approximate times and setting. You can send some preparation material later. Waiting for every final detail can reduce the time available to find suitable professionals.'),
            ('Two to three weeks is useful guidance, not a guarantee', 'Published UK guidance in some sectors recommends arranging registered British Sign Language interpreters at least two to three weeks ahead where possible. Availability still depends on region, specialism, timing and the assignment itself.'),
            ('Large events often need much longer planning', 'Conferences, festivals, exhibitions, ceremonies and livestreamed events may need multiple professionals, rehearsals, stage planning, travel and specialist preparation. For fixed major events, planning several months ahead can be sensible.'),
            ('Evenings, weekends and specialist work can be harder to fill', 'A short daytime meeting and a specialist Saturday event are different availability problems. Tell the provider the full circumstances so they can search for the right professional rather than only someone who is free.'),
            ('Urgent booking? Still ask', 'If the booking is tomorrow or next week, do not give up. Send a complete enquiry immediately. A provider can check current availability, but short notice may reduce choice and can make specialist support harder to secure.'),
            ('Prepare now, confirm later', 'You can often begin with the date, times, location, purpose and communication preference, then send final slides, agendas, speaker names or joining links later. A clear early enquiry is usually more useful than a perfect enquiry sent too late.'),
        ],
        'extra': '<p><strong>See the evidence:</strong> <a href="data.html">BookBSL Data</a> shows the current NRCPD registration snapshot and explains why specialist communication support can be difficult to secure at short notice.</p>',
    },
]

all_links = [
    ('how-to-book-bsl-interpreter.html', 'How to book a British Sign Language interpreter'),
    ('bsl-interpreter-cost.html', 'How much does a British Sign Language interpreter cost?'),
    ('bsl-interpreter-work-meetings.html', 'Work and meetings'),
    ('bsl-interpreter-events.html', 'Events and conferences'),
    ('access-to-work-bsl-interpreter.html', 'Access to Work bookings'),
    ('one-or-two-bsl-interpreters.html', 'One or two interpreters?'),
    ('bsl-interpreter-legal-official.html', 'Legal and official appointments'),
    ('how-far-ahead-book-bsl-interpreter.html', 'How far ahead should I book?'),
    ('bsl-interpreter-healthcare.html', 'Healthcare appointments'),
    ('online-bsl-interpreter.html', 'Online interpreting'),
    ('bsl-interpreter-education.html', 'Education and training'),
]


def build_page(g):
    text = base
    text = re.sub(r'<title>.*?</title>', f'<title>{g["title"]}</title>', text, count=1, flags=re.S)
    text = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{g["desc"]}">', text, count=1)
    url = f'https://bookbsl.co.uk/{g["file"]}'
    text = re.sub(r'<link rel="canonical" href="[^"]*">', f'<link rel="canonical" href="{url}">', text, count=1)
    text = re.sub(r'<meta property="og:title" content="[^"]*">', f'<meta property="og:title" content="{g["title"]}">', text, count=1)
    text = re.sub(r'<meta property="og:description" content="[^"]*">', f'<meta property="og:description" content="{g["desc"]}">', text, count=1)
    text = re.sub(r'<meta property="og:url" content="[^"]*">', f'<meta property="og:url" content="{url}">', text, count=1)
    schema = {
        '@context': 'https://schema.org',
        '@type': 'Article',
        'headline': g['headline'],
        'description': g['desc'],
        'mainEntityOfPage': url,
        'publisher': {'@type': 'Organization', 'name': 'BookBSL by cSeeker Ltd', 'url': 'https://bookbsl.co.uk/'},
    }
    text = re.sub(
        r'<script type="application/ld\+json">.*?</script>',
        '<script type="application/ld+json">' + json.dumps(schema, ensure_ascii=False) + '</script>',
        text,
        count=1,
        flags=re.S,
    )
    cards = ''.join(f'<section class="card"><h2>{h}</h2><p>{p}</p></section>' for h, p in g['sections'])
    related = ''.join(
        f'<a href="{href}">{label}</a>'
        for href, label in all_links
        if href != g['file']
    )
    main = f'''<main><section class="hero"><div class="shell"><span class="kicker">{g['kicker']}</span><h1>{g['h1']}</h1><p class="lead">{g['intro']}</p></div></section>
<section class="content"><div class="shell">{cards}
<section class="card"><h2>Use this guide with BookBSL</h2>{g['extra']}</section>
<div class="cta"><h2>Turn the guidance into a clear enquiry</h2><p>Use BookBSL’s free checklist to collect the date, timing, format, communication preference, support type, recording plans and preparation information before requesting availability and a quote.</p><a class="btn" href="./#checker">Start the free checklist</a></div>
<h2>More BookBSL guides</h2><div class="related">{related}</div></div></section></main>'''
    text = sub_once(r'<main>.*?</main>', main, text, f'{g["file"]} main content')
    return text

for guide in GUIDES:
    write(guide['file'], build_page(guide))


# Refresh related links on the existing seven SEO guides without changing their
# article copy.
existing_guides = [
    'how-to-book-bsl-interpreter.html',
    'bsl-interpreter-cost.html',
    'bsl-interpreter-work-meetings.html',
    'bsl-interpreter-events.html',
    'bsl-interpreter-healthcare.html',
    'online-bsl-interpreter.html',
    'bsl-interpreter-education.html',
]
for filename in existing_guides:
    text = read(filename)
    related = ''.join(f'<a href="{href}">{label}</a>' for href, label in all_links if href != filename)
    text = re.sub(
        r'<h2>More BookBSL guides</h2><div class="related">.*?</div>',
        f'<h2>More BookBSL guides</h2><div class="related">{related}</div>',
        text,
        count=1,
        flags=re.S,
    )
    write(filename, text)


# -----------------------------------------------------------------------------
# 3) Data page: one meaningful horizontal NRCPD chart, then practical action.
# -----------------------------------------------------------------------------
data = read('data.html')

# Remove the older workforce-pressure and repeated NRCPD-card sections so the
# page does not become a wall of numbers.
data = re.sub(r'<section class="pressureWrap" id="accessSupplyPressure">.*?</section>\s*', '', data, count=1, flags=re.S)
data = re.sub(
    r'<section class="section"><div class="shell"><div class="intro"><div class="eyebrow">UK support</div><h2>How many communication professionals are registered in the UK\?</h2>.*?</section>',
    '',
    data,
    count=1,
    flags=re.S,
)

overview = '''
<section class="section dataOverview" aria-labelledby="data-overview-title"><div class="shell">
  <div class="intro"><div class="eyebrow">UK snapshot</div><h2 id="data-overview-title">Four numbers worth understanding first.</h2><p class="lead">These figures measure different things. Read them as context for access planning, not as interchangeable population totals.</p></div>
  <div class="overviewGrid">
    <article><strong>12m</strong><span>Deaf or hard of hearing in the UK</span></article>
    <article><strong>151k</strong><span>Estimated British Sign Language users in the UK</span></article>
    <article><strong>87k</strong><span>Estimated Deaf British Sign Language users in the UK</span></article>
    <article><strong>1,664</strong><span>Registered Sign Language Interpreters in the current NRCPD snapshot</span></article>
  </div>
</div></section>

<section class="section paper workforceViz" aria-labelledby="workforce-chart-title"><div class="shell">
  <div class="intro"><div class="eyebrow">Registered communication professionals</div><h2 id="workforce-chart-title">A specialist workforce at a glance.</h2><p class="lead">Current NRCPD registration figures shown by category. The bars use a true linear scale, so the much smaller specialist registers remain visibly much smaller.</p></div>
  <div class="workforceChart" role="list" aria-label="NRCPD registered communication professionals by category">
    <div class="barRow" role="listitem"><div class="barLabel">Sign Language Interpreters</div><div class="barTrack"><span class="barFill" style="--bar:100%"></span></div><strong>1,664</strong></div>
    <div class="barRow" role="listitem"><div class="barLabel">Trainee Sign Language Interpreters</div><div class="barTrack"><span class="barFill" style="--bar:14.5%"></span></div><strong>242</strong></div>
    <div class="barRow" role="listitem"><div class="barLabel">Sign Language Translators</div><div class="barTrack"><span class="barFill" style="--bar:5.8%"></span></div><strong>97</strong></div>
    <div class="barRow" role="listitem"><div class="barLabel">Relay Intralingual Interpreters</div><div class="barTrack"><span class="barFill" style="--bar:3.8%"></span></div><strong>63</strong></div>
    <div class="barRow" role="listitem"><div class="barLabel">Lipspeakers</div><div class="barTrack"><span class="barFill" style="--bar:3.2%"></span></div><strong>54</strong></div>
    <div class="barRow" role="listitem"><div class="barLabel">Speech to Text Reporters</div><div class="barTrack"><span class="barFill" style="--bar:1.9%"></span></div><strong>32</strong></div>
    <div class="barRow" role="listitem"><div class="barLabel">Trainee Sign Language Translators</div><div class="barTrack"><span class="barFill" style="--bar:1.2%"></span></div><strong>20</strong></div>
    <div class="barRow" role="listitem"><div class="barLabel">Deafblind Interpreters</div><div class="barTrack"><span class="barFill" style="--bar:1.1%"></span></div><strong>19</strong></div>
  </div>
  <p class="chartNote"><strong>Important:</strong> do not add the categories together to estimate unique professionals. NRCPD states that its totals include dual registrations, so one person can appear in more than one register.</p>
  <a class="sourceLink" href="https://www.nrcpd.org.uk/registration-figures" target="_blank" rel="noopener">View current NRCPD registration figures ↗</a>
</div></section>

<section class="section bookingMeaning" aria-labelledby="booking-meaning-title"><div class="shell">
  <div class="intro"><div class="eyebrow">What this means for your booking</div><h2 id="booking-meaning-title">Turn the evidence into three practical actions.</h2></div>
  <div class="meaningGrid">
    <article><span>1</span><h3>Ask what support is preferred</h3><p>Do not assume every Deaf person needs the same communication professional. Confirm the individual’s preference first.</p></article>
    <article><span>2</span><h3>Start early when the date is fixed</h3><p>Specialist registers are small and availability varies by location, timing and subject. Early enquiries give providers more time to find suitable professionals.</p></article>
    <article><span>3</span><h3>Send a complete brief</h3><p>Date, times, format, purpose, recording plans and preparation material help the provider confirm the appropriate support and team.</p></article>
  </div>
  <div class="meaningLinks"><a href="how-far-ahead-book-bsl-interpreter.html">How far ahead should I book? →</a><a href="one-or-two-bsl-interpreters.html">Do I need one or two interpreters? →</a></div>
</div></section>
'''

data = sub_once(
    r'(<main id="main"><section class="hero">.*?</section>)',
    r'\1' + overview,
    data,
    'data-page overview insertion',
)

if 'bookbsl-data-viz-20260912' not in data:
    data_css = '''<style id="bookbsl-data-viz-20260912">
.overviewGrid{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-top:28px}.overviewGrid article{border:1.5px solid var(--ink);border-radius:24px;padding:21px;background:#fff}.overviewGrid article:first-child{background:var(--yellow)}.overviewGrid strong{display:block;font-size:clamp(2.5rem,5vw,4rem);line-height:.95;letter-spacing:-.06em;color:var(--ink);margin-bottom:9px}.overviewGrid span{font-size:.88rem;color:var(--muted);font-weight:700}
.workforceChart{display:grid;gap:14px;margin:30px 0 18px}.barRow{display:grid;grid-template-columns:minmax(220px,1.1fr) minmax(220px,2fr) 72px;gap:14px;align-items:center}.barLabel{font-weight:800;color:var(--ink);font-size:.9rem}.barTrack{height:18px;border:1px solid var(--line);border-radius:999px;background:var(--soft);overflow:hidden}.barFill{display:block;width:var(--bar);min-width:6px;height:100%;background:var(--blue);border-radius:999px}.barRow strong{text-align:right;color:var(--ink);font-variant-numeric:tabular-nums}.chartNote{max-width:880px;color:var(--muted);font-size:.88rem}
.meaningGrid{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin-top:28px}.meaningGrid article{border:1.5px solid var(--ink);border-radius:24px;padding:22px;background:#fff}.meaningGrid article>span{width:38px;height:38px;display:grid;place-items:center;border-radius:50%;background:var(--yellow);border:1.5px solid var(--ink);font-weight:900;margin-bottom:18px}.meaningGrid h3{margin-bottom:8px}.meaningGrid p{margin:0;color:var(--muted)}.meaningLinks{display:flex;gap:12px;flex-wrap:wrap;margin-top:20px}.meaningLinks a{font-weight:850;color:var(--blue)}
@media(max-width:900px){.overviewGrid{grid-template-columns:1fr 1fr}.meaningGrid{grid-template-columns:1fr}.barRow{grid-template-columns:1fr 64px}.barLabel{grid-column:1/-1}.barTrack{min-width:0}}
@media(max-width:600px){.overviewGrid{grid-template-columns:1fr}.barRow{gap:8px}.barTrack{height:16px}}
</style>'''
    data = data.replace('</head>', data_css + '\n</head>', 1)

write('data.html', data)


# -----------------------------------------------------------------------------
# 4) Access preparation: clearer, concrete promise and consistent label.
# -----------------------------------------------------------------------------
awareness = read('awareness.html')
awareness = awareness.replace(
    '<h1>Prepare better access <span>before a Deaf person arrives.</span></h1>',
    '<h1>Prepare Deaf access <span>before the meeting, appointment or event.</span></h1>'
)
awareness = awareness.replace('Prepare better Deaf access before someone arrives.', 'Prepare Deaf access before a meeting, appointment or event.')
write('awareness.html', awareness)


# -----------------------------------------------------------------------------
# 5) Law page: keep the strong simple-answer structure; only ensure the clear
#    information-not-legal-advice wording remains visible.
# -----------------------------------------------------------------------------
law = read('law.html')
if 'Simple guidance, not legal advice.' not in law:
    law = law.replace('</p></div></section>', '</p><p class="updated">Simple guidance, not legal advice.</p></div></section>', 1)
write('law.html', law)


# -----------------------------------------------------------------------------
# 6) Sitemap: add only the four substantial new indexable guides.
# -----------------------------------------------------------------------------
sitemap = read('sitemap.xml')
new_urls = [g['file'] for g in GUIDES]
for filename in new_urls:
    url = f'https://bookbsl.co.uk/{filename}'
    if url not in sitemap:
        entry = f'  <url><loc>{url}</loc><lastmod>{TODAY}</lastmod><changefreq>monthly</changefreq><priority>0.9</priority></url>\n'
        sitemap = sitemap.replace('</urlset>', entry + '</urlset>')
write('sitemap.xml', sitemap)


# -----------------------------------------------------------------------------
# Verification
# -----------------------------------------------------------------------------
index = read('index.html')
assert index.index('how-to-book-bsl-interpreter.html') < index.index('bsl-interpreter-cost.html') < index.index('bsl-interpreter-work-meetings.html')
assert 'Popular guide' in index
assert '<strong>Access preparation</strong>' in index
assert 'Awareness</strong>' not in index

for g in GUIDES:
    text = read(g['file'])
    assert g['headline'] in text
    assert './#checker' in text
    assert 'BookBSL' in text

check_data = read('data.html')
assert 'A specialist workforce at a glance.' in check_data
assert 'What this means for your booking' in check_data
assert 'barFill' in check_data
assert 'id="accessSupplyPressure"' not in check_data

check_awareness = read('awareness.html')
assert 'before the meeting, appointment or event.' in check_awareness

for filename in new_urls:
    assert f'https://bookbsl.co.uk/{filename}' in read('sitemap.xml')

print('BookBSL marketing/content upgrade applied successfully.')
