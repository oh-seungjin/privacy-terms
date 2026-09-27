from pathlib import Path
from html import escape

ROOT = Path(__file__).parent
BASE = "https://oh-seungjin.github.io/privacy-terms/majak-pulse"

PAGES = {
    "privacy": {
        "ko": ("개인정보처리방침", [
            ("운영자와 범위", "대한민국의 넥스트 스튜디오(Next Studio)가 Majak Pulse를 운영합니다. iOS와 Android 앱 식별자는 com.osj.majak입니다. 문의는 dhalska2@gmail.com으로 보내주세요."),
            ("게임 및 계정 데이터", "기기에 완료 횟수, 연속 기록, 무료 힌트, 선택한 테마와 효과음·진동 설정을 저장합니다. Supabase 익명 사용자 ID로 앱을 시작하며 Apple 로그인 시 진행을 계정에 연결할 수 있습니다."),
            ("랭킹과 국가", "랭크 게임 참여 시 서버가 발급한 보드, 제거 순서, 완료 시간, 국가 코드와 계정 식별자를 처리합니다. 공개 랭킹에는 국가 국기와 마스킹된 이메일만 표시하며 전체 이메일과 Apple 로그인 정보는 공개하지 않습니다."),
            ("App Store 구매", "Apple의 거래 ID, 상품 ID, 구매 환경, 구매·환불·환불 취소 상태와 검증 결과를 처리해 힌트, 랭크 도전권, 광고 제거와 테마 권한을 지급하거나 회수합니다. 결제 카드 정보는 앱이나 Next Studio가 직접 수집하지 않습니다. 거래 원장은 중복 지급 방지, 환불 처리와 법적 의무 이행에 필요한 기간 보관될 수 있습니다."),
            ("광고", "모바일 앱은 Google AdMob 전면 광고와 사용자가 선택하는 보상형 광고를 사용합니다. 광고 SDK는 광고 제공·측정·부정 이용 방지를 위해 IP 주소, 대략적 위치, 기기·광고 식별자, 광고 상호작용, 진단 및 동의 상태를 처리할 수 있습니다. 정확한 위치 권한은 요청하지 않습니다."),
            ("앱 분석과 진단", "광고 노출·실패, 힌트 제안, 구매 결과 등 앱 내 이벤트와 오류·진단 정보를 서비스 운영, 장애 대응, 부정 이용 방지와 기능 개선 목적으로 처리할 수 있습니다."),
            ("보유와 삭제", "앱의 데이터 삭제 기능은 Majak Pulse의 서버 데이터와 권한을 삭제합니다. 공용 Apple 신원과 다른 게임 데이터는 삭제 대상이 아닙니다. 중복 보상과 삭제 후 재업로드 방지를 위한 최소 표식은 보관할 수 있습니다."),
            ("처리업체와 권리", "인증·저장에는 Supabase, 광고에는 Google, Apple 로그인에는 Apple, 웹 호스팅에는 GitHub를 사용합니다. 적용 법령에 따른 열람·정정·삭제·동의 철회 요청은 지원 이메일로 접수할 수 있습니다."),
        ]),
        "en": ("Privacy Policy", [
            ("Operator and scope", "Next Studio in the Republic of Korea operates Majak Pulse. The iOS and Android identifier is com.osj.majak. Contact dhalska2@gmail.com."),
            ("Game and account data", "The app stores completion count, streak, free hints, selected theme, sound and haptic settings on the device. It starts with a Supabase anonymous user ID and can link progress through Sign in with Apple."),
            ("Rankings and country", "For ranked games, the server processes the server-issued board, removal sequence, completion time, country code and account identifier. The public leaderboard shows only a country flag and masked email. Full email addresses and Apple sign-in information are not public."),
            ("App Store purchases", "The app processes Apple transaction ID, product ID, purchase environment, purchase, refund and refund-reversal status, and verification results to grant or revoke hints, ranked tickets, ad removal and themes. Neither the app nor Next Studio directly collects payment-card details. The transaction ledger may be retained as needed to prevent duplicate grants, process refunds and meet legal obligations."),
            ("Advertising", "The mobile app uses Google AdMob interstitial ads and optional rewarded ads. The advertising SDK may process IP address, approximate location, device or advertising identifiers, ad interactions, diagnostics and consent state for delivery, measurement and fraud prevention. The app does not request precise location permission."),
            ("App analytics and diagnostics", "The service may process in-app events such as ad impressions and failures, hint offers and purchase results, together with errors and diagnostic information, to operate and improve the service, resolve failures and prevent abuse."),
            ("Retention and deletion", "The in-app deletion action removes Majak Pulse server data and entitlements. A shared Apple identity and data belonging to other games are outside its scope. Minimal markers may remain to prevent duplicate rewards and uploads from a deleted session."),
            ("Processors and rights", "The app uses Supabase for authentication and storage, Google for advertising, Apple for sign-in and GitHub for web hosting. Contact support to exercise access, correction, deletion or consent rights available under applicable law."),
        ]),
    },
    "terms": {
        "ko": ("이용약관", [("서비스", "Majak Pulse는 같은 마작패를 제거하는 퍼즐 게임입니다. 서비스는 예고 후 변경되거나 중단될 수 있습니다."), ("이용 규칙", "광고 보상, 계정 또는 앱을 조작하거나 서비스 운영을 방해해서는 안 됩니다."), ("광고와 외부 서비스", "광고와 로그인에는 Google, Apple 및 Supabase의 별도 약관이 적용될 수 있습니다."), ("면책과 문의", "법이 허용하는 범위에서 서비스는 현 상태로 제공됩니다. 문의는 dhalska2@gmail.com으로 보내주세요.")]),
        "en": ("Terms of Service", [("Service", "Majak Pulse is a tile-matching solitaire puzzle. Features may change or be discontinued after notice where required."), ("Acceptable use", "Do not manipulate ad rewards, accounts or the app, or interfere with service operation."), ("Ads and third parties", "Google, Apple and Supabase terms may separately apply to advertising and sign-in."), ("Disclaimer and contact", "The service is provided as available to the extent permitted by law. Contact dhalska2@gmail.com.")]),
    },
    "support": {
        "ko": ("고객지원", [("게임 방법", "위에 다른 패가 없고 좌우 중 한쪽이 열린 같은 문양의 패 두 개를 선택하세요. 모든 패를 없애면 완료됩니다."), ("도구", "힌트, 되돌리기, 섞기, 재시작을 사용할 수 있습니다. 무료 힌트가 끝나면 선택형 보상 광고로 한 번의 힌트를 받을 수 있습니다."), ("문의", "앱 버전, 기기와 운영체제, 재현 순서를 적어 dhalska2@gmail.com으로 보내주세요. 비밀번호, 인증 코드, 결제 카드 정보는 보내지 마세요.")]),
        "en": ("Support", [("How to play", "Choose two identical tiles that are not covered and have at least one open side. Clear every tile to finish."), ("Tools", "You can use hint, undo, shuffle and restart. After free hints are used, an optional rewarded ad can provide one hint."), ("Contact", "Send the app version, device, operating system and reproduction steps to dhalska2@gmail.com. Never send passwords, authentication codes or payment-card details.")]),
    },
    "delete-account": {
        "ko": ("데이터 삭제 안내", [("앱에서 삭제", "설정에서 Apple 계정에 로그인한 뒤 데이터 삭제를 선택하고 재인증을 완료하세요. Majak Pulse의 진행과 권한만 삭제합니다."), ("이메일 요청", "앱에 접근할 수 없으면 Apple 로그인에 사용한 주소와 Majak Pulse 삭제 요청임을 적어 dhalska2@gmail.com으로 보내세요. 본인 확인이 필요할 수 있습니다."), ("영향 범위", "다른 게임 데이터, 공용 Apple 신원, App Store 거래 기록은 삭제되지 않습니다. 로컬 데이터는 앱 저장 공간 삭제로 제거할 수 있습니다.")]),
        "en": ("Delete Game Data", [("Delete in the app", "Sign in with Apple in Settings, choose the data-deletion action and complete reauthentication. Only Majak Pulse progress and entitlements are removed."), ("Email request", "If the app is unavailable, email dhalska2@gmail.com from or with the address used for Apple sign-in and identify Majak Pulse. Identity verification may be required."), ("Scope", "Other games, the shared Apple identity and App Store transaction history are not deleted. Remove local data through the operating system's app-storage controls.")]),
    },
}

NAV = {"ko": {"index": "홈", "privacy": "개인정보처리방침", "terms": "이용약관", "support": "고객지원", "delete-account": "데이터 삭제"}, "en": {"index": "Home", "privacy": "Privacy", "terms": "Terms", "support": "Support", "delete-account": "Delete data"}}

def render(slug, lang, title, sections):
    suffix = "" if lang == "ko" else "-en"
    links = "".join(f'<a href="{key}{"" if lang == "ko" else "-en"}.html"{(" aria-current=\"page\"" if key == slug else "")}>{label}</a>' for key, label in NAV[lang].items() if key != "index")
    body = "".join(f"<section><h2>{escape(head)}</h2><p>{escape(text)}</p></section>" for head, text in sections)
    other = f"{slug}{'-en' if lang == 'ko' else ''}.html"
    other_label = "English" if lang == "ko" else "한국어"
    return f'''<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Majak Pulse · {escape(title)}</title><meta name="description" content="Majak Pulse · {escape(title)} · Next Studio"><link rel="stylesheet" href="style.css"><link rel="icon" href="icon.png"><link rel="canonical" href="{BASE}/{slug}{suffix}.html"></head><body><main><header><a class="brand" href="index{suffix}.html"><img src="icon.png" width="42" height="42" alt=""> MAJAK PULSE</a><a class="language" href="{other}">{other_label}</a></header><nav>{links}</nav><article><h1>{escape(title)}</h1><p class="date">2026-09-27</p>{body}<aside>Next Studio · 넥스트 스튜디오<br><a href="mailto:dhalska2@gmail.com?subject=Majak%20Pulse%20Support">dhalska2@gmail.com</a></aside></article><footer>© 2026 Next Studio</footer></main></body></html>'''

for slug, languages in PAGES.items():
    for lang, (title, sections) in languages.items():
        suffix = "" if lang == "ko" else "-en"
        (ROOT / f"{slug}{suffix}.html").write_text(render(slug, lang, title, sections), encoding="utf-8")

for lang in ("ko", "en"):
    suffix = "" if lang == "ko" else "-en"
    title = "차분하게 즐기는 마작 솔리테어" if lang == "ko" else "Calm mahjong solitaire"
    intro = "같은 열린 패를 찾아 모든 패를 제거하세요." if lang == "ko" else "Match open tiles and clear the board."
    links = "".join(f'<a class="card" href="{key}{suffix}.html">{label}</a>' for key, label in NAV[lang].items() if key != "index")
    (ROOT / f"index{suffix}.html").write_text(f'<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Majak Pulse</title><link rel="stylesheet" href="style.css"><link rel="icon" href="icon.png"></head><body><main><header><span class="brand"><img src="icon.png" width="42" height="42" alt=""> MAJAK PULSE</span><a class="language" href="index{"-en" if lang == "ko" else ""}.html">{"English" if lang == "ko" else "한국어"}</a></header><article><h1>{title}</h1><p>{intro}</p><div class="grid">{links}</div></article><footer>© 2026 Next Studio · <a href="mailto:dhalska2@gmail.com">dhalska2@gmail.com</a></footer></main></body></html>', encoding="utf-8")
