// Menu, photo viewer, pool calculator and the quote form.
(function () {
  var en = document.documentElement.lang === "en";
  var WA = "306936505824";
  var EMAIL = "pisina.gr@gmail.com";

  // menu: close on link click or outside tap
  var menu = document.querySelector(".menu");
  if (menu) {
    menu.addEventListener("click", function (e) { if (e.target.closest(".menu-panel a")) menu.open = false; });
    document.addEventListener("click", function (e) { if (menu.open && !menu.contains(e.target)) menu.open = false; });
    document.addEventListener("keydown", function (e) { if (e.key === "Escape") menu.open = false; });
  }

  // photo viewer for every a.zoom on the page
  var lb = document.querySelector(".lb");
  var zooms = Array.prototype.slice.call(document.querySelectorAll("a.zoom"));
  var cur = 0;
  function show(i) {
    cur = (i + zooms.length) % zooms.length;
    var a = zooms[cur];
    lb.querySelector("img").src = a.href;
    lb.querySelector("img").alt = a.dataset.cap || "";
    lb.querySelector("figcaption").textContent = a.dataset.cap || "";
    lb.hidden = false;
  }
  if (lb && zooms.length) {
    zooms.forEach(function (a, i) { a.addEventListener("click", function (e) { e.preventDefault(); show(i); }); });
    lb.querySelector(".lb-x").onclick = function () { lb.hidden = true; };
    lb.querySelector(".lb-p").onclick = function () { show(cur - 1); };
    lb.querySelector(".lb-n").onclick = function () { show(cur + 1); };
    lb.addEventListener("click", function (e) { if (e.target === lb) lb.hidden = true; });
    document.addEventListener("keydown", function (e) {
      if (lb.hidden) return;
      if (e.key === "Escape") lb.hidden = true;
      if (e.key === "ArrowLeft") show(cur - 1);
      if (e.key === "ArrowRight") show(cur + 1);
    });
    var x0 = null;
    lb.addEventListener("touchstart", function (e) { x0 = e.touches[0].clientX; }, { passive: true });
    lb.addEventListener("touchend", function (e) {
      if (x0 === null) return;
      var dx = e.changedTouches[0].clientX - x0;
      if (Math.abs(dx) > 50) show(cur + (dx < 0 ? 1 : -1));
      x0 = null;
    });
  }

  // pool calculator
  function fmt(n, d) { return n.toLocaleString(en ? "en-GB" : "el-GR", { maximumFractionDigits: d || 0 }); }
  document.querySelectorAll(".calc").forEach(function (c) {
    var f = function (n) { return c.querySelector("[name=" + n + "]"); };
    var o = function (n) { return c.querySelector("[data-o=" + n + "]"); };
    var water = c.querySelector(".cp-water");
    function run() {
      var L = Math.max(1, parseFloat(String(f("len").value).replace(",", ".")) || 0);
      var W = Math.max(1, parseFloat(String(f("wid").value).replace(",", ".")) || 0);
      var ph = parseFloat(f("ph").value);
      var area = L * W;
      var vol = area * (ph - 0.12);
      var pump = vol / 5; // whole volume through the filter in about 5 hours
      o("area").textContent = fmt(area, 1) + " m²";
      o("vol").textContent = "≈ " + fmt(vol) + " m³";
      o("trucks").textContent = fmt(Math.ceil(vol / 20));
      o("pump").textContent = "≈ " + fmt(pump, 1) + " m³/h";
      o("permit").textContent = area < 50
        ? (en ? "Under 50 m²: small-scale works approval is enough (no building permit), if the plot meets the other conditions."
              : "Κάτω από 50 m²: αρκεί έγκριση εργασιών μικρής κλίμακας, χωρίς οικοδομική άδεια, αν πληρούνται και οι υπόλοιποι όροι.")
        : (en ? "50 m² or more: a building permit is needed. Shrinking the pool slightly can keep it under the limit."
              : "50 m² και πάνω: χρειάζεται οικοδομική άδεια. Συχνά μια μικρή αλλαγή στις διαστάσεις την κρατά κάτω από το όριο.");
      c.classList.toggle("over", area >= 50);
      // drawing: keep the proportions inside a 220 x 110 box
      var s = Math.min(220 / L, 110 / W);
      var w = L * s, h = W * s;
      water.setAttribute("width", w.toFixed(1));
      water.setAttribute("height", h.toFixed(1));
      water.setAttribute("x", ((300 - w) / 2).toFixed(1));
      water.setAttribute("y", ((160 - h) / 2).toFixed(1));
    }
    c.addEventListener("input", run);
    run();
  });

  // quote form: emailed through the site's Worker; WhatsApp, Viber and email as alternatives
  document.querySelectorAll(".qform").forEach(function (form) {
    var res = form.querySelector(".qres");
    var btn = form.querySelector("button[type=submit]");
    var L = en
      ? { name: "Name", phone: "Phone", area: "Area", type: "Interested in", dims: "Size", msg: "Message",
          need: "Please fill in your name and phone.", sending: "Sending…",
          ok: "Thank you! We received your request and will call you soon.",
          fail: "The form could not be sent right now. Please send the same message with one tap:", hi: "Hello, I would like a quote for a pool." }
      : { name: "Όνομα", phone: "Τηλέφωνο", area: "Περιοχή", type: "Τύπος πισίνας", dims: "Διαστάσεις", msg: "Μήνυμα",
          need: "Συμπληρώστε όνομα και τηλέφωνο.", sending: "Αποστολή…",
          ok: "Ευχαριστούμε! Λάβαμε το αίτημά σας και θα σας καλέσουμε σύντομα.",
          fail: "Η αποστολή δεν έγινε αυτή τη στιγμή. Στείλτε το ίδιο μήνυμα με ένα πάτημα:", hi: "Γεια σας, θα ήθελα προσφορά για πισίνα." };
    function val(n) { return String((form.elements[n] || {}).value || "").trim(); }
    function text() {
      var lines = [L.hi];
      ["name", "phone", "area", "type", "dims", "msg"].forEach(function (k) { if (val(k)) lines.push(L[k] + ": " + val(k)); });
      return lines.join("\n");
    }
    function link(via) {
      var t = encodeURIComponent(text());
      if (via === "wa") return "https://wa.me/" + WA + "?text=" + t;
      if (via === "viber") return "viber://chat?number=%2B" + WA + "&draft=" + t;
      return "mailto:" + EMAIL + "?subject=" + encodeURIComponent(en ? "Pool quote request" : "Αίτημα προσφοράς πισίνας") + "&body=" + t;
    }
    function say(html, err) { res.hidden = false; res.className = "full qres" + (err ? " err" : ""); res.innerHTML = html; }
    form.querySelectorAll("[data-via]").forEach(function (b) {
      b.addEventListener("click", function () { window.location.href = link(b.dataset.via); });
    });
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      if (!val("name") || !val("phone")) { say("<p>" + L.need + "</p>", true); return; }
      var d = new FormData();
      // keys are the labels the owner reads in the email (worker.js expects Όνομα and Τηλέφωνο)
      d.append("Όνομα", val("name"));
      d.append("Τηλέφωνο", val("phone"));
      if (val("area")) d.append("Περιοχή", val("area"));
      d.append("Τύπος πισίνας", val("type"));
      if (val("dims")) d.append("Διαστάσεις", val("dims"));
      if (val("msg")) d.append("Μήνυμα", val("msg"));
      d.append("Γλώσσα", en ? "English" : "Ελληνικά");
      d.append("Σελίδα", location.href);
      d.append("_honey", val("_honey"));
      btn.disabled = true;
      var old = btn.textContent;
      btn.textContent = L.sending;
      fetch("/api/lead", { method: "POST", body: d })
        .then(function (r) { return r.json().catch(function () { return {}; }).then(function (j) { if (!r.ok || !j.success) throw 0; }); })
        .then(function () { say("<p>" + L.ok + "</p>"); form.reset(); })
        .catch(function () {
          say("<p>" + L.fail + "</p><a class=\"btn btn-sm\" href=\"" + link("wa") + "\">WhatsApp</a>" +
              "<a class=\"btn btn-sm btn-ghost\" href=\"" + link("viber") + "\">Viber</a>" +
              "<a class=\"btn btn-sm btn-ghost\" href=\"" + link("mail") + "\">Email</a>", true);
        })
        .then(function () { btn.disabled = false; btn.textContent = old; });
    });
  });
})();
