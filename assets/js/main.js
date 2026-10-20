(function () {
  var RM = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // PWA
  if ('serviceWorker' in navigator) {
    window.addEventListener('load', function () {
      navigator.serviceWorker.register(new URL('manifest.webmanifest', document.baseURI).pathname.replace('manifest.webmanifest', '') + 'sw.js').then(function (r) { if (r && r.update) r.update(); }).catch(function () {});
    });
  }

  // Header: transparent over the hero, solid after scroll (home); always solid on inner pages
  var tb = document.getElementById('topbar');
  if (tb) {
    if (document.body.classList.contains('inner')) {
      tb.classList.add('solid');
    } else {
      var onScroll = function () { tb.classList.toggle('solid', window.scrollY > 28); };
      onScroll();
      window.addEventListener('scroll', onScroll, { passive: true });
    }
  }

  // Menu overlay
  var menu = document.getElementById('menu');
  var mb = document.getElementById('menuBtn');
  var mc = document.getElementById('menuClose');
  if (menu && mb) {
    var links = menu.querySelectorAll('.mlinks a');
    var openMenu = function () {
      menu.classList.add('open');
      menu.setAttribute('aria-hidden', 'false');
      document.body.classList.add('lock');
      links.forEach(function (a, i) { a.style.transitionDelay = RM ? '0s' : (0.06 + i * 0.05) + 's'; });
    };
    var closeMenu = function () {
      links.forEach(function (a) { a.style.transitionDelay = '0s'; });
      menu.classList.remove('open');
      menu.setAttribute('aria-hidden', 'true');
      document.body.classList.remove('lock');
    };
    mb.addEventListener('click', openMenu);
    if (mc) mc.addEventListener('click', closeMenu);
    links.forEach(function (a) { a.addEventListener('click', closeMenu); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') closeMenu(); });
  }

  // Scroll reveals
  var rv = document.querySelectorAll('[data-rv]');
  if (rv.length) {
    if (RM || !('IntersectionObserver' in window)) {
      rv.forEach(function (el) { el.classList.add('in'); });
    } else {
      var io = new IntersectionObserver(function (es) {
        es.forEach(function (en) {
          if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); }
        });
      }, { threshold: 0.12 });
      rv.forEach(function (el) { io.observe(el); });
    }
  }

  // Count-up for verified numbers only
  var cs = document.querySelectorAll('[data-count]');
  if (cs.length) {
    var run = function (el) {
      var v = parseFloat(el.getAttribute('data-count'));
      var d = parseInt(el.getAttribute('data-dec') || '0', 10);
      if (RM) { el.textContent = v.toFixed(d); return; }
      var t0 = null, dur = 900;
      var step = function (ts) {
        if (!t0) t0 = ts;
        var k = Math.min(1, (ts - t0) / dur);
        var e = 1 - Math.pow(1 - k, 3);
        el.textContent = (v * e).toFixed(d);
        if (k < 1) requestAnimationFrame(step);
      };
      requestAnimationFrame(step);
    };
    if ('IntersectionObserver' in window) {
      var io2 = new IntersectionObserver(function (es) {
        es.forEach(function (en) {
          if (en.isIntersecting) { run(en.target); io2.unobserve(en.target); }
        });
      }, { threshold: 0.5 });
      cs.forEach(function (el) { io2.observe(el); });
    } else { cs.forEach(run); }
  }

  // Subtle parallax on project images
  var px = document.querySelectorAll('.plx img');
  if (px.length && !RM) {
    var tick = false;
    var upd = function () {
      tick = false;
      var vh = window.innerHeight;
      px.forEach(function (img) {
        var r = img.parentElement.getBoundingClientRect();
        if (r.bottom < 0 || r.top > vh) return;
        var c = (r.top + r.height / 2 - vh / 2) / vh;
        img.style.transform = 'scale(1.14) translateY(' + (c * -24).toFixed(1) + 'px)';
      });
    };
    var onS2 = function () { if (!tick) { tick = true; requestAnimationFrame(upd); } };
    window.addEventListener('scroll', onS2, { passive: true });
    window.addEventListener('resize', onS2);
    upd();
  }

  // Blueprint intro: decorative linework draws once per day, then fades to the render.
  // ?intro=1 forces it (testing/demo). Reduced motion: static lines, brief hold, instant swap.
  var bp = document.getElementById('bp');
  if (bp) {
    var force = /[?&]intro=1\b/.test(location.search);
    var seen = false;
    try {
      var bts = localStorage.getItem('big-bp-ts');
      seen = bts && (Date.now() - (+bts) < 864e5);
    } catch (e) {}
    var markSeen = function () { try { localStorage.setItem('big-bp-ts', String(Date.now())); } catch (e) {} };
    var dropBp = function () { if (bp.parentNode) bp.parentNode.removeChild(bp); };
    if (force || !seen) {
      bp.hidden = false;
      if (RM) {
        setTimeout(function () { dropBp(); markSeen(); }, 1600);
      } else {
        var ps = bp.querySelectorAll('path');
        ps.forEach(function (p, i) {
          var l = p.getTotalLength();
          p.style.strokeDasharray = l;
          p.style.strokeDashoffset = l;
          p.style.transition = 'stroke-dashoffset 1.9s ease ' + (i * 16) + 'ms';
        });
        requestAnimationFrame(function () {
          requestAnimationFrame(function () {
            ps.forEach(function (p) { p.style.strokeDashoffset = '0'; });
          });
        });
        var tot = 1900 + ps.length * 16 + 700;
        setTimeout(function () { bp.classList.add('fade'); markSeen(); }, tot);
        setTimeout(dropBp, tot + 1300);
      }
    } else {
      dropBp();
    }
  }

  // Contact form -> mailto
  var qf = document.getElementById('qform');
  if (qf) {
    qf.addEventListener('submit', function (e) {
      e.preventDefault();
      var n = qf.name.value.trim(), p = qf.phone.value.trim(), m = qf.msg.value.trim();
      var s = encodeURIComponent('Project enquiry from ' + n);
      var b = encodeURIComponent('Name: ' + n + '\nPhone: ' + p + '\n\n' + m);
      window.location.href = 'mailto:info@blueivygroup.in?subject=' + s + '&body=' + b;
    });
  }
})();
