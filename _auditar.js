// Revisor de responsive (no se publica en la web): se inyecta en cada página y devuelve problemas
window.__auditar = (doc, win) => {
  const W = doc.documentElement.clientWidth, out = [];
  const recortado = (el) => { for (let p = el.parentElement; p; p = p.parentElement) { const o = win.getComputedStyle(p).overflowX; if (['auto', 'scroll', 'hidden', 'clip'].includes(o)) return true; } return false; };
  const nombre = (el) => el.tagName.toLowerCase() + (typeof el.className === 'string' && el.className ? '.' + el.className.trim().split(/\s+/).slice(0, 2).join('.') : '');
  if (doc.documentElement.scrollWidth > W + 1) out.push('DESBORDE página: ' + doc.documentElement.scrollWidth + ' > ' + W);
  doc.querySelectorAll('main *, footer *, header *').forEach((el) => {
    const cs = win.getComputedStyle(el); if (cs.display === 'none' || cs.visibility === 'hidden') return;
    if (el.closest('svg') && el.tagName.toLowerCase() !== 'svg') return;
    const r = el.getBoundingClientRect(); if (!r.width || !r.height) return;
    if ((r.right > W + 2 || r.left < -2) && !recortado(el) && cs.position !== 'fixed' && !el.closest('.menu')) out.push('SE SALE: ' + nombre(el) + ' [' + Math.round(r.left) + '→' + Math.round(r.right) + ']');
    if (W < 861 && el.matches('a.btn, button, summary, .hamb, .wa, a.enlace') && r.height < 40 && !el.closest('.menu')) out.push('TOQUE PEQUEÑO (' + Math.round(r.height) + 'px): ' + nombre(el) + ' "' + el.textContent.trim().slice(0, 24) + '"');
    if (el.children.length === 0 && el.textContent.trim() && parseFloat(cs.fontSize) < 11.5 && !el.closest('.logo')) out.push('LETRA PEQUEÑA (' + cs.fontSize + '): ' + nombre(el) + ' "' + el.textContent.trim().slice(0, 24) + '"');
    if (el.children.length === 0 && el.textContent.trim().length > 3 && el.scrollWidth > el.clientWidth + 2 && ['hidden', 'clip'].includes(cs.overflowX)) out.push('TEXTO CORTADO: ' + nombre(el));
  });
  return [...new Set(out)].slice(0, 12);
};
