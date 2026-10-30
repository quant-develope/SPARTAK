# Πισίνα Προκάτ Ελλάδα (Pisina Prokat Greece): second Spartakos pools site

Live: https://spartak.unknwn-creation.workers.dev/ (Cloudflare Worker `spartak`).
Every push to `main` deploys through Cloudflare Workers Builds (`npx wrangler deploy`, see `wrangler.jsonc`).

## Layout

- `src/build.py`: static site generator. Run `python3 src/build.py` (needs Pillow); it rewrites `site/`.
- `src/parts.py`: header, footer, quote form, calculator, schema, contact details, `DOMAIN`.
- `src/el_main.py`, `src/el_build.py`, `src/el_more.py`: Greek pages. `src/en_pages.py`: English pages (`/en/`).
- `src/photos/`: source photos (owner's own, same set as spartakos-pisina.com, renamed). The build makes WebP 480/960/1600 and a 1200×630 og image in `site/img/`.
- `src/static/`: CSS, JS, icons.
- `site/`: built output, committed, served as static assets.
- `worker.js`: serves `site/` and handles `POST /api/lead` (quote form). Leads are emailed to pisina.gr@gmail.com
  from form@spartakos-pisina.com through Cloudflare Email Routing of the spartakos-pisina.com zone (same as site 1).

## Content rules (owner)

Prefab pools only, never concrete pools. No prices, only "price on request". Light theme. Texts must not repeat
spartakos-pisina.com: write new wording for every page. Commit `src/` and `site/` together.
