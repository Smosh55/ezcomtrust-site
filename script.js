/* ============================================================
   EZ COMTRUST — interactions
   ============================================================ */
(function () {
  'use strict';

  /* ---- Sticky header shadow on scroll ---- */
  var header = document.getElementById('header');
  function onScroll() {
    if (window.scrollY > 12) header.classList.add('scrolled');
    else header.classList.remove('scrolled');
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  /* ---- Mobile nav toggle ---- */
  var hamburger = document.getElementById('hamburger');
  var nav = document.getElementById('nav');

  function closeNav() {
    nav.classList.remove('open');
    hamburger.classList.remove('open');
    hamburger.setAttribute('aria-expanded', 'false');
    document.body.style.overflow = '';
  }
  function toggleNav() {
    var open = nav.classList.toggle('open');
    hamburger.classList.toggle('open', open);
    hamburger.setAttribute('aria-expanded', open ? 'true' : 'false');
    document.body.style.overflow = open ? 'hidden' : '';
  }
  hamburger.addEventListener('click', toggleNav);

  // Close menu when a nav link is tapped
  nav.querySelectorAll('a').forEach(function (a) {
    a.addEventListener('click', closeNav);
  });
  // Close on Escape
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') closeNav();
  });

  /* ---- Scroll reveal ---- */
  var reveals = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('in');
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
    reveals.forEach(function (el) { io.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add('in'); });
  }

  /* ---- FAQ: allow only one open at a time (optional accordion) ---- */
  var accs = document.querySelectorAll('.acc');
  accs.forEach(function (acc) {
    acc.addEventListener('toggle', function () {
      if (acc.open) {
        accs.forEach(function (other) {
          if (other !== acc) other.removeAttribute('open');
        });
      }
    });
  });

  /* ---- Year in footer ---- */
  var yr = document.getElementById('year');
  if (yr) yr.textContent = new Date().getFullYear();

  /* ---- Lead form handling ----
     By default this shows a success message client-side.
     To receive submissions by email, either:
       1) Set FORM_ENDPOINT below to a Formspree/Basin/Web3Forms URL, OR
       2) Replace with your own backend endpoint.
  ---------------------------------------------------------------- */
  var FORM_ENDPOINT = ''; // e.g. 'https://formspree.io/f/xxxxxxx'
  var form = document.getElementById('leadForm');
  var success = document.getElementById('formSuccess');

  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();

      // Basic validation
      var required = form.querySelectorAll('[required]');
      var valid = true;
      required.forEach(function (input) {
        if (!input.value.trim() || (input.type === 'email' && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(input.value))) {
          input.style.borderColor = '#e5484d';
          valid = false;
        } else {
          input.style.borderColor = '';
        }
      });
      if (!valid) return;

      var submitBtn = form.querySelector('button[type="submit"]');
      var original = submitBtn.textContent;

      function showSuccess() {
        form.querySelectorAll('.field, .field-row').forEach(function (f) { f.style.display = 'none'; });
        submitBtn.style.display = 'none';
        var fine = form.querySelector('.form__fine');
        if (fine) fine.style.display = 'none';
        if (success) success.hidden = false;
        success.scrollIntoView({ behavior: 'smooth', block: 'center' });
      }

      if (FORM_ENDPOINT) {
        submitBtn.textContent = 'Sending…';
        submitBtn.disabled = true;
        fetch(FORM_ENDPOINT, {
          method: 'POST',
          headers: { 'Accept': 'application/json' },
          body: new FormData(form)
        }).then(function (res) {
          if (res.ok) showSuccess();
          else throw new Error('Bad response');
        }).catch(function () {
          submitBtn.textContent = original;
          submitBtn.disabled = false;
          // Fallback: open mail client with details
          var params = new URLSearchParams(new FormData(form)).toString().replace(/&/g, '%0D%0A').replace(/=/g, ': ');
          window.location.href = 'mailto:info@ezcomtrust.com?subject=Free%20Assessment%20Request&body=' + params;
        });
      } else {
        // No backend configured — show success (demo mode)
        showSuccess();
      }
    });
  }
})();
