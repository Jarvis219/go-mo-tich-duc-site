#!/usr/bin/env python3
"""Builds every image the site uses into assets/.

Inputs (override with env vars): APP_DIR = the app repo (asset catalog + fonts),
ART_DIR = the 1254 px generated originals, SHOTS_DIR = simulator screenshots
(home_vi.png, home_en.png, 11_shop.png, 03_ledger.png, 14_quotes.png, 02_goal.png).
"""
import os
import pathlib
from PIL import Image, ImageDraw, ImageFont, ImageOps

ROOT = pathlib.Path(__file__).resolve().parent.parent
APP = pathlib.Path(os.environ.get("APP_DIR", ROOT.parent / "go-mo-tich-duc"))
ART = pathlib.Path(os.environ.get("ART_DIR", pathlib.Path.home() / "Downloads/go_mo"))
SHOTS = pathlib.Path(os.environ.get("SHOTS_DIR", ROOT / "raw-shots"))   # the StoreScreenshotTests output dir
# Share cards rendered by the app's ShareCardRenderTests (TEST_RUNNER_SHARE_DIR).
CARDS = pathlib.Path(os.environ.get("CARDS_DIR", ROOT / "raw-cards"))
OUT = ROOT / "assets"
CAT = APP / "GoMo/Resources/Assets.xcassets"
PAPER = (244, 238, 227)
INK = (43, 36, 32)
MUTED = (138, 126, 114)

def art(name):
    """Prefer the 1254 px original; fall back to the app's trimmed copy."""
    for path in [ART / f"{name}.png", *CAT.glob(f"*/{name}.imageset/{name}.png"), *CAT.glob(f"*/{name}.imageset/{name}.jpg")]:
        if path.exists():
            return Image.open(path)
    raise FileNotFoundError(name)

def trim(image):
    image = image.convert("RGBA")
    box = image.getchannel("A").point(lambda a: 255 if a > 24 else 0).getbbox()
    return image.crop(box) if box else image

def webp(image, path, longest, quality=86):
    image = image.copy()
    image.thumbnail((longest, longest), Image.LANCZOS)
    path.parent.mkdir(parents=True, exist_ok=True)
    image.save(path, "WEBP", quality=quality, method=6)

def font(name, size):
    return ImageFont.truetype(str(APP / "GoMo/Resources/Fonts" / name), size)

def og(lang):
    W, H = 1200, 630
    canvas = Image.new("RGB", (W, H), PAPER)
    bg = art("bg_paper").convert("RGB").resize((W, int(W * 1672 / 941)))
    canvas.paste(bg.crop((0, 300, W, 300 + H)), (0, 0))
    mo = trim(art("mo_wood"))
    mo.thumbnail((430, 430))
    canvas.paste(mo, (700, 150), mo)
    tinh = trim(art("mascot_happy"))
    tinh.thumbnail((210, 210))
    canvas.paste(tinh, (600, 390), tinh)
    d = ImageDraw.Draw(canvas)
    title = "Gõ Mõ Tích Đức" if lang == "vi" else "Merit Tap"
    sub = ("Gõ một cái, +1 công đức.\nSổ nghiệp, shop công đức, lịch âm.\nMiễn phí · offline · không quảng cáo."
           if lang == "vi" else "Tap once, +1 merit.\nA karma ledger, a merit-only shop, lunar days.\nFree · offline · no ads.")
    d.text((80, 150), title, font=font("Lora-Medium.ttf", 76), fill=INK)
    d.multiline_text((84, 270), sub, font=font("BeVietnamPro-Regular.ttf", 32), fill=MUTED, spacing=14)
    d.rounded_rectangle([84, 470, 330, 524], radius=27, fill=(107, 68, 38))
    d.text((112, 480), "App Store · iOS", font=font("BeVietnamPro-Medium.ttf", 26), fill=PAPER)
    canvas.save(OUT / f"og-{lang}.png", optimize=True)

def main():
    icon = Image.open(ART / "icon.png" if (ART / "icon.png").exists() else CAT / "AppIcon.appiconset/AppIcon.png").convert("RGB")
    webp(icon, OUT / "img/icon.webp", 256)
    icon.resize((180, 180), Image.LANCZOS).save(OUT / "apple-touch-icon.png")
    icon.resize((32, 32), Image.LANCZOS).save(OUT / "favicon-32.png")
    for mood in ["idle", "happy", "bliss", "sleep", "chant", "enlightened", "wave", "shop", "repent", "dizzy", "sad", "angry"]:
        webp(trim(art(f"mascot_{mood}")), OUT / f"img/mascot_{mood}.webp", 520)
    for skin in ["wood", "red", "jade", "gold", "pixel", "rgb", "diamond", "banhchung", "noel", "bamboo"]:
        webp(trim(art(f"mo_{skin}")), OUT / f"img/mo_{skin}.webp", 560)
    for name in ["mallet", "fx_lotus", "fx_lotus_bloom", "fx_halo", "item_xinxam", "item_incense", "item_charm", "rank_4", "rank_6"]:
        webp(trim(art(name)), OUT / f"img/{name}.webp", 420)
    # The page's mallet hangs head-left over the mõ: mirror the art (head top-left, grip bottom-right).
    webp(trim(art("mallet")).transpose(Image.FLIP_LEFT_RIGHT), OUT / "img/mallet_left.webp", 420)
    webp(art("bg_paper").convert("RGB"), OUT / "img/bg_paper.webp", 1400, quality=80)
    webp(art("bg_mist").convert("RGB"), OUT / "img/bg_mist.webp", 1400, quality=80)
    # iPhone screenshots from the app's StoreScreenshotTests: <SHOTS>/iphone/<lang>-<n>-<name>.png
    for path in sorted((SHOTS / "iphone").glob("*.png")):
        lang, _, name = path.stem.split("-", 2)
        webp(ImageOps.exif_transpose(Image.open(path)).convert("RGB"), OUT / f"shots/{lang}-{name}.webp", 900, quality=82)
    # Widget renders from the app's WidgetRenderTests (docs/store/widgets in the app repo).
    for path in sorted((APP / "docs/store/widgets").glob("*.png")):
        webp(Image.open(path).convert("RGBA"), OUT / f"widgets/{path.stem}.webp", 720, quality=88)
    # <type>.<detail>_story_<lang>.png → cards/<type>_<lang>.webp
    for path in sorted(CARDS.glob("*_story_*.png")):
        kind, lang = path.stem.split(".")[0], path.stem.rsplit("_", 1)[1]
        webp(Image.open(path).convert("RGB"), OUT / f"cards/{kind}_{lang}.webp", 720, quality=84)
    og("vi")
    og("en")
    total = sum(p.stat().st_size for p in OUT.rglob("*") if p.is_file())
    print(f"assets: {total / 1_000_000:.1f} MB")

if __name__ == "__main__":
    main()
