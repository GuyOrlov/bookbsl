from pathlib import Path

ROOT = Path('.')
MEASUREMENT_ID = 'G-GKTLWHQNQS'

GA4_JS = r'''(() => {
  const ID = 'G-GKTLWHQNQS';
  const KEY = 'bookbsl_ga4_consent';

  function readChoice(){
    try { return localStorage.getItem(KEY) || ''; } catch(e) { return ''; }
  }

  function writeChoice(value){
    try { localStorage.setItem(KEY, value); } catch(e) {}
  }

  function loadAnalytics(){
    if (window.__bookbslGa4Loaded) return;
    window.__bookbslGa4Loaded = true;
    window['ga-disable-' + ID] = false;
    window.dataLayer = window.dataLayer || [];
    window.gtag = window.gtag || function(){ window.dataLayer.push(arguments); };
    window.gtag('js', new Date());
    window.gtag('config', ID, { send_page_view: true });
    const script = document.createElement('script');
    script.async = true;
    script.src = 'https://www.googletagmanager.com/gtag/js?id=' + encodeURIComponent(ID);
    document.head.appendChild(script);
  }

  function stopAnalytics(){
    window['ga-disable-' + ID] = true;
  }

  function updateSettingsStatus(){
    const status = document.getElementById('ga4Status');
    if (!status) return;
    const choice = readChoice();
    status.textContent = choice === 'granted'
      ? 'Google Analytics is ON for this browser.'
      : choice === 'denied'
        ? 'Google Analytics is OFF for this browser.'
        : 'No analytics choice has been saved yet. Google Analytics is OFF until you accept.';
  }

  function removeBanner(){
    const banner = document.getElementById('bookbslAnalyticsBanner');
    if (banner) banner.remove();
  }

  function setChoice(value){
    writeChoice(value);
    if (value === 'granted') loadAnalytics();
    else stopAnalytics();
    updateSettingsStatus();
    removeBanner();
  }

  function bindSettingsPage(){
    const accept = document.getElementById('ga4Accept');
    const decline = document.getElementById('ga4Decline');
    if (accept && !accept.dataset.gaBound) {
      accept.dataset.gaBound = '1';
      accept.addEventListener('click', () => setChoice('granted'));
    }
    if (decline && !decline.dataset.gaBound) {
      decline.dataset.gaBound = '1';
      decline.addEventListener('click', () => setChoice('denied'));
    }
    updateSettingsStatus();
  }

  function showBanner(){
    if (readChoice() || document.getElementById('bookbslAnalyticsBanner')) return;
    const wrap = document.createElement('div');
    wrap.id = 'bookbslAnalyticsBanner';
    wrap.setAttribute('role', 'region');
    wrap.setAttribute('aria-label', 'Analytics choice');
    wrap.innerHTML = `
      <div class="bookbslAnalyticsInner">
        <div class="bookbslAnalyticsText">
          <strong>Help improve BookBSL?</strong>
          <span>We would like to use Google Analytics to understand visits and improve the booking checklist. Analytics is off until you accept.</span>
          <a href="cookies.html#googleAnalytics">Cookie & analytics details</a>
        </div>
        <div class="bookbslAnalyticsActions">
          <button type="button" id="bookbslAnalyticsDecline">Decline</button>
          <button type="button" id="bookbslAnalyticsAccept" class="primary">Accept analytics</button>
        </div>
      </div>`;
    const style = document.createElement('style');
    style.id = 'bookbslAnalyticsStyle';
    style.textContent = `
      #bookbslAnalyticsBanner{position:fixed;z-index:9999;left:16px;right:16px;bottom:16px;background:#fff;color:#142126;border:2px solid #092A35;border-radius:20px;box-shadow:7px 7px 0 #092A35;font-family:Manrope,system-ui,-apple-system,"Segoe UI",sans-serif}
      .bookbslAnalyticsInner{width:min(1120px,100%);margin:auto;padding:18px;display:flex;align-items:center;justify-content:space-between;gap:22px}
      .bookbslAnalyticsText{display:grid;gap:5px;max-width:760px}.bookbslAnalyticsText strong{font-size:1.05rem;color:#092A35}.bookbslAnalyticsText span{font-size:.9rem;line-height:1.45;color:#405159}.bookbslAnalyticsText a{font-size:.86rem;font-weight:800;color:#2456B3;text-underline-offset:3px}
      .bookbslAnalyticsActions{display:flex;gap:9px;flex:0 0 auto}.bookbslAnalyticsActions button{min-height:44px;padding:9px 15px;border:2px solid #092A35;border-radius:999px;background:#fff;color:#092A35;font:inherit;font-weight:850;cursor:pointer}.bookbslAnalyticsActions button.primary{background:#FFD84D}.bookbslAnalyticsActions button:focus-visible{outline:3px solid #2456B3;outline-offset:3px}
      @media(max-width:700px){#bookbslAnalyticsBanner{left:10px;right:10px;bottom:10px}.bookbslAnalyticsInner{display:grid;padding:15px}.bookbslAnalyticsActions{display:grid;grid-template-columns:1fr 1fr}.bookbslAnalyticsActions button{width:100%}}
    `;
    document.head.appendChild(style);
    document.body.appendChild(wrap);
    document.getElementById('bookbslAnalyticsAccept').addEventListener('click', () => setChoice('granted'));
    document.getElementById('bookbslAnalyticsDecline').addEventListener('click', () => setChoice('denied'));
  }

  window.BookBSLAnalyticsConsent = {
    grant: () => setChoice('granted'),
    deny: () => setChoice('denied'),
    status: readChoice
  };

  if (readChoice() === 'granted') loadAnalytics();
  else stopAnalytics();

  const ready = () => {
    bindSettingsPage();
    if (!readChoice()) showBanner();
  };
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', ready, { once:true });
  else ready();
})();
'''

(ROOT / 'ga4-consent.js').write_text(GA4_JS, encoding='utf-8')

for page in ROOT.glob('*.html'):
    if page.name == 'stats.html':
        continue
    text = page.read_text(encoding='utf-8')
    if 'src="ga4-consent.js"' not in text:
        text = text.replace('</head>', '<script src="ga4-consent.js"></script>\n</head>', 1)
    page.write_text(text, encoding='utf-8')

cookies = ROOT / 'cookies.html'
if cookies.exists():
    text = cookies.read_text(encoding='utf-8')
    if 'id="googleAnalytics"' not in text:
        block = '''<div class="card" id="googleAnalytics"><h2>Google Analytics 4 (optional)</h2><p>BookBSL uses Google Analytics 4 only if you choose to accept analytics. It helps us understand which pages are visited, how visitors arrive at the site, device and browser information, and interactions such as starting or completing the checklist and clicking to request a quote.</p><p>Google Analytics is <strong>off by default</strong> until you accept. We do not send your checklist answers, names, email addresses or booking notes to Google Analytics as event details.</p><p>The BookBSL Google Analytics measurement ID is <code>G-GKTLWHQNQS</code>. You can change your choice for this browser below at any time.</p></div>
<div class="choice"><h2>Your Google Analytics choice</h2><p>Choose whether BookBSL may load Google Analytics in this browser.</p><div class="choiceBtns"><button class="btn dark" type="button" id="ga4Accept">Accept analytics</button><button class="btn" type="button" id="ga4Decline">Decline analytics</button></div><p class="status" id="ga4Status" aria-live="polite"></p></div>
'''
        marker = '<div class="card"><h2>Third-party and browser controls</h2>'
        if marker in text:
            text = text.replace(marker, block + marker, 1)
        else:
            text = text.replace('<div class="legalLinks">', block + '<div class="legalLinks">', 1)
    text = text.replace('This page explains the browser storage and aggregate usage counters used by BookBSL, and gives you a simple way to object to the usage statistics.', 'This page explains BookBSL browser storage, aggregate usage counters and optional Google Analytics, with controls for your analytics choices.')
    cookies.write_text(text, encoding='utf-8')

privacy = ROOT / 'privacy.html'
if privacy.exists():
    text = privacy.read_text(encoding='utf-8')
    if '<h2>Google Analytics</h2>' not in text:
        block = '''<div class="card"><h2>Google Analytics</h2><p>If you consent, BookBSL uses Google Analytics 4 to understand page views, traffic sources, device and browser information, and interactions such as checklist starts, checklist completions and quote clicks. Google Analytics is not loaded until you accept analytics.</p><p>BookBSL does not send checklist answers, booking notes, names or email addresses to Google Analytics as analytics event details. Your analytics choice is stored in this browser so the site can remember it.</p><p>You can change your analytics choice at any time on the <a href="cookies.html#googleAnalytics">Cookies &amp; usage statistics page</a>.</p></div>
'''
        marker = '<div class="card"><h2>Your rights</h2>'
        if marker in text:
            text = text.replace(marker, block + marker, 1)
        else:
            text = text.replace('<div class="legalLinks">', block + '<div class="legalLinks">', 1)
    privacy.write_text(text, encoding='utf-8')
