// The Skin Haus · cabecera, menú, apariciones y formulario a WhatsApp
(function () {
  var cab = document.querySelector('.cab');
  function alScroll() { cab.classList.toggle('solida', window.scrollY > 30); }
  alScroll(); window.addEventListener('scroll', alScroll, { passive: true });

  var hamb = document.querySelector('.hamb');
  hamb.addEventListener('click', function () {
    var ab = document.body.classList.toggle('abierto');
    hamb.setAttribute('aria-expanded', ab);
  });
  document.querySelectorAll('.menu a').forEach(function (a) {
    a.addEventListener('click', function () { document.body.classList.remove('abierto'); });
  });

  var revs = document.querySelectorAll('.rev');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('ve'); io.unobserve(e.target); } });
    }, { rootMargin: '0px 0px -8% 0px' });
    revs.forEach(function (r) { io.observe(r); });
  } else { revs.forEach(function (r) { r.classList.add('ve'); }); }

  var form = document.querySelector('#form-valoracion');
  if (form) form.addEventListener('submit', function (ev) {
    ev.preventDefault();
    var d = new FormData(form);
    var txt = 'Hola, soy ' + d.get('nombre') + '. Quiero agendar una valoración en The Skin Haus.' +
      (d.get('interes') ? '\nMe interesa: ' + d.get('interes') : '') +
      (d.get('mensaje') ? '\n' + d.get('mensaje') : '');
    window.open('https://wa.me/' + form.dataset.wa + '?text=' + encodeURIComponent(txt), '_blank', 'noopener');
  });
})();
