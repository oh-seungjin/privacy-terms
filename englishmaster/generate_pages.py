"""Generate the public English Master pages: index, privacy, terms, support, delete-account in Korean and English.
Content must match the shipped app. Update the date and every claim when behaviour changes (this version describes: five exams, Writing/Speaking, Crashlytics in release builds, in-app deletion; AI feedback is switched off server-side)."""

from html import escape as esc
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SITE = "https://oh-seungjin.github.io/privacy-terms/englishmaster"
EMAIL = "dhalska2@gmail.com"
KINDS = ("index", "privacy", "terms", "support", "delete-account")

LANGUAGES = {
    "ko": {
        "app": "English Master", "label": "한국어", "html": "ko", "nav": ["소개", "개인정보처리방침", "이용약관", "지원", "계정 삭제"],
        "tag": "TOEIC·TEPS·TOEFL·IELTS·OPIc를 연습하고 복습하는 학습 앱",
        "intro": "다섯 시험의 연습문제와 모의고사, 오답노트와 복습 일정을 제공합니다. Writing은 직접 쓰고, Speaking은 녹음해 저장합니다. 모든 문제는 자체 제작한 학습용 문제입니다.",
        "features": ["TOEIC L&R Part 1~7, TEPS, TOEFL iBT(2026 형식의 고정 연습형), IELTS(Academic·General Training), OPIc 연습문제와 해설", "듣기 음원은 자체 제작한 음성입니다", "시험별 모의고사·회차: 시간 제한, 일시정지와 이어하기, 결과와 해설", "Writing 작성·저장, Speaking 녹음·저장과 전사(말한 내용 확인용)", "오답노트와 복습 일정, 프리미엄 구독(1개월·3개월·12개월)"],
        "offline": "English Master는 TOEIC·TOEFL·TEPS·IELTS·OPIc 시험 기관이 개발·보증한 서비스가 아니며 제휴 관계가 없습니다. 점수와 평가는 학습용 추정치이며 공식 점수·등급과 같지 않습니다. 발음·억양·유창성은 평가하지 않습니다. 각 시험명은 해당 소유자의 상표입니다.",
        "date": "시행일: 2026년 11월 14일",
        "privacy_title": "English Master 개인정보처리방침",
        "privacy_intro": "English Master는 Next Studio(넥스트 스튜디오)가 제공하는 영어 시험 학습 앱입니다. 학습 기록을 저장하고 구독을 확인하려면 Apple 또는 Google 계정으로 로그인해야 합니다.",
        "privacy": [
            ("서버에 저장하는 정보", "로그인 계정 식별자와 이메일(로그인 제공자가 전달하는 경우), 표시 이름·언어 설정, 내가 푼 문제와 선택한 답, 오답노트(원인 표시·즐겨찾기 포함), 모의고사 응시 기록과 이어하기 상태, 복습 일정, 학습 목표, 기능 사용 횟수, 문제 오류 신고 내용이 서버에 저장됩니다. 채점, 학습 기록 표시, 복습 계획, 이용 한도 관리에만 사용합니다."),
            ("Writing 답안과 Speaking 녹음", "Writing에서 직접 쓴 글과 Speaking에서 녹음한 음성 파일, 그 음성에서 만든 전사(텍스트)가 내 계정에 저장됩니다. 녹음 파일은 비공개 저장소의 내 폴더에만 올라가며 본인만 재생할 수 있습니다. 마이크는 Speaking 녹음을 할 때만 사용하며, 전사는 말한 내용을 확인하는 용도입니다. 발음·억양·유창성은 평가하지 않습니다. 보내지 못한 임시 녹음은 기기에 남을 수 있고 업로드 후 삭제되며 7일이 지나면 삭제됩니다."),
            ("구매와 구독", "결제는 Apple App Store와 Google Play가 처리하며 English Master는 카드 정보를 받지 않습니다. 구독을 확인하려고 스토어가 알려 주는 거래 번호, 상품 종류, 만료일, 갱신·해지·환불 상태를 서버에 저장합니다."),
            ("AI 피드백", "AI 오답 피드백 등 AI 기능이 제공되는 경우에만, 해당 문제의 지문·문제·선택지와 내가 고른 답(또는 내가 쓴 글이나 전사)이 AI 사업자(Anthropic)의 API로 전송되어 설명이 만들어집니다. 이 용도 외에는 전송하지 않으며, 결과는 학습용 추정치입니다. 이 기능은 현재 꺼져 있으며, 켤 때는 앱에서 안내합니다."),
            ("오류 진단", "정식 배포 앱이 비정상 종료되면 오류 기록, 기기 모델, 운영체제와 앱 버전, 설치 단위의 임의 식별자가 Google Firebase Crashlytics로 전송됩니다. 이 정보는 내 계정과 연결하지 않으며 오류를 고치는 데만 씁니다."),
            ("광고와 추적", "English Master에는 광고가 없고, 광고 식별자(IDFA)를 읽지 않으며, 앱 간 추적을 하지 않습니다."),
            ("보관과 삭제", "서버의 계정과 학습 기록은 계정이 있는 동안 보관되며, 앱의 설정에서 계정 삭제를 하면 학습 기록, 작성한 글, 녹음 파일과 전사, AI 기록, 구독 연결 정보, 프로필이 삭제되고 로그인 계정도 삭제됩니다(같은 로그인으로 다른 앱을 쓰는 경우 로그인 계정은 유지되고 English Master 데이터만 삭제됩니다). 문제 오류 신고는 신고자 정보를 지운 채 남을 수 있고, 구독 이벤트 기록은 계정과의 연결 없이 남을 수 있습니다. 별도의 보관 기간은 정하지 않았으며, 법령상 보관 의무가 있는 정보는 그 기간 동안 보관합니다."),
            ("처리 위탁과 국외 이전", "인증·데이터베이스·파일 저장은 Supabase(데이터 처리 지역: 일본 도쿄), 로그인과 결제는 Apple·Google, 오류 진단은 Google Firebase Crashlytics, AI 피드백(켜져 있는 경우)은 Anthropic이 처리합니다. 이 외의 제3자에게 정보를 판매하거나 제공하지 않습니다."),
            ("이용자의 권리", "앱에서 내 기록을 확인하고 계정을 삭제할 수 있습니다. 열람·정정·삭제 요청은 아래 이메일로 보내 주세요."),
            ("아동 및 변경", "English Master는 일반 사용자를 위한 앱이며 아동의 개인정보를 고의로 수집하지 않습니다. 방침이 바뀌면 이 페이지의 시행일을 갱신합니다."),
        ],
        "terms_title": "English Master 이용약관",
        "terms_intro": "이 약관은 Next Studio(넥스트 스튜디오)가 제공하는 English Master 앱의 이용 조건을 정합니다. 앱을 설치하거나 사용하면 이 약관에 동의한 것으로 봅니다.",
        "terms": [
            ("서비스", "English Master는 TOEIC, TEPS, TOEFL iBT, IELTS, OPIc 학습용 앱입니다. 연습문제, 해설, 모의고사, 오답노트, Writing 작성과 Speaking 녹음 저장 기능을 제공합니다. 무료 기능과 프리미엄 기능의 구분은 앱 화면의 안내를 따릅니다."),
            ("구독과 결제", "프리미엄은 1개월, 3개월, 12개월 자동 갱신 구독이며 기능은 모두 같고 기간만 다릅니다. 가격은 스토어에 표시된 금액이 적용됩니다. 구독은 스토어 계정 설정에서 갱신 24시간 전까지 해지하지 않으면 자동으로 갱신됩니다. 결제·해지·환불은 Apple 또는 Google의 정책을 따르고, 환불이 승인되면 프리미엄이 회수됩니다. 구독이 끝나도 학습 기록은 삭제되지 않고 프리미엄 기능만 제한됩니다. 구독 화면에서 구매 복원을 할 수 있습니다."),
            ("학습용 서비스입니다", "모든 문제와 해설은 자체 제작한 학습용 자료이며 실제 시험과 같지 않을 수 있습니다. TOEFL 연습은 고정된 연습 구성이며 공식 적응형 시험이 아닙니다. 점수·등급·AI 평가는 학습용 추정치이며 공식 점수와 같다고 보장하지 않고, 시험 결과를 보장하지 않습니다. Speaking은 녹음과 전사를 제공할 뿐 발음·억양·유창성을 평가하지 않습니다. 시험 기관과 제휴하지 않았으며 각 시험명은 해당 소유자의 상표입니다."),
            ("이용자의 글과 녹음", "내가 쓴 글과 녹음은 내 것이며, 학습 기능을 제공하는 목적으로만 처리합니다. 처리 방식은 개인정보처리방침을 따릅니다."),
            ("금지 행위", "서비스를 해킹하거나 비정상적인 방법으로 접근하는 행위, 다른 사람의 계정을 도용하거나 구독을 부정한 방법으로 얻는 행위, 문제와 음원을 대량으로 복제해 재배포하는 행위를 금지합니다."),
            ("서비스 변경과 중단", "기능은 개선을 위해 바뀌거나 중단될 수 있으며, 중요한 변경은 앱이나 이 페이지에 알립니다."),
            ("책임의 제한", "Next Studio는 법이 허용하는 범위에서 데이터 손실, 문제·해설·음원의 오류, 앱 이용으로 생긴 간접 손해에 대해 책임지지 않습니다. 오류는 앱의 신고 기능이나 이메일로 알려 주세요."),
            ("준거법과 문의", "이 약관은 대한민국 법을 따릅니다. 문의는 아래 이메일로 보내 주세요. 약관이 바뀌면 이 페이지의 시행일을 갱신합니다."),
        ],
        "support_title": "English Master 도움말 및 지원",
        "support_intro": "앱을 쓰다가 문제가 생기면 아래를 확인하고, 해결되지 않으면 이메일로 문의해 주세요.",
        "support": [
            ("구매했는데 적용되지 않아요", "로그인한 계정이 구매할 때의 계정과 같은지 확인하고, 구독 화면의 구매 복원을 눌러 보세요. 인터넷에 연결되어 있어야 합니다."),
            ("구독을 해지하고 싶어요", "구독 화면의 스토어에서 구독 관리 버튼으로 스토어의 구독 관리 페이지를 열어 해지하세요. 해지해도 남은 기간까지는 프리미엄을 쓸 수 있고, 무료 기능과 학습 기록은 그대로 남습니다."),
            ("환불을 받고 싶어요", "환불은 구입한 스토어가 처리합니다. Apple은 reportaproblem.apple.com, Google Play는 주문 내역에서 요청하세요. 환불이 승인되면 프리미엄이 자동으로 회수됩니다."),
            ("녹음이 안 돼요", "설정에서 English Master의 마이크 권한을 허용했는지 확인하세요. 녹음은 인터넷이 연결되어 있어야 저장됩니다."),
            ("문제나 정답, 음원이 이상해요", "문제 화면의 신고 기능을 쓰거나, 문제 번호와 의심되는 부분을 적어 이메일로 알려 주세요. 확인 후 새 버전으로 수정합니다."),
            ("문의할 때", "기기 종류, 운영체제 버전, 앱 버전, 문제를 다시 만드는 순서를 적어 보내 주세요."),
        ],
        "delete_title": "English Master 계정 및 데이터 삭제",
        "delete_intro": "English Master는 로그인한 계정의 학습 기록을 서버에 저장합니다. 아래 방법으로 계정과 데이터를 삭제할 수 있습니다.",
        "delete-account": [
            ("앱에서 삭제하기", "앱의 설정에서 계정 삭제를 누르고 안내에 따라 확인하면 바로 삭제가 시작됩니다. 끝나면 로그아웃되고 같은 계정으로 다시 로그인해도 이전 기록은 남아 있지 않습니다."),
            ("이메일로 요청하기", f"앱을 쓸 수 없는 경우 가입한 로그인(Apple 또는 Google)과 앱 이름(English Master)을 적어 {EMAIL}로 삭제를 요청해 주세요. 본인 확인 후 영업일 기준 7일 안에 삭제하고 알려 드립니다."),
            ("삭제되는 정보", "로그인 계정, 푼 문제·오답노트·모의고사·복습 일정·학습 목표, 작성한 글, Speaking 녹음 파일과 전사, AI 기록 등 계정에 연결된 서버 데이터가 삭제됩니다. 오류 신고는 신고자 정보를 지운 채, 구독 이벤트 기록은 계정과의 연결 없이 남을 수 있습니다."),
            ("구독은 따로 해지하세요", "계정을 삭제해도 스토어 구독은 자동으로 해지되지 않습니다. 삭제 전에 App Store 또는 Google Play에서 구독을 해지해 주세요."),
            ("기기의 데이터", "기기에만 저장된 설정과 임시 녹음은 앱을 삭제하면 함께 지워집니다."),
        ],
        "contact": "문의", "skip": "본문으로 이동", "choose": "언어 선택", "copyright": "© 2026 Next Studio · 넥스트 스튜디오",
    },
    "en": {
        "app": "English Master", "label": "English", "html": "en", "nav": ["Overview", "Privacy", "Terms", "Support", "Delete account"],
        "tag": "Practice and review for TOEIC, TEPS, TOEFL, IELTS and OPIc",
        "intro": "Practice questions and mock exams for five exams, a wrong-answer notebook and a review schedule. You type Writing answers and record Speaking answers. All questions are original study material.",
        "features": ["Practice with explanations: TOEIC L&R Part 1-7, TEPS, TOEFL iBT (2026 format, fixed practice sets), IELTS (Academic and General Training), OPIc", "Listening audio is self-produced speech", "Mock exams and rounds per exam: timer, pause and resume, results and explanations", "Writing: type and save; Speaking: record, save and a transcript (to check what was said)", "Wrong-answer notebook, review schedule, Premium subscription (1, 3 or 12 months)"],
        "offline": "English Master is not developed or endorsed by, and is not affiliated with, the organizations that administer TOEIC, TOEFL, TEPS, IELTS or OPIc. Scores and feedback are study estimates, not official scores. Pronunciation, intonation and fluency are not assessed. Exam names are trademarks of their owners.",
        "date": "Effective November 14, 2026",
        "privacy_title": "English Master Privacy Policy",
        "privacy_intro": "English Master is an English exam study app provided by Next Studio. To save your study records and verify your subscription you sign in with Apple or Google.",
        "privacy": [
            ("Information stored on our server", "Your sign-in account identifier and email (if the provider shares it), display name and language settings, the questions you solved and the answers you chose, wrong-answer notes (including cause tags and favorites), mock exam attempts and resume state, review schedule, study goals, feature usage counts and the content of error reports you send. We use it only for grading, showing your records, review planning and usage limits."),
            ("Writing answers and Speaking recordings", "The text you write, the audio you record in Speaking and the transcript made from it are stored under your account. Recordings go to a private storage folder that only you can play. The microphone is used only while you record a Speaking answer, and the transcript is only for checking what was said. We do not assess pronunciation, intonation or fluency. An unsent recording may stay on your device, is deleted after upload, and is deleted after 7 days at the latest."),
            ("Purchases and subscriptions", "Payments are handled by the Apple App Store and Google Play; English Master never receives your card details. To verify your subscription we store the transaction number, product, expiry date and renewal, cancellation and refund status that the store reports."),
            ("AI feedback", "Only when an AI feature such as AI wrong-answer feedback is available, the passage, question, choices and your answer (or your text or transcript) are sent to the AI provider's API (Anthropic) to generate the explanation. Nothing else is sent for this purpose and the result is a study estimate. This feature is currently switched off; the app will say so when it is switched on."),
            ("Crash diagnostics", "If the released app crashes, the crash log, device model, operating system and app version and a random per-installation identifier are sent to Google Firebase Crashlytics. This data is not linked to your account and is used only to fix errors."),
            ("Ads and tracking", "English Master has no ads, does not read the advertising identifier (IDFA), and does not track you across apps."),
            ("Retention and deletion", "Your account and records stay while the account exists. When you delete your account in the app's settings, your study records, written text, recordings and transcripts, AI records, subscription link and profile are deleted, and the sign-in account is deleted too (if you use another app with the same login, the sign-in account stays and only English Master data is deleted). Error reports may remain without your identity, and subscription event records may remain without a link to you. We have not set a separate retention period; information that a law requires us to keep is kept for that period."),
            ("Service providers and transfers", "Supabase provides authentication, database and file storage (data region: Tokyo, Japan), Apple and Google provide sign-in and payments, Google Firebase Crashlytics provides crash diagnostics, and Anthropic processes AI feedback when it is switched on. We do not sell your information or share it with other third parties."),
            ("Your rights", "You can review your records in the app and delete your account there. For access, correction or deletion requests write to the email below."),
            ("Children and changes", "English Master is for general users and does not knowingly collect children's personal information. If this policy changes we update the effective date on this page."),
        ],
        "terms_title": "English Master Terms of Use",
        "terms_intro": "These terms govern your use of English Master, provided by Next Studio. By installing or using the app you agree to them.",
        "terms": [
            ("Service", "English Master is a study app for TOEIC, TEPS, TOEFL iBT, IELTS and OPIc. It offers practice questions, explanations, mock exams, a wrong-answer notebook, Writing and Speaking recording storage. Which features are free and which are Premium is shown in the app."),
            ("Subscriptions and payment", "Premium is an auto-renewing subscription of 1, 3 or 12 months; the features are identical and only the period differs. The price shown in the store applies. The subscription renews automatically unless you cancel it in your store account settings at least 24 hours before renewal. Payment, cancellation and refunds follow Apple's or Google's policies, and Premium is revoked if a refund is approved. When a subscription ends your study records are kept and only Premium features are limited. You can restore purchases on the subscription screen."),
            ("Study use only", "All questions and explanations are original study material and may differ from the real exam. TOEFL practice uses fixed practice sets and is not the official adaptive test. Scores, levels and AI feedback are study estimates, are not guaranteed to match official scores, and we do not guarantee any exam result. Speaking provides recording and a transcript and does not assess pronunciation, intonation or fluency. We are not affiliated with any exam organization and exam names are trademarks of their owners."),
            ("Your text and recordings", "Your text and recordings are yours; we process them only to provide the study features, as described in the Privacy Policy."),
            ("Prohibited conduct", "Hacking or abnormal access to the service, using another person's account or obtaining a subscription by improper means, and copying questions or audio in bulk to redistribute them are prohibited."),
            ("Changes and suspension", "Features may change or stop for improvement; important changes are announced in the app or on this page."),
            ("Limitation of liability", "To the extent the law allows, Next Studio is not liable for data loss, errors in questions, explanations or audio, or indirect damages from using the app. Please report errors with the in-app report or by email."),
            ("Governing law and contact", "These terms are governed by the laws of the Republic of Korea. Write to the email below with questions. If the terms change we update the effective date on this page."),
        ],
        "support_title": "English Master Help and Support",
        "support_intro": "If something goes wrong, check the items below and email us if it is not resolved.",
        "support": [
            ("I bought it but it is not applied", "Check that you are signed in with the same account you bought with, then tap Restore purchases on the subscription screen. You need an internet connection."),
            ("I want to cancel", "Use the Manage subscription in the store button on the subscription screen to open the store's subscription page and cancel there. You keep Premium until the end of the paid period, and free features and your records remain."),
            ("I want a refund", "Refunds are handled by the store you bought from: reportaproblem.apple.com for Apple, your order history for Google Play. When a refund is approved Premium is revoked automatically."),
            ("Recording does not work", "Check that microphone access is allowed for English Master in your device settings. Recordings are saved only while you are online."),
            ("A question, answer or audio looks wrong", "Use the report option on the question screen, or email us the question number and what looks wrong. We check it and fix it as a new version."),
            ("When you write to us", "Please include your device model, operating system version, app version and the steps to reproduce the problem."),
        ],
        "delete_title": "English Master Account and Data Deletion",
        "delete_intro": "English Master stores the study records of a signed-in account on our server. You can have your account and data deleted as described below.",
        "delete-account": [
            ("Delete in the app", "Open Settings, tap Delete account and confirm. Deletion starts right away; when it finishes you are signed out, and signing in again with the same login shows none of the old records."),
            ("Request by email", f"If you cannot use the app, email {EMAIL} with the sign-in you used (Apple or Google) and the app name (English Master). After verifying it is you we delete the data within 7 business days and let you know."),
            ("What is deleted", "Your sign-in account and the server data connected to it: solved questions, wrong-answer notes, mock exams, review schedule, study goals, written text, Speaking recordings and transcripts, and AI records. Error reports may remain without your identity, and subscription event records without a link to you."),
            ("Cancel your subscription separately", "Deleting your account does not cancel a store subscription. Cancel it in the App Store or Google Play before deleting."),
            ("Data on your device", "Settings and unsent recordings stored only on your device are removed when you delete the app."),
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
