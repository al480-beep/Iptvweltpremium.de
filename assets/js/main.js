/* IPTV Welt Premium – Interaktionen */
(function () {
  "use strict";

  // ---- Kontakt-Einstellungen: hier anpassen ----
  var CONFIG = {
    whatsapp: "490000000",          // internationale Nummer ohne + und Leerzeichen (vorläufig)
    whatsappDisplay: "+49 000 0000", // so wird die Nummer auf der Seite angezeigt
    email: "kontakt@iptvweltpremium.de",
    // Ersatzweg für Bestellungen, falls /api/order ausfällt (der öffentliche Schlüssel darf im Browser stehen)
    emailjs: { service: "service_8qunnth", template: "template_kir731r", publicKey: "R6r0yfArKg9oG_O0g" }
  };

  // ---- Kundenstimmen ----
  // Nur echte Bewertungen eintragen. Solange die Liste leer ist, bleibt der Bereich ausgeblendet.
  // Beispiel: { name: "Thomas K.", city: "Berlin", stars: 5, text: "Läuft super stabil ..." }
  var REVIEWS = [];

  var safeGet = function (k) { try { return localStorage.getItem(k); } catch (e) { return null; } };
  var safeSet = function (k, v) { try { localStorage.setItem(k, v); } catch (e) {} };
  var reduceMotion = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  // ---- Preise (Euro) je Geräteanzahl ----
  var PRICES = {
    1: { 1: 9, 3: 29, 6: 39, 12: 49 },
    2: { 1: 18, 3: 50, 6: 69, 12: 89 },
    3: { 1: 27, 3: 75, 6: 105, 12: 135 },
    4: { 1: 36, 3: 99, 6: 140, 12: 180 },
    5: { 1: 45, 3: 120, 6: 175, 12: 225 }
  };
  var DURATION_LABEL = { 1: "1 Monat", 3: "3 Monate", 6: "6 Monate", 12: "1 Jahr" };

  var euro = function (n) {
    return n.toLocaleString("de-DE", { minimumFractionDigits: Number.isInteger(n) ? 0 : 2, maximumFractionDigits: 2 });
  };
  var deviceLabel = function (d) { return d + (d === 1 ? " Gerät" : " Geräte"); };
  var checkoutUrl = function (d, m) { return "/checkout/?geraete=" + d + "&laufzeit=" + m; };
  var waLink = function (text) {
    return "https://wa.me/" + CONFIG.whatsapp + "?text=" + encodeURIComponent(text);
  };

  // Header-Hintergrund beim Scrollen
  var header = document.querySelector(".header");
  var onScroll = function () { header.classList.toggle("scrolled", window.scrollY > 20); };
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  // Aktuelle Seite in der Navigation markieren
  document.querySelectorAll(".nav-links > li:not(.nav-mobile-ctas) > a").forEach(function (a) {
    if (a.getAttribute("href") === location.pathname) a.setAttribute("aria-current", "page");
  });

  // Mobile Navigation
  var menuBtn = document.querySelector(".menu-btn");
  menuBtn.addEventListener("click", function () {
    var open = document.body.classList.toggle("menu-open");
    menuBtn.setAttribute("aria-expanded", open);
  });
  document.querySelectorAll(".nav-links a").forEach(function (a) {
    a.addEventListener("click", function () {
      document.body.classList.remove("menu-open");
      menuBtn.setAttribute("aria-expanded", "false");
    });
  });

  // Einblend-Animationen
  var reveals = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); }
      });
    }, { threshold: 0.12, rootMargin: "0px 0px -40px 0px" });
    reveals.forEach(function (el) { io.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add("in"); });
  }

  // Lichtschein auf Karten folgt der Maus
  document.querySelectorAll(".card").forEach(function (card) {
    card.addEventListener("pointermove", function (e) {
      var r = card.getBoundingClientRect();
      card.style.setProperty("--mx", e.clientX - r.left + "px");
      card.style.setProperty("--my", e.clientY - r.top + "px");
    });
  });

  // Preisrechner
  var current = 1;
  var switchEl = document.querySelector(".device-switch");
  if (switchEl) {
  var glider = switchEl.querySelector(".switch-glider");
  var buttons = switchEl.querySelectorAll("button");

  function moveGlider(btn) {
    glider.style.width = btn.offsetWidth + "px";
    glider.style.transform = "translateX(" + btn.offsetLeft + "px)";
  }

  function renderPrices(devices) {
    var table = PRICES[devices];
    var monthly = table[1];
    document.querySelectorAll(".plan").forEach(function (plan) {
      var months = Number(plan.dataset.months);
      var price = table[months];
      var priceEl = plan.querySelector(".plan-price b");
      var perEl = plan.querySelector(".plan-monthly");
      var saveEl = plan.querySelector(".plan-save");
      var devEl = plan.querySelector(".plan-devices");
      var anim = plan.querySelector(".price-anim");

      anim.classList.add("swap");
      setTimeout(function () {
        priceEl.textContent = euro(price);
        devEl.textContent = deviceLabel(devices);
        if (months === 1) {
          perEl.textContent = "einmalig, ohne Verlängerung";
          saveEl.textContent = "";
        } else {
          perEl.textContent = "nur " + euro(Math.round((price / months) * 100) / 100) + " € pro Monat";
          var save = Math.round((1 - price / (monthly * months)) * 100);
          saveEl.textContent = save > 0 ? "Sie sparen " + save + " %" : "";
        }
        anim.classList.remove("swap");
      }, 160);

      plan.querySelector(".plan-btn").href = checkoutUrl(devices, months);
    });
  }

  buttons.forEach(function (btn) {
    btn.addEventListener("click", function () {
      buttons.forEach(function (b) { b.classList.remove("active"); b.setAttribute("aria-selected", "false"); });
      btn.classList.add("active");
      btn.setAttribute("aria-selected", "true");
      moveGlider(btn);
      btn.scrollIntoView({ block: "nearest", inline: "center", behavior: "smooth" });
      current = Number(btn.dataset.devices);
      renderPrices(current);
    });
  });
  window.addEventListener("resize", function () { moveGlider(switchEl.querySelector("button.active")); });
  window.addEventListener("load", function () { moveGlider(switchEl.querySelector("button.active")); });
  moveGlider(switchEl.querySelector("button.active"));
  renderPrices(current);

  }

  // Alle WhatsApp-/E-Mail-Links mit der Konfiguration füllen
  document.querySelectorAll("[data-wa]").forEach(function (a) {
    a.href = waLink(a.dataset.wa || "Hallo IPTV Welt Premium, ich habe eine Frage.");
    a.target = "_blank";
    a.rel = "noopener";
  });
  document.querySelectorAll("[data-mail]").forEach(function (a) {
    a.href = "mailto:" + CONFIG.email;
    if (!a.children.length && a.textContent.trim() === "") a.textContent = CONFIG.email;
  });

  document.querySelectorAll("[data-wa-display]").forEach(function (el) { el.textContent = CONFIG.whatsappDisplay; });

  // Preisübersicht (alle Kombinationen)
  var matrix = document.querySelector("[data-matrix]");
  if (matrix) {
    [1, 3, 6, 12].forEach(function (m) {
      var tr = document.createElement("tr");
      if (m === 12) tr.className = "best";
      var html = "<td>" + DURATION_LABEL[m] + (m === 12 ? " 🏆" : "") + "</td>";
      for (var d = 1; d <= 5; d++) {
        var price = PRICES[d][m];
        html += '<td><a class="matrix-buy" href="' + checkoutUrl(d, m) + '" aria-label="' +
          DURATION_LABEL[m] + ", " + deviceLabel(d) + " für " + euro(price) + ' € bestellen"><b>' + euro(price) +
          " €</b><small>" + (m === 1 ? "einmalig" : euro(Math.round((price / m) * 100) / 100) + " €/Monat") + "</small></a></td>";
      }
      tr.innerHTML = html;
      matrix.appendChild(tr);
    });
  }

  // Hero-Slideshow
  var slides = document.querySelectorAll(".hero-slide");
  if (slides.length) {
  var heroDots = document.querySelectorAll(".hero-dots button");
  var si = 0, heroTimer;
  function showSlide(i) {
    slides[si].classList.remove("active"); heroDots[si].classList.remove("active");
    si = i;
    slides[si].classList.add("active"); heroDots[si].classList.add("active");
  }
  function startHero() {
    clearInterval(heroTimer);
    if (!reduceMotion) heroTimer = setInterval(function () { showSlide((si + 1) % slides.length); }, 6000);
  }
  heroDots.forEach(function (d, i) { d.addEventListener("click", function () { showSlide(i); startHero(); }); });
  startHero();
  }

  // Highlights-Slider
  var slider = document.querySelector(".slider");
  if (slider) {
    var bar = document.querySelector(".slider-progress i");
    var step = function () { var s = slider.querySelector(".slide"); return s ? s.offsetWidth + 18 : 300; };
    var updateBar = function () {
      var max = slider.scrollWidth - slider.clientWidth;
      var vis = slider.clientWidth / slider.scrollWidth;
      bar.style.width = Math.max(vis * 100, 12) + "%";
      bar.style.marginLeft = (max > 0 ? (slider.scrollLeft / max) * (100 - Math.max(vis * 100, 12)) : 0) + "%";
    };
    var go = function (dir) {
      var max = slider.scrollWidth - slider.clientWidth - 4;
      if (dir > 0 && slider.scrollLeft >= max) slider.scrollTo({ left: 0 });
      else slider.scrollBy({ left: dir * step() });
    };
    document.querySelectorAll(".slider-btn").forEach(function (b) {
      b.addEventListener("click", function () { go(Number(b.dataset.dir)); });
    });
    slider.addEventListener("scroll", updateBar, { passive: true });
    window.addEventListener("resize", updateBar);
    updateBar();
    var paused = false;
    ["pointerenter", "focusin", "touchstart"].forEach(function (ev) { slider.addEventListener(ev, function () { paused = true; }, { passive: true }); });
    ["pointerleave", "focusout"].forEach(function (ev) { slider.addEventListener(ev, function () { paused = false; }); });
    if (!reduceMotion) setInterval(function () {
      var r = slider.getBoundingClientRect();
      if (!paused && r.top < innerHeight && r.bottom > 0) go(1);
    }, 4000);
  }

  // Kundenstimmen-Slider
  var reviewSec = document.getElementById("bewertungen");
  if (reviewSec && REVIEWS.length) {
    reviewSec.hidden = false;
    var track = reviewSec.querySelector(".review-track");
    var dotsEl = reviewSec.querySelector(".review-dots");
    var esc = function (t) { var d = document.createElement("div"); d.textContent = t; return d.innerHTML; };
    track.innerHTML = REVIEWS.map(function (r) {
      return '<div class="review"><div class="review-card"><div class="review-stars">' + "★★★★★".slice(0, r.stars || 5) +
        "</div><p>„" + esc(r.text) + '“</p><div class="review-author"><span class="review-avatar">' + esc(r.name.charAt(0)) +
        "</span><span>" + esc(r.name) + "<small>" + esc(r.city || "") + "</small></span></div></div></div>";
    }).join("");
    var perView = function () { return innerWidth <= 640 ? 1 : innerWidth <= 1080 ? 2 : 3; };
    var ri = 0;
    var pages = function () { return Math.max(1, REVIEWS.length - perView() + 1); };
    var renderDots = function () {
      dotsEl.innerHTML = "";
      for (var i = 0; i < pages(); i++) {
        var b = document.createElement("button");
        b.setAttribute("aria-label", "Bewertung " + (i + 1));
        b.addEventListener("click", (function (n) { return function () { goReview(n); }; })(i));
        dotsEl.appendChild(b);
      }
    };
    var goReview = function (n) {
      ri = (n + pages()) % pages();
      track.style.transform = "translateX(" + (-ri * 100 / perView()) + "%)";
      dotsEl.querySelectorAll("button").forEach(function (b, i) { b.classList.toggle("active", i === ri); });
    };
    renderDots(); goReview(0);
    window.addEventListener("resize", function () { renderDots(); goReview(Math.min(ri, pages() - 1)); });
    if (!reduceMotion) setInterval(function () { goReview(ri + 1); }, 5500);
  }

  // Interaktive Schritte
  var stepsEl = document.querySelector("[data-steps]");
  if (stepsEl) {
    var stepItems = stepsEl.querySelectorAll(".step");
    var line = stepsEl.querySelector(".steps-line i");
    var sti = 0, stepTimer;
    var setStep = function (i) {
      sti = i;
      stepItems.forEach(function (el, k) { el.classList.toggle("active", k === i); });
      line.style.width = ((i + 1) / stepItems.length) * 100 + "%";
    };
    var runSteps = function () {
      clearInterval(stepTimer);
      if (!reduceMotion) stepTimer = setInterval(function () { setStep((sti + 1) % stepItems.length); }, 3000);
    };
    stepItems.forEach(function (el, k) { el.addEventListener("click", function () { setStep(k); runSteps(); }); });
    setStep(0); runSteps();
  }

  // Mobile Schnellzugriff-Leiste (nicht auf Formularseiten)
  var mcta = document.querySelector(".mobile-cta");
  if (mcta) {
    if (document.querySelector(".trial-page")) {
      mcta.remove();
    } else {
      document.body.classList.add("has-mobile-cta");
      var onMcta = function () { mcta.classList.toggle("show", window.scrollY > 480); };
      window.addEventListener("scroll", onMcta, { passive: true });
      onMcta();
    }
  }

  // Paket-Karussell (Handy): Punkte zeigen die aktuelle Karte
  var plansEl = document.querySelector("[data-plans]");
  var plansDots = document.querySelectorAll(".plans-dots i");
  if (plansEl && plansDots.length) {
    plansEl.addEventListener("scroll", function () {
      var card = plansEl.querySelector(".plan");
      var idx = Math.round(plansEl.scrollLeft / (card.offsetWidth + 14));
      plansDots.forEach(function (d, k) { d.classList.toggle("active", k === idx); });
    }, { passive: true });
  }

  // Nach-oben-Button
  var toTop = document.querySelector(".to-top");
  window.addEventListener("scroll", function () { toTop.classList.toggle("show", window.scrollY > 900); }, { passive: true });
  toTop.addEventListener("click", function () { window.scrollTo({ top: 0 }); });

  // Bestellseite: Paket aus der Adresse lesen
  var order = null;
  var summary = document.querySelector("[data-order-summary]");
  if (summary) {
    var q = new URLSearchParams(location.search);
    var od = Number(q.get("geraete")), om = Number(q.get("laufzeit"));
    if (!PRICES[od]) od = 1;
    if (!PRICES[1][om]) om = 12;
    var op = PRICES[od][om];
    order = { devices: od, months: om, price: op };
    summary.querySelector("[data-order-title]").textContent = DURATION_LABEL[om] + " · " + deviceLabel(od);
    summary.querySelector("[data-order-price]").textContent = euro(op);
    summary.querySelector("[data-order-meta]").textContent = (om === 1 ? "einmalig" : "nur " + euro(Math.round((op / om) * 100) / 100) + " € pro Monat") +
      " · keine automatische Verlängerung";
    summary.querySelector("[data-order-bonus]").hidden = om !== 12;
    document.title = DURATION_LABEL[om] + ", " + deviceLabel(od) + " – Bestellung – IPTV Welt Premium";
  }

  // Formulare „Kostenlos testen“ und Bestellung
  var trialForm = document.querySelector("[data-trial-form]");
  if (trialForm) {
    // Ländervorwahlen: Deutschland zuerst und vorausgewählt, danach alle Länder alphabetisch
    var DIAL = "AF93 AL355 DZ213 AS1684 AD376 AO244 AI1264 AG1268 AR54 AM374 AW297 AU61 AT43 AZ994 BS1242 BH973 BD880 BB1246 BY375 BE32 BZ501 BJ229 BM1441 BT975 BO591 BA387 BW267 BR55 VG1284 BN673 BG359 BF226 BI257 KH855 CM237 CA1 CV238 KY1345 CF236 TD235 CL56 CN86 CO57 KM269 CG242 CD243 CK682 CR506 CI225 HR385 CU53 CW599 CY357 CZ420 DK45 DJ253 DM1767 DO1809 EC593 EG20 SV503 GQ240 ER291 EE372 SZ268 ET251 FO298 FJ679 FI358 FR33 GF594 PF689 GA241 GM220 GE995 DE49 GH233 GI350 GR30 GL299 GD1473 GP590 GU1671 GT502 GG44 GN224 GW245 GY592 HT509 HN504 HK852 HU36 IS354 IN91 ID62 IR98 IQ964 IE353 IM44 IL972 IT39 JM1876 JP81 JE44 JO962 KZ7 KE254 KI686 XK383 KW965 KG996 LA856 LV371 LB961 LS266 LR231 LY218 LI423 LT370 LU352 MO853 MG261 MW265 MY60 MV960 ML223 MT356 MH692 MQ596 MR222 MU230 YT262 MX52 FM691 MD373 MC377 MN976 ME382 MS1664 MA212 MZ258 MM95 NA264 NR674 NP977 NL31 NC687 NZ64 NI505 NE227 NG234 KP850 MK389 NO47 OM968 PK92 PW680 PS970 PA507 PG675 PY595 PE51 PH63 PL48 PT351 PR1787 QA974 RE262 RO40 RU7 RW250 KN1869 LC1758 VC1784 WS685 SM378 ST239 SA966 SN221 RS381 SC248 SL232 SG65 SX1721 SK421 SI386 SB677 SO252 ZA27 KR82 SS211 ES34 LK94 SD249 SR597 SE46 CH41 SY963 TW886 TJ992 TZ255 TH66 TL670 TG228 TO676 TT1868 TN216 TR90 TM993 TC1649 TV688 UG256 UA380 AE971 GB44 US1 UY598 UZ998 VU678 VA39 VE58 VN84 VI1340 YE967 ZM260 ZW263";
    var regionName = function (c) {
      try { return new Intl.DisplayNames(["de"], { type: "region" }).of(c) || c; } catch (e) { return c; }
    };
    var flag = function (c) { return String.fromCodePoint.apply(null, c.split("").map(function (ch) { return 127397 + ch.charCodeAt(0); })); };
    var countries = DIAL.split(" ").map(function (t) { return { code: t.slice(0, 2), dial: t.slice(2), name: regionName(t.slice(0, 2)) }; });
    var de = countries.filter(function (c) { return c.code === "DE"; })[0];
    var rest = countries.filter(function (c) { return c.code !== "DE"; }).sort(function (a, b) { return a.name.localeCompare(b.name, "de"); });
    var sel = trialForm.querySelector("[data-country-select]");
    [de].concat(rest).forEach(function (c, k) {
      var o = document.createElement("option");
      o.value = c.code + ":+" + c.dial;
      o.textContent = flag(c.code) + " " + c.name + " (+" + c.dial + ")";
      if (k === 0) o.selected = true;
      sel.appendChild(o);
    });

    var errEl = trialForm.querySelector("[data-form-error]");
    var success = document.querySelector("[data-trial-success]");
    var showError = function (msg) { errEl.textContent = msg; errEl.hidden = !msg; };
    trialForm.addEventListener("submit", function (e) {
      e.preventDefault();
      var f = trialForm.elements;
      var data = {
        firstName: f.firstName.value.trim(),
        email: f.email.value.trim(),
        country: f.dial.value.split(":")[0],
        dial: f.dial.value.split(":")[1],
        phone: f.phone.value.replace(/[^\d]/g, "").replace(/^0+/, ""),
        notes: f.notes.value.trim(),
        website: f.website.value
      };
      if (order) { data.devices = order.devices; data.months = order.months; }
      var bad = {
        firstName: !data.firstName,
        email: !/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(data.email),
        phone: data.phone.length < 5 || data.phone.length > 15
      };
      Object.keys(bad).forEach(function (k) { f[k].classList.toggle("invalid", bad[k]); });
      if (bad.firstName || bad.email || bad.phone) {
        showError("Bitte füllen Sie Vorname, eine gültige E-Mail-Adresse und Ihre Handynummer aus.");
        return;
      }
      showError("");
      var btn = trialForm.querySelector("button[type=submit]");
      btn.disabled = true;
      var countryName = regionName(data.country);
      // Bestellungen: zuerst über /api/order (Resend), bei einem Fehler über EmailJS
      var sendViaEmailjs = function () {
        return fetch("https://api.emailjs.com/api/v1.0/email/send", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            service_id: CONFIG.emailjs.service,
            template_id: CONFIG.emailjs.template,
            user_id: CONFIG.emailjs.publicKey,
            template_params: {
              site_name: "IPTV Welt Premium",
              plan: DURATION_LABEL[order.months] + ", " + deviceLabel(order.devices) + " – " + euro(order.price) + " €" +
                (order.months === 12 ? " (inkl. IBO Player Pro Premium Abo)" : ""),
              price: euro(order.price) + " €",
              device: deviceLabel(order.devices),
              name: data.firstName,
              from_name: data.firstName,
              from_email: data.email,
              email: data.email,
              phone: data.dial + " " + data.phone,
              country: countryName + " (" + data.country + ")",
              message: data.notes || "–",
              time: new Date().toLocaleString("de-DE")
            }
          })
        }).then(function (r) { if (!r.ok) throw new Error(r.status); return {}; });
      };
      var request = order
        ? fetch("/api/order", { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(data) })
            .then(function (r) { if (!r.ok) throw new Error(r.status); return {}; })
            .catch(sendViaEmailjs)
        : fetch("/api/trial", { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(data) })
            .then(function (r) {
              if (r.status === 409) { var e = new Error("used"); e.used = true; throw e; }
              if (!r.ok) throw new Error(r.status);
              return r.json();
            });
      request
        .then(function () {
          trialForm.hidden = true;
          success.querySelector("[data-success-email]").textContent = data.email;
          success.hidden = false;
          success.focus();
          window.scrollTo({ top: 0 });
        })
        .catch(function (err) {
          btn.disabled = false;
          var text = (order ? "Hallo IPTV Welt Premium, ich möchte bestellen: " + DURATION_LABEL[order.months] + ", " +
            deviceLabel(order.devices) + " für " + euro(order.price) + " €." : "Hallo IPTV Welt Premium, ich möchte einen kostenlosen Test.") + "\nVorname: " + data.firstName +
            "\nE-Mail: " + data.email + "\nTelefon: " + data.dial + " " + data.phone + (data.notes ? "\nNotizen: " + data.notes : "");
          var wa = '<a href="' + waLink(text) + '" target="_blank" rel="noopener">WhatsApp</a>';
          errEl.innerHTML = err && err.used
            ? "Für diese E-Mail-Adresse oder Telefonnummer wurde bereits ein Testzugang erstellt. Schreiben Sie uns gern per " + wa + "."
            : "Das hat leider nicht geklappt. Bitte versuchen Sie es erneut oder schreiben Sie uns per " + wa + ".";
          errEl.hidden = false;
        });
    });
  }

  // Datenschutz-Hinweis
  var cookie = document.querySelector(".cookie");
  if (cookie && !safeGet("cookie_ok")) {
    cookie.hidden = false;
    cookie.querySelector("[data-cookie]").addEventListener("click", function (e) {
      e.preventDefault();
      cookie.hidden = true;
      safeSet("cookie_ok", "1");
    });
  }

  var year = document.getElementById("year");
  if (year) year.textContent = new Date().getFullYear();
})();
