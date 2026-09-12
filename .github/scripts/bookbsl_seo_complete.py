from pathlib import Path
import re

ROOT = Path(".")
OG = "https://bookbsl.co.uk/og-image.png"
FAV = "https://bookbsl.co.uk/favicon.png"
APPLE = "https://bookbsl.co.uk/apple-touch-icon.png"

existing_pages = ["index.html","awareness.html","data.html","law.html","privacy.html","terms.html","cookies.html"]

def add_asset_meta(text):
    if 'rel="icon"' not in text:
        marker = '<meta name="theme-color"'
        pos = text.find(marker)
        if pos != -1:
            end = text.find(">", pos) + 1
            block = f'\n<link rel="icon" type="image/png" href="{FAV}">\n<link rel="apple-touch-icon" href="{APPLE}">'
            text = text[:end] + block + text[end:]
    if 'property="og:image"' not in text:
        marker = '<meta property="og:type"'
        pos = text.find(marker)
        if pos != -1:
            end = text.find(">", pos) + 1
            block = f'\n<meta property="og:image" content="{OG}">\n<meta property="og:image:width" content="600">\n<meta property="og:image:height" content="315">'
            text = text[:end] + block + text[end:]
    if 'name="twitter:image"' not in text:
        marker = '<meta name="twitter:card"'
        pos = text.find(marker)
        if pos != -1:
            end = text.find(">", pos) + 1
            text = text[:end] + f'\n<meta name="twitter:image" content="{OG}">' + text[end:]
        else:
            marker = '<link rel="canonical"'
            pos = text.find(marker)
            if pos != -1:
                text = text[:pos] + f'<meta name="twitter:card" content="summary_large_image">\n<meta name="twitter:image" content="{OG}">\n' + text[pos:]
    if 'src="page-analytics.js"' not in text:
        text = text.replace("</body>", '<script src="page-analytics.js" defer></script>\n</body>')
    return text

for name in existing_pages:
    p = ROOT / name
    if p.exists():
        text = p.read_text(encoding="utf-8")
        text = add_asset_meta(text)
        if name in {"privacy.html","terms.html","cookies.html"}:
            if 'name="robots"' in text:
                text = re.sub(r'<meta name="robots"[^>]*>', '<meta name="robots" content="noindex,follow">', text, count=1)
            else:
                text = text.replace('<meta name="theme-color"', '<meta name="robots" content="noindex,follow">\n<meta name="theme-color"', 1)
        p.write_text(text, encoding="utf-8")

guides = [
    {
        "file":"bsl-interpreter-events.html",
        "title":"BSL Interpreter for Events UK | Booking Guide | BookBSL",
        "desc":"Plan a BSL interpreter booking for conferences, exhibitions, festivals and public events in the UK. Check timings, access, breaks, livestreams and booking details.",
        "h1":"Booking a BSL interpreter for events",
        "kicker":"Events, conferences & exhibitions",
        "intro":"Events can move quickly, so interpreters need clear information before the day. Use this guide to prepare a stronger British Sign Language interpreter enquiry for conferences, exhibitions, festivals, ceremonies and public events.",
        "sections":[
            ("What to include in the booking","Give the date, venue, start and finish times, audience size, expected Deaf attendees, event format and a named contact. Add the running order, speaker list and presentation materials when available."),
            ("When two interpreters may be needed","Long, intensive or continuous assignments can require a team of interpreters so they can alternate and maintain quality. The exact arrangement depends on duration, complexity and working conditions."),
            ("Stage, lighting and sightlines","Keep the interpreter visible to Deaf attendees. Think about lighting, stage position, seating, screens and any camera or livestream setup before the event starts."),
            ("Livestreams and recording","Say clearly if the interpreter will appear on camera, be recorded, streamed or used in promotional content. This should be discussed as part of the booking rather than assumed.")
        ]
    },
    {
        "file":"bsl-interpreter-work-meetings.html",
        "title":"BSL Interpreter for Work & Meetings UK | BookBSL",
        "desc":"Prepare a BSL interpreter booking for workplace meetings, interviews, training and business events. Use BookBSL to check the information interpreters need.",
        "h1":"Booking a BSL interpreter for work and meetings",
        "kicker":"Workplaces, interviews & training",
        "intro":"A clear workplace booking helps everyone prepare. This guide covers meetings, interviews, training, presentations and other professional situations involving British Sign Language.",
        "sections":[
            ("Share the purpose of the meeting","Explain what the meeting is for, who will attend and whether it is a one-to-one conversation, interview, team meeting, training session or presentation."),
            ("Provide documents early","Agendas, slides, technical terms, names and background documents help interpreters prepare. Send relevant material as early as reasonably possible."),
            ("Online, hybrid or in person","State the format clearly. For hybrid meetings, explain which platform is being used, where the Deaf participant will be and how the interpreter will be seen on screen."),
            ("Access to Work","Some workplace interpreting can be supported through Access to Work. Funding arrangements and booking responsibility should be confirmed before the assignment.")
        ]
    },
    {
        "file":"online-bsl-interpreter.html",
        "title":"Online BSL Interpreter UK | Remote BSL Booking Guide | BookBSL",
        "desc":"Book and prepare for an online BSL interpreter in the UK. Guidance for Zoom, Teams, remote meetings, camera setup, links, access and clear communication.",
        "h1":"Booking an online BSL interpreter",
        "kicker":"Remote BSL interpreting",
        "intro":"Online interpreting can work well when the platform, camera and meeting access are prepared properly. Use this guide for Zoom, Microsoft Teams and other remote meetings.",
        "sections":[
            ("Send the meeting link","Give the interpreter the correct platform, joining link, passcode if required, start time and a contact person in case there is a technical problem."),
            ("Make the interpreter easy to see","Participants should know how to pin or spotlight the interpreter. Avoid layouts where the interpreter becomes a very small video tile."),
            ("Check cameras and lighting","The Deaf participant and interpreter need a clear view of each other. Use stable cameras, good lighting and enough bandwidth for smooth video."),
            ("Allow for preparation","Share the agenda, names, slides and specialist vocabulary before the session just as you would for an in-person booking.")
        ]
    },
    {
        "file":"bsl-interpreter-cost.html",
        "title":"How Much Does a BSL Interpreter Cost in the UK? | BookBSL",
        "desc":"Understand what can affect BSL interpreter costs in the UK, including duration, travel, preparation, evening work, remote bookings and interpreter teams.",
        "h1":"How much does a BSL interpreter cost?",
        "kicker":"Understanding BSL interpreter pricing",
        "intro":"There is no single UK price for every British Sign Language interpreting assignment. Cost depends on the booking itself, the interpreter, location, timing and what preparation is required.",
        "sections":[
            ("What affects the price","Common factors include the length of the assignment, location, travel, time of day, preparation, specialist subject matter and whether the work is online or in person."),
            ("Minimum booking periods","Some interpreters or agencies use minimum booking periods even when the meeting itself is short. Ask what is included before confirming."),
            ("When two interpreters affect cost","Long or demanding assignments may require two interpreters. That usually means paying for both professionals, but it can be necessary for safe and effective communication."),
            ("Ask for a clear quote","Provide complete information and ask what the quote includes: interpreting time, travel, preparation, expenses, cancellation terms and any additional charges.")
        ]
    },
    {
        "file":"how-to-book-bsl-interpreter.html",
        "title":"How to Book a BSL Interpreter in the UK | BookBSL",
        "desc":"Step-by-step guide to booking a British Sign Language interpreter in the UK. Prepare the date, time, location, purpose, access details and supporting information.",
        "h1":"How to book a BSL interpreter in the UK",
        "kicker":"Step-by-step booking guide",
        "intro":"A strong BSL interpreter enquiry is specific, easy to understand and gives enough information for the interpreter or agency to assess the assignment quickly.",
        "sections":[
            ("1. Confirm the basics","Start with the date, exact start and finish time, location or online platform, and a contact name."),
            ("2. Explain the purpose","Say what the interpreter is being booked for and who will be involved. A short description makes a big difference."),
            ("3. Share access and preparation information","Include agendas, presentations, specialist terms, travel information, parking, room layout, livestream details or anything else relevant."),
            ("4. Confirm the booking","Ask for confirmation of availability, rate, cancellation terms and any additional requirements. Keep the final booking details in one clear message.")
        ]
    },
    {
        "file":"bsl-interpreter-healthcare.html",
        "title":"BSL Interpreter for Healthcare Appointments UK | BookBSL",
        "desc":"Guidance for arranging a BSL interpreter for healthcare appointments in the UK, including communication preferences, appointment details, privacy and preparation.",
        "h1":"Arranging BSL interpreting for healthcare",
        "kicker":"Healthcare communication access",
        "intro":"Healthcare communication must be clear and accessible. When arranging interpreting, confirm the Deaf person's communication preference and give the interpreter enough practical information to attend the appointment.",
        "sections":[
            ("Ask the Deaf person what they need","Do not assume one communication method suits everyone. Confirm whether British Sign Language interpreting or another form of communication support is requested."),
            ("Give accurate appointment information","Provide the date, arrival time, expected duration, hospital or clinic location, department and a contact number."),
            ("Protect privacy","Only share information necessary for the interpreter to prepare and deliver the assignment. Follow the organisation's normal information-governance procedures."),
            ("Plan for longer appointments","Complex consultations, procedures or multiple appointments can require additional time or more than one interpreter. Discuss the likely format before confirming.")
        ]
    },
    {
        "file":"bsl-interpreter-education.html",
        "title":"BSL Interpreter for Education & Training UK | BookBSL",
        "desc":"Prepare BSL interpreter bookings for education, colleges, universities, training and learning events. Guidance on timetables, materials, terminology and access.",
        "h1":"Booking BSL interpreting for education and training",
        "kicker":"Schools, colleges, universities & courses",
        "intro":"Education bookings can involve specialist vocabulary, long sessions and changing timetables. Good preparation helps interpreters support communication effectively.",
        "sections":[
            ("Share the timetable","Give exact session times, breaks, room changes and the overall duration. For recurring courses, provide all known dates."),
            ("Send learning materials","Slides, lesson plans, reading material, technical terms and names help interpreters prepare for the subject."),
            ("Think about session length","Long teaching days or intensive sessions may require more than one interpreter. Build interpreter breaks into the timetable."),
            ("Keep changes communicated","If a room, lecturer, topic or timetable changes, update the interpreter or agency as soon as possible.")
        ]
    },
]

guide_links = "".join(
    f'<a class="guideCard" href="{g["file"]}"><strong>{g["h1"]}</strong><span>{g["kicker"]}</span></a>'
    for g in guides
)

guide_section = f'''
<section class="section paper" id="guides">
  <div class="shell">
    <div class="eyebrow">BSL booking guides</div>
    <h2>Practical guides for common BSL interpreter bookings.</h2>
    <p class="lead">Use these guides to prepare the right information before you contact an interpreter or request a quote.</p>
    <div class="guideGrid">{guide_links}</div>
  </div>
</section>
<style>
.guideGrid{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px;margin-top:24px}}
.guideCard{{display:flex;flex-direction:column;gap:7px;text-decoration:none;background:#fff;border:1.5px solid var(--ink);border-radius:22px;padding:20px;box-shadow:4px 4px 0 var(--yellow)}}
.guideCard strong{{color:var(--ink);font-size:1rem}}.guideCard span{{color:var(--muted);font-size:.86rem}}
@media(max-width:720px){{.guideGrid{{grid-template-columns:1fr}}}}
</style>
'''

ip = ROOT / "index.html"
if ip.exists():
    index = ip.read_text(encoding="utf-8")
    if 'id="guides"' not in index:
        index = index.replace("</main>", guide_section + "\n</main>")
    if 'href="#guides"' not in index:
        index = index.replace('<a href="#support">Support</a>', '<a href="#guides">Guides</a><a href="#support">Support</a>', 1)
    ip.write_text(index, encoding="utf-8")

shared_css = '''
:root{--ink:#092A35;--soft:#F4F7F5;--paper:#fff;--yellow:#FFD84D;--blue:#2456B3;--text:#142126;--muted:#596970;--line:#C8D3D6}
*{box-sizing:border-box}body{margin:0;font-family:Manrope,Arial,sans-serif;background:var(--soft);color:var(--text);line-height:1.65}
a{color:var(--blue)}.shell{width:min(980px,calc(100% - 32px));margin:auto}.top{background:var(--paper);border-bottom:1px solid var(--line)}
.topin{min-height:68px;display:flex;align-items:center;justify-content:space-between;gap:18px}.brand{text-decoration:none;font-weight:900;color:var(--ink);font-size:1.2rem}
.topnav{display:flex;gap:15px;flex-wrap:wrap}.topnav a{text-decoration:none;font-weight:800;color:var(--ink);font-size:.9rem}
.hero{padding:70px 0 45px}.kicker{display:inline-flex;background:var(--yellow);border:1.5px solid var(--ink);border-radius:999px;padding:6px 11px;font-weight:900;font-size:.8rem}
h1{font-size:clamp(2.6rem,7vw,5rem);line-height:.98;letter-spacing:-.05em;color:var(--ink);max-width:850px;margin:18px 0}
.lead{font-size:1.15rem;color:var(--muted);max-width:780px}.content{background:#fff;border-block:1px solid var(--line);padding:55px 0}
.card{border:1.5px solid var(--ink);border-radius:24px;padding:23px;margin:0 0 16px;background:#fff}.card h2{margin-top:0;color:var(--ink)}
.cta{margin:40px 0;padding:28px;border:2px solid var(--ink);border-radius:26px;background:var(--yellow)}
.btn{display:inline-block;text-decoration:none;background:var(--ink);color:#fff;padding:12px 18px;border-radius:999px;font-weight:900;margin-top:10px}
.related{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px}.related a{background:#fff;border:1px solid var(--line);border-radius:16px;padding:13px;text-decoration:none;font-weight:800}
footer{padding:30px 0;color:var(--muted);font-size:.9rem}@media(max-width:680px){.topin{align-items:flex-start;flex-direction:column;padding:14px 0}.related{grid-template-columns:1fr}}
'''

def page_html(g):
    cards = "\n".join(f'<section class="card"><h2>{h}</h2><p>{p}</p></section>' for h,p in g["sections"])
    rel = "".join(f'<a href="{x["file"]}">{x["h1"]}</a>' for x in guides if x["file"] != g["file"])
    url = "https://bookbsl.co.uk/" + g["file"]
    schema = (
        '{"@context":"https://schema.org","@type":"Article","headline":'
        + repr(g["h1"]).replace("'", '"')
        + ',"description":'
        + repr(g["desc"]).replace("'", '"')
        + ',"mainEntityOfPage":"'
        + url
        + '","publisher":{"@type":"Organization","name":"BookBSL by cSeeker Ltd","url":"https://bookbsl.co.uk/"}}'
    )
    return f'''<!doctype html>
<html lang="en-GB"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{g["title"]}</title>
<meta name="description" content="{g["desc"]}">
<meta name="robots" content="index,follow,max-image-preview:large">
<link rel="canonical" href="{url}">
<link rel="icon" type="image/png" href="{FAV}"><link rel="apple-touch-icon" href="{APPLE}">
<meta property="og:title" content="{g["title"]}"><meta property="og:description" content="{g["desc"]}">
<meta property="og:type" content="article"><meta property="og:url" content="{url}">
<meta property="og:image" content="{OG}"><meta property="og:image:width" content="600"><meta property="og:image:height" content="315">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:image" content="{OG}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;600;700;800&display=swap" rel="stylesheet">
<script type="application/ld+json">{schema}</script><style>{shared_css}</style></head>
<body><header class="top"><div class="shell topin"><a class="brand" href="./">BookBSL</a><nav class="topnav" aria-label="Main navigation"><a href="./#checker">Start checklist</a><a href="awareness.html">Awareness</a><a href="data.html">Data</a><a href="law.html">Laws</a></nav></div></header>
<main><section class="hero"><div class="shell"><span class="kicker">{g["kicker"]}</span><h1>{g["h1"]}</h1><p class="lead">{g["intro"]}</p></div></section>
<section class="content"><div class="shell">{cards}
<div class="cta"><h2>Check your booking before you send it</h2><p>Use BookBSL's free checklist to spot missing details and prepare a clearer interpreter enquiry.</p><a class="btn" href="./#checker">Start the free 2-minute checklist</a></div>
<h2>More BookBSL guides</h2><div class="related">{rel}</div></div></section></main>
<footer><div class="shell">BookBSL by cSeeker Ltd · <a href="privacy.html">Privacy</a> · <a href="terms.html">Terms</a> · <a href="cookies.html">Cookies</a></div></footer>
<script src="page-analytics.js" defer></script></body></html>'''

for g in guides:
    (ROOT/g["file"]).write_text(page_html(g), encoding="utf-8")

analytics_js = r'''(()=>{try{
  if(localStorage.getItem('bookbsl_stats_optout')==='1')return;
  const path=(location.pathname.replace(/^\/|\/$/g,'')||'home').replace(/[^a-z0-9]+/gi,'-').toLowerCase();
  const once='bookbsl-pageview-'+path;
  if(sessionStorage.getItem(once))return;
  sessionStorage.setItem(once,'1');
  fetch('https://countapi.mileshilliard.com/api/v1/hit/bookbsl-guyorlov-page-'+path,{mode:'cors'}).catch(()=>{});
}catch(e){}})();'''
(ROOT/"page-analytics.js").write_text(analytics_js, encoding="utf-8")

rows = [("Home","home")] + [(g["h1"], g["file"].replace(".html","-html")) for g in guides] + [
    ("Deaf awareness","awareness-html"),("Data & evidence","data-html"),("BSL laws","law-html")
]
row_html = "".join(f'<tr><td>{label}</td><td id="p-{slug}">—</td></tr>' for label,slug in rows)
keys_js = ",".join(f'["{label}","{slug}"]' for label,slug in rows)
stats_html = f'''<!doctype html><html lang="en-GB"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow"><title>BookBSL site statistics</title><style>{shared_css}table{{width:100%;border-collapse:collapse;background:white}}th,td{{padding:12px;border-bottom:1px solid #ddd;text-align:left}}</style></head>
<body><main class="shell" style="padding:40px 0"><h1 style="font-size:2.4rem">BookBSL site statistics</h1><p>Session-based page popularity counters plus the main booking funnel counters. Search Console remains the source for Google impressions and clicks.</p>
<h2>Pages</h2><table><thead><tr><th>Page</th><th>Sessions counted</th></tr></thead><tbody>{row_html}</tbody></table>
<h2 style="margin-top:35px">Booking funnel</h2><table><tbody><tr><td>Homepage visits</td><td id="f-visits">—</td></tr><tr><td>Checklist starts</td><td id="f-starts">—</td></tr><tr><td>Checklist finishes</td><td id="f-finishes">—</td></tr><tr><td>Quote clicks</td><td id="f-quotes">—</td></tr></tbody></table></main>
<script>
const API='https://countapi.mileshilliard.com/api/v1/get/';
async function get(k){{try{{const r=await fetch(API+k);if(!r.ok)return 0;const j=await r.json();return Number(j.value??j.count??0)}}catch{{return 0}}}}
const pages=[{keys_js}];
pages.forEach(async ([label,slug])=>document.getElementById('p-'+slug).textContent=(await get('bookbsl-guyorlov-page-'+slug)).toLocaleString('en-GB'));
[['visits','bookbsl-guyorlov-202609-visits'],['starts','bookbsl-guyorlov-202609-starts'],['finishes','bookbsl-guyorlov-202609-finishes'],['quotes','bookbsl-guyorlov-202609-quotes']].forEach(async ([id,k])=>document.getElementById('f-'+id).textContent=(await get(k)).toLocaleString('en-GB'));
</script></body></html>'''
(ROOT/"stats.html").write_text(stats_html, encoding="utf-8")

urls = [
    ("https://bookbsl.co.uk/","1.0","weekly"),
    ("https://bookbsl.co.uk/awareness.html","0.9","monthly"),
    ("https://bookbsl.co.uk/data.html","0.8","monthly"),
    ("https://bookbsl.co.uk/law.html","0.8","monthly"),
] + [(f"https://bookbsl.co.uk/{g['file']}","0.9","monthly") for g in guides]
xml = ['<?xml version="1.0" encoding="UTF-8"?>','<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for url,pri,freq in urls:
    xml.append(f'  <url><loc>{url}</loc><lastmod>2026-09-12</lastmod><changefreq>{freq}</changefreq><priority>{pri}</priority></url>')
xml.append('</urlset>')
(ROOT/"sitemap.xml").write_text("\n".join(xml)+"\n", encoding="utf-8")
