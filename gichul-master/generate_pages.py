"""Generate the public Gichul Master (기출마스터) pages: index, privacy, terms, support, delete-account in Korean and English.
Content must match the shipped app (see certmaster repo docs/store-listing.md). Update the date and every claim when behaviour changes."""

from html import escape as esc
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SITE = "https://oh-seungjin.github.io/privacy-terms/gichul-master"
EMAIL = "dhalska2@gmail.com"
KINDS = ("index", "privacy", "terms", "support", "delete-account")

LANGUAGES = {
    "ko": {
        "app": "기출마스터", "label": "한국어", "html": "ko", "nav": ["소개", "개인정보처리방침", "이용약관", "지원", "계정 삭제"],
        "tag": "자격증 기출문제, 회차별로 풀고 오답만 다시", "intro": "공인중개사 등 국가자격 기출문제를 회차·과목별로 풀고, 틀린 문제는 오답노트로 반복하세요.",
        "features": ["공식 최종정답과 대조한 기출문제만 제공", "오답노트·북마크·통계·모의고사·이어 풀기", "과목마다 무료 체험 문항, 이용권은 자동 갱신 없는 30·90일권"],
        "offline": "문제풀이 기록은 기기에만 저장되고 광고와 추적이 없습니다. 이용권을 사려는 경우에만 로그인합니다. 문제와 정답의 출처는 한국산업인력공단(Q-Net)이며 공공누리 제1유형에 따라 이용합니다. 이 앱은 한국산업인력공단과 관련이 없는 민간 앱입니다.",
        "date": "시행일: 2026년 10월 21일",
        "privacy_title": "기출마스터 개인정보처리방침",
        "privacy_intro": "기출마스터는 Next Studio가 제공하는 자격증 기출문제 학습 앱입니다. 로그인하지 않으면 학습 기록은 모두 내 기기에만 저장됩니다.",
        "privacy": [
            ("기기에 저장하는 정보", "푼 문제와 선택한 답, 오답노트, 북마크, 학습 통계, 모의고사 점수, 이어 풀기 위치, 글자 크기 같은 설정, 구매한 이용권의 캐시(만료 확인용)가 기기에 저장됩니다. 이 정보는 서버로 전송되지 않으며 앱을 삭제하면 지워집니다."),
            ("로그인과 서버에 저장하는 정보", "이용권을 구매하거나 복원하려면 Apple 또는 Google 계정으로 로그인합니다. 계정 식별자와 이메일(제공자가 전달하는 경우)이 인증 서비스(Supabase)에 저장되며, 이용권을 계정에 연결하는 데에만 사용합니다. 로그인하지 않아도 무료 체험 문항은 쓸 수 있습니다."),
            ("구매와 이용권", "결제는 Apple App Store가 처리하며 기출마스터는 카드 정보를 받지 않습니다. 이용권을 주려고 스토어가 알려 주는 거래 번호와 상품 종류를 받아 스토어 서버에서 확인하고, 이용권의 종류·시작·종료 시각과 구매 기록을 서버에 저장합니다. 환불되면 해당 이용권은 회수됩니다."),
            ("오류 정보", "앱이 비정상 종료되면 원인을 찾기 위해 Firebase Crashlytics로 오류 기록(기기 모델, 운영체제 버전, 앱 버전, 오류 내용, 임의의 설치 ID)이 전송됩니다. 이름·이메일·문제풀이 내용은 포함하지 않습니다."),
            ("광고와 추적", "기출마스터에는 광고가 없고, 광고 식별자(IDFA)를 읽지 않으며, 앱 간 추적을 하지 않습니다. 제3자 분석 도구도 쓰지 않습니다."),
            ("보관과 삭제", "기기의 기록은 앱을 삭제하면 지워집니다. 서버의 계정 정보는 앱의 계정 → 계정 삭제로 즉시 삭제됩니다. 구매 기록은 환불 처리와 장부 보관을 위해 계정과의 연결을 끊은 채 관련 법령이 정한 기간(전자상거래 등에서의 소비자보호에 관한 법률상 5년) 보관한 뒤 삭제합니다."),
            ("처리 위탁", "인증과 서버 저장은 Supabase, 오류 수집은 Google(Firebase), 로그인과 결제는 Apple·Google이 처리합니다. 이 외의 제3자에게 정보를 판매하거나 제공하지 않습니다."),
            ("콘텐츠 출처", "문제와 최종정답은 한국산업인력공단(Q-Net)이 공공누리 제1유형으로 개방한 자료이며, 앱은 이를 가공해 보여줍니다. 이 앱은 한국산업인력공단 또는 어떤 공공기관과도 관련이 없습니다."),
            ("아동 및 변경", "기출마스터는 일반 사용자를 위한 앱이며 아동의 개인정보를 고의로 수집하지 않습니다. 방침이 바뀌면 이 페이지의 시행일을 갱신하고, 중요한 변경은 앱에서 알립니다."),
        ],
        "terms_title": "기출마스터 이용약관",
        "terms_intro": "이 약관은 Next Studio가 제공하는 기출마스터 앱의 이용 조건을 정합니다. 앱을 설치하거나 사용하면 이 약관에 동의한 것으로 봅니다.",
        "terms": [
            ("서비스", "기출마스터는 국가자격시험 기출문제를 풀고 오답·통계를 관리하는 학습 앱입니다. 과목마다 일부 문항은 무료이며, 나머지는 이용권을 구매해 정해진 기간 동안 이용합니다."),
            ("이용권과 결제", "이용권은 과목·자격증 전체·모든 자격증 단위의 30일 또는 90일 이용권이며 자동으로 갱신되지 않습니다. 가격은 스토어에 표시된 금액이고 결제는 Apple ID로 청구됩니다. 같은 대상의 이용권을 다시 사면 현재 기간이 끝난 뒤부터 이어집니다. 환불은 Apple의 정책과 절차에 따릅니다. 환불되면 해당 이용권은 회수됩니다."),
            ("합격을 보장하지 않습니다", "문제와 정답은 시험 당시 공개된 자료를 그대로 옮긴 것이며, 이후 법령이 개정되어 지금의 정답이나 설명과 다를 수 있습니다. 옮기는 과정에서 오류가 있을 수 있으니 중요한 판단은 공식 자료로 확인하세요. 앱 이용이 시험 합격을 보장하지 않습니다."),
            ("콘텐츠의 출처와 권리", "문제와 정답은 한국산업인력공단(Q-Net)이 공공누리 제1유형(출처표시)으로 개방한 자료를 가공한 것이며, 앱의 화면 구성·기록·통계 기능은 Next Studio에 권리가 있습니다. 이 앱은 한국산업인력공단과 관련이 없는 민간 앱입니다."),
            ("금지 행위", "서비스를 해킹하거나 비정상적인 방법으로 접근하는 행위, 다른 사람의 계정을 도용하거나 이용권을 부정한 방법으로 얻는 행위, 기기 시간을 조작해 이용 기간을 늘리는 행위, 서버에 과도한 부하를 주는 행위를 금지합니다."),
            ("서비스 변경과 중단", "기능은 개선을 위해 바뀌거나 중단될 수 있으며, 중요한 변경은 앱이나 이 페이지에 알립니다."),
            ("책임의 제한", "Next Studio는 법이 허용하는 범위에서 데이터 손실, 문제 내용의 오류, 앱 이용으로 생긴 간접 손해에 대해 책임지지 않습니다."),
            ("준거법과 문의", "이 약관은 대한민국 법을 따릅니다. 문의는 아래 이메일로 보내 주세요. 약관이 바뀌면 이 페이지의 시행일을 갱신합니다."),
        ],
        "support_title": "기출마스터 도움말 및 지원",
        "support_intro": "앱을 쓰다가 문제가 생기면 아래를 확인하고, 해결되지 않으면 이메일로 문의해 주세요.",
        "support": [
            ("문제가 잠겨 있어요", "과목마다 무료 체험 문항만 열려 있습니다. 홈 화면 오른쪽 위의 이용권 버튼에서 이용권을 구매하면 전체 문항이 열립니다."),
            ("구매했는데 적용되지 않아요", "로그인한 계정이 구매할 때의 계정과 같은지 확인하고, 이용권 화면의 구매 복원을 눌러 보세요. 인터넷에 연결되어 있어야 적용됩니다. 그래도 안 되면 구매 영수증을 첨부해 문의해 주세요."),
            ("오프라인에서 쓰고 싶어요", "구매한 이용권은 마지막으로 서버와 확인한 뒤 7일 동안 오프라인에서도 쓸 수 있습니다. 7일이 지나면 인터넷에 연결해 확인해야 합니다."),
            ("환불을 받고 싶어요", "환불은 Apple이 처리합니다. reportaproblem.apple.com에서 요청하세요. 환불이 승인되면 이용권이 자동으로 회수됩니다."),
            ("문제나 정답이 이상해요", "회차·과목·문제 번호와 의심되는 부분을 적어 이메일로 알려 주세요. 원본 자료와 대조해 수정합니다."),
            ("문의할 때", "기기 종류, 운영체제 버전, 앱 버전, 문제를 다시 만드는 순서를 적어 보내 주세요."),
        ],
        "delete_title": "기출마스터 계정 및 데이터 삭제",
        "delete_intro": "기출마스터는 로그인 없이도 쓸 수 있고, 로그인한 경우에만 계정 정보가 서버에 저장됩니다. 아래 방법으로 삭제할 수 있습니다.",
        "delete-account": [
            ("앱에서 삭제하기 (권장)", "기출마스터에서 홈 오른쪽 위의 계정 → 계정 삭제를 누르세요. 서버의 계정과 연결 정보가 즉시 삭제됩니다. 삭제한 계정의 이용권은 복구할 수 없습니다."),
            ("앱에 접근할 수 없을 때", f"가입한 로그인(Apple 또는 Google)과 앱 이름을 적어 {EMAIL}로 삭제를 요청해 주세요. 본인 확인 후 영업일 기준 7일 안에 삭제하고 알려 드립니다."),
            ("기기의 데이터", "기기에만 저장된 문제풀이 기록은 앱을 삭제하면 함께 지워집니다."),
            ("삭제되는 정보", "로그인 계정, 계정에 연결된 서버 데이터가 삭제됩니다. 구매 기록은 환불 처리와 법령상 보관을 위해 계정과의 연결을 끊은 채 정해진 기간 보관한 뒤 삭제합니다. App Store의 결제 내역은 Apple이 관리합니다."),
        ],
        "contact": "문의", "skip": "본문으로 이동", "choose": "언어 선택", "copyright": "© 2026 Next Studio · 넥스트 스튜디오",
    },
    "en": {
        "app": "Gichul Master", "label": "English", "html": "en", "nav": ["Overview", "Privacy", "Terms", "Support", "Delete account"],
        "tag": "Practice past exam questions by year, then redo your mistakes", "intro": "Solve past questions of Korean national license exams, such as the real estate agent exam, by year and subject, and repeat the ones you missed.",
        "features": ["Only questions checked against the official final answer key", "Wrong-answer notes, bookmarks, statistics, mock exams, resume where you stopped", "Free sample questions in every subject; passes last 30 or 90 days and never auto-renew"],
        "offline": "Your study records stay on your device, with no ads and no tracking. You sign in only if you want to buy a pass. Questions and answers come from the Human Resources Development Service of Korea (Q-Net) under the Korea Open Government License Type 1. This is an independent app and is not affiliated with that organization. Content is in Korean.",
        "date": "Effective October 21, 2026",
        "privacy_title": "Gichul Master Privacy Policy",
        "privacy_intro": "Gichul Master is a past-exam practice app provided by Next Studio. If you do not sign in, all your study records stay on your device.",
        "privacy": [
            ("Information stored on your device", "Questions you solved and the answers you chose, wrong-answer notes, bookmarks, study statistics, mock exam scores, where you stopped, settings such as text size, and a cache of your purchased passes (to check expiry). This information is not sent to a server and is removed when you delete the app."),
            ("Sign-in and information stored on our server", "To buy or restore a pass you sign in with Apple or Google. Your account identifier and email (if the provider shares it) are stored with our authentication service (Supabase) and used only to attach your pass to your account. The free sample questions work without signing in."),
            ("Purchases and passes", "Payments are handled by the Apple App Store; Gichul Master never receives your card details. To grant a pass, the app receives the transaction number and product from the store, we confirm it with the store's servers, and we store the pass type, start and end times, and the purchase record on our server. If a purchase is refunded, the pass is revoked."),
            ("Crash information", "If the app crashes, an error report (device model, operating system version, app version, error details and a random installation ID) is sent to Firebase Crashlytics to find the cause. It does not include your name, email, or what you studied."),
            ("Ads and tracking", "Gichul Master has no ads, does not read the advertising identifier (IDFA), and does not track you across apps. We do not use third-party analytics tools."),
            ("Retention and deletion", "Records on your device are removed when you delete the app. Your account data on the server is deleted immediately when you choose Account → Delete account in the app. Purchase records are kept, unlinked from your account, for refund handling and bookkeeping for the period required by law (five years under the Korean Act on Consumer Protection in Electronic Commerce) and then deleted."),
            ("Service providers", "Supabase provides authentication and server storage, Google (Firebase) provides crash reporting, and Apple and Google provide sign-in and payments. We do not sell your information or share it with anyone else."),
            ("Content source", "Questions and final answers are materials released by the Human Resources Development Service of Korea (Q-Net) under the Korea Open Government License Type 1 (attribution), which the app reformats for display. This app is not affiliated with that organization or any public agency."),
            ("Children and changes", "Gichul Master is for general users and does not knowingly collect personal information from children. If this policy changes, we update the effective date on this page and announce important changes in the app."),
        ],
        "terms_title": "Gichul Master Terms of Use",
        "terms_intro": "These terms set the conditions for using the Gichul Master app provided by Next Studio. By installing or using the app you agree to them.",
        "terms": [
            ("Service", "Gichul Master is a study app for solving past questions of national license exams and managing mistakes and statistics. Some questions in every subject are free; the rest require a pass for a fixed period."),
            ("Passes and payment", "A pass gives 30 or 90 days of access to one subject, all subjects of one qualification, or all qualifications, and never renews automatically. Prices are those shown in the store and are charged to your Apple ID. Buying a pass for the same target again continues after the current period ends. Refunds follow Apple's policy and process; a refunded pass is revoked."),
            ("No guarantee of passing", "Questions and answers reproduce materials published at the time of each exam. Laws may have changed since, so today's correct answer or explanation can differ, and transcription mistakes are possible. Verify important decisions with official sources. Using the app does not guarantee that you will pass an exam."),
            ("Content source and rights", "Questions and answers are reformatted materials released by the Human Resources Development Service of Korea (Q-Net) under the Korea Open Government License Type 1 (attribution). The app's design, records and statistics features belong to Next Studio. This is an independent app not affiliated with that organization."),
            ("Prohibited conduct", "Hacking or abnormally accessing the service, using someone else's account or obtaining passes by improper means, changing the device clock to extend a pass, and placing excessive load on the servers are prohibited."),
            ("Changes and interruptions", "Features may change or stop as the app improves. Important changes are announced in the app or on this page."),
            ("Limitation of liability", "To the extent allowed by law, Next Studio is not liable for data loss, errors in question content, or indirect damages arising from use of the app."),
            ("Governing law and contact", "These terms are governed by the laws of the Republic of Korea. Contact us at the email below. If the terms change we update the effective date on this page."),
        ],
        "support_title": "Gichul Master Help and Support",
        "support_intro": "If you run into a problem, check the items below, and email us if it is not solved.",
        "support": [
            ("Questions are locked", "Only the free sample questions are open in each subject. Buy a pass with the pass button at the top right of the home screen to open all questions."),
            ("I bought a pass but it is not applied", "Make sure you are signed in with the same account you bought with, and tap Restore purchases on the pass screen. An internet connection is required. If it still does not work, email us with your purchase receipt."),
            ("Using the app offline", "A purchased pass keeps working offline for 7 days after the app last confirmed it with the server. After that, connect to the internet once to confirm."),
            ("I want a refund", "Refunds are handled by Apple. Request one at reportaproblem.apple.com. When a refund is approved, the pass is revoked automatically."),
            ("A question or answer looks wrong", "Email us the year, subject, question number and what looks wrong. We will check it against the original material and fix it."),
            ("When contacting us", "Include your device model, operating-system version, app version, and the steps to reproduce the issue."),
        ],
        "delete_title": "Delete your Gichul Master account and data",
        "delete_intro": "Gichul Master works without signing in, and account information is stored on our server only if you sign in. You can delete it as follows.",
        "delete-account": [
            ("Delete in the app (recommended)", "In Gichul Master, choose Account at the top right of the home screen → Delete account. Your account and linked server data are deleted immediately. Passes of a deleted account cannot be recovered."),
            ("If you cannot open the app", f"Email {EMAIL} with the sign-in method (Apple or Google) and the app name. After verifying it is you, we delete the data within 7 business days and let you know."),
            ("Data on your device", "Study records stored only on your device are removed when you delete the app."),
            ("What is deleted", "Your sign-in account and server data linked to it. Purchase records are kept, unlinked from the account, for the period required by law for refunds and bookkeeping, then deleted. Payment history in the App Store is managed by Apple."),
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
    APP = data["app"]
    if kind == "index":
        title = APP
        content = (
            f'<p class="muted">EXAM · PRACTICE · RECORD</p><h1>{esc(data["tag"])}</h1><p class="lead">{esc(data["intro"])}</p><ul class="features">'
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
            f'<a href="mailto:{EMAIL}?subject=GichulMaster%20{kind}">{EMAIL}</a></p></aside>'
        )
    return f'''<!doctype html>
<html lang="{data['html']}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="description" content="{APP} · {esc(title)} · Next Studio"><title>{APP} · {esc(title)}</title>
<link rel="stylesheet" href="../style.css"><link rel="canonical" href="{SITE}/{code}/{kind}.html">
{alternates(kind)}</head><body><a class="skip" href="#content">{esc(data['skip'])}</a><main>
<header class="top"><a class="brand" href="index.html">{APP}</a><label><span class="skip">{esc(data['choose'])}</span><select class="language" aria-label="{esc(data['choose'])}" onchange="location.href=this.value">{language_options(code, kind)}</select></label></header>
<nav aria-label="{APP}">{nav(data, kind)}</nav><article id="content">{content}</article><footer>{esc(data['copyright'])}<br><a href="mailto:{EMAIL}">{EMAIL}</a></footer></main></body></html>'''



for locale, strings in LANGUAGES.items():
    destination = ROOT / locale
    destination.mkdir(exist_ok=True)
    for page_kind in KINDS:
        (destination / f"{page_kind}.html").write_text(page(locale, page_kind, strings), encoding="utf-8")

links = "".join(f'<a href="{code}/index.html" hreflang="{d["html"]}">{esc(d["label"])}</a>' for code, d in LANGUAGES.items())
(ROOT / "index.html").write_text(
    f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="Gichul Master (기출마스터)"><title>Gichul Master · 기출마스터 · Next Studio</title><link rel="stylesheet" href="style.css"></head><body><main><header class="top"><span class="brand">Gichul Master · 기출마스터</span></header><article><p class="muted">EXAM · PRACTICE · RECORD</p><h1>Gichul Master · 기출마스터</h1><p class="lead">Choose your language. · 언어를 선택하세요.</p><div class="cards languages">{links}</div></article><footer>© 2026 Next Studio<br><a href="mailto:{EMAIL}">{EMAIL}</a></footer></main></body></html>""",
    encoding="utf-8",
)
print(f"Generated {len(LANGUAGES) * len(KINDS) + 1} pages.")
