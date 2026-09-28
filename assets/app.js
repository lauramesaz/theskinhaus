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

  // movimiento suave al bajar + manifiesto palabra a palabra
  var quieto = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var vels = [].slice.call(document.querySelectorAll('[data-vel]'));
  var manifs = [].slice.call(document.querySelectorAll('.manif'));
  var pend = false;
  function cuadro() {
    pend = false;
    var vh = window.innerHeight;
    if (!quieto && window.innerWidth > 860) vels.forEach(function (el) {
      var r = el.getBoundingClientRect(), c = r.top + r.height / 2 - vh / 2;
      el.style.setProperty('--py', (c * parseFloat(el.dataset.vel)).toFixed(1) + 'px');
    });
    manifs.forEach(function (m) {
      var r = m.getBoundingClientRect(), sp = m.children;
      var avance = (vh * 0.85 - r.top) / (r.height + vh * 0.35);
      var n = Math.round(Math.max(0, Math.min(1, avance)) * sp.length);
      for (var i = 0; i < sp.length; i++) sp[i].classList.toggle('on', quieto || i < n);
    });
  }
  function pedir() { if (!pend) { pend = true; requestAnimationFrame(cuadro); } }
  window.addEventListener('scroll', pedir, { passive: true });
  window.addEventListener('resize', pedir);
  cuadro();

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
