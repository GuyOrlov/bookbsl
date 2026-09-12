(()=>{try{
  if(localStorage.getItem('bookbsl_stats_optout')==='1')return;
  const path=(location.pathname.replace(/^\/|\/$/g,'')||'home').replace(/[^a-z0-9]+/gi,'-').toLowerCase();
  const once='bookbsl-pageview-'+path;
  if(sessionStorage.getItem(once))return;
  sessionStorage.setItem(once,'1');
  fetch('https://countapi.mileshilliard.com/api/v1/hit/bookbsl-guyorlov-page-'+path,{mode:'cors'}).catch(()=>{});
}catch(e){}})();