(() => {
  const id = 'bookbslGlobalNavPolish';
  if (document.getElementById(id)) return;

  const style = document.createElement('style');
  style.id = id;
  style.textContent = `
    @media (min-width:681px){
      .top .topin{
        gap:32px!important;
      }

      .top .topnav{
        margin-left:auto!important;
        display:flex!important;
        align-items:center!important;
        justify-content:flex-end!important;
        gap:14px!important;
        flex-wrap:nowrap!important;
      }

      .top .topnav>.bookbslMobilePanel{
        display:contents!important;
      }

      .top .topnav>a:not(.header-cta),
      .top .topnav>.bookbslMobilePanel>a:not(.header-cta){
        display:inline-flex!important;
        align-items:center!important;
        justify-content:center!important;
        min-height:42px!important;
        padding:0 14px!important;
        border-radius:999px!important;
        color:#092A35!important;
        background:transparent!important;
        text-decoration:none!important;
        font-size:.92rem!important;
        font-weight:800!important;
        line-height:1!important;
        white-space:nowrap!important;
        transition:color .16s ease,background-color .16s ease,transform .08s ease!important;
      }

      .top .topnav>a:not(.header-cta):hover,
      .top .topnav>a:not(.header-cta):focus-visible,
      .top .topnav>a:not(.header-cta):active,
      .top .topnav>.bookbslMobilePanel>a:not(.header-cta):hover,
      .top .topnav>.bookbslMobilePanel>a:not(.header-cta):focus-visible,
      .top .topnav>.bookbslMobilePanel>a:not(.header-cta):active{
        color:#2456B3!important;
        background:#fff!important;
        text-decoration:underline!important;
        text-decoration-thickness:2px!important;
        text-underline-offset:6px!important;
      }

      .top .topnav>a:not(.header-cta):active,
      .top .topnav>.bookbslMobilePanel>a:not(.header-cta):active{
        transform:translateY(1px)!important;
      }

      .top .topnav>a[aria-current="page"],
      .top .topnav>.bookbslMobilePanel>a[aria-current="page"]{
        color:#2456B3!important;
        text-decoration:underline!important;
        text-decoration-thickness:2px!important;
        text-underline-offset:6px!important;
      }

      .top .topnav .header-cta{
        display:inline-flex!important;
        align-items:center!important;
        justify-content:center!important;
        box-sizing:border-box!important;
        width:auto!important;
        min-width:0!important;
        max-width:none!important;
        min-height:42px!important;
        height:42px!important;
        margin-left:10px!important;
        padding:0 20px!important;
        border:2px solid #092A35!important;
        border-radius:999px!important;
        background:#092A35!important;
        color:#fff!important;
        text-decoration:none!important;
        box-shadow:none!important;
        font-size:.92rem!important;
        font-weight:800!important;
        line-height:1!important;
        letter-spacing:-.01em!important;
        white-space:nowrap!important;
        flex:0 0 auto!important;
        transition:background-color .16s ease,border-color .16s ease,transform .08s ease!important;
      }

      .top .topnav .header-cta:hover,
      .top .topnav .header-cta:focus-visible,
      .top .topnav .header-cta:active{
        background:#2456B3!important;
        border-color:#2456B3!important;
        color:#fff!important;
        text-decoration:none!important;
      }

      .top .topnav .header-cta:active{
        transform:translateY(1px)!important;
      }
    }
  `;

  document.head.appendChild(style);
})();
