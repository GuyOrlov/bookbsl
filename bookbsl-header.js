(() => {
  function installBookBSLNavigation(){
    const header = document.querySelector('.top');
    const topin = header && header.querySelector('.topin');
    const nav = topin && topin.querySelector('.topnav');
    if (!header || !topin || !nav || nav.querySelector('.bookbslMenuToggle')) return;

    const brandSub = topin.querySelector('.brandSub');
    if (brandSub) brandSub.textContent = 'A cSeeker service';

    // Keep the main information architecture consistent across every page.
    // Older page headers may not yet include Data and Laws, so add them once here.
    const existingLinks = () => Array.from(nav.querySelectorAll('a'));
    const findByHref = suffix => existingLinks().find(a => (a.getAttribute('href') || '').endsWith(suffix));

    const dataLink = findByHref('data.html');
    const pricingLinkExisting = findByHref('bsl-interpreter-cost.html');
    if (dataLink && !pricingLinkExisting && dataLink.textContent.trim().toLowerCase() === 'data') {
      // Leave an intentional Data link alone; pricing is added separately below when missing.
    }

    const headerCtaBeforeInsert = nav.querySelector('.header-cta');
    const insertBeforeCta = (href, label) => {
      if (findByHref(href)) return;
      const a = document.createElement('a');
      a.href = href;
      a.textContent = label;
      if (headerCtaBeforeInsert) nav.insertBefore(a, headerCtaBeforeInsert);
      else nav.appendChild(a);
    };

    insertBeforeCta('data.html', 'Data');
    insertBeforeCta('law.html', 'Laws');

    const headerCta = nav.querySelector('.header-cta');
    if (headerCta) {
      const desktopText = headerCta.querySelector('.desktopCtaText');
      const mobileText = headerCta.querySelector('.mobileCtaText');
      if (desktopText) desktopText.textContent = 'Start booking';
      if (mobileText) mobileText.textContent = 'Start booking';
    }

    const pricingLink = findByHref('bsl-interpreter-cost.html');
    if (pricingLink && /\/bsl-interpreter-cost\.html$/.test(window.location.pathname)) {
      pricingLink.setAttribute('aria-current', 'page');
    }
    const currentMap = [
      ['data.html', /\/data\.html$/],
      ['law.html', /\/law\.html$/],
      ['awareness.html', /\/awareness\.html$/]
    ];
    currentMap.forEach(([href, pattern]) => {
      const link = findByHref(href);
      if (link && pattern.test(window.location.pathname)) link.setAttribute('aria-current', 'page');
    });

    const items = Array.from(nav.children);
    if (!items.length) return;

    const panel = document.createElement('div');
    panel.className = 'bookbslMobilePanel';
    panel.id = 'bookbslMobileNav';
    items.forEach(item => panel.appendChild(item));

    const toggle = document.createElement('button');
    toggle.type = 'button';
    toggle.className = 'bookbslMenuToggle';
    toggle.setAttribute('aria-expanded', 'false');
    toggle.setAttribute('aria-controls', panel.id);
    toggle.setAttribute('aria-label', 'Open site menu');
    toggle.innerHTML = '<span class="bookbslMenuIcon" aria-hidden="true"><span></span><span></span><span></span></span><span class="bookbslMenuText">Menu</span>';

    nav.appendChild(toggle);
    nav.appendChild(panel);

    const setOpen = (open) => {
      nav.classList.toggle('is-open', open);
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
      toggle.setAttribute('aria-label', open ? 'Close site menu' : 'Open site menu');
      const label = toggle.querySelector('.bookbslMenuText');
      if (label) label.textContent = open ? 'Close' : 'Menu';
    };

    toggle.addEventListener('click', () => {
      setOpen(toggle.getAttribute('aria-expanded') !== 'true');
    });

    panel.addEventListener('click', event => {
      if (event.target.closest('a')) setOpen(false);
    });

    document.addEventListener('click', event => {
      if (!nav.contains(event.target)) setOpen(false);
    });

    document.addEventListener('keydown', event => {
      if (event.key === 'Escape' && toggle.getAttribute('aria-expanded') === 'true') {
        setOpen(false);
        toggle.focus();
      }
    });

    window.addEventListener('resize', () => {
      if (window.innerWidth > 680) setOpen(false);
    }, { passive:true });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', installBookBSLNavigation, { once:true });
  } else {
    installBookBSLNavigation();
  }
})();
