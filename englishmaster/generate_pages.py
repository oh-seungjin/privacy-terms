"""Generate the public English Master pages: index, privacy, terms, support, delete-account in Korean and English.
Content must match the shipped app. Update the date and every claim when behaviour changes (Crashlytics, recording, in-app deletion are NOT in the app yet)."""

from html import escape as esc
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SITE = "https://oh-seungjin.github.io/privacy-terms/englishmaster"
EMAIL = "dhalska2@gmail.com"
KINDS = ("index", "privacy", "terms", "support", "delete-account")

LANGUAGES = {
    "ko": {
        "app": "English Master", "label": "한국어", "html": "ko", "nav": ["소개", "개인정보처리방침", "이용약관", "지원", "계정 삭제"],
        "tag": "TOEIC 문제를 풀고, 틀린 문제를 복습하는 학습 앱",
        "intro": "TOEIC L&R Part 1~7 연습문제와 200문항 모의고사, 오답노트와 복습 일정을 제공합니다. 모든 문제는 자체 제작한 학습용 문제입니다.",
        "features": ["Part 1~7 연습문제와 기본 해설은 무료", "모의고사(듣기 45분 + 읽기 75분), 오답노트, 기본 통계", "프리미엄: 약점 분석, 맞춤 추천, 간격 반복 복습, 학습 계획, AI 오답 피드백", "1개월·3개월·12개월 자동 갱신 구독, 무료 체험 없음"],
        "offline": "English Master는 TOEIC 시험을 시행하는 ETS가 개발·보증한 서비스가 아닙니다. 점수와 AI 평가는 학습용 추정치이며 공식 점수와 같지 않습니다. TOEIC은 ETS의 등록 상표입니다.",
        "date": "시행일: 2026년 11월 2일",
        "privacy_title": "English Master 개인정보처리방침",
        "privacy_intro": "English Master는 Next Studio가 제공하는 영어 시험 학습 앱입니다. 학습 기록을 저장하고 구독을 확인하려면 Apple 또는 Google 계정으로 로그인해야 합니다.",
        "privacy": [
            ("서버에 저장하는 정보", "로그인 계정 식별자와 이메일(로그인 제공자가 전달하는 경우), 내가 푼 문제와 선택한 답, 오답노트(원인 표시·즐겨찾기 포함), 모의고사 응시 기록, 복습 일정, 학습 목표와 설정, 구독 상태가 서버에 저장됩니다. 학습 기록을 보여 주고 복습을 계획하는 데만 사용합니다."),
            ("구매와 구독", "결제는 Apple App Store와 Google Play가 처리하며 English Master는 카드 정보를 받지 않습니다. 구독을 확인하려고 스토어가 알려 주는 거래 번호, 상품 종류, 만료일, 갱신·해지·환불 상태를 서버에 저장합니다."),
            ("AI 오답 피드백", "프리미엄 구독자가 AI 오답 피드백을 누르면 해당 문제의 지문·문제·선택지와 내가 고른 답이 Anthropic의 API로 전송되어 설명이 만들어집니다. 이 용도 외에는 전송하지 않으며, 결과는 학습용 추정 설명입니다."),
            ("광고와 추적", "English Master에는 광고가 없고, 광고 식별자(IDFA)를 읽지 않으며, 앱 간 추적을 하지 않습니다. 제3자 분석 도구도 쓰지 않습니다."),
            ("보관과 삭제", "서버의 계정과 학습 기록은 계정 삭제를 요청하면 삭제됩니다(계정 삭제 페이지 참고). 구매 기록은 환불 처리와 법령상 보관을 위해 계정과의 연결을 끊은 채 정해진 기간 보관할 수 있습니다."),
            ("처리 위탁", "인증과 서버 저장은 Supabase, 로그인과 결제는 Apple·Google, AI 오답 피드백은 Anthropic이 처리합니다. 이 외의 제3자에게 정보를 판매하거나 제공하지 않습니다."),
            ("아동 및 변경", "English Master는 일반 사용자를 위한 앱이며 아동의 개인정보를 고의로 수집하지 않습니다. 방침이 바뀌면 이 페이지의 시행일을 갱신합니다."),
        ],
        "terms_title": "English Master 이용약관",
        "terms_intro": "이 약관은 Next Studio가 제공하는 English Master 앱의 이용 조건을 정합니다. 앱을 설치하거나 사용하면 이 약관에 동의한 것으로 봅니다.",
        "terms": [
            ("서비스", "English Master는 TOEIC L&R 학습용 앱입니다. Part 1~7 연습문제, 기본 해설, 모의고사, 기본 오답노트와 통계는 무료이며, 약점 분석·맞춤 추천·간격 반복 복습·학습 계획·AI 오답 피드백·상세 점수 변화 분석은 프리미엄 구독으로 제공합니다."),
            ("구독과 결제", "프리미엄은 1개월, 3개월, 12개월 자동 갱신 구독입니다. 기능은 모두 같고 기간만 다르며 무료 체험은 없습니다. 가격은 스토어에 표시된 금액이 적용되고, 해지하지 않으면 기간이 끝날 때 자동으로 갱신됩니다. 해지와 환불은 구입한 스토어(App Store 또는 Google Play)의 설정과 정책에 따라 처리됩니다."),
            ("학습용 서비스입니다", "모든 문제와 해설은 자체 제작한 학습용 자료이며 실제 시험과 같지 않을 수 있습니다. 점수·등급·AI 평가는 학습용 추정치이며 공식 점수와 같다고 보장하지 않습니다. 합격을 보장하지 않습니다. English Master는 ETS가 개발하거나 보증한 서비스가 아니며 TOEIC은 ETS의 등록 상표입니다."),
            ("금지 행위", "서비스를 해킹하거나 비정상적인 방법으로 접근하는 행위, 다른 사람의 계정을 도용하거나 구독을 부정한 방법으로 얻는 행위, 문제를 대량으로 복제해 재배포하는 행위를 금지합니다."),
            ("서비스 변경과 중단", "기능은 개선을 위해 바뀌거나 중단될 수 있으며, 중요한 변경은 앱이나 이 페이지에 알립니다."),
            ("책임의 제한", "Next Studio는 법이 허용하는 범위에서 데이터 손실, 문제·해설의 오류, 앱 이용으로 생긴 간접 손해에 대해 책임지지 않습니다."),
            ("준거법과 문의", "이 약관은 대한민국 법을 따릅니다. 문의는 아래 이메일로 보내 주세요. 약관이 바뀌면 이 페이지의 시행일을 갱신합니다."),
        ],
        "support_title": "English Master 도움말 및 지원",
        "support_intro": "앱을 쓰다가 문제가 생기면 아래를 확인하고, 해결되지 않으면 이메일로 문의해 주세요.",
        "support": [
            ("구매했는데 적용되지 않아요", "로그인한 계정이 구매할 때의 계정과 같은지 확인하고, 구독 화면의 구매 복원을 눌러 보세요. 인터넷에 연결되어 있어야 합니다."),
            ("구독을 해지하고 싶어요", "구독 화면의 구독 관리 버튼으로 스토어의 구독 관리 페이지를 열어 해지하세요. 해지해도 남은 기간까지는 프리미엄을 쓸 수 있고, 무료 기능과 학습 기록은 그대로 남습니다."),
            ("환불을 받고 싶어요", "환불은 구입한 스토어가 처리합니다. Apple은 reportaproblem.apple.com, Google Play는 주문 내역에서 요청하세요. 환불이 승인되면 프리미엄이 자동으로 회수됩니다."),
            ("문제나 정답이 이상해요", "문제 번호와 의심되는 부분을 적어 이메일로 알려 주세요. 확인 후 새 버전으로 수정합니다."),
            ("문의할 때", "기기 종류, 운영체제 버전, 앱 버전, 문제를 다시 만드는 순서를 적어 보내 주세요."),
        ],
        "delete_title": "English Master 계정 및 데이터 삭제",
        "delete_intro": "English Master는 로그인한 계정의 학습 기록을 서버에 저장합니다. 아래 방법으로 계정과 데이터를 삭제할 수 있습니다.",
        "delete-account": [
            ("삭제 요청하기", f"가입한 로그인(Apple 또는 Google)과 앱 이름(English Master)을 적어 {EMAIL}로 삭제를 요청해 주세요. 본인 확인 후 영업일 기준 7일 안에 삭제하고 알려 드립니다."),
            ("삭제되는 정보", "로그인 계정, 푼 문제·오답노트·모의고사·복습 일정·학습 목표 등 계정에 연결된 서버 데이터가 삭제됩니다. 구매 기록은 환불 처리와 법령상 보관을 위해 계정과의 연결을 끊은 채 정해진 기간 보관될 수 있습니다."),
            ("구독은 따로 해지하세요", "계정을 삭제해도 스토어 구독은 자동으로 해지되지 않습니다. 삭제 전에 App Store 또는 Google Play에서 구독을 해지해 주세요."),
            ("기기의 데이터", "기기에만 저장된 설정은 앱을 삭제하면 함께 지워집니다."),
        ],
        "contact": "문의", "skip": "본문으로 이동", "choose": "언어 선택", "copyright": "© 2026 Next Studio · 넥스트 스튜디오",
    },
    "en": {
        "app": "English Master", "label": "English", "html": "en", "nav": ["Overview", "Privacy", "Terms", "Support", "Delete account"],
        "tag": "Practice TOEIC questions and review the ones you missed",
        "intro": "English Master offers TOEIC L&R Part 1-7 practice, 200-question mock exams, a wrong-answer notebook and a review schedule. All questions are original study material.",
        "features": ["Part 1-7 practice with basic explanations is free", "Mock exams (45 min listening + 75 min reading), wrong-answer notebook, basic statistics", "Premium: weakness analysis, personal recommendations, spaced review, study plan, AI wrong-answer feedback", "Auto-renewing subscriptions of 1, 3 or 12 months, no free trial"],
        "offline": "English Master is not developed or endorsed by ETS, which administers the TOEIC tests. Scores and AI feedback are study estimates, not official scores. TOEIC is a registered trademark of ETS.",
        "date": "Effective November 2, 2026",
        "privacy_title": "English Master Privacy Policy",
        "privacy_intro": "English Master is an English exam study app provided by Next Studio. To save your study records and verify your subscription you sign in with Apple or Google.",
        "privacy": [
            ("Information stored on our server", "Your sign-in account identifier and email (if the provider shares it), the questions you solved and the answers you chose, wrong-answer notes (including cause tags and favorites), mock exam attempts, review schedule, study goals and settings, and your subscription status are stored on our server. We use them only to show your records and plan your review."),
            ("Purchases and subscriptions", "Payments are handled by the Apple App Store and Google Play; English Master never receives your card details. To verify your subscription we store the transaction number, product, expiry date and renewal, cancellation and refund status the store reports."),
            ("AI wrong-answer feedback", "When a Premium subscriber requests AI feedback, the passage, question, choices and the answer you chose are sent to Anthropic's API to generate an explanation. We send nothing else for this purpose. The result is a study estimate."),
            ("Ads and tracking", "English Master has no ads, does not read the advertising identifier (IDFA), and does not track you across apps. We do not use third-party analytics tools."),
            ("Retention and deletion", "Your account and study records on the server are deleted when you request account deletion (see the Delete account page). Purchase records may be kept for a set period, disconnected from your account, for refund handling and legal retention."),
            ("Service providers", "Supabase provides authentication and server storage, Apple and Google provide sign-in and payments, and Anthropic processes AI wrong-answer feedback. We do not sell your information or share it with other third parties."),
            ("Children and changes", "English Master is for general users and does not knowingly collect children's personal information. If this policy changes we update the effective date on this page."),
        ],
        "terms_title": "English Master Terms of Use",
        "terms_intro": "These terms govern your use of English Master, provided by Next Studio. By installing or using the app you agree to them.",
        "terms": [
            ("Service", "English Master is a TOEIC L&R study app. Part 1-7 practice, basic explanations, mock exams, the basic wrong-answer notebook and basic statistics are free; weakness analysis, personal recommendations, spaced review, a study plan, AI wrong-answer feedback and detailed score-change analysis come with a Premium subscription."),
            ("Subscriptions and payment", "Premium is an auto-renewing subscription of 1, 3 or 12 months. Features are identical; only the period differs, and there is no free trial. The price shown in the store applies, and the subscription renews automatically at the end of each period unless you cancel. Cancellation and refunds follow the settings and policies of the store you bought from (App Store or Google Play)."),
            ("Study use only", "All questions and explanations are original study material and may differ from the real exam. Scores, levels and AI feedback are study estimates and are not guaranteed to match official scores. We do not guarantee any result on an exam. English Master is not developed or endorsed by ETS, and TOEIC is a registered trademark of ETS."),
            ("Prohibited conduct", "Hacking or abnormal access to the service, using another person's account or obtaining a subscription by improper means, and copying questions in bulk to redistribute them are prohibited."),
            ("Changes and suspension", "Features may change or stop for improvement; important changes are announced in the app or on this page."),
            ("Limitation of liability", "To the extent the law allows, Next Studio is not liable for data loss, errors in questions or explanations, or indirect damages from using the app."),
            ("Governing law and contact", "These terms are governed by the laws of the Republic of Korea. Write to the email below with questions. If the terms change we update the effective date on this page."),
        ],
        "support_title": "English Master Help and Support",
        "support_intro": "If something goes wrong, check the items below and email us if it is not resolved.",
        "support": [
            ("I bought it but it is not applied", "Check that you are signed in with the same account you bought with, then tap Restore purchases on the subscription screen. You need an internet connection."),
            ("I want to cancel", "Use the Manage subscription button on the subscription screen to open the store's subscription page and cancel there. You keep Premium until the end of the paid period, and free features and your records remain."),
            ("I want a refund", "Refunds are handled by the store you bought from: reportaproblem.apple.com for Apple, your order history for Google Play. When a refund is approved Premium is revoked automatically."),
            ("A question or answer looks wrong", "Email us the question number and what looks wrong. We check it and fix it as a new version."),
            ("When you write to us", "Please include your device model, operating system version, app version and the steps to reproduce the problem."),
        ],
        "delete_title": "English Master Account and Data Deletion",
        "delete_intro": "English Master stores the study records of a signed-in account on our server. You can have your account and data deleted as described below.",
        "delete-account": [
            ("Request deletion", f"Email {EMAIL} with the sign-in you used (Apple or Google) and the app name (English Master). After verifying it is you we delete the data within 7 business days and let you know."),
            ("What is deleted", "Your sign-in account and the server data connected to it: solved questions, wrong-answer notes, mock exams, review schedule and study goals. Purchase records may be kept for a set period, disconnected from your account, for refund handling and legal retention."),
            ("Cancel your subscription separately", "Deleting your account does not cancel a store subscription. Cancel it in the App Store or Google Play before deleting."),
            ("Data on your device", "Settings stored only on your device are removed when you delete the app."),
        ],
        "contact": "Contact", "skip": "Skip to content", "choose": "Language", "copyright": "© 2026 Next Studio",
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
            f'<a href="mailto:{EMAIL}?subject=EnglishMaster%20{kind}">{EMAIL}</a></p></aside>'
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
    f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="English Master"><title>English Master · 기출마스터 · Next Studio</title><link rel="stylesheet" href="style.css"></head><body><main><header class="top"><span class="brand">English Master · 기출마스터</span></header><article><p class="muted">EXAM · PRACTICE · RECORD</p><h1>English Master · 기출마스터</h1><p class="lead">Choose your language. · 언어를 선택하세요.</p><div class="cards languages">{links}</div></article><footer>© 2026 Next Studio<br><a href="mailto:{EMAIL}">{EMAIL}</a></footer></main></body></html>""",
    encoding="utf-8",
)
print(f"Generated {len(LANGUAGES) * len(KINDS) + 1} pages.")
