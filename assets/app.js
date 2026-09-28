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

  // curva punteada que une los círculos del camino
  function curvas() {
    document.querySelectorAll('.camino').forEach(function (c) {
      var svg = c.querySelector('svg.curva'); if (!svg || getComputedStyle(svg).display === 'none') return;
      // medidas del .paso (offsetParent = .pasos) para que la animación de aparición no las altere;
      // el círculo .num es su primer hijo, arriba a la izquierda
      var pts = [].map.call(c.querySelectorAll('.paso'), function (p) {
        var n = p.querySelector('.num');
        return [p.offsetLeft + n.offsetWidth / 2, p.offsetTop + n.offsetHeight / 2];
      });
      if (pts.length < 2) return;
      var d = 'M' + (pts[0][0] - 120) + ',' + (pts[0][1] + 60) + ' Q' + (pts[0][0] - 60) + ',' + pts[0][1] + ' ' + pts[0][0] + ',' + pts[0][1];
      for (var i = 1; i < pts.length; i++) {
        var a = pts[i - 1], b = pts[i], mx = (a[0] + b[0]) / 2;
        d += ' C' + mx + ',' + a[1] + ' ' + mx + ',' + b[1] + ' ' + b[0] + ',' + b[1];
      }
      var u = pts[pts.length - 1];
      d += ' Q' + (u[0] + 80) + ',' + u[1] + ' ' + (u[0] + 160) + ',' + (u[1] - 40);
      svg.querySelector('path').setAttribute('d', d);
    });
  }
  curvas(); window.addEventListener('load', curvas);
  document.fonts && document.fonts.ready.then(curvas);
  if ('ResizeObserver' in window) {
    var ro = new ResizeObserver(function () { curvas(); });
    document.querySelectorAll('.camino .pasos').forEach(function (p) { ro.observe(p); });
  } else { window.addEventListener('resize', curvas); }

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
