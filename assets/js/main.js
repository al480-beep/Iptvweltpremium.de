/* IPTV Welt Premium – Interaktionen */
(function () {
  "use strict";

  // ---- Kontakt-Einstellungen: hier anpassen ----
  var CONFIG = {
    whatsapp: "4900000000000", // internationale Nummer ohne + und Leerzeichen
    email: "info@iptvweltpremium.de"
  };

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
  var waLink = function (text) {
    return "https://wa.me/" + CONFIG.whatsapp + "?text=" + encodeURIComponent(text);
  };

  // Header-Hintergrund beim Scrollen
  var header = document.querySelector(".header");
  var onScroll = function () { header.classList.toggle("scrolled", window.scrollY > 20); };
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

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

      plan.querySelector(".plan-btn").dataset.price = price;
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

  // Bestell-Dialog
  var modal = document.getElementById("order-modal");
  var lastFocus = null;

  function openModal(months) {
    var price = PRICES[current][months];
    modal.querySelector("[data-sum-plan]").textContent = DURATION_LABEL[months];
    modal.querySelector("[data-sum-devices]").textContent = deviceLabel(current);
    modal.querySelector("[data-sum-total]").textContent = euro(price) + " €";
    var text = "Hallo IPTV Welt Premium, ich möchte bestellen:\n" +
      "Paket: " + DURATION_LABEL[months] + "\n" +
      "Geräte: " + deviceLabel(current) + "\n" +
      "Preis: " + euro(price) + " €";
    modal.querySelector("[data-order-wa]").href = waLink(text);
    modal.querySelector("[data-order-mail]").href = "mailto:" + CONFIG.email +
      "?subject=" + encodeURIComponent("Bestellung: " + DURATION_LABEL[months] + ", " + deviceLabel(current)) +
      "&body=" + encodeURIComponent(text);
    lastFocus = document.activeElement;
    modal.classList.add("open");
    modal.setAttribute("aria-hidden", "false");
    document.body.style.overflow = "hidden";
    modal.querySelector(".modal-close").focus();
  }
  function closeModal() {
    modal.classList.remove("open");
    modal.setAttribute("aria-hidden", "true");
    document.body.style.overflow = "";
    if (lastFocus) lastFocus.focus();
  }
  document.querySelectorAll(".plan-btn").forEach(function (btn) {
    btn.addEventListener("click", function () { openModal(Number(btn.closest(".plan").dataset.months)); });
  });
  modal.querySelectorAll("[data-close]").forEach(function (el) { el.addEventListener("click", closeModal); });
  document.addEventListener("keydown", function (e) { if (e.key === "Escape" && modal.classList.contains("open")) closeModal(); });

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

  var year = document.getElementById("year");
  if (year) year.textContent = new Date().getFullYear();
})();
