"""Generate Prism Block Puzzle marketing, privacy, and support pages (ko, en)."""

from html import escape as esc
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SITE = "https://oh-seungjin.github.io/privacy-terms/prism-block-puzzle"
EMAIL = "dhalska2@gmail.com"

LANGUAGES = {
    "ko": {
        "label": "한국어", "html": "ko", "nav": ["소개", "개인정보처리방침", "지원"],
        "tag": "블록을 끌어 놓고 줄을 지워 콤보를 이어가세요",
        "intro": "Prism Block Puzzle은 8×8 보드에 블록 3개를 끌어 놓아 가로·세로 줄을 지우는 퍼즐 게임입니다.",
        "features": ["여러 줄 동시 제거와 콤보 보너스", "자동 저장, 오프라인 플레이", "효과음·BGM·진동을 각각 설정"],
        "offline": "계정 없이 플레이할 수 있고, 게임 진행 상황은 기기에만 저장됩니다. 광고 제거는 1회성 결제입니다.",
        "privacy_title": "Prism Block Puzzle 개인정보처리방침", "date": "시행일: 2026년 11월 14일",
        "privacy_intro": "Prism Block Puzzle은 Next Studio가 제공하는 블록 퍼즐 게임입니다. 계정 없이 사용할 수 있으며 게임 진행 정보는 기기에만 저장합니다.",
        "privacy": [
            ("기기에 저장하는 정보", "점수, 최고 점수, 진행 중인 판, 효과음·BGM·진동 설정, 튜토리얼 확인 여부, 광고 제거 구매 상태를 기기에만 저장합니다. Next Studio는 이 정보를 서버로 전송하지 않습니다."),
            ("광고", "앱은 Google AdMob 광고를 표시합니다. AdMob은 광고 제공·측정·부정 사용 방지를 위해 광고 ID, IP 주소, 기기 정보, 앱 사용 및 진단 정보를 수집할 수 있습니다. 광고 ID는 Android 설정에서 재설정하거나 맞춤 광고를 끌 수 있으며, 자세한 내용은 https://policies.google.com/technologies/ads 에서 확인할 수 있습니다. 광고 제거를 구매하면 광고가 표시되지 않습니다."),
            ("결제", "광고 제거는 Google Play 결제로 처리됩니다. Next Studio는 카드 정보 등 결제 수단 정보를 받지 않으며, 앱은 구매 여부만 확인합니다."),
            ("삭제", "앱을 삭제하거나 기기의 앱 데이터를 지우면 기기에 저장된 정보가 삭제됩니다. 운영체제의 백업·복원 정책의 영향을 받을 수 있습니다. 계정이 없으므로 별도의 계정 삭제 절차는 없습니다."),
            ("아동 및 변경", "이 게임은 만 13세 미만 아동을 대상으로 하지 않으며 아동의 개인정보를 고의로 수집하지 않습니다. 방침이 변경되면 이 페이지의 시행일을 갱신합니다."),
        ],
        "support_title": "Prism Block Puzzle 도움말 및 지원", "support_intro": "게임 중 문제가 있다면 아래 내용을 확인하거나 이메일로 문의해 주세요.",
        "support": [
            ("게임 방법", "하단의 블록을 보드로 끌어 놓으세요. 가로 또는 세로 한 줄이 모두 채워지면 줄이 사라집니다. 연속으로 줄을 지우면 콤보 보너스를 받고, 놓을 곳이 없으면 게임이 끝납니다. 설정에서 게임 방법을 다시 볼 수 있습니다."),
            ("광고 제거 구매·복원", "설정에서 광고 제거를 구매할 수 있습니다. 기기를 바꾸거나 앱을 다시 설치했다면 구매한 Google 계정으로 로그인한 뒤 설정의 구매 복원을 누르세요."),
            ("진행 상황", "진행 상황은 기기에 자동 저장되며 다른 기기로 옮겨지지 않습니다."),
            ("문의할 때", "기기 모델, Android 버전, 앱 버전과 문제를 재현하는 순서를 적어 보내 주세요."),
        ],
        "contact": "문의", "skip": "본문으로 이동", "choose": "언어 선택", "copyright": "© 2026 Next Studio · 넥스트 스튜디오",
    },
    "en": {
        "label": "English", "html": "en", "nav": ["Overview", "Privacy", "Support"],
        "tag": "Drag blocks, clear lines, chain combos",
        "intro": "Prism Block Puzzle is an 8x8 puzzle: drag three blocks onto the board and fill rows or columns to clear them.",
        "features": ["Multi-line clears and combo bonuses", "Auto-save and offline play", "Separate sound, music and vibration settings"],
        "offline": "No account needed. Your progress stays on your device. Removing ads is a one-time purchase.",
        "privacy_title": "Prism Block Puzzle Privacy Policy", "date": "Effective November 14, 2026",
        "privacy_intro": "Prism Block Puzzle is a block puzzle game provided by Next Studio. It works without an account and keeps game progress on your device.",
        "privacy": [
            ("Information stored on your device", "Your score, best score, game in progress, sound, music and vibration settings, whether you have seen the tutorial, and your ad-removal purchase state are stored only on your device. Next Studio does not send this information to a server."),
            ("Advertising", "The app shows ads from Google AdMob. AdMob may collect the advertising ID, IP address, device information, and app usage and diagnostics data to deliver and measure ads and prevent fraud. You can reset your advertising ID or opt out of personalized ads in Android settings; see https://policies.google.com/technologies/ads. If you purchase ad removal, ads are no longer shown."),
            ("Purchases", "Ad removal is processed by Google Play. Next Studio does not receive your payment details; the app only checks whether the purchase was made."),
            ("Deletion", "Uninstalling the app or clearing its data in device settings removes the information stored on your device, subject to system backup and restore behavior. There is no account, so there is no separate account-deletion process."),
            ("Children and changes", "This game is not directed to children under 13 and does not knowingly collect children's personal information. If this policy changes, the effective date on this page will be updated."),
        ],
        "support_title": "Prism Block Puzzle Help & Support", "support_intro": "Review these tips or email us if you need help.",
        "support": [
            ("How to play", "Drag the blocks at the bottom onto the board. A completely filled row or column disappears. Clear lines back to back for combo bonuses; when no block fits, the game ends. You can replay the tutorial from Settings."),
            ("Remove ads: purchase and restore", "You can buy Remove Ads in Settings. If you changed devices or reinstalled, sign in with the Google account that made the purchase and tap Restore purchase in Settings."),
            ("Progress", "Progress is saved automatically on your device and does not transfer to other devices."),
            ("When contacting us", "Include your device model, Android version, app version and steps to reproduce the issue."),
        ],
        "contact": "Contact", "skip": "Skip to content", "choose": "Choose language", "copyright": "© 2026 Next Studio",
    },
}

STYLE = """:root{--bg:#eef2ff;--card:#fff;--ink:#101a40;--muted:#5b6490;--green:#2a49c9;--soft:#dfe6ff;--line:#cfd7f5}*{box-sizing:border-box}body{margin:0;background:radial-gradient(circle at 90% 0,#d5defb 0,transparent 32rem),var(--bg);color:var(--ink);font:16px/1.65 system-ui,-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif}a{color:var(--green)}main{max-width:980px;margin:auto;padding:22px 18px 64px}.skip{position:absolute;left:-9999px}.skip:focus{left:12px;top:12px;background:#fff;padding:10px;z-index:5}.top{display:flex;align-items:center;justify-content:space-between;gap:16px}.brand{display:flex;align-items:center;gap:10px;color:var(--ink);font-weight:900;letter-spacing:.04em;text-decoration:none}.brand img{border-radius:11px}.language{font:inherit;color:var(--ink);background:var(--card);border:1px solid var(--line);border-radius:12px;padding:9px 30px 9px 11px}nav{display:flex;gap:18px;flex-wrap:wrap;margin:24px 0}nav a{font-weight:700;text-decoration:none}nav a[aria-current=page]{text-decoration:underline;text-underline-offset:6px}article{background:var(--card);border:1px solid var(--line);border-radius:28px;padding:clamp(24px,6vw,58px);box-shadow:0 24px 60px #233d2c12}h1{font-size:clamp(2.25rem,6vw,4.2rem);line-height:1.05;letter-spacing:-.045em;margin:.15em 0 .35em}h2{font-size:1.25rem;margin:2em 0 .35em}.lead{font-size:1.15rem;max-width:42rem}.date,.muted{color:var(--muted)}.features{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;padding:0;margin:34px 0;list-style:none}.features li{background:var(--soft);border-radius:18px;padding:20px;font-weight:700}.cards{display:grid;grid-template-columns:repeat(2,1fr);gap:14px;margin-top:32px}.card{border:1px solid var(--line);border-radius:16px;padding:18px;text-decoration:none;font-weight:800}.contact{margin-top:40px;background:var(--soft);border-radius:18px;padding:20px}footer{text-align:center;color:var(--muted);margin-top:30px}.languages{display:flex;flex-wrap:wrap;gap:12px}@media(max-width:680px){main{padding:16px 12px 42px}.features,.cards{grid-template-columns:1fr}article{border-radius:20px;padding:26px 19px}}"""

KINDS = ("index", "privacy", "support")


def nav(data, current):
    return "".join(f'<a href="{kind}.html"' + (' aria-current="page"' if kind == current else "") + f'>{esc(data["nav"][i])}</a>' for i, kind in enumerate(KINDS))


def language_options(current, kind):
    return "".join(f'<option value="../{code}/{kind}.html"' + (' selected' if code == current else "") + f'>{esc(data["label"])}</option>' for code, data in LANGUAGES.items())


def alternates(kind):
    links = "\n".join(f'<link rel="alternate" hreflang="{data["html"]}" href="{SITE}/{code}/{kind}.html">' for code, data in LANGUAGES.items())
    return links + f'\n<link rel="alternate" hreflang="x-default" href="{SITE}/en/{kind}.html">'


def page(code, kind, data):
    if kind == "index":
        title = "Prism Block Puzzle"
        content = f'<p class="muted">BLOCK · PUZZLE · COMBO</p><h1>{esc(data["tag"])}</h1><p class="lead">{esc(data["intro"])}</p><ul class="features">' + "".join(f'<li>{esc(item)}</li>' for item in data["features"]) + f'</ul><p class="lead">{esc(data["offline"])}</p><div class="cards"><a class="card" href="privacy.html">{esc(data["nav"][1])} →</a><a class="card" href="support.html">{esc(data["nav"][2])} →</a></div>'
    else:
        title = data[f"{kind}_title"]
        content = f'<h1>{esc(title)}</h1><p class="date">{esc(data["date"])}</p><p class="lead">{esc(data[f"{kind}_intro"])}</p>'
        content += "".join(f'<section><h2>{i}. {esc(heading)}</h2><p>{esc(text)}</p></section>' for i, (heading, text) in enumerate(data[kind], 1))
        subject = "PrismBlockPuzzle%20Privacy" if kind == "privacy" else "PrismBlockPuzzle%20Support"
        content += f'<aside class="contact"><h2>{esc(data["contact"])}</h2><p>Next Studio · 넥스트 스튜디오<br><a href="mailto:{EMAIL}?subject={subject}">{EMAIL}</a></p></aside>'
    return f'''<!doctype html>
<html lang="{data['html']}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="description" content="Prism Block Puzzle · {esc(title)} · Next Studio"><title>Prism Block Puzzle · {esc(title)}</title>
<link rel="stylesheet" href="../style.css"><link rel="canonical" href="{SITE}/{code}/{kind}.html">
{alternates(kind)}</head><body><a class="skip" href="#content">{esc(data['skip'])}</a><main>
<header class="top"><a class="brand" href="index.html">Prism Block Puzzle</a><label><span class="skip">{esc(data['choose'])}</span><select class="language" aria-label="{esc(data['choose'])}" onchange="location.href=this.value">{language_options(code, kind)}</select></label></header>
<nav aria-label="Prism Block Puzzle">{nav(data, kind)}</nav><article id="content">{content}</article><footer>{esc(data['copyright'])}<br><a href="mailto:{EMAIL}">{EMAIL}</a></footer></main></body></html>'''


for locale, strings in LANGUAGES.items():
    destination = ROOT / locale
    destination.mkdir(exist_ok=True)
    for page_kind in KINDS:
        (destination / f"{page_kind}.html").write_text(page(locale, page_kind, strings), encoding="utf-8")

(ROOT / "style.css").write_text(STYLE, encoding="utf-8")
links = "".join(f'<a href="{code}/index.html" hreflang="{data["html"]}">{esc(data["label"])}</a>' for code, data in LANGUAGES.items())
(ROOT / "index.html").write_text(f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="Prism Block Puzzle official website"><title>Prism Block Puzzle · Next Studio</title><link rel="stylesheet" href="style.css"></head><body><main><header class="top"><span class="brand">Prism Block Puzzle</span></header><article><p class="muted">BLOCK · PUZZLE · COMBO</p><h1>Drag blocks, clear lines, chain combos</h1><p class="lead">Choose your language.</p><div class="cards languages">{links}</div></article><footer>© 2026 Next Studio · 넥스트 스튜디오</footer></main></body></html>''', encoding="utf-8")
print(f"Generated {len(LANGUAGES) * len(KINDS) + 1} pages.")
