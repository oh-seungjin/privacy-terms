"""Generate Petlog public pages (index, privacy, terms, support, delete-account) in Korean and English."""

from html import escape as esc
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SITE = "https://oh-seungjin.github.io/privacy-terms/petlog"
EMAIL = "dhalska2@gmail.com"
KINDS = ("index", "privacy", "terms", "support", "delete-account")

LANGUAGES = {
    "ko": {
        "label": "한국어", "html": "ko", "nav": ["소개", "개인정보처리방침", "이용약관", "지원", "계정 삭제"],
        "tag": "우리 아이의 건강을 한곳에", "intro": "접종·투약·체중·병원·지출을 기록하고, 다음 일정을 알림으로 챙기세요.",
        "features": ["접종·투약 알림과 홈 화면 위젯", "체중 차트와 병원·지출 기록", "무료는 기기에만 저장, Pro는 가족과 공유·동기화"],
        "offline": "광고와 추적 없이, 기록은 기본적으로 내 기기에만 저장됩니다. 로그인과 Pro를 쓸 때만 서버에 저장됩니다.",
        "date": "시행일: 2026년 10월 9일",
        "privacy_title": "Petlog 개인정보처리방침",
        "privacy_intro": "Petlog는 Next Studio가 제공하는 반려동물 건강 기록 앱입니다. 로그인하지 않으면 모든 기록이 내 기기에만 저장됩니다.",
        "privacy": [
            ("기기에 저장하는 정보", "반려동물 이름·종·품종·생일·사진, 접종·투약·체중·건강 메모(사진 포함)·병원 방문·지출 기록, 알림 시간, 화면·언어·단위·앱 잠금 설정은 기기 안에만 저장됩니다. 앱 잠금에 쓰는 Face ID/지문 정보는 운영체제가 처리하며 앱은 받지 않습니다."),
            ("로그인과 서버에 저장하는 정보", "Apple 또는 Google 계정으로 로그인하면 계정 식별자와 이메일(제공자가 전달하는 경우)이 인증 서비스(Supabase)에 저장됩니다. 로그인한 Pro 사용자가 동기화를 켜면 반려동물과 모든 기록, 사진이 서버(Supabase)에 저장되어 기기 간 동기화와 가족 공유에 쓰입니다. 로그인하지 않으면 서버로 아무것도 보내지 않습니다."),
            ("가족 공유", "초대 코드로 가족을 초대하면 초대받은 사람은 공유한 반려동물의 기록을 볼 수 있고, 권한에 따라 수정할 수도 있습니다. 구성원 목록에는 이메일이 일부 가려진 형태(예: ab***@gmail.com)로만 표시됩니다."),
            ("구독과 결제", "결제는 Apple App Store 또는 Google Play가 처리하며 Petlog는 카드 정보를 받지 않습니다. 구독 상태를 확인하려고 스토어의 구매 영수증(거래 번호, 상품, 만료일)을 서버로 보내 Apple·Google에 검증하고 구독 상태를 저장합니다."),
            ("오류 정보", "앱이 비정상 종료되면 원인 파악을 위해 Firebase Crashlytics로 오류 기록(기기 모델, 운영체제 버전, 앱 버전, 오류 내용, 임의의 설치 식별자)이 전송됩니다. 반려동물 기록이나 이름은 포함하지 않습니다. 개발 중 빌드에서는 수집하지 않습니다."),
            ("광고와 추적", "Petlog에는 광고가 없고, 광고 식별자(IDFA)를 읽지 않으며, 앱 간 추적을 하지 않습니다. 제3자 분석 도구도 쓰지 않습니다."),
            ("알림·카메라·사진", "알림은 기기에서 예약되는 로컬 알림이며 내용이 서버로 전송되지 않습니다. 카메라와 사진 보관함은 사용자가 사진을 추가할 때만 접근하며 권한은 기기 설정에서 끌 수 있습니다."),
            ("보관과 삭제", "기기의 기록은 앱을 삭제하거나 반려동물을 삭제하면 지워집니다. 서버의 데이터는 로그인 상태에서 더보기 → 계정 → 계정 삭제를 누르면 모든 기록과 사진이 즉시 삭제되고, 다른 앱에서 쓰지 않는 로그인 계정도 함께 삭제됩니다. 앱에 접근할 수 없으면 계정 삭제 페이지 안내에 따라 이메일로 요청할 수 있습니다."),
            ("처리 위탁", "서버 저장과 인증은 Supabase, 오류 수집은 Google(Firebase), 결제는 Apple·Google이 처리합니다. 이 외의 제3자에게 정보를 판매하거나 제공하지 않습니다."),
            ("아동 및 변경", "Petlog는 일반 사용자를 위한 앱이며 아동의 개인정보를 고의로 수집하지 않습니다. 방침이 바뀌면 이 페이지의 시행일을 갱신합니다."),
        ],
        "terms_title": "Petlog 이용약관",
        "terms_intro": "이 약관은 Next Studio가 제공하는 Petlog 앱의 이용 조건을 정합니다. 앱을 설치하거나 사용하면 이 약관에 동의한 것으로 봅니다.",
        "terms": [
            ("서비스", "Petlog는 반려동물의 접종·투약·체중·건강 메모·병원·지출을 기록하고 알림을 받는 앱입니다. 기본 기능은 무료이며, Pro 구독으로 반려동물 무제한, 기기 간 동기화, 가족 공유, 병원용 요약 PDF를 쓸 수 있습니다."),
            ("의료 조언이 아닙니다", "앱의 접종 주기, 건강관리·해로운 음식 등 상식 정보는 반려동물 수첩 등을 바탕으로 정리한 참고 자료이며 수의사의 진단·치료를 대신하지 않습니다. 반려동물의 건강에 문제가 있으면 동물병원에 문의하세요. 알림은 보조 수단이므로 중요한 일정은 직접 확인하세요."),
            ("구독과 결제", "Pro는 월간·연간 자동 갱신 구독입니다. 가격은 스토어에 표시된 금액이며 결제는 Apple ID 또는 Google 계정에 청구됩니다. 구독은 현재 기간이 끝나기 최소 24시간 전에 해지하지 않으면 자동으로 갱신됩니다. 해지와 환불은 각 스토어의 구독 관리 및 환불 정책에 따릅니다. 구독이 끝나도 입력한 기록은 기기에 남으며, Pro 기능만 제한됩니다."),
            ("사용자의 기록", "입력한 기록과 사진의 권리는 사용자에게 있습니다. 가족 공유로 초대한 사람에게는 공유한 반려동물의 기록이 보입니다. 타인의 권리를 침해하는 사진이나 불법적인 내용을 올리지 마세요."),
            ("금지 행위", "서비스를 해킹하거나 비정상적인 방법으로 접근하는 행위, 다른 사람의 계정을 도용하는 행위, 서버에 과도한 부하를 주는 행위를 금지합니다."),
            ("서비스 변경과 중단", "기능은 개선을 위해 바뀌거나 중단될 수 있으며, 중요한 변경은 앱이나 이 페이지에 알립니다."),
            ("책임의 제한", "Next Studio는 법이 허용하는 범위에서 알림 누락, 데이터 손실, 앱 이용으로 생긴 간접 손해에 대해 책임지지 않습니다. 중요한 기록은 백업 기능으로 보관하세요."),
            ("준거법과 문의", "이 약관은 대한민국 법을 따릅니다. 문의는 아래 이메일로 보내 주세요. 약관이 바뀌면 이 페이지의 시행일을 갱신합니다."),
        ],
        "support_title": "Petlog 도움말 및 지원",
        "support_intro": "앱을 쓰다가 문제가 생기면 아래를 확인하고, 해결되지 않으면 이메일로 문의해 주세요.",
        "support": [
            ("알림이 오지 않을 때", "기기 설정에서 Petlog 알림 권한이 켜져 있는지 확인하고, 더보기 → 알림에서 항목별 알림과 시간을 확인하세요. 접종 일정 알림은 다음 예정일이 있는 항목에만 예약됩니다."),
            ("기록을 다른 기기로 옮기기", "Pro에서는 로그인 후 더보기 → 백업·복원에서 클라우드 동기화를 켜세요. 무료에서는 백업 파일을 내보내고 새 기기에서 가져올 수 있습니다."),
            ("구독 복원과 해지", "구독 화면에서 \"구독 복원\"을 누르세요. 해지는 iPhone의 설정 → Apple ID → 구독, Android의 Google Play → 구독에서 할 수 있습니다."),
            ("가족 공유가 안 될 때", "가족 공유는 Pro 구독자가 반려동물을 초대하는 방식입니다. 초대 코드는 한 번만 쓸 수 있고 유효 시간이 있으니 새 코드를 만들어 보세요."),
            ("문의할 때", "기기 종류, 운영체제 버전, 앱 버전, 문제를 다시 만드는 순서를 적어 보내 주세요. 반려동물의 개인적인 기록은 적지 않아도 됩니다."),
        ],
        "delete_title": "Petlog 계정 및 데이터 삭제",
        "delete_intro": "Petlog는 로그인 없이도 쓸 수 있고, 로그인한 경우에만 서버에 데이터가 저장됩니다. 아래 방법으로 삭제할 수 있습니다.",
        "delete-account": [
            ("앱에서 삭제하기 (권장)", "Petlog에서 더보기 → 계정 → 계정 삭제를 누르세요. 서버에 저장된 모든 반려동물 기록과 사진이 즉시 삭제되고, 다른 앱에서 쓰지 않는 로그인 계정도 함께 삭제됩니다. 구독은 자동으로 해지되지 않으므로 스토어에서 따로 해지하세요."),
            ("앱에 접근할 수 없을 때", f"가입한 로그인(Apple 또는 Google)과 앱 이름을 적어 {EMAIL}로 삭제를 요청해 주세요. 본인 확인 후 영업일 기준 7일 안에 삭제하고 알려 드립니다."),
            ("기기의 데이터", "기기에만 저장된 기록은 앱을 삭제하면 함께 지워집니다."),
            ("삭제되는 정보", "반려동물과 접종·투약·체중·건강 메모·병원·지출 기록, 업로드한 사진, 가족 공유 구성원 정보, 구독 상태 기록이 삭제됩니다. 스토어의 결제 내역은 Apple·Google이 관리하므로 삭제되지 않습니다."),
        ],
        "contact": "문의", "skip": "본문으로 이동", "choose": "언어 선택", "copyright": "© 2026 Next Studio · 넥스트 스튜디오",
    },
    "en": {
        "label": "English", "html": "en", "nav": ["Overview", "Privacy", "Terms", "Support", "Delete account"],
        "tag": "Your pet's health in one place", "intro": "Track vaccines, medicine, weight, vet visits, and expenses, and get reminders for what is next.",
        "features": ["Vaccine and medicine reminders, home-screen widgets", "Weight charts, vet visit and expense records", "Free stays on your device; Pro adds family sharing and sync"],
        "offline": "No ads and no tracking. Your records stay on your device unless you sign in and use Pro.",
        "date": "Effective October 9, 2026",
        "privacy_title": "Petlog Privacy Policy",
        "privacy_intro": "Petlog is a pet health record app provided by Next Studio. If you do not sign in, all your records stay on your device.",
        "privacy": [
            ("Information stored on your device", "Pet names, species, breed, birthdays and photos; vaccine, medicine, weight, health note (with photos), vet visit and expense records; reminder times; and display, language, unit and app-lock settings are stored only on your device. Face ID or fingerprint data used for app lock is handled by the operating system; the app never receives it."),
            ("Sign-in and information stored on our server", "If you sign in with Apple or Google, your account identifier and email (if the provider shares it) are stored with our authentication service (Supabase). If you are a signed-in Pro user and turn on sync, your pets, all records and photos are stored on our server (Supabase) for device sync and family sharing. If you do not sign in, nothing is sent to a server."),
            ("Family sharing", "When you invite family with an invite code, the invited person can view (and, depending on the role, edit) the records of the pet you shared. The member list shows emails only in a masked form (for example ab***@gmail.com)."),
            ("Subscriptions and payments", "Payments are handled by the Apple App Store or Google Play. Petlog never receives your card details. To confirm your subscription, the app sends the store purchase receipt (transaction ID, product, expiry date) to our server, which verifies it with Apple or Google and stores the subscription status."),
            ("Crash information", "If the app crashes, an error report (device model, operating system version, app version, error details and a random installation ID) is sent to Firebase Crashlytics to help us fix the problem. It does not include pet records or names. Development builds do not collect it."),
            ("Ads and tracking", "Petlog has no ads, does not read the advertising identifier (IDFA), and does not track you across apps. We do not use third-party analytics tools."),
            ("Notifications, camera, photos", "Reminders are local notifications scheduled on your device; their content is not sent to a server. The camera and photo library are accessed only when you add a photo, and you can turn off the permission in device settings."),
            ("Retention and deletion", "Records on your device are removed when you delete the app or a pet. Server data is deleted immediately, together with all records and photos, when you choose More → Account → Delete account while signed in; the sign-in account is deleted too if no other app of ours uses it. If you cannot open the app, you can request deletion by email as described on the delete-account page."),
            ("Service providers", "Supabase provides authentication and server storage, Google (Firebase) provides crash reporting, and Apple and Google process payments. We do not sell your information or share it with anyone else."),
            ("Children and changes", "Petlog is a general-audience app and does not knowingly collect children's personal information. If this policy changes, the effective date on this page will be updated."),
        ],
        "terms_title": "Petlog Terms of Use",
        "terms_intro": "These terms set the conditions for using the Petlog app provided by Next Studio. By installing or using the app you agree to them.",
        "terms": [
            ("The service", "Petlog lets you record your pet's vaccines, medicine, weight, health notes, vet visits and expenses and get reminders. Core features are free. A Pro subscription adds unlimited pets, device sync, family sharing, and a vet summary PDF."),
            ("Not medical advice", "Vaccine schedules and the health, care and harmful-food information in the app are reference material compiled from pet health handbooks and do not replace a veterinarian's diagnosis or treatment. If your pet has a health problem, contact a vet. Reminders are an aid, so double-check important dates yourself."),
            ("Subscriptions and payment", "Pro is an auto-renewing monthly or yearly subscription. The price is the amount shown in the store and is charged to your Apple ID or Google account. The subscription renews automatically unless you cancel at least 24 hours before the end of the current period. Cancellation and refunds follow each store's subscription management and refund policy. If a subscription ends, your records stay on your device and only Pro features are limited."),
            ("Your records", "You own the records and photos you enter. People you invite through family sharing can see the records of the pet you share. Do not upload photos that infringe others' rights or illegal content."),
            ("Prohibited conduct", "Hacking or accessing the service in abnormal ways, using someone else's account, and placing excessive load on our servers are prohibited."),
            ("Changes and discontinuation", "Features may change or end as we improve the service. Important changes will be announced in the app or on this page."),
            ("Limitation of liability", "To the extent permitted by law, Next Studio is not liable for missed reminders, data loss, or indirect damages from using the app. Keep important records safe with the backup feature."),
            ("Governing law and contact", "These terms are governed by the laws of the Republic of Korea. Contact us at the email below. If the terms change, the effective date on this page will be updated."),
        ],
        "support_title": "Petlog Help & Support",
        "support_intro": "If something goes wrong, check these tips first, then email us if it is not solved.",
        "support": [
            ("If reminders do not arrive", "Check that notification permission is on for Petlog in device settings, then check each reminder and time under More → Notifications. Vaccine reminders are only scheduled for items that have a next due date."),
            ("Moving records to another device", "With Pro, sign in and turn on cloud sync under More → Backup & restore. On the free plan you can export a backup file and import it on the new device."),
            ("Restore or cancel a subscription", "Tap \"Restore subscription\" on the subscription screen. To cancel, use Settings → Apple ID → Subscriptions on iPhone, or Google Play → Subscriptions on Android."),
            ("If family sharing does not work", "Family sharing is a Pro feature where the subscriber invites people to a pet. An invite code can be used once and expires, so try creating a new code."),
            ("When contacting us", "Include your device model, operating-system version, app version, and the steps to reproduce the issue. You do not need to include private details about your pet."),
        ],
        "delete_title": "Delete your Petlog account and data",
        "delete_intro": "Petlog works without signing in, and data is stored on our server only if you sign in. You can delete it as follows.",
        "delete-account": [
            ("Delete in the app (recommended)", "In Petlog, choose More → Account → Delete account. All pet records and photos on our server are deleted immediately, and the sign-in account is deleted too if no other app of ours uses it. Subscriptions are not cancelled automatically, so cancel in the store separately."),
            ("If you cannot open the app", f"Email {EMAIL} with the sign-in method (Apple or Google) and the app name. After verifying it is you, we delete the data within 7 business days and let you know."),
            ("Data on your device", "Records stored only on your device are removed when you delete the app."),
            ("What is deleted", "Pets and their vaccine, medicine, weight, health note, vet visit and expense records, uploaded photos, family-sharing member information, and subscription status records. Payment history in the stores is managed by Apple and Google and is not deleted."),
        ],
        "contact": "Contact", "skip": "Skip to content", "choose": "Choose language", "copyright": "© 2026 Next Studio",
    },
}


def nav(data, current):
    return "".join(
        f'<a href="{kind}.html"' + (' aria-current="page"' if kind == current else "") + f'>{esc(data["nav"][i])}</a>'
        for i, kind in enumerate(KINDS)
    )


def language_options(current, kind):
    return "".join(
        f'<option value="../{code}/{kind}.html"' + (" selected" if code == current else "") + f'>{esc(d["label"])}</option>'
        for code, d in LANGUAGES.items()
    )


def alternates(kind):
    links = "\n".join(f'<link rel="alternate" hreflang="{d["html"]}" href="{SITE}/{code}/{kind}.html">' for code, d in LANGUAGES.items())
    return links + f'\n<link rel="alternate" hreflang="x-default" href="{SITE}/en/{kind}.html">'


def page(code, kind, data):
    if kind == "index":
        title = "Petlog"
        content = (
            f'<p class="muted">PET · HEALTH · RECORD</p><h1>{esc(data["tag"])}</h1><p class="lead">{esc(data["intro"])}</p><ul class="features">'
            + "".join(f"<li>{esc(item)}</li>" for item in data["features"])
            + f'</ul><p class="lead">{esc(data["offline"])}</p>'
        )
    else:
        key = {"delete-account": "delete"}.get(kind, kind)
        title = data[f"{key}_title"]
        content = f'<h1>{esc(title)}</h1><p class="date">{esc(data["date"])}</p><p class="lead">{esc(data[f"{key}_intro"])}</p>'
        content += "".join(f"<section><h2>{i}. {esc(h)}</h2><p>{esc(t)}</p></section>" for i, (h, t) in enumerate(data[kind], 1))
        content += (
            f'<aside class="contact"><h2>{esc(data["contact"])}</h2><p>Next Studio · 넥스트 스튜디오<br>'
            f'<a href="mailto:{EMAIL}?subject=Petlog%20{kind}">{EMAIL}</a></p></aside>'
        )
    return f'''<!doctype html>
<html lang="{data['html']}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="description" content="Petlog · {esc(title)} · Next Studio"><title>Petlog · {esc(title)}</title>
<link rel="stylesheet" href="../style.css"><link rel="canonical" href="{SITE}/{code}/{kind}.html">
{alternates(kind)}</head><body><a class="skip" href="#content">{esc(data['skip'])}</a><main>
<header class="top"><a class="brand" href="index.html">Petlog</a><label><span class="skip">{esc(data['choose'])}</span><select class="language" aria-label="{esc(data['choose'])}" onchange="location.href=this.value">{language_options(code, kind)}</select></label></header>
<nav aria-label="Petlog">{nav(data, kind)}</nav><article id="content">{content}</article><footer>{esc(data['copyright'])}<br><a href="mailto:{EMAIL}">{EMAIL}</a></footer></main></body></html>'''


for locale, strings in LANGUAGES.items():
    destination = ROOT / locale
    destination.mkdir(exist_ok=True)
    for page_kind in KINDS:
        (destination / f"{page_kind}.html").write_text(page(locale, page_kind, strings), encoding="utf-8")

links = "".join(f'<a href="{code}/index.html" hreflang="{d["html"]}">{esc(d["label"])}</a>' for code, d in LANGUAGES.items())
(ROOT / "index.html").write_text(
    f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="Petlog official website"><title>Petlog · Next Studio</title><link rel="stylesheet" href="style.css"></head><body><main><header class="top"><span class="brand">Petlog</span></header><article><p class="muted">PET · HEALTH · RECORD</p><h1>Petlog</h1><p class="lead">Choose your language. · 언어를 선택하세요.</p><div class="cards languages">{links}</div></article><footer>© 2026 Next Studio · 넥스트 스튜디오</footer></main></body></html>''',
    encoding="utf-8",
)
print(f"Generated {len(LANGUAGES) * len(KINDS) + 1} pages.")
