(() => {
  function installBookBSLNavigation(){
    const header = document.querySelector('.top');
    const topin = header && header.querySelector('.topin');
    const nav = topin && topin.querySelector('.topnav');
    if (!header || !topin || !nav || nav.querySelector('.bookbslMenuToggle')) return;

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
