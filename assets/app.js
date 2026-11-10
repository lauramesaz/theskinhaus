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

  // pestañas de tratamientos
  document.querySelectorAll('.pestanas').forEach(function (grupo) {
    var botones = grupo.querySelectorAll('button');
    botones.forEach(function (b) {
      b.addEventListener('click', function () {
        botones.forEach(function (x) {
          var on = x === b;
          x.setAttribute('aria-selected', on);
          var pan = document.getElementById(x.dataset.pan);
          pan.hidden = !on;
          if (on) pan.querySelectorAll('.rev').forEach(function (r) { r.classList.add('ve'); });
        });
      });
    });
  });

  // Medición: cada clic a WhatsApp cuenta como contacto (Google Analytics + Clarity)
  function contarWhatsApp(origen) {
    if (window.gtag) gtag('event', 'clic_whatsapp', { pagina: location.pathname, origen: origen });
    if (window.clarity) clarity('event', 'clic_whatsapp');
  }
  document.addEventListener('click', function (ev) {
    var a = ev.target.closest && ev.target.closest('a[href*="wa.me"]');
    if (a) contarWhatsApp(a.classList.contains('wa') ? 'boton-flotante' : (a.dataset.origen || 'enlace'));
  }, true);

  // 9-nov-2026: también se cuenta el clic en lo que lleva al formulario de /valoracion (mismo patrón, con página y origen)
  function zona(a) {
    if (a.dataset.origen) return a.dataset.origen;
    if (a.closest('.cab')) return 'menu';
    if (a.closest('.hero')) return 'hero';
    if (a.closest('.cierre')) return 'cierre';
    if (a.closest('.pie-web')) return 'pie';
    return 'texto';
  }
  document.addEventListener('click', function (ev) {
    var a = ev.target.closest && ev.target.closest('a[href]');
    if (!a || !/(^|\/)valoracion([?#]|$)/.test(a.getAttribute('href'))) return;
    if (window.gtag) gtag('event', 'clic_valoracion', { pagina: location.pathname, origen: zona(a) });
    if (window.clarity) clarity('event', 'clic_valoracion');
  }, true);

  // 4-nov-2026: clics en los accesos redondos y la franja de diciembre de la portada (data-ev = nombre del evento)
  document.addEventListener('click', function (ev) {
    var el = ev.target.closest && ev.target.closest('[data-ev]');
    if (!el) return;
    if (window.gtag) gtag('event', el.dataset.ev, { destino: el.dataset.destino || el.getAttribute('href'), pagina: location.pathname });
    if (window.clarity) clarity('event', el.dataset.ev);
  }, true);

  var form = document.querySelector('#form-valoracion');
  // 9-nov-2026: /valoracion?interes=<slug>&desde=<página> deja elegido el tratamiento y recuerda de dónde vino la persona.
  // "desde" solo vale si está en la lista de páginas del sitio (nunca se copia texto de la dirección al mensaje).
  var vieneDe = '';
  if (form) try {
    var q = new URLSearchParams(location.search), interes = q.get('interes'), desde = q.get('desde');
    var sel = form.querySelector('select[name="interes"]');
    if (interes && sel) [].forEach.call(sel.options, function (o) { if (o.dataset.slug === interes) sel.value = o.value; });
    var lista = JSON.parse((document.getElementById('origenes') || {}).textContent || '{}');
    if (desde && Object.prototype.hasOwnProperty.call(lista, desde)) vieneDe = lista[desde];
  } catch (e) {}
  if (form) form.addEventListener('submit', function (ev) {
    ev.preventDefault();
    contarWhatsApp('formulario');
    var d = new FormData(form);
    var txt = 'Hola, soy ' + d.get('nombre') + '. Quiero agendar una valoración en The Skin Haus.' +
      (d.get('interes') ? '\nMe interesa: ' + d.get('interes') : '') +
      (d.get('mensaje') ? '\n' + d.get('mensaje') : '') +
      (vieneDe ? '\nVengo de la página: ' + vieneDe : '');
    window.open('https://wa.me/' + form.dataset.wa + '?text=' + encodeURIComponent(txt), '_blank', 'noopener');
  });
})();


/* La píldora flotante de WhatsApp no repite el botón de la primera pantalla: aparece al bajar. */
/* 9-nov-2026 (ronda 3): y se esconde mientras se ve en pantalla otro botón que hace lo mismo (el de WhatsApp de la
   banda, del cierre, de "Dónde estamos", de la nota del artículo o el de enviar del formulario), para no mostrar
   dos veces lo mismo ni montarse sobre el bloque. */
(function(){
  var p=document.querySelector('.wa.pildora'); if(!p) return;
  var enPantalla=0;
  function ver(){ p.classList.toggle('arriba', window.scrollY < window.innerHeight*0.6 || enPantalla>0); }
  if('IntersectionObserver' in window){
    var io=new IntersectionObserver(function(es){
      es.forEach(function(e){ var antes=e.target._ve||false; e.target._ve=e.isIntersecting; enPantalla+=(e.isIntersecting?1:0)-(antes?1:0); });
      ver();
    });
    document.querySelectorAll('main a.btn[href*="wa.me"], main .acciones a[href*="wa.me"], #form-valoracion button[type="submit"]').forEach(function(b){ io.observe(b); });
  }
  ver(); window.addEventListener('scroll', ver, {passive:true});
})();
