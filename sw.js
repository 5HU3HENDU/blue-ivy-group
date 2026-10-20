const C = 'big-v1';
const CORE = [
  'index.html','about.html','projects.html','contact.html',
  'assets/css/style.css','assets/js/main.js',
  'assets/img/hero.jpg','assets/img/og-cover.jpg','assets/img/icon-192.png','assets/img/icon-512.png'
];
const scope = new URL('./', self.registration.scope).pathname;
self.addEventListener('install', e => {
  e.waitUntil(caches.open(C).then(c => c.addAll(CORE.map(u => scope + u))).then(() => self.skipWaiting()));
});
self.addEventListener('activate', e => {
  e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k !== C).map(k => caches.delete(k)))).then(() => self.clients.claim()));
});
self.addEventListener('fetch', e => {
  if (e.request.method !== 'GET') return;
  const url = new URL(e.request.url);
  if (url.origin !== self.location.origin) return;
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
