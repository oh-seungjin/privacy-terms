from pathlib import Path
from html import escape

ROOT = Path(__file__).parent
BASE = "https://oh-seungjin.github.io/privacy-terms/classic-card-game"
EMAIL = "dhalska2@gmail.com"
DATE_EN = "September 27, 2026"
DATE_KO = "2026년 9월 27일"

PAGES = {
    "en": {
        "labels": {"index": "Home", "privacy": "Privacy Policy", "terms": "Terms of Use", "support": "Help & Support", "delete-account": "Delete Data"},
        "skip": "Skip to content", "language": "Language", "date": f"Effective / revised: {DATE_EN}",
        "index": ("Play a timeless classic at your own pace.", "Classic Solitaire: Card Calm official information, policies, and support.", []),
        "privacy": ("Privacy Policy", "This policy explains how Classic Solitaire: Card Calm (com.osj.classiccard) handles information.", [
            ("1. Operator and contact", f"Next Studio (South Korea) operates the app. Privacy inquiries: <a href=\"mailto:{EMAIL}\">{EMAIL}</a>."),
            ("2. Information stored on your device", "The app stores an active game, elapsed time, game settings, language, sound and haptic choices, and local activity records. Local data remains until it is cleared or the app is deleted. Device and cloud backups are controlled by your platform provider."),
            ("3. Supabase account and game data", "The app creates an anonymous Supabase user ID by default. If you choose Apple or Google sign-in, account identifiers, email when supplied by the provider, authentication records, country code, synced preferences and progress, ranked tickets, ranked attempt seeds, ordered gameplay action logs, verified clear times, and leaderboard records may be stored. Ranked action logs are used to validate results and prevent cheating."),
            ("4. Advertising", "The mobile app uses Google AdMob for interstitial and optional rewarded ads. Google may process IP address, approximate location derived from IP, device or advertising identifiers, ad views and interactions, diagnostics, fraud signals, and consent choices. The app does not request precise location. Regional consent controls are provided where required. On iOS, advertising tracking requiring the identifier for advertisers is used only after App Tracking Transparency permission."),
            ("5. Purchases", "If in-app products are offered and you make a purchase, Apple and our verification service may process product and transaction identifiers, purchase environment, verification status, and resulting entitlement or balance. We do not receive payment card details. Availability and displayed products depend on the released build and store configuration."),
            ("6. Analytics, crashes, and notifications", "The current app does not use Firebase Analytics or a separate crash-reporting SDK and does not send push notifications. We will revise this policy before enabling materially different collection."),
            ("7. Purposes and legal basis", "We process information to save and restore game state, authenticate accounts, operate verified rankings, deliver and verify optional ad rewards, verify purchases, prevent abuse, provide support, comply with legal obligations, and improve service reliability. The legal basis depends on the feature and applicable law, including contract performance, consent, legitimate interests, and legal obligations."),
            ("8. Sharing and international processing", "Service providers may process data only for their services: Supabase for authentication and storage; Apple and Google for sign-in, store services, consent, and advertising; GitHub Pages for this website; and Gmail for support inquiries. Their servers may be outside South Korea. This website contains no advertising or analytics scripts, but GitHub may process IP addresses and access logs for hosting and security."),
            ("9. Retention and deletion", "Game account data is retained while needed to provide restoration, ranking, entitlement, security, and legal functions. Completed ranked results may remain until game data deletion. Purchase records involved in disputes or legal duties may be retained as required. Support email is retained only as needed to resolve the inquiry. Store transaction records held by Apple or Google are controlled by those providers."),
            ("10. Your choices and rights", "You can decline optional sign-in, personalized advertising consent, or ATT permission and still use available non-personalized or limited features. Subject to applicable law, you may request access, correction, deletion, portability, restriction, objection, or withdrawal of consent. We may verify identity within a reasonable scope."),
            ("11. Children, security, and changes", "The game does not require users to type personal information into gameplay. We do not knowingly ask children to submit personal information. A guardian may contact us for review or deletion. We use reasonable safeguards but no system is absolutely secure. Material changes will be reflected by updating this page and date."),
        ]),
        "terms": ("Terms of Use", "Terms governing use of Classic Solitaire: Card Calm.", [
            ("1. Service", "The app provides draw-one Klondike solitaire, daily play, local saves, optional account sync, and a verified time-based ranked mode. Ranked mode may require sign-in and a server-issued attempt ticket."),
            ("2. Ranked play", "Ranked tickets refill under the rules shown in the app. A ticket is consumed when a ranked attempt is claimed and is not refunded when you leave early. Hints, undo, auto-move, and resume are disabled in ranked play. Results are accepted only after server replay validation; invalid, altered, expired, duplicate, or unverifiable submissions may be rejected. Equal verified times share rank using competition ranking."),
            ("3. Ads and purchases", "Free play may include interstitial ads and optional rewarded ads. A reward is granted only after server verification where applicable. If products are offered, review the store's current description and local price before purchase. Billing, refunds, and store transaction records are handled under the applicable store rules. There are no subscriptions unless explicitly shown in the store."),
            ("4. Acceptable use", "Use the app for lawful personal purposes. Do not interfere with the service, manipulate ranked logs or timing, automate abuse, evade security, or infringe the rights of others."),
            ("5. Availability and changes", "Online features depend on networks and third-party services and may be interrupted. We may change or discontinue features for maintenance, security, fairness, or legal reasons. The service is provided as-is to the maximum extent permitted by law, without limiting rights that cannot lawfully be excluded."),
            ("6. Intellectual property", "The app's original code, branding, art, and content belong to Next Studio or their respective owners. Generic card-game rules and standard playing-card concepts are not claimed as exclusive property."),
        ]),
        "support": ("Help & Support", "Troubleshooting and contact information.", [
            ("1. How to play", "Build each foundation by suit from Ace through King. On the tableau, place cards in descending rank with alternating colors. Move complete face-up runs, draw from the stock, and reveal face-down cards. In ranked mode, use only manual moves; hints, undo, auto-move, and resume are disabled."),
            ("2. Saves and ranked games", "Casual games save on the device. Sign-in can sync supported progress and enables ranked submission. Ranked attempts consume one ticket when claimed; leaving does not refund it. Tickets refill up to the limit shown in the app. A clear appears on the leaderboard only after the server verifies the full ordered action log."),
            ("3. Ads and rewards", "If an ad fails to load, check your connection and try later. A rewarded-ad view alone does not guarantee a reward: the signed server callback must be verified. Never tap live ads for testing. Privacy choices can be reviewed from the app when the consent provider makes them available."),
            ("4. Purchases and restoration", "Purchase availability depends on platform and store configuration. Use the in-app restore option for restorable App Store purchases. For billing, cancellation, or refunds, use your store's support process. Never email card details or store passwords."),
            ("5. Report a problem", f"Email <a href=\"mailto:{EMAIL}?subject=Classic%20Solitaire%20Support\">{EMAIL}</a> with the app name, app version, device and OS, language, sign-in status, steps to reproduce, and a screenshot with personal information hidden. Do not send passwords, authentication codes, receipts containing unnecessary personal data, or card details."),
        ]),
        "delete-account": ("Delete Game Data", "How to remove local and Classic Solitaire server data.", [
            ("1. Delete from the app", "Open Settings and choose Delete game data. After confirmation and any required Apple reauthentication, the app requests deletion of Classic Solitaire game data and clears this game's local account-scoped data. The shared authentication identity and data belonging to other games are not deleted by this game-specific action."),
            ("2. What is deleted", "Deletion covers Classic Solitaire synced state, ranked attempts and results, profile balances and settings, purchase entitlements recorded for this game, reward records covered by the server procedure, and the game-specific account association, subject to required legal retention. Store transaction records controlled by Apple or Google are not deleted by us."),
            ("3. Delete device data", "On iOS, use Delete App rather than Offload App if you also want local files removed. On Android, use Clear storage for the app or uninstall it. Platform backups may retain copies under your platform account settings."),
            ("4. Request without the app", f"Email <a href=\"mailto:{EMAIL}?subject=Classic%20Solitaire%20Data%20Deletion\">{EMAIL}</a> with the subject “Classic Solitaire Data Deletion,” your sign-in email if applicable, and the scope requested. Do not send a password, authentication code, government ID, or card details. We may request limited verification and will respond within the timeframe required by applicable law."),
        ]),
    },
    "ko": {
        "labels": {"index": "홈", "privacy": "개인정보처리방침", "terms": "이용약관", "support": "고객지원", "delete-account": "게임 데이터 삭제"},
        "skip": "본문 바로가기", "language": "언어", "date": f"시행 및 수정일: {DATE_KO}",
        "index": ("익숙한 클래식을 나만의 속도로 즐기세요.", "클래식 솔리테어: 카드 휴식 공식 정보·정책·고객지원 페이지입니다.", []),
        "privacy": ("개인정보처리방침", "클래식 솔리테어: 카드 휴식(com.osj.classiccard)의 정보 처리 방식을 안내합니다.", [
            ("1. 운영자와 연락처", f"대한민국의 넥스트 스튜디오(Next Studio)가 앱을 운영합니다. 개인정보 문의: <a href=\"mailto:{EMAIL}\">{EMAIL}</a>."),
            ("2. 기기에 저장되는 정보", "진행 중인 게임, 경과 시간, 게임 설정, 언어, 소리·진동 선택과 로컬 활동 기록을 기기에 저장합니다. 로컬 정보는 앱 저장공간을 지우거나 앱을 삭제할 때까지 남을 수 있으며 기기·클라우드 백업은 플랫폼 사업자가 관리합니다."),
            ("3. Supabase 계정과 게임 데이터", "앱은 기본적으로 익명 Supabase 사용자 ID를 만듭니다. Apple 또는 Google 로그인을 선택하면 제공자가 전달한 계정 식별자와 이메일, 인증 기록, 국가 코드, 동기화 설정과 진행 상황, 랭크 도전권, 랭크 시드, 순서가 있는 행동 로그, 검증된 클리어 시간과 리더보드 기록을 저장할 수 있습니다. 랭크 행동 로그는 결과 검증과 부정행위 방지에 사용합니다."),
            ("4. 광고", "모바일 앱은 Google AdMob 전면 광고와 선택형 보상 광고를 사용합니다. Google은 IP 주소, IP로 추정한 대략적 위치, 기기·광고 식별자, 광고 조회·상호작용, 진단·부정행위 방지 신호와 동의 선택을 처리할 수 있습니다. 정확한 위치 권한은 요청하지 않습니다. 필요한 지역에는 동의 선택을 제공하며, iOS 광고 식별자를 이용한 추적은 앱 추적 투명성(ATT)에 동의한 경우에만 수행합니다."),
            ("5. 인앱결제", "출시 빌드에서 인앱 상품을 제공하고 사용자가 구매하면 Apple과 검증 서버가 상품·거래 식별자, 구매 환경, 검증 상태와 지급된 권한·잔액을 처리할 수 있습니다. 결제 카드 정보는 당사가 받지 않습니다. 판매 상품과 이용 가능 여부는 출시 빌드 및 스토어 설정에 따릅니다."),
            ("6. 분석·오류 보고·알림", "현재 앱은 Firebase Analytics나 별도 Crashlytics SDK를 사용하지 않고 푸시 알림을 보내지 않습니다. 실질적으로 다른 수집 기능을 활성화하기 전에 이 방침을 수정합니다."),
            ("7. 처리 목적과 근거", "게임 저장·복구, 계정 인증, 검증된 랭킹 운영, 선택형 광고 보상 확인, 구매 검증, 부정 이용 방지, 고객지원, 법적 의무 준수와 서비스 안정성 확보를 위해 정보를 처리합니다. 구체적 법적 근거는 기능과 적용 법률에 따라 계약 이행, 동의, 정당한 이익 또는 법적 의무가 될 수 있습니다."),
            ("8. 제공업체와 국외 처리", "Supabase는 인증·저장, Apple과 Google은 로그인·스토어·동의·광고, GitHub Pages는 이 웹사이트 호스팅, Gmail은 문의 처리를 위해 정보를 처리할 수 있으며 서버가 대한민국 밖에 있을 수 있습니다. 이 웹페이지에는 광고·분석 스크립트나 입력 폼이 없지만 GitHub는 호스팅과 보안을 위해 IP 주소와 접속 로그를 처리할 수 있습니다."),
            ("9. 보관과 삭제", "계정 복구, 랭킹, 권한, 보안과 법적 기능 제공에 필요한 기간 게임 데이터를 보관합니다. 완료된 랭크 결과는 게임 데이터 삭제 시까지 남을 수 있습니다. 거래 분쟁·법적 의무가 있는 구매 기록은 필요한 기간 보관할 수 있고 문의 메일은 해결에 필요한 기간만 보관합니다. Apple·Google이 보유한 스토어 거래 기록은 각 사업자가 관리합니다."),
            ("10. 선택권과 권리", "선택 로그인, 맞춤 광고 동의 또는 ATT 권한을 거부해도 제공 가능한 비맞춤·제한 기능을 이용할 수 있습니다. 적용 법률에 따라 열람, 정정, 삭제, 이동, 처리 제한, 반대, 동의 철회를 요청할 수 있으며 합리적인 범위에서 본인 확인을 요청할 수 있습니다."),
            ("11. 아동·보안·변경", "게임 플레이 중 개인정보 직접 입력을 요구하지 않으며 아동에게 개인정보 제출을 고의로 요청하지 않습니다. 보호자는 열람·삭제를 문의할 수 있습니다. 합리적 보호조치를 사용하지만 절대적 보안을 보장할 수는 없습니다. 중요한 변경은 이 페이지의 내용과 날짜를 갱신하고 필요한 고지·동의 절차를 제공합니다."),
        ]),
        "terms": ("이용약관", "클래식 솔리테어: 카드 휴식 이용 조건입니다.", [
            ("1. 서비스", "한 장 뽑기 클론다이크 솔리테어, 오늘의 게임, 로컬 저장, 선택적 계정 동기화와 검증된 시간 기준 랭크 모드를 제공합니다. 랭크 모드는 로그인과 서버가 발급한 도전권을 요구할 수 있습니다."),
            ("2. 랭크 게임", "랭크 도전권은 앱에 표시된 규칙으로 충전됩니다. 랭크 시도를 발급받을 때 도전권 1개가 차감되며 중도 이탈해도 반환되지 않습니다. 랭크에서는 힌트·되돌리기·자동 이동·이어하기를 사용할 수 없습니다. 서버 행동 재생 검증을 통과한 기록만 반영하며 변조·불가능·만료·중복·검증 불가 제출은 거절할 수 있습니다. 검증된 시간이 같으면 경쟁 순위 방식의 공동 순위를 적용합니다."),
            ("3. 광고와 구매", "무료 플레이에는 전면 광고와 선택형 보상 광고가 포함될 수 있습니다. 해당 기능에서는 서버 확인을 마쳐야 보상이 지급됩니다. 상품이 판매되는 경우 구매 전에 스토어의 최신 설명과 현지 가격을 확인하세요. 결제·취소·환불·스토어 거래 기록에는 각 스토어 규칙이 적용됩니다. 스토어에 명시되지 않은 구독 상품은 없습니다."),
            ("4. 허용되는 이용", "합법적인 개인 용도로 이용해야 합니다. 서비스 방해, 랭크 로그·시간 조작, 자동화된 남용, 보안 우회 또는 타인의 권리 침해를 해서는 안 됩니다."),
            ("5. 제공과 변경", "온라인 기능은 네트워크와 제3자 서비스 상태에 따라 중단될 수 있습니다. 유지보수·보안·공정성·법적 이유로 기능을 변경하거나 종료할 수 있습니다. 법으로 배제할 수 없는 권리를 제한하지 않는 범위에서 서비스는 현재 상태로 제공됩니다."),
            ("6. 지식재산권", "앱의 독자적인 코드·브랜드·아트·콘텐츠는 넥스트 스튜디오 또는 각 권리자에게 귀속됩니다. 일반적인 카드 게임 규칙과 표준 플레잉 카드 개념에 독점권을 주장하지 않습니다."),
        ]),
        "support": ("고객지원", "게임 이용 방법과 문제 해결 안내입니다.", [
            ("1. 게임 방법", "foundation에는 무늬별로 A부터 K까지 쌓습니다. tableau에는 색을 번갈아 내림차순으로 놓고, 앞면으로 연결된 묶음을 이동하며, 스톡에서 카드를 뽑아 뒷면 카드를 모두 공개합니다. 랭크에서는 수동 이동만 허용되고 힌트·되돌리기·자동 이동·이어하기는 사용할 수 없습니다."),
            ("2. 저장과 랭크", "일반 게임은 기기에 저장됩니다. 로그인하면 지원되는 진행 상황을 동기화하고 랭크 기록을 제출할 수 있습니다. 랭크 시도 발급 시 도전권 1개가 차감되고 중도 이탈 시 반환되지 않습니다. 도전권은 앱에 표시된 최대치까지 충전되며 전체 행동 로그를 서버가 검증한 기록만 리더보드에 표시됩니다."),
            ("3. 광고와 보상", "광고가 로드되지 않으면 네트워크를 확인하고 나중에 다시 시도하세요. 보상 광고를 봤다는 사실만으로 보상이 확정되지 않으며 서명된 서버 콜백 검증을 통과해야 합니다. 테스트 목적으로 실제 광고를 누르지 마세요. 동의 제공자가 허용하는 경우 앱에서 광고 개인정보 선택을 다시 확인할 수 있습니다."),
            ("4. 구매와 복원", "구매 가능 여부는 플랫폼과 스토어 설정에 따릅니다. 복원 가능한 App Store 구매는 앱의 구매 복원 기능을 사용하세요. 결제·취소·환불은 해당 스토어 지원 절차를 이용하고 카드 정보나 스토어 비밀번호를 이메일로 보내지 마세요."),
            ("5. 문제 신고", f"<a href=\"mailto:{EMAIL}?subject=Classic%20Solitaire%20Support\">{EMAIL}</a>로 앱 이름, 앱 버전, 기기·OS, 언어, 로그인 상태, 재현 단계와 개인정보를 가린 화면을 보내주세요. 비밀번호·인증 코드·불필요한 개인정보가 포함된 영수증·카드 정보는 보내지 마세요."),
        ]),
        "delete-account": ("게임 데이터 삭제", "기기 및 클래식 솔리테어 서버 데이터를 삭제하는 방법입니다.", [
            ("1. 앱에서 삭제", "설정에서 ‘게임 데이터 삭제’를 선택하세요. 확인 및 필요한 Apple 재인증 후 클래식 솔리테어 게임 데이터 삭제를 요청하고 이 게임의 계정별 로컬 데이터를 지웁니다. 게임별 삭제이므로 공용 로그인 계정 자체와 다른 게임의 데이터는 삭제하지 않습니다."),
            ("2. 삭제 범위", "클래식 솔리테어 동기화 상태, 랭크 시도·결과, 프로필 잔액·설정, 서버에 기록된 이 게임의 구매 권한, 서버 삭제 절차 대상 보상 기록과 게임별 계정 연결을 삭제합니다. 법적 보관 의무가 있는 항목은 예외일 수 있으며 Apple·Google이 관리하는 스토어 거래 기록은 당사가 삭제하지 않습니다."),
            ("3. 기기 데이터 삭제", "iOS에서는 로컬 파일까지 지우려면 앱 정리하기가 아니라 앱 삭제를 사용하세요. Android에서는 시스템 설정에서 앱 저장공간을 지우거나 앱을 제거하세요. 플랫폼 백업은 해당 계정 설정에서 별도로 관리됩니다."),
            ("4. 앱 없이 요청", f"제목을 ‘Classic Solitaire Data Deletion’으로 하여 <a href=\"mailto:{EMAIL}?subject=Classic%20Solitaire%20Data%20Deletion\">{EMAIL}</a>로 로그인 이메일(해당하는 경우)과 삭제 범위를 보내주세요. 비밀번호·인증 코드·신분증·카드 정보는 보내지 마세요. 제한적인 본인 확인을 요청할 수 있으며 적용 법률이 정한 기간 안에 처리 결과를 안내합니다."),
        ]),
    },
}

ORDER = ["index", "privacy", "terms", "support", "delete-account"]

def page(lang: str, key: str) -> str:
    data = PAGES[lang]
    title, lead, sections = data[key]
    other = "ko" if lang == "en" else "en"
    labels = data["labels"]
    canonical = f"{BASE}/{lang}/{key}.html"
    nav = "".join(f'<a href="{name}.html"' + (' aria-current="page"' if name == key else '') + f'>{escape(labels[name])}</a>' for name in ORDER)
    cards = "" if key != "index" else '<div class="cards">' + "".join(f'<a class="card" href="{name}.html"><strong>{escape(labels[name])}</strong><span aria-hidden="true">↗</span></a>' for name in ORDER[1:]) + '</div>'
    body = "".join(f"<section><h2>{heading}</h2><p>{text}</p></section>" for heading, text in sections)
    return f'''<!doctype html>
<html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="description" content="Classic Solitaire: Card Calm · {escape(title)} · Next Studio"><title>Classic Solitaire: Card Calm · {escape(title)}</title>
<link rel="stylesheet" href="../style.css"><link rel="canonical" href="{canonical}">
<link rel="alternate" hreflang="ko" href="{BASE}/ko/{key}.html"><link rel="alternate" hreflang="en" href="{BASE}/en/{key}.html"><link rel="alternate" hreflang="x-default" href="{BASE}/en/{key}.html"></head>
<body><a class="skip" href="#content">{data['skip']}</a><main><div class="top"><a class="brand" href="index.html">CLASSIC SOLITAIRE · CARD CALM</a>
<label><span class="sr-only">{data['language']}</span><select class="language" aria-label="{data['language']}" onchange="location.href=this.value"><option value="../ko/{key}.html"{' selected' if lang == 'ko' else ''}>한국어</option><option value="../en/{key}.html"{' selected' if lang == 'en' else ''}>English</option></select></label></div>
<nav aria-label="{escape(title)}">{nav}</nav><noscript><div class="languages"><a href="../ko/{key}.html" lang="ko">한국어</a><a href="../en/{key}.html" lang="en">English</a></div></noscript>
<article id="content"><p class="eyebrow">CLASSIC SOLITAIRE · CARD CALM</p><h1>{title}</h1><p class="lead">{lead}</p>{cards}{'' if key == 'index' else f'<p class="date">{data["date"]}</p>'}{body}
<aside><h2>{'Contact' if lang == 'en' else '문의'}</h2><p>Next Studio · 넥스트 스튜디오<br><a href="mailto:{EMAIL}?subject=Classic%20Solitaire%20Support">{EMAIL}</a></p></aside></article>
<footer>© 2026 Next Studio · 넥스트 스튜디오<br><a href="mailto:{EMAIL}">{EMAIL}</a></footer></main></body></html>'''

for language in PAGES:
    target = ROOT / language
    target.mkdir(exist_ok=True)
    for page_key in ORDER:
        (target / f"{page_key}.html").write_text(page(language, page_key), encoding="utf-8")

(ROOT / "index.html").write_text('''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Classic Solitaire: Card Calm</title><link rel="stylesheet" href="style.css"><link rel="canonical" href="https://oh-seungjin.github.io/privacy-terms/classic-card-game/"><link rel="alternate" hreflang="ko" href="https://oh-seungjin.github.io/privacy-terms/classic-card-game/ko/index.html"><link rel="alternate" hreflang="en" href="https://oh-seungjin.github.io/privacy-terms/classic-card-game/en/index.html"><link rel="alternate" hreflang="x-default" href="https://oh-seungjin.github.io/privacy-terms/classic-card-game/en/index.html"></head><body><main><article><p class="eyebrow">CLASSIC SOLITAIRE · CARD CALM</p><h1>Choose a language · 언어 선택</h1><div class="cards"><a class="card" href="ko/index.html"><strong>한국어</strong><span>→</span></a><a class="card" href="en/index.html"><strong>English</strong><span>→</span></a></div></article></main></body></html>''', encoding="utf-8")
