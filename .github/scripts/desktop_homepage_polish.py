from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
path = ROOT / "index.html"
text = path.read_text(encoding="utf-8")

STYLE_ID = "bookbsl-desktop-home-polish-20260912"
STYLE = f'''<style id="{STYLE_ID}">
/* Desktop-only polish: tighter nav, clearer CTAs, more space around the booking card */
@media (min-width:901px){{
  html body .top .topin{{
    min-height:68px!important;
    display:flex!important;
    align-items:center!important;
    justify-content:space-between!important;
    gap:28px!important;
    flex-wrap:nowrap!important;
  }}
  html body .top .topnav{{
    margin-left:auto!important;
    width:auto!important;
    display:flex!important;
    align-items:center!important;
    justify-content:flex-end!important;
    gap:6px!important;
    flex-wrap:nowrap!important;
  }}
  html body .top .topnav>a:not(.header-cta){{
    display:inline-flex!important;
    align-items:center!important;
    justify-content:center!important;
    min-height:40px!important;
    padding:0 12px!important;
    border-radius:999px!important;
    font-size:.88rem!important;
    font-weight:750!important;
  }}
  html body .top .topnav>a:not(.header-cta):hover{{
    background:#fff!important;
  }}
  html body .top .topnav .header-cta{{
    min-width:auto!important;
    min-height:42px!important;
    height:42px!important;
    margin-left:10px!important;
    padding:0 20px!important;
    font-size:.88rem!important;
    font-weight:800!important;
  }}

  html body .hero .shell.heroGrid{{
    grid-template-columns:minmax(0,1fr) 500px!important;
    gap:86px!important;
    align-items:center!important;
  }}
  html body .hero .heroCard.heroStart{{
    width:500px!important;
    max-width:500px!important;
    justify-self:end!important;
    transform:translateX(32px)!important;
  }}
  html body .hero .actions{{
    display:grid!important;
    grid-template-columns:1fr!important;
    gap:10px!important;
    width:500px!important;
    max-width:100%!important;
    margin-top:22px!important;
  }}
  html body .hero .actions .btn{{
    width:100%!important;
    min-height:50px!important;
    justify-content:center!important;
    text-align:center!important;
  }}
  html body .hero .actions .btn.primary{{
    box-shadow:4px 4px 0 var(--ink,#092A35)!important;
  }}
  html body .hero .actions .btn:not(.primary){{
    box-shadow:none!important;
  }}
  html body .hero .micro{{
    max-width:500px!important;
  }}
}}

@media (min-width:901px) and (max-width:1200px){{
  html body .hero .shell.heroGrid{{
    grid-template-columns:minmax(0,1fr) 460px!important;
    gap:54px!important;
  }}
  html body .hero .heroCard.heroStart{{
    width:460px!important;
    max-width:460px!important;
    transform:translateX(12px)!important;
  }}
  html body .hero .actions{{width:470px!important}}
}}
</style>'''

pattern = re.compile(rf'<style id="{re.escape(STYLE_ID)}">.*?</style>', re.S)
if pattern.search(text):
    text = pattern.sub(STYLE, text, count=1)
else:
    text = text.replace("</head>", STYLE + "\n</head>", 1)

# Force browsers to fetch the current navigation script instead of a cached copy.
text = re.sub(r'<script src="ga4-consent\.js(?:\?v=[^"]*)?"></script>',
              '<script src="ga4-consent.js?v=20260912-3"></script>', text, count=1)

path.write_text(text, encoding="utf-8")
print("Applied desktop homepage polish to index.html")
