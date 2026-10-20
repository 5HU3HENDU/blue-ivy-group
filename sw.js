const C = 'big-v5';
const scope = new URL('./', self.registration.scope).pathname;
self.addEventListener('install', e => { self.skipWaiting(); });
self.addEventListener('activate', e => {
  e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k !== C).map(k => caches.delete(k)))).then(() => self.clients.claim()));
});
self.addEventListener('fetch', e => {
  if (e.request.method !== 'GET') return;
  const url = new URL(e.request.url);
  if (url.origin !== self.location.origin) return;
  // Pages and code: network first so updates show immediately; cache is the offline fallback.
  if (e.request.mode === 'navigate' || /\.(html|css|js|webmanifest)$/.test(url.pathname)) {
    e.respondWith(
      fetch(e.request).then(res => {
        if (res.ok) { const cp = res.clone(); caches.open(C).then(c => c.put(e.request, cp)); }
        return res;
      }).catch(() => caches.match(e.request).then(hit => hit || caches.match(scope + 'index.html')))
    );
    return;
  }
  // Images and icons: cache first, refresh in the background.
  e.respondWith(
    caches.match(e.request).then(hit => {
      const net = fetch(e.request).then(res => {
        if (res.ok) { const cp = res.clone(); caches.open(C).then(c => c.put(e.request, cp)); }
        return res;
      }).catch(() => hit);
      return hit || net;
    })
  );
});
