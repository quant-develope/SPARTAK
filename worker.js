// Worker "spartak" (second site): serves site/ as static assets and handles POST /api/lead from the quote form.
// A lead is emailed to the owner through Cloudflare Email Routing (binding LEAD in wrangler.jsonc).
// The sender address must be on the domain, and the destination must be verified in Email Routing.
import { EmailMessage } from "cloudflare:email";

const FROM = "form@spartakos-pisina.com";
const TO = "pisina.gr@gmail.com";
const MAX_FIELD = 2000;

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    if (url.pathname !== "/api/lead") return env.ASSETS.fetch(request);
    if (request.method !== "POST") return json({ success: false, message: "POST only" }, 405);
    const origin = request.headers.get("Origin");
    if (origin && new URL(origin).hostname !== url.hostname) return json({ success: false, message: "bad origin" }, 403);

    let form;
    try { form = await request.formData(); } catch { return json({ success: false, message: "bad form" }, 400); }
    const fields = [];
    for (const [k, v] of form) {
      const value = String(v).trim().slice(0, MAX_FIELD);
      if (!k.startsWith("_") && value) fields.push([k.slice(0, 50), value]);
    }
    const get = (k) => (fields.find((f) => f[0] === k) || [])[1] || "";
    if (form.get("_honey")) return json({ success: true });
    if (!get("Όνομα") || !get("Τηλέφωνο")) return json({ success: false, message: "name and phone required" }, 400);

    const subject = "Νέα αίτηση (spartak): " + get("Όνομα") + (get("Γλώσσα") === "English" ? " (English)" : "");
    const text = fields.map(([k, v]) => k + ": " + v).join("\n") + "\n";
    const replyTo = /^[^\s@<>"]+@[^\s@<>"]+\.[^\s@<>"]+$/.test(get("Email")) ? get("Email") : "";
    const headers = [
      "From: =?UTF-8?B?" + b64("Spartakos Pisines (site 2)") + "?= <" + FROM + ">",
      "To: <" + TO + ">",
      replyTo && "Reply-To: <" + replyTo + ">",
      "Subject: =?UTF-8?B?" + b64(subject) + "?=",
      "Date: " + new Date().toUTCString(),
      "Message-ID: <" + crypto.randomUUID() + "@spartakos-pisina.com>",
      "MIME-Version: 1.0",
      "Content-Type: text/plain; charset=UTF-8",
      "Content-Transfer-Encoding: base64",
    ].filter(Boolean);
    const raw = headers.join("\r\n") + "\r\n\r\n" + b64(text).replace(/.{76}/g, "$&\r\n");

    try {
      await env.LEAD.send(new EmailMessage(FROM, TO, raw));
    } catch (e) {
      console.error("lead email failed", e && e.message);
      return json({ success: false, message: "send failed" }, 502);
    }
    return json({ success: true });
  },
};

function b64(s) {
  let bin = "";
  for (const byte of new TextEncoder().encode(s)) bin += String.fromCharCode(byte);
  return btoa(bin);
}

function json(body, status = 200) {
  return new Response(JSON.stringify(body), { status, headers: { "Content-Type": "application/json" } });
}
