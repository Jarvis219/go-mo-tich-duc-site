#!/usr/bin/env python3
"""Generates every page of the site: landing (vi at /, en at /en/), privacy and support
(bilingual with #vi / #en anchors), 404, sitemap.xml and robots.txt.

    python3 scripts/build_pages.py

All copy lives in this file. Links are relative so the site works under /go-mo-tich-duc-site/.
"""
import hashlib
import html
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
BASE = "https://jarvis219.github.io/go-mo-tich-duc-site/"
EMAIL = "jarvis.219.studio@gmail.com"
EFFECTIVE_VI = "21/10/2026"
EFFECTIVE_EN = "October 21, 2026"
CSS_VERSION = hashlib.sha1((ROOT / "assets/style.css").read_bytes()).hexdigest()[:8]
FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
         '<link href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;500;600'
         '&family=Lora:wght@400;500&display=swap" rel="stylesheet">')

COPY = {
    "vi": {
        "lang": "vi", "name": "Gõ Mõ Tích Đức", "path": "",
        "title": "Gõ Mõ Tích Đức · Gõ một cái, +1 công đức",
        "description": "App gõ mõ vô tri cho dân văn phòng: mỗi cú cốc +1 công đức, lắc máy là mang nghiệp, tiêu công đức ở Chùa Shop. Miễn phí, offline, không quảng cáo.",
        "eyebrow": "App iOS · miễn phí",
        "tagline": "Nút xả stress 5 giây giữa hai cuộc họp. Gõ một cái, +1 công đức. Có sổ sách đàng hoàng.",
        "store": "Sắp có trên App Store", "store_small": "iPhone & iPad · iOS 17+",
        "support": "Hỗ trợ",
        "pills": ["Không quảng cáo", "Không tài khoản", "Offline 100%", "Tiếng Việt · English"],
        "tap_hint": "Gõ thử đi", "tap_count": "công đức (gõ thử)", "float": "+1 công đức", "float_lucky": "+100 Phật thấy rồi",
        "steps_title": "Cách tích đức",
        "steps": [
            ("mo_wood", "Gõ mõ", "Mỗi cú cốc là +1 công đức. Thỉnh thoảng +5 \"gõ có tâm\", hiếm hơn nữa +100 \"Phật thấy rồi\"."),
            ("mascot_dizzy", "Lắc hay Xả là nghiệp", "Lắc máy hoặc bấm Xả: −1 công đức, +1 nghiệp. Gõ 10 cú trong 10 giây để sám hối."),
            ("mascot_shop", "Tiêu ở Chùa Shop", "Công đức là tiền tệ duy nhất: mõ vàng, mõ RGB, tiếng ting ting chuyển khoản. Danh hiệu không bao giờ tụt."),
        ],
        "features_title": "Vô tri nhưng có sổ sách",
        "features": [
            ("item_charm", "Sổ nghiệp", "Thu, chi, số dư tâm linh mỗi ngày. Ghi chú vì sao xả, phóng sinh công đức cho nhẹ lòng."),
            ("rank_4", "Danh hiệu & thành tựu", "Từ Người phàm tới Bồ Tát đi làm 8 tiếng. 29 thành tựu, có cái phải gõ lúc nửa đêm."),
            ("fx_lotus", "Lịch âm", "Rằm và mùng 1 công đức x2, Tết x3. Ngày âm hiện ngay trên màn chính."),
            ("item_xinxam", "540 câu phán", "Hôm nay hợp ăn bún đậu, kỵ mở Excel. Có gói Dev, Thất tình, Thi cử, Tết và quẻ hiếm."),
            ("mascot_chant", "Niệm & hẹn giờ", "Giữ nút Niệm để tự gõ, hoặc hẹn giờ tụng 1, 5, 15 phút, có Live Activity."),
            ("item_incense", "Widget gõ ngoài màn hình", "Gõ mõ ngay trên màn hình chính, mở app là công đức vào sổ."),
        ],
        "shop_title": "Chùa Shop", "shop_sub": "Mua bằng công đức, không bằng tiền.",
        "skins": [("wood", "Mõ gỗ"), ("bamboo", "Mõ tre"), ("red", "Mõ đỏ may mắn"), ("pixel", "Mõ 8-bit"), ("noel", "Mõ Noel"),
                  ("banhchung", "Mõ bánh chưng"), ("jade", "Mõ ngọc bích"), ("rgb", "Mõ RGB gaming"), ("gold", "Mõ vàng ròng"),
                  ("diamond", "Mõ kim cương")],
        "share_title": "Khoe công đức", "share_sub": "Mỗi ngày một tấm sổ công đức, câu phán, danh hiệu, tổng kết năm. Story 9:16 hoặc vuông 1:1.",
        "shots_title": "Trong app",
        "shots": [("home_vi", "Gõ mõ"), ("11_shop", "Chùa Shop"), ("03_ledger", "Sổ và nhiệm vụ"), ("14_quotes", "Kinh thư"), ("02_goal", "Đủ mục tiêu")],
        "promise_title": "Lời hứa của chùa",
        "promise_sub": "Không gì rời khỏi máy bạn. Không bán gì cho bạn.",
        "promise": ["Miễn phí mãi mãi", "Không mua trong app", "Không quảng cáo", "Không theo dõi", "Không tài khoản", "Dữ liệu chỉ trên máy"],
        "faq_title": "Hỏi nhanh",
        "faq": [
            ("App có tốn tiền không?", "Không. Miễn phí hoàn toàn, không mua trong app, không quảng cáo. Mọi thứ trong shop mua bằng công đức gõ ra."),
            ("Công đức có giá trị gì không?", "Không có giá trị gì ngoài giá trị tinh thần và giá trị khoe. App là đồ vô tri, không phải lời khuyên tâm linh."),
            ("Đổi máy có mất công đức không?", "Vào Cài đặt → Xuất backup, hoặc bật sao lưu iCloud của chính bạn. Không có máy chủ nào giữ hộ."),
            ("App có đùa về Phật không?", "Không. Câu đùa là về đời văn phòng, deadline và chính mình. Phật chỉ đứng xem và gật đầu."),
        ],
        "privacy": "Quyền riêng tư", "other_lang": "English", "other_href": "en/",
        "rights": "© 2026 Jarvis 219 Studio. Ảnh minh hoạ và nội dung thuộc về Gõ Mõ Tích Đức.",
    },
    "en": {
        "lang": "en", "name": "Merit Tap", "path": "en/",
        "title": "Merit Tap · Tap once, +1 merit",
        "description": "A deadpan wooden-fish app for office survivors: every knock is +1 merit, shaking the phone adds karma, and the shop only takes merit. Free, offline, no ads.",
        "eyebrow": "iOS app · free",
        "tagline": "A five-second stress button between two meetings. Tap once, +1 merit. With proper bookkeeping.",
        "store": "Coming to the App Store", "store_small": "iPhone & iPad · iOS 17+",
        "support": "Support",
        "pills": ["No ads", "No account", "100% offline", "English · Tiếng Việt"],
        "tap_hint": "Try it", "tap_count": "merit (practice)", "float": "+1 merit", "float_lucky": "+100 The Buddha saw that",
        "steps_title": "How merit works",
        "steps": [
            ("mo_wood", "Tap the fish", "Every knock is +1 merit. Sometimes +5 for a mindful tap, rarely +100 when the Buddha happens to be watching."),
            ("mascot_dizzy", "Shake or vent = karma", "Shake the phone or press Vent: −1 merit, +1 karma. Ten taps in ten seconds to repent."),
            ("mascot_shop", "Spend it at the temple shop", "Merit is the only currency: a gold fish, an RGB gaming fish, a payment-received ding. Your rank never drops."),
        ],
        "features_title": "Pointless, but with a ledger",
        "features": [
            ("item_charm", "Karma ledger", "Earned, lost and the day's spiritual balance. Note why you vented; let merit go when you need to."),
            ("rank_4", "Ranks & badges", "From Mere Mortal to 9-to-5 Bodhisattva. 29 badges, some only after midnight."),
            ("fx_lotus", "Lunar calendar", "Full and new moon days pay x2, Tết x3. The lunar date sits on the home screen."),
            ("item_xinxam", "540 oracles", "Today favors noodles; avoid Excel. Packs for devs, heartbreak, exams, Tết, plus rare fortunes."),
            ("mascot_chant", "Chant & timer", "Hold Chant to tap for you, or set a 1, 5 or 15 minute chant with a Live Activity."),
            ("item_incense", "Tap from the home screen", "An interactive widget; the merit lands in your ledger next time you open the app."),
        ],
        "shop_title": "The temple shop", "shop_sub": "Paid in merit, never in money.",
        "skins": [("wood", "Wooden fish"), ("bamboo", "Bamboo"), ("red", "Lucky red"), ("pixel", "8-bit"), ("noel", "Santa"),
                  ("banhchung", "Bánh chưng"), ("jade", "Jade"), ("rgb", "RGB gaming"), ("gold", "Solid gold"), ("diamond", "Diamond")],
        "share_title": "Show off your merit", "share_sub": "A daily merit ledger, oracles, ranks and a year in review, as 9:16 stories or 1:1 squares.",
        "shots_title": "Inside the app",
        "shots": [("home_en", "Tapping"), ("11_shop", "Temple shop"), ("03_ledger", "Ledger and quests"), ("14_quotes", "Oracle collection"), ("02_goal", "Goal reached")],
        "promise_title": "The temple's promise",
        "promise_sub": "Nothing leaves your phone. Nothing is for sale.",
        "promise": ["Free forever", "No in-app purchases", "No ads", "No tracking", "No account", "Data stays on device"],
        "faq_title": "Quick answers",
        "faq": [
            ("Does it cost anything?", "No. Completely free, no in-app purchases, no ads. Everything in the shop is bought with merit you tap out."),
            ("Is merit worth anything?", "Only emotionally, and for bragging. It's a joke app, not spiritual advice."),
            ("Will I lose merit on a new phone?", "Export a backup from Settings, or turn on backup to your own iCloud. There is no server holding it for you."),
            ("Does it make fun of Buddhism?", "No. The jokes are about office life, deadlines and ourselves. The Buddha only watches and nods."),
        ],
        "privacy": "Privacy", "other_lang": "Tiếng Việt", "other_href": "../",
        "rights": "© 2026 Jarvis 219 Studio. Artwork and copy belong to Merit Tap / Gõ Mõ Tích Đức.",
    },
}

e = html.escape

def head(title, description, canonical, prefix, lang, og, alternates=""):
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(description)}">
<link rel="canonical" href="{canonical}">
{alternates}<meta name="theme-color" content="#F4EEE3">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Gõ Mõ Tích Đức · Merit Tap">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(description)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{BASE}assets/og-{og}.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="{BASE}assets/og-{og}.png">
<link rel="icon" type="image/png" sizes="32x32" href="{prefix}assets/favicon-32.png">
<link rel="apple-touch-icon" href="{prefix}assets/apple-touch-icon.png">
{FONTS}
<link rel="stylesheet" href="{prefix}assets/style.css?v={CSS_VERSION}">
</head>
"""

def topbar(prefix, name, lang_links):
    links = "".join(f'<a href="{href}" hreflang="{code}"{" aria-current=\"true\"" if current else ""}>{label}</a>'
                    for code, label, href, current in lang_links)
    return f"""<div class="wrap top">
  <a class="brand" href="{prefix}"><img src="{prefix}assets/img/icon.webp" width="40" height="40" alt="">{e(name)}</a>
  <nav class="lang-switch" aria-label="Language">{links}</nav>
</div>
"""

def footer(prefix, c, extra_lang=True):
    return f"""<footer>
  <div class="wrap">
    <nav>
      <a href="{prefix}privacy/#{c['lang']}">{c['privacy']}</a>
      <a href="{prefix}support/#{c['lang']}">{c['support']}</a>
      <a href="mailto:{EMAIL}">{EMAIL}</a>
    </nav>
    <div>{e(c['rights'])}</div>
  </div>
</footer>
"""

def landing(c):
    prefix = "" if c["lang"] == "vi" else "../"
    canonical = BASE + c["path"]
    alternates = (f'<link rel="alternate" hreflang="vi" href="{BASE}">\n'
                  f'<link rel="alternate" hreflang="en" href="{BASE}en/">\n'
                  f'<link rel="alternate" hreflang="x-default" href="{BASE}">\n')
    langs = [("vi", "Tiếng Việt", prefix, c["lang"] == "vi"), ("en", "English", f"{prefix}en/", c["lang"] == "en")]
    pills = "".join(f'<span class="pill">{e(p)}</span>' for p in c["pills"])
    steps = "".join(f"""
      <div class="card step"><img src="{prefix}assets/img/{img}.webp" alt="" loading="lazy"><div class="n">0{i + 1}</div><h3>{e(t)}</h3><p class="muted">{e(d)}</p></div>"""
                    for i, (img, t, d) in enumerate(c["steps"]))
    features = "".join(f"""
      <div class="card feature"><img src="{prefix}assets/img/{img}.webp" alt="" loading="lazy"><div><h3>{e(t)}</h3><p>{e(d)}</p></div></div>"""
                       for img, t, d in c["features"])
    skins = "".join(f"""<figure><img src="{prefix}assets/img/mo_{k}.webp" alt="{e(n)}" loading="lazy"><figcaption>{e(n)}</figcaption></figure>"""
                    for k, n in c["skins"])
    cards = "".join(f'<img src="{prefix}assets/cards/{k}_{c["lang"]}.webp" alt="" loading="lazy">' for k in ["day", "quote", "rank", "ach", "year"])
    shots = "".join(f'<img src="{prefix}assets/shots/{k}.webp" alt="{e(n)}" loading="lazy">' for k, n in c["shots"])
    promise = "".join(f"<li>{e(p)}</li>" for p in c["promise"])
    faq = "".join(f"<details><summary>{e(q)}</summary><p>{e(a)}</p></details>" for q, a in c["faq"])
    return head(c["title"], c["description"], canonical, prefix, c["lang"], c["lang"], alternates) + f"""<body>
{topbar(prefix, c['name'], langs)}
<main>
  <div class="wrap hero">
    <div>
      <div class="eyebrow">{e(c['eyebrow'])}</div>
      <h1>{e(c['name'])}</h1>
      <p class="tagline">{e(c['tagline'])}</p>
      <div class="cta">
        <span class="btn primary" aria-disabled="true"><span>{e(c['store'])}<small>{e(c['store_small'])}</small></span></span>
        <a class="btn ghost" href="{prefix}support/#{c['lang']}">{e(c['support'])}</a>
      </div>
      <div class="pills">{pills}</div>
    </div>
    <div class="stage" id="stage" data-float="{e(c['float'])}" data-lucky="{e(c['float_lucky'])}">
      <div class="ring"></div>
      <div class="count"><b id="count">0</b>{e(c['tap_count'])}</div>
      <button type="button" aria-label="{e(c['tap_hint'])}"><img class="mo" src="{prefix}assets/img/mo_wood.webp" alt=""></button>
      <img class="mallet" src="{prefix}assets/img/mallet_left.webp" alt="">
      <img class="tinh" src="{prefix}assets/img/mascot_wave.webp" alt="">
    </div>
  </div>

  <section>
    <div class="wrap">
      <h2>{e(c['steps_title'])}</h2>
      <div class="grid3">{steps}
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>{e(c['features_title'])}</h2>
      <div class="grid2">{features}
      </div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>{e(c['shop_title'])}</h2>
      <p class="muted">{e(c['shop_sub'])}</p>
      <div class="shelf">{skins}</div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>{e(c['share_title'])}</h2>
      <p class="muted">{e(c['share_sub'])}</p>
      <div class="shots cards">{cards}</div>
    </div>
  </section>

  <section>
    <div class="wrap">
      <h2>{e(c['shots_title'])}</h2>
      <div class="shots">{shots}</div>
    </div>
  </section>

  <section class="promise">
    <div class="wrap">
      <img src="{prefix}assets/img/mascot_bliss.webp" alt="" width="180" style="margin:0 auto 10px" loading="lazy">
      <h2>{e(c['promise_title'])}</h2>
      <p class="muted">{e(c['promise_sub'])}</p>
      <ul>{promise}</ul>
    </div>
  </section>

  <section>
    <div class="wrap" style="max-width:760px">
      <h2>{e(c['faq_title'])}</h2>
      {faq}
    </div>
  </section>
</main>
{footer(prefix, c)}
<audio id="knock" src="{prefix}assets/audio/mo.m4a" preload="auto"></audio>
<script>
(() => {{
  const stage = document.getElementById("stage"), count = document.getElementById("count"), knock = document.getElementById("knock");
  let n = 0;
  stage.querySelector("button").addEventListener("pointerdown", (event) => {{
    const lucky = Math.random() < 0.03;
    n += lucky ? 100 : 1;
    count.textContent = n.toLocaleString(document.documentElement.lang);
    stage.classList.remove("hit"); void stage.offsetWidth; stage.classList.add("hit");
    setTimeout(() => stage.classList.remove("hit"), 90);
    try {{ knock.currentTime = 0; knock.play(); }} catch (e) {{}}
    const rect = stage.getBoundingClientRect(), f = document.createElement("span");
    f.className = "float" + (lucky ? " lucky" : "");
    f.textContent = lucky ? stage.dataset.lucky : stage.dataset.float;
    f.style.left = (event.clientX - rect.left) + "px"; f.style.top = (event.clientY - rect.top) + "px";
    stage.appendChild(f); setTimeout(() => f.remove(), 850);
  }});
}})();
</script>
</body>
</html>
"""

PRIVACY = {
    "vi": f"""
<h2>Tóm tắt</h2>
<p><span class="seal">Không thu thập dữ liệu</span></p>
<p>Gõ Mõ Tích Đức không thu thập, không gửi đi và không bán bất kỳ dữ liệu nào của bạn. App không có tài khoản, không có máy chủ, không quảng cáo, không công cụ phân tích hay theo dõi của bên thứ ba.</p>
<h3>Dữ liệu nằm ở đâu</h3>
<ul>
<li>Sổ công đức (số cú gõ, công đức, nghiệp, ghi chú nghiệp, nhiệm vụ, đồ trong shop, câu phán đã mở, cài đặt) được lưu trong bộ nhớ của app trên chính thiết bị của bạn.</li>
<li>Widget đọc một bản tóm tắt nhỏ (công đức hôm nay, chuỗi ngày) qua vùng chia sẻ giữa app và widget trên cùng thiết bị.</li>
<li>Ghi chú nghiệp bạn tự gõ chỉ nằm trên máy, không ai khác đọc được.</li>
</ul>
<h3>Sao lưu</h3>
<ul>
<li><strong>Xuất backup:</strong> chỉ khi bạn bấm, app tạo một file JSON và mở bảng chia sẻ của iOS để bạn tự chọn nơi lưu.</li>
<li><strong>Sao lưu iCloud (tuỳ chọn, mặc định tắt):</strong> nếu bạn bật, bản backup được lưu vào kho iCloud key-value của chính tài khoản Apple của bạn. Chúng tôi không truy cập được dữ liệu này.</li>
</ul>
<h3>Quyền app sử dụng</h3>
<ul>
<li><strong>Chuyển động (Motion):</strong> để nhận biết khi bạn lắc máy (lắc là mang nghiệp). Dữ liệu cảm biến được xử lý ngay trên máy, không lưu, không gửi đi. Tắt được trong Cài đặt.</li>
<li><strong>Thông báo:</strong> nhắc gõ mõ, nhắc giữ chuỗi, nhắc ngày rằm. Đây là thông báo cục bộ do app tự lên lịch trên máy, không qua máy chủ.</li>
</ul>
<h3>Trẻ em</h3>
<p>App phù hợp mọi lứa tuổi và không thu thập dữ liệu của bất kỳ ai, kể cả trẻ em.</p>
<h3>Xoá dữ liệu</h3>
<p>Vào Cài đặt → Hoàn tục để xoá toàn bộ, hoặc xoá app. Nếu đã bật sao lưu iCloud, tắt nó trong app trước, hoặc xoá dữ liệu app trong cài đặt iCloud của iOS.</p>
<h3>Thay đổi chính sách</h3>
<p>Nếu chính sách thay đổi, trang này sẽ được cập nhật kèm ngày hiệu lực mới.</p>
<h3>Liên hệ</h3>
<p><a href="mailto:{EMAIL}">{EMAIL}</a></p>
""",
    "en": f"""
<h2>Summary</h2>
<p><span class="seal">Data Not Collected</span></p>
<p>Merit Tap (Gõ Mõ Tích Đức) does not collect, transmit or sell any of your data. There is no account, no server, no advertising and no third-party analytics or tracking.</p>
<h3>Where your data lives</h3>
<ul>
<li>Your merit ledger (taps, merit, karma, karma notes, quests, shop items, unlocked oracles, settings) is stored in the app's own storage on your device.</li>
<li>The widget reads a small summary (today's merit, streak) through the app group shared between the app and its widget on the same device.</li>
<li>Karma notes you type stay on your device; nobody else can read them.</li>
</ul>
<h3>Backups</h3>
<ul>
<li><strong>Export backup:</strong> only when you tap it, the app creates a JSON file and opens the iOS share sheet so you choose where it goes.</li>
<li><strong>iCloud backup (optional, off by default):</strong> when you turn it on, the backup is stored in the iCloud key-value store of your own Apple account. We cannot access it.</li>
</ul>
<h3>Permissions</h3>
<ul>
<li><strong>Motion:</strong> to notice when you shake the phone (shaking adds karma). Sensor data is processed on the device, never stored or sent. You can turn it off in Settings.</li>
<li><strong>Notifications:</strong> tap nudges, streak reminders and full/new moon mornings. These are local notifications scheduled on the device, with no server involved.</li>
</ul>
<h3>Children</h3>
<p>The app is suitable for all ages and collects no data from anyone, including children.</p>
<h3>Deleting your data</h3>
<p>Use Settings → Leave the temple to erase everything, or delete the app. If iCloud backup is on, turn it off in the app first, or remove the app's data in iOS iCloud settings.</p>
<h3>Changes</h3>
<p>If this policy changes, this page will be updated with a new effective date.</p>
<h3>Contact</h3>
<p><a href="mailto:{EMAIL}">{EMAIL}</a></p>
""",
}

SUPPORT = {
    "vi": [
        ("Gõ mà không nghe tiếng", "Kiểm tra công tắc im lặng bên hông iPhone (app tôn trọng chế độ im lặng), âm lượng, và trong Cài đặt app: Âm thanh đang bật, \"Gõ trong họp (chỉ rung)\" đang tắt."),
        ("Lắc máy mà không tính nghiệp", "Vào Cài đặt → Nghiệp, bật \"Lắc máy là mang nghiệp\" và chỉnh độ nhạy. Mỗi lần lắc cách nhau ít nhất 2 giây mới tính."),
        ("Mất chuỗi ngày", "Chuỗi tính theo ngày đủ mục tiêu. Mỗi 7 ngày liên tiếp app tặng 1 bùa giữ chuỗi (giữ tối đa 2), bùa tự dùng khi bạn lỡ một ngày. Có thể mua thêm ở Chùa Shop."),
        ("Gõ trên widget không thấy cộng", "Cú gõ trên widget được ghi hàng chờ, mở app là công đức vào sổ."),
        ("Tiêu công đức có làm tụt danh hiệu?", "Không. Danh hiệu tính theo công đức tích luỹ (không bao giờ giảm), ví chỉ để mua sắm."),
        ("Chỉnh giờ máy để qua ngày?", "Sổ chỉ đi tới, không đi lùi. Chỉnh giờ lùi lại sẽ không mở lại ngày cũ hay làm mới nhiệm vụ."),
        ("Đổi máy mới", "Cài đặt → Xuất backup trên máy cũ, gửi file sang máy mới rồi Nhập backup. Hoặc bật Sao lưu iCloud rồi Khôi phục từ iCloud trên máy mới."),
        ("Backup báo đã bị sửa", "File backup có chữ ký chống sửa. Nếu file bị chỉnh tay, app sẽ không nhận. Dùng file gốc do app xuất ra."),
    ],
    "en": [
        ("No sound when tapping", "Check the silent switch (the app respects it), the volume, and in the app's Settings: Sound on, \"Meeting mode (vibrate only)\" off."),
        ("Shaking doesn't add karma", "Settings → Karma: turn on \"Shaking adds karma\" and adjust the sensitivity. Shakes less than 2 seconds apart count once."),
        ("I lost my streak", "A streak counts days you reach the goal. Every 7 days in a row gives a streak charm (hold up to 2), used automatically when you miss a day. More in the temple shop."),
        ("Widget taps don't show up", "Taps on the widget are queued; they land in your ledger when you open the app."),
        ("Does spending merit lower my rank?", "No. Ranks follow lifetime merit, which never goes down; the wallet is only for shopping."),
        ("Changing the clock to skip a day?", "The ledger only moves forward. Turning the clock back never reopens a past day or refreshes quests."),
        ("Moving to a new phone", "Settings → Export backup on the old phone, send the file over and Import backup. Or turn on iCloud backup and Restore from iCloud on the new phone."),
        ("The backup says it was edited", "Backups are signed. A hand-edited file is refused; use the original file the app exported."),
    ],
}

def doc_page(kind):
    prefix = "../"
    is_privacy = kind == "privacy"
    title = "Chính sách quyền riêng tư · Privacy Policy — Gõ Mõ Tích Đức" if is_privacy else "Hỗ trợ · Support — Gõ Mõ Tích Đức"
    description = ("Gõ Mõ Tích Đức không thu thập dữ liệu: không tài khoản, không máy chủ, không theo dõi. · Merit Tap collects no data."
                   if is_privacy else "Câu hỏi thường gặp và liên hệ hỗ trợ cho Gõ Mõ Tích Đức (Merit Tap).")
    mascot = "mascot_sleep" if is_privacy else "mascot_wave"
    langs = [("vi", "Tiếng Việt", "#vi", False), ("en", "English", "#en", False)]
    sections = []
    for lang in ("vi", "en"):
        heading = {"vi": ("Chính sách quyền riêng tư" if is_privacy else "Hỗ trợ"),
                   "en": ("Privacy Policy" if is_privacy else "Support")}[lang]
        if is_privacy:
            body = PRIVACY[lang]
            date = f"Hiệu lực từ {EFFECTIVE_VI}" if lang == "vi" else f"Effective {EFFECTIVE_EN}"
            inner = f'<p class="date">{date}</p>{body}'
        else:
            faq = "".join(f"<details><summary>{e(q)}</summary><p>{e(a)}</p></details>" for q, a in SUPPORT[lang])
            contact = ("Không thấy câu trả lời? Gửi email, kèm phiên bản app (Cài đặt → Giới thiệu) và đời iPhone:"
                       if lang == "vi" else "Didn't find it? Email us with the app version (Settings → About) and your iPhone model:")
            inner = f'{faq}<h3>{"Liên hệ" if lang == "vi" else "Contact"}</h3><p>{contact} <a href="mailto:{EMAIL}?subject=G%C3%B5%20M%C3%B5">{EMAIL}</a></p>'
        sections.append(f'<article class="card" id="{lang}" lang="{lang}"><h2>{heading}</h2>{inner}</article>')
    canonical = BASE + kind + "/"
    return head(title, description, canonical, prefix, "vi", "vi") + f"""<body>
{topbar(prefix, "Gõ Mõ Tích Đức", langs)}
<main class="wrap doc">
  <header>
    <img class="mascot" src="{prefix}assets/img/{mascot}.webp" alt="">
    <h1 style="font-size:clamp(32px,6vw,48px)">{"Quyền riêng tư · Privacy" if is_privacy else "Hỗ trợ · Support"}</h1>
    <p class="muted">Gõ Mõ Tích Đức · Merit Tap</p>
  </header>
  {"".join(sections)}
</main>
{footer(prefix, COPY['vi'])}
</body>
</html>
"""

def not_found():
    root = "/go-mo-tich-duc-site/"
    return f"""<!doctype html>
<html lang="vi">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>404 · Gõ Mõ Tích Đức</title>
{FONTS}
<link rel="stylesheet" href="{root}assets/style.css?v={CSS_VERSION}">
</head>
<body>
<main class="wrap doc" style="text-align:center;padding-top:60px">
  <img src="{root}assets/img/mascot_dizzy.webp" alt="" width="200" style="margin:0 auto">
  <h1 style="font-size:44px">404</h1>
  <p>Trang này đã đi tu. · This page has left for the temple.</p>
  <p><a class="btn primary" href="{root}">Về trang chủ · Home</a></p>
</main>
</body>
</html>
"""

def main():
    (ROOT / "index.html").write_text(landing(COPY["vi"]), encoding="utf-8")
    (ROOT / "en/index.html").write_text(landing(COPY["en"]), encoding="utf-8")
    (ROOT / "privacy/index.html").write_text(doc_page("privacy"), encoding="utf-8")
    (ROOT / "support/index.html").write_text(doc_page("support"), encoding="utf-8")
    (ROOT / "404.html").write_text(not_found(), encoding="utf-8")
    urls = ["", "en/", "privacy/", "support/"]
    (ROOT / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
                                      + "".join(f"  <url><loc>{BASE}{u}</loc></url>\n" for u in urls) + "</urlset>\n", encoding="utf-8")
    (ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {BASE}sitemap.xml\n", encoding="utf-8")
    print("pages written")

if __name__ == "__main__":
    main()
