(() => {
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

  function installMobileNavStyles(){
    if (document.getElementById('bookbslMobileNavStyle')) return;
    const style = document.createElement('style');
    style.id = 'bookbslMobileNavStyle';
    style.textContent = `
      .bookbslMenuToggle{display:none}
      .bookbslMobilePanel{display:contents}

      @media(min-width:901px){
        .top .topin{
          display:flex!important;
          align-items:center!important;
          justify-content:space-between!important;
          gap:28px!important;
        }
        .top .topnav{
          margin-left:auto!important;
          display:flex!important;
          align-items:center!important;
          justify-content:flex-end!important;
          gap:4px!important;
          flex-wrap:nowrap!important;
        }
        .top .topnav>a:not(.header-cta){
          display:inline-flex!important;
          align-items:center!important;
          justify-content:center!important;
          min-height:42px!important;
          padding:0 12px!important;
          border-radius:999px!important;
        }
        .top .topnav>a:not(.header-cta):hover{
          background:#fff!important;
        }
        .top .topnav .header-cta{
          min-width:auto!important;
          margin-left:8px!important;
          padding:0 18px!important;
        }
        .hero .heroGrid{
          grid-template-columns:minmax(0,1.10fr) minmax(430px,.78fr)!important;
          gap:64px!important;
        }
        .hero .heroStart{
          justify-self:end!important;
          width:min(500px,100%)!important;
          transform:translateX(14px);
        }
        .hero .actions{
          display:grid!important;
          grid-template-columns:1fr!important;
          gap:10px!important;
          max-width:500px!important;
        }
        .hero .actions .btn{
          width:100%!important;
          min-height:50px!important;
          justify-content:center!important;
        }
      }
      @media(min-width:901px) and (max-width:1200px){
        .hero .heroGrid{
          grid-template-columns:minmax(0,1fr) minmax(410px,.82fr)!important;
          gap:46px!important;
        }
        .hero .heroStart{transform:none!important}
      }

      @media(max-width:680px){
        .top{overflow:visible!important}
        .top .topin{
          height:70px!important;
          min-height:70px!important;
          position:relative!important;
          display:grid!important;
          grid-template-columns:minmax(0,1fr) auto!important;
          align-items:center!important;
          column-gap:12px!important;
          row-gap:0!important;
          flex-wrap:nowrap!important;
        }
        .top .brand{
          grid-column:1!important;
          min-width:0!important;
          width:auto!important;
          margin:0!important;
          display:flex!important;
          align-items:center!important;
          flex:0 1 auto!important;
          font-size:1.05rem!important;
          gap:8px!important;
          white-space:nowrap!important;
        }
        .top .brandmark{width:38px!important;height:38px!important;flex:0 0 38px!important;font-size:.74rem!important}
        .top .brandSub{display:none!important}
        .top .topnav{
          grid-column:2!important;
          justify-self:end!important;
          align-self:center!important;
          width:auto!important;
          max-width:max-content!important;
          min-width:0!important;
          margin:0!important;
          padding:0!important;
          display:flex!important;
          align-items:center!important;
          justify-content:flex-end!important;
          gap:0!important;
          flex:0 0 auto!important;
          position:static!important;
        }
        .top .bookbslMenuToggle{
          display:inline-flex!important;
          width:auto!important;
          max-width:max-content!important;
          margin:0!important;
          align-items:center!important;
          justify-content:center!important;
          gap:8px!important;
          min-height:42px!important;
          padding:8px 14px!important;
          border:2px solid #092A35!important;
          border-radius:999px!important;
          background:#fff!important;
          color:#092A35!important;
          font:inherit!important;
          font-size:.84rem!important;
          font-weight:800!important;
          line-height:1!important;
          white-space:nowrap!important;
          cursor:pointer!important;
        }
        .top .bookbslMenuToggle[aria-expanded="true"]{background:#FFD84D!important}
        .top .bookbslMenuToggle:focus-visible{outline:3px solid #2456B3!important;outline-offset:3px!important}
        .bookbslMenuIcon{width:17px;height:14px;display:grid;align-content:space-between;flex:0 0 17px}
        .bookbslMenuIcon span{display:block;height:2px;border-radius:999px;background:currentColor}
        .bookbslMobilePanel{display:none!important;position:absolute!important;z-index:80!important;top:calc(100% + 7px)!important;left:0!important;right:0!important;padding:10px!important;background:#fff!important;border:2px solid #092A35!important;border-radius:18px!important;box-shadow:6px 6px 0 #092A35!important}
        .topnav.is-open .bookbslMobilePanel{display:grid!important;gap:4px!important}
        .bookbslMobilePanel>a{display:flex!important;align-items:center!important;justify-content:flex-start!important;width:100%!important;min-height:46px!important;padding:10px 12px!important;border:0!important;border-radius:12px!important;background:transparent!important;color:#092A35!important;text-decoration:none!important;font-size:.94rem!important;font-weight:750!important;line-height:1.2!important;white-space:normal!important;box-shadow:none!important}
        .bookbslMobilePanel>a:hover,.bookbslMobilePanel>a:focus-visible{background:#DDF4EC!important}
        .bookbslMobilePanel>a[aria-current="page"],.bookbslMobilePanel>a.active{background:#EDF3FF!important;color:#2456B3!important}
        .bookbslMobilePanel .btn,.bookbslMobilePanel .header-cta,.bookbslMobilePanel .navCta{display:flex!important;width:100%!important;min-width:0!important;height:auto!important;min-height:46px!important;padding:10px 12px!important;border:0!important;border-radius:12px!important;background:#092A35!important;color:#fff!important}
      }
    `;
    document.head.appendChild(style);
  }

  function installMobileNavigation(){
    const topin = document.querySelector('.topin');
    const nav = topin && topin.querySelector('.topnav');
    if (!topin || !nav || nav.querySelector('.bookbslMenuToggle')) return;

    const children = Array.from(nav.children);
    if (!children.length) return;

    const panel = document.createElement('div');
    panel.className = 'bookbslMobilePanel';
    panel.id = 'bookbslMobileNav';
    children.forEach(child => panel.appendChild(child));

    const toggle = document.createElement('button');
    toggle.type = 'button';
    toggle.className = 'bookbslMenuToggle';
    toggle.setAttribute('aria-expanded', 'false');
    toggle.setAttribute('aria-controls', panel.id);
    toggle.setAttribute('aria-label', 'Open site menu');
    toggle.innerHTML = '<span class="bookbslMenuIcon" aria-hidden="true"><span></span><span></span><span></span></span><span class="bookbslMenuText">Menu</span>';

    nav.appendChild(toggle);
    nav.appendChild(panel);

    const closeMenu = () => {
      nav.classList.remove('is-open');
      toggle.setAttribute('aria-expanded', 'false');
      toggle.setAttribute('aria-label', 'Open site menu');
      const label = toggle.querySelector('.bookbslMenuText');
      if (label) label.textContent = 'Menu';
    };

    const openMenu = () => {
      nav.classList.add('is-open');
      toggle.setAttribute('aria-expanded', 'true');
      toggle.setAttribute('aria-label', 'Close site menu');
      const label = toggle.querySelector('.bookbslMenuText');
      if (label) label.textContent = 'Close';
    };

    toggle.addEventListener('click', () => {
      if (toggle.getAttribute('aria-expanded') === 'true') closeMenu();
      else openMenu();
    });

    panel.addEventListener('click', event => {
      if (event.target.closest('a')) closeMenu();
    });

    document.addEventListener('click', event => {
      if (!nav.contains(event.target)) closeMenu();
    });

    document.addEventListener('keydown', event => {
      if (event.key === 'Escape' && toggle.getAttribute('aria-expanded') === 'true') {
        closeMenu();
        toggle.focus();
      }
    });

    window.addEventListener('resize', () => {
      if (window.innerWidth > 680) closeMenu();
    }, { passive:true });
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

  installMobileNavStyles();

  if (readChoice() === 'granted') loadAnalytics();
  else stopAnalytics();

  const ready = () => {
    installMobileNavigation();
    bindSettingsPage();
    if (!readChoice()) showBanner();
  };
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', ready, { once:true });
  else ready();
})();
