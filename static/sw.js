const CACHE = 'time-v2';

// Everything the app needs to run a full session offline: the shell, the
// manifest, both icons, the background photo, and — this is the part v1
// was missing — all four built-in bell files. A bell that only loads over
// network defeats the point of a meditation timer the moment signal drops.
const PRECACHE = [
  '/',
  '/static/manifest.json',
  '/static/favicon.ico',
  '/static/bell.jpg',
  '/static/icons/icon-192.png',
  '/static/icons/icon-512.png',
  '/static/sounds/Sharp Bell.mp3',
  '/static/sounds/Small Bell Mellower.m4a',
  '/static/sounds/Smooth Bell.mp3',
  '/static/sounds/Soft_Bell_Hit.wav',
];

self.addEventListener('install', e => {
  e.waitUntil(caches.open(CACHE).then(c => c.addAll(PRECACHE)));
  self.skipWaiting();
});

self.addEventListener('activate', e => {
  e.waitUntil(caches.keys().then(keys =>
    Promise.all(keys.filter(k => k !== CACHE).map(k => caches.delete(k)))
  ));
  self.clients.claim();
});

self.addEventListener('fetch', e => {
  if (e.request.method !== 'GET') return;
  const url = new URL(e.request.url);

  // Static, unchanging assets (bells, icons, manifest, background photo):
  // cache-first. These never change once shipped, and a sit shouldn't wait
  // on a network round-trip — or fail outright with no signal — just to
  // play a bell that's already sitting on the phone.
  if (url.pathname.startsWith('/static/')) {
    e.respondWith(
      caches.match(e.request).then(cached => cached || fetch(e.request))
    );
    return;
  }

  // Everything else (the app shell, /api/* calls the page already handles
  // failures for): network-first so updates and custom-uploaded sounds
  // stay fresh, falling back to cache only if the network is unavailable.
  e.respondWith(
    fetch(e.request).catch(() => caches.match(e.request))
  );
});
