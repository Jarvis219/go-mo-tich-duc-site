# Gõ Mõ Tích Đức · Merit Tap — site

Static GitHub Pages site for the Gõ Mõ Tích Đức iOS app: landing page (`index.html` Vietnamese, `en/` English),
privacy policy (`privacy/`) and support (`support/`), both bilingual with `#vi` / `#en` anchors.

Live: https://jarvis219.github.io/go-mo-tich-duc-site/

- No analytics, no trackers, no external JavaScript. Fonts from Google Fonts (Lora, Be Vietnam Pro). The landing page has
  one small inline script: the tappable wooden fish (plays a CC0 mokugyo knock).
- Links are relative so the site works under `/go-mo-tich-duc-site/`; only `404.html` uses root paths.

## Rebuild

```sh
python3 scripts/build_assets.py   # images from the app repo + generated originals + screenshots + share cards
python3 scripts/build_pages.py    # every page, sitemap.xml, robots.txt (all copy lives in this script)
python3 scripts/check_links.py    # every local href/src exists
```

`build_assets.py` reads `APP_DIR` (default `../go-mo-tich-duc`), `ART_DIR` (default `~/Downloads/go_mo`), `SHOTS_DIR`
(simulator screenshots) and `CARDS_DIR` (PNGs from the app's `ShareCardRenderTests` with `TEST_RUNNER_SHARE_DIR`).
