/* Daily Stack box drawer.
   A box always starts with one stack; add-ons only ship inside a stack box.
   State lives in localStorage; checkout goes through /api/checkout (Stripe). */
(() => {
  const D = window.DS_CART; if (!D) return;
  const KEY = 'ds_box_v1';
  const eur = c => '€' + (c / 100).toFixed(2).replace('.', ',');
  const img = p => `/assets/products/${p}.webp`;
  let state = { stack: null, addons: [] };
  try { const s = JSON.parse(localStorage.getItem(KEY) || 'null'); if (s) state = s; } catch (e) {}
  // drop anything that no longer exists in the catalogue
  if (state.stack && !D.stacks[state.stack]) state.stack = null;
  state.addons = (state.addons || []).filter(a => D.addons[a]);
  const save = () => { try { localStorage.setItem(KEY, JSON.stringify(state)); } catch (e) {} };

  // ---------- markup ----------
  const ov = document.createElement('div'); ov.className = 'cart-ov'; ov.hidden = true;
  const el = document.createElement('aside'); el.className = 'cart'; el.hidden = true;
  el.setAttribute('role', 'dialog'); el.setAttribute('aria-modal', 'true'); el.setAttribute('aria-label', 'Your box');
  el.innerHTML = `<div class="cart-head"><h2>Your box</h2>
    <button type="button" class="cart-close" aria-label="Close"><svg width="22" height="22" viewBox="0 0 24 24"><path d="M5 5l14 14M19 5L5 19" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg></button></div>
    <div class="cart-body"></div><div class="cart-foot"></div>`;
  document.body.append(ov, el);
  const body = el.querySelector('.cart-body'), foot = el.querySelector('.cart-foot');

  // header button
  const btn = document.createElement('button');
  btn.type = 'button'; btn.className = 'cart-btn'; btn.setAttribute('aria-label', 'Your box'); btn.dataset.openCart = '';
  btn.innerHTML = `<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"><path d="M3 8l9-4 9 4v9l-9 4-9-4z"/><path d="M3 8l9 4 9-4M12 12v9"/></svg><span class="cart-count" hidden>0</span>`;
  const nav = document.querySelector('header.top nav');
  if (nav) nav.prepend(btn);

  // ---------- render ----------
  const line = (cls, pic, title, sub, tag, right) =>
    `<div class="cart-line ${cls}"><div class="cl-img ${Array.isArray(pic) ? 'cl-collage' : ''}">${Array.isArray(pic) ? pic.map(p => `<img src="${img(p)}" alt="">`).join('') : `<img src="${img(pic)}" alt="">`}</div>
      <div><h3>${title}</h3><p>${sub}</p>${tag ? `<span class="cl-tag">${tag}</span>` : ''}</div><div class="cl-right">${right}</div></div>`;
  const trash = (attr) => `<button type="button" class="cl-remove" ${attr} aria-label="Remove"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M4 7h16M9 7V4h6v3M6 7l1 13h10l1-13"/></svg></button>`;

  function render() {
    const st = state.stack && D.stacks[state.stack];
    const n = (st ? 1 : 0) + state.addons.length;
    const c = btn.querySelector('.cart-count'); c.textContent = n; c.hidden = !n;
    const per = st && st.recurring ? ' / month' : '';
    if (!st) {
      const waiting = state.addons.length ? `<p class="cart-msg">Saved for you: <b>${state.addons.map(a => D.addons[a].name).join(', ')}</b>. Pick a stack and it goes in the same box.</p>` : '';
      body.innerHTML = `<div class="cart-empty">${waiting}<p>Every box starts with a stack. Pick one, then add extras if you want.</p>
        ${Object.entries(D.stacks).map(([id, s]) => `<button type="button" class="cart-line cart-pick" data-pick="${id}">
          <div class="cl-img cl-collage">${s.photos.map(p => `<img src="${img(p)}" alt="">`).join('')}</div>
          <div><h3>${s.name}</h3><p>${s.count} products · 30-day packs${s.recurring ? ' · every month' : ' · one-time'}</p></div>
          <div class="cl-right"><span class="cl-price">${eur(s.price)}${s.recurring ? '<small> /mo</small>' : ''}</span></div></button>`).join('')}</div>`;
      foot.innerHTML = `<p class="cart-fine">Free shipping · Pay with iDEAL · Cancel anytime</p>`;
      return;
    }
    let h = `<p class="cart-banner">${st.recurring ? 'Free shipping. Every month, through your letterbox.' : 'Free shipping on the Winter Stack.'}</p>`;
    h += line('cart-stack', st.photos, st.name, `${st.count} products · 30-day packs`, st.recurring ? 'Delivered every month' : 'One-time box',
      `${trash('data-rm-stack')}<span class="cl-price">${eur(st.price)}<small>${per}</small></span>`);
    state.addons.forEach(id => { const a = D.addons[id];
      h += line('', a.photo, a.name, `${a.brand} · ${a.product}`, a.grade === 'B' ? 'Grade B · early evidence' : 'Grade A · same box', `${trash(`data-rm="${id}"`)}<span class="cl-price">+${eur(a.price)}<small>${per}</small></span>`); });
    const sugg = st.suggest.filter(s => !state.addons.includes(s)).slice(0, 3);
    if (sugg.length) {
      h += `<div class="cart-sub">Add an extra</div><div class="cart-sugg">`;
      sugg.forEach(id => { const a = D.addons[id];
        h += line('', a.photo, a.name, `${a.brand} · ${a.product}`, '', `<span class="cl-price">${eur(a.price)}<small>${per}</small></span><button type="button" class="cart-add" data-add="${id}">Add</button>`); });
      h += `</div>`;
    }
    h += `<a class="cart-more" href="/add-ons">See all add-ons →</a>`;
    body.innerHTML = h;
    const extras = state.addons.reduce((s, id) => s + D.addons[id].price, 0);
    foot.innerHTML = `<div class="cart-msgbox"></div>
      <div class="cart-row"><span>${st.name}</span><span>${eur(st.price)}</span></div>
      ${extras ? `<div class="cart-row"><span>Extras (${state.addons.length})</span><span>${eur(extras)}</span></div>` : ''}
      <div class="cart-row"><span>Shipping</span><span>Free</span></div>
      <div class="cart-total"><b>Total</b><span>${eur(st.price + extras)}<small>${per}</small></span></div>
      <button type="button" class="btn green cart-pay">Pay with iDEAL →</button>
      <p class="cart-fine">iDEAL, card or Apple Pay. ${st.recurring ? 'Pause or cancel anytime.' : ''}</p>`;
  }

  // ---------- open / close ----------
  let lastFocus = null;
  function open() {
    render(); lastFocus = document.activeElement;
    ov.hidden = el.hidden = false; document.body.classList.add('cart-open');
    requestAnimationFrame(() => { ov.classList.add('show'); el.classList.add('show'); });
    el.querySelector('.cart-close').focus();
  }
  function close() {
    ov.classList.remove('show'); el.classList.remove('show'); document.body.classList.remove('cart-open');
    setTimeout(() => { ov.hidden = el.hidden = true; }, 250);
    if (lastFocus && lastFocus.focus) lastFocus.focus();
  }
  ov.addEventListener('click', close);
  el.querySelector('.cart-close').addEventListener('click', close);
  document.addEventListener('keydown', e => { if (e.key === 'Escape' && !el.hidden) close(); });

  // ---------- actions ----------
  const addAddon = id => { if (D.addons[id] && !state.addons.includes(id)) state.addons.push(id); save(); };
  document.addEventListener('click', e => {
    const t = e.target.closest('[data-box],[data-addon],[data-open-cart],[data-pick],[data-add],[data-rm],[data-rm-stack],.cart-pay');
    if (!t) return;
    if (t.matches('[data-box]')) { if (!D.stacks[t.dataset.box]) return; e.preventDefault(); state.stack = t.dataset.box; save(); open(); return; }
    if (t.matches('[data-addon]')) { e.preventDefault(); addAddon(t.dataset.addon); t.classList.add('added'); open(); return; }
    if (t.matches('[data-open-cart]')) { e.preventDefault(); open(); return; }
    if (t.matches('[data-pick]')) { state.stack = t.dataset.pick; save(); render(); return; }
    if (t.matches('[data-add]')) { addAddon(t.dataset.add); render(); return; }
    if (t.matches('[data-rm]')) { state.addons = state.addons.filter(a => a !== t.dataset.rm); save(); render(); return; }
    if (t.matches('[data-rm-stack]')) { state.stack = null; save(); render(); return; }
    if (t.matches('.cart-pay')) checkout(t);
  });

  async function checkout(b) {
    const st = D.stacks[state.stack]; if (!st) return;
    b.disabled = true; b.textContent = 'Opening secure checkout…';
    try {
      const r = await fetch('/api/checkout', { method: 'POST', headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ stack: state.stack, addons: state.addons }) });
      const j = await r.json().catch(() => ({}));
      if (r.ok && j.url) { location.href = j.url; return; }
      throw new Error(j.error || 'checkout');
    } catch (err) {
      b.disabled = false; b.textContent = 'Pay with iDEAL →';
      const m = foot.querySelector('.cart-msgbox');
      m.innerHTML = `<p class="cart-msg">Checkout with extras isn't available right now.${state.addons.length ? '' : ''} <a href="${st.link}">Pay for the ${st.name} only</a>, or try again in a minute.</p>`;
    }
  }

  // open the drawer straight away when coming from a link like /#box
  if (location.hash === '#box') open();
  render();
})();
