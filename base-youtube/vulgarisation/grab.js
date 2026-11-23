// Récupération des sous-titres YouTube (original + traduction française) depuis une page youtube.com/watch
(() => {
  if (!window.__hooked) {
    window.__hooked = true; window.__cap = [];
    const o = XMLHttpRequest.prototype.open;
    XMLHttpRequest.prototype.open = function (m, u) { try { if (String(u).includes('timedtext')) window.__cap.push(String(u)); } catch (e) {} return o.apply(this, arguments); };
    const f = window.fetch;
    window.fetch = function (u) { try { const s = typeof u === 'string' ? u : u.url; if (s && s.includes('timedtext')) window.__cap.push(s); } catch (e) {} return f.apply(this, arguments); };
  }
  const tick = () => new Promise(r => { const c = new MessageChannel(); c.port1.onmessage = () => r(); c.port2.postMessage(0); });
  const sleep = async ms => { const end = performance.now() + ms; while (performance.now() < end) await tick(); };
  window.__sleep = sleep;
  const conv = j => (j.events || []).filter(e => e.segs).map(e => ({ t: Math.round((e.tStartMs || 0) / 1000), x: e.segs.map(s => s.utf8).join('').replace(/\n/g, ' ') })).filter(s => s.x.trim());
  window.__grab = async (id, wantFr = true) => {
    const p = document.getElementById('movie_player');
    window.__cap = []; p.loadVideoById(id); p.mute();
    for (let i = 0; i < 100; i++) { await sleep(150); if (p.getPlayerResponse()?.videoDetails?.videoId === id) break; }
    await sleep(800);
    const pr = p.getPlayerResponse(); const tl = pr?.captions?.playerCaptionsTracklistRenderer?.captionTracks || [];
    const man = tl.filter(t => t.kind !== 'asr'), asr = tl.filter(t => t.kind === 'asr');
    const f = (arr, re) => arr.find(t => re.test(t.languageCode));
    const pick = f(man, /^fr/) || f(man, /^en/) || f(asr, /^fr$/) || f(asr, /^en$/) || f(asr, /^fr/) || f(asr, /^en/) || man[0] || asr[0];
    const meta = { id, title: pr?.videoDetails?.title, author: pr?.videoDetails?.author, secs: +pr?.videoDetails?.lengthSeconds, date: pr?.microformat?.playerMicroformatRenderer?.publishDate };
    if (!pick) return { ...meta, err: 'no captions' };
    window.__cap = [];
    try { p.unloadModule('captions'); } catch (e) {}
    await sleep(200); p.loadModule('captions'); await sleep(200);
    p.setOption('captions', 'track', { languageCode: pick.languageCode, kind: pick.kind });
    let u; for (let i = 0; i < 60 && !(u = window.__cap.find(x => x.includes('v=' + id))); i++) await sleep(150);
    if (!u) return { ...meta, err: 'no url' };
    const base = u.replace(/&fmt=[^&]*/, '').replace(/&tlang=[^&]*/, '');
    const orig = conv(await (await fetch(base + '&fmt=json3')).json());
    let fr = null;
    if (wantFr && !/^fr/.test(pick.languageCode)) {
      const r = await fetch(base + '&fmt=json3&tlang=fr');
      fr = r.ok ? conv(await r.json()) : 'ERR' + r.status;
    }
    return { ...meta, lang: pick.languageCode, kind: pick.kind || 'manual', orig, fr, frsrc: Array.isArray(fr) ? 'traduction automatique YouTube' : null, base };
  };
  // Traite une liste d'identifiants ; window.__out garde les résultats, window.__prog la progression
  window.__batch = async (ids, pauseMs = 4000) => {
    window.__out = window.__out || {}; window.__stop = false;
    for (const id of ids) {
      if (window.__stop) break;
      if (window.__out[id] && !window.__out[id].err && (Array.isArray(window.__out[id].fr) || /^fr/.test(window.__out[id].lang || ''))) continue;
      try { window.__out[id] = await window.__grab(id); } catch (e) { window.__out[id] = { id, err: String(e) }; }
      window.__prog = { done: Object.keys(window.__out).length, last: id, at: new Date().toISOString() };
      await sleep(pauseMs);
    }
    window.__prog.finished = true;
  };
  return 'grab.js chargé';
})();
