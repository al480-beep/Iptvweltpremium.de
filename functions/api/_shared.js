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
  return { contact };
}
