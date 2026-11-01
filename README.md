# Daily Stack website

A simple, fast website: no frameworks, just HTML files. Works on Vercel as-is.

## Files
- `index.html`: the main page (the four boxes first, brand carousel, how it works, FAQ, checkout buttons)
- `thank-you.html`: order confirmation page (use it as the Stripe "after payment" page)
- `terms.html`: terms & conditions outline (have it completed before selling)
- `privacy.html`: privacy policy template
- `impressum.html`: legal notice (required for German visitors)
- `assets/`: logo, favicons, share image; `assets/brands/` for official brand logos
- `vercel.json`: nice URLs (/thank-you instead of /thank-you.html)

## Put it online with Vercel
1. Upload all files to a GitHub repository (github.com → New repository → "uploading an existing file").
2. vercel.com → Sign up with GitHub → Add New → Project → import the repo → Deploy (no build settings).
3. Settings → Domains → add your domain and copy the DNS records to your registrar.
Every time you change a file on GitHub, Vercel updates the site automatically.

## Connect Stripe checkout (no coding)
You need: KVK registration and a business bank account.
1. Create an account at stripe.com and complete the business details.
2. Settings → Payment methods: turn on iDEAL, Cards and SEPA Direct Debit (iDEAL is used for the first payment, then monthly direct debit).
3. Product catalog → Add product, one per box:
   - Foundation Stack €84.95 · recurring · monthly
   - Her Stack €99.95 · recurring · monthly
   - Energy Stack €89.95 · recurring · monthly
   - Winter Stack €69.95 · one-off
4. Payment Links → Create link for each product:
   - Collect customers' shipping address: on, countries Netherlands and Germany
   - After payment: "Don't show confirmation page" → redirect to `https://dailystack-virid.vercel.app/thank-you?box=foundation` (use her / energy / winter for the others)
5. Settings → Billing → Customer portal: turn it on so customers can cancel and update payment details themselves; turn on the portal link in customer emails.
6. Open `index.html`, find `SETTINGS` near the bottom, and paste each payment link into `CHECKOUT`.
Until the links are filled in, the Subscribe buttons show "Checkout opens soon".

## Logos
Put official brand logos (with permission) in `assets/brands/` named `nordic-naturals.png`, `pure-encapsulations.png`, `mattisson.png`, `brand-4.png` … `brand-8.png`. They replace the text names automatically in the box cards and the carousel.

## Fill in before you sell (search for `[` in the files)
- `[BRAND TBC]` products, `[DATE]`, `[X]` working days
- Company details in `terms.html`, `privacy.html`, `impressum.html`
- Prices checked against wholesale costs
- Replace the drawn bottles with official product photos (with permission)
- In `index.html`, change `og:image` to the full URL, e.g. `https://dailystack-virid.vercel.app/assets/og-image-1200x630.png`
- Have the health claims, terms and product information checked (NPN / KOAG-KAG) and make sure each product's label information can be viewed before purchase
