# EZ Comtrust — Website

Marketing website for **EZ Computer Trust (EZ Comtrust)** — managed IT & cybersecurity for nursing homes and long-term care.

- **Domain:** www.ezcomtrust.com
- **Phone:** 347-893-6504
- **Email:** info@ezcomtrust.com

## Files

| File | Purpose |
|------|---------|
| `index.html` | The full single-page site (hero, services, HIPAA/security, process, testimonials, FAQ, contact). |
| `styles.css` | Design system + all styling, matched to the logo's blue gradient. Fully responsive. |
| `script.js` | Mobile menu, sticky header, scroll animations, FAQ accordion, and lead-form handling. |
| `assets/logo.png` | Your logo (used in header + favicon). |
| `robots.txt`, `sitemap.xml` | SEO. |

## Preview locally

From this folder, run any static server, e.g.:

```bash
python -m http.server 5510
```

Then open http://localhost:5510

## Make the contact form deliver leads to you

The form works in "demo mode" out of the box (shows a success message). To actually **receive submissions by email**, use a free form backend — no server needed:

1. Sign up at **[Formspree](https://formspree.io)** (or Web3Forms / Basin) and create a form. You'll get an endpoint URL like `https://formspree.io/f/abcdwxyz`.
2. Open `script.js` and set:
   ```js
   var FORM_ENDPOINT = 'https://formspree.io/f/abcdwxyz';
   ```
3. Done — submissions now email you, with an automatic `mailto:` fallback.

> Update the destination email in `script.js` (the `mailto:` fallback) and in `index.html` if you use something other than `info@ezcomtrust.com`.

## Deploy (pick one — all support your custom domain)

**Cloudflare Pages / Netlify / Vercel (recommended, free):**
- Drag-and-drop this folder into the dashboard, or connect a Git repo.
- Add the custom domain `www.ezcomtrust.com` and follow the DNS instructions (usually a CNAME record at your registrar).

**Traditional web host (cPanel, etc.):**
- Upload the contents of this folder to the `public_html` (web root) directory.

**GitHub Pages:**
- Push these files to a repo, enable Pages, and add a `CNAME` file containing `www.ezcomtrust.com`.

## Things you may want to edit later

- **Testimonials** (`index.html`) — swap in real client quotes/names once you have permission to use them. They're currently written as representative examples.
- **Tech logos strip** — the "PointClickCare / MatrixCare…" names reflect systems commonly supported; adjust to match what you actually service.
- **Email/social links** — update in the header, contact section, and footer.
