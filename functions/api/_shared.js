// Shared helpers for the form endpoints. Files starting with "_" are not turned into routes by Cloudflare Pages.

export const json = (body, status = 200) =>
  new Response(JSON.stringify(body), { status, headers: { "Content-Type": "application/json; charset=utf-8" } });

export const esc = (s) =>
  String(s).replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));

// Validates the contact fields every form shares. Returns { error } or { contact }.
export async function readContact(request) {
  let d;
  try {
    d = await request.json();
  } catch {
    return { error: json({ error: "bad_request" }, 400) };
  }
  // Bots fill the hidden "website" field; pretend success so they do not retry.
  if (d.website) return { error: json({ ok: true }) };

  const contact = {
    firstName: String(d.firstName || "").trim().slice(0, 60),
    email: String(d.email || "").trim().slice(0, 120),
    country: String(d.country || "").trim().slice(0, 2).toUpperCase(),
    dial: String(d.dial || "").trim(),
    phone: String(d.phone || "").replace(/\D/g, ""),
    notes: String(d.notes || "").trim().slice(0, 1000),
  };
  const c = contact;
  if (!c.firstName || !/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(c.email) || !/^\+\d{1,4}$/.test(c.dial) || c.phone.length < 5 || c.phone.length > 15) {
    return { error: json({ error: "invalid" }, 422) };
  }
  return { contact, data: d };
}

// Sends one e-mail through Resend and returns its id. With scheduled_at set, Resend sends it later.
export async function sendMail(env, msg) {
  const r = await fetch("https://api.resend.com/emails", {
    method: "POST",
    headers: { Authorization: `Bearer ${env.RESEND_API_KEY}`, "Content-Type": "application/json" },
    body: JSON.stringify(msg),
  });
  if (!r.ok) throw new Error(`resend ${r.status}: ${await r.text()}`);
  return (await r.json().catch(() => ({}))).id || "";
}

export async function cancelMail(env, id) {
  const r = await fetch(`https://api.resend.com/emails/${encodeURIComponent(id)}/cancel`, {
    method: "POST",
    headers: { Authorization: `Bearer ${env.RESEND_API_KEY}` },
  });
  if (!r.ok) throw new Error(`resend cancel ${r.status}: ${await r.text()}`);
}

export const mailFrom = (env) => env.TRIAL_FROM || "IPTV Welt Premium <kontakt@iptvweltpremium.de>";
export const mailTo = (env) => env.TRIAL_TO || "kontakt@iptvweltpremium.de";

// The trial a customer got, stored in TRIAL_KV under "e:<email>" and "p:<phone>".
// Older entries hold only an ISO date string.
export async function findTrial(env, email, phone) {
  if (!env.TRIAL_KV) return null;
  for (const k of [`e:${email.toLowerCase()}`, `p:${phone}`]) {
    const v = await env.TRIAL_KV.get(k);
    if (!v) continue;
    try {
      const t = JSON.parse(v);
      if (t && typeof t === "object") return { key: k, ...t };
    } catch {}
    return { key: k, created: v };
  }
  return null;
}
