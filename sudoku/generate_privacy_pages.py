"""Generate Sudoku Pulse public pages (privacy policy + help & support, 8 languages).

Run: python3 generate_privacy_pages.py

Output (all relative to this folder):
  index.html                 language hub
  <lang>/privacy.html        privacy policy  (ko, en, ja, zh-hans, es, fr, de, pt-br)
  <lang>/support.html        help & support
  privacy.html, privacy-<lang>.html
                             legacy privacy URLs used by shipped app builds;
                             same content as <lang>/privacy.html. Never delete.
terms.html is hand-written (ko/en) and not generated here.
"""
from html import escape
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT_URL = "https://oh-seungjin.github.io/privacy-terms/sudoku/"
EMAIL = "dhalska2@gmail.com"

# (folder, html lang, label, legacy privacy filename)
LANGUAGES = [
    ("ko", "ko", "한국어", "privacy.html"),
    ("en", "en", "English", "privacy-en.html"),
    ("ja", "ja", "日本語", "privacy-ja.html"),
    ("zh-hans", "zh-Hans", "简体中文", "privacy-zh-hans.html"),
    ("es", "es", "Español", "privacy-es.html"),
    ("fr", "fr", "Français", "privacy-fr.html"),
    ("de", "de", "Deutsch", "privacy-de.html"),
    ("pt-br", "pt-BR", "Português (Brasil)", "privacy-pt-br.html"),
]

PAGES = {
    "ko": {
        "ui": {"privacy": "개인정보처리방침", "support": "도움말 및 지원", "terms": "이용약관", "languages": "언어 선택", "skip": "본문으로", "updated": "최종 수정: 2026년 10월 3일"},
        "privacy": {
            "title": "Sudoku Pulse 개인정보처리방침",
            "effective": "시행일: 2026년 10월 3일",
            "intro": "넥스트 스튜디오(Next Studio)는 iOS·Android용 Sudoku Pulse를 운영합니다. 이 방침은 앱이 처리하는 정보와 그 목적, 이용자가 선택할 수 있는 사항을 설명하며 앱과 이 웹사이트에 적용됩니다.",
            "sections": [
                ("1. 계정과 로그인", "앱을 처음 실행하면 이름이나 이메일 없이 익명 Supabase 세션이 자동으로 만들어집니다. 이 세션 덕분에 로그인하지 않아도 구매, 힌트, 플레이 통계를 이용할 수 있습니다. Apple(iOS) 또는 Google(Android) 로그인은 선택 사항이며 글로벌 랭킹에 표시될 때만 필요합니다. 로그인하면 익명 세션의 Sudoku 데이터(힌트 잔량, 광고 제거, 구매 기록, 플레이 기록)가 해당 계정에 연결·병합됩니다."),
                ("2. 수집하는 정보와 이용 목적", [
                    "로그인 이메일과 로그인 공급자 식별자(로그인한 경우): 계정 식별에 사용합니다. 랭킹에는 일부를 가린(마스킹한) 이메일만 표시됩니다.",
                    "이용자가 선택한 국가 코드: 랭킹에 국기를 표시하는 데 사용합니다.",
                    "플레이 기록: 난이도, 완료 시간, 실수 수, 칸 수, 사용한 힌트 수, 펄스 콤보 보너스, 오늘의 퍼즐 여부, 퍼즐의 해시 지문, 입력 기록(칸, 숫자, 게임 시계 기준 초, 입력 유형), 플레이 세션 시작·종료 시각. 서버는 이를 결과 검증, 점수 계산, 부정행위 방지, 통계에 사용합니다.",
                    "일일 무료 힌트 사용 횟수: 광고 시청이나 구매 없이 하루 3개까지 쓸 수 있는 무료 힌트의 사용 횟수를 서버 기준 UTC 날짜별로 세며, 서버의 Sudoku 게임 프로필에 함께 저장합니다.",
                    "진행 중인 퍼즐(로그인한 이용자만): 다른 기기에서 이어서 풀 수 있도록 진행 중인 퍼즐을 서버에 저장할 수 있습니다.",
                    "구매 정보: 상품 ID, 거래 ID, 검증 상태. 힌트 팩과 광고 제거 지급, 구매 복원에 사용합니다. 비소모성 상품인 광고 제거는 같은 Apple ID를 쓰는 다른 계정으로 옮겨질 수 있습니다. 결제 정보는 Apple 또는 Google이 처리하며 회사는 받거나 저장하지 않습니다.",
                    "푸시 알림 정보(알림을 켠 경우에만): FCM 토큰, 플랫폼, 언어, 알림 설정. 순위 변동 알림과 리마인더를 보내는 데 사용합니다. 알림은 기본적으로 꺼져 있으며, 설정에서 끄면 더 이상 발송되지 않습니다.",
                    "광고: Google AdMob과 Google UMP(동의 관리) SDK가 광고 제공, 노출 빈도 관리, 부정행위 방지, 동의 기록을 위해 기기 식별자, IP 주소, 진단 정보를 처리할 수 있습니다. iOS 광고 식별자(IDFA)는 앱 추적 투명성(ATT) 요청에서 허용한 경우에만 사용됩니다. 보상형 광고는 이름이나 이메일이 아닌, 앱이 만든 무작위 식별자로 서버에서 보상을 검증합니다.",
                    "충돌 보고: 앱이 비정상 종료되면 Firebase Crashlytics가 기기 모델, OS 버전, 앱 버전, 충돌 스택 트레이스, 설치 식별자를 수집하며 오류 수정에 사용합니다. 디버그 빌드에서는 수집하지 않습니다.",
                ]),
                ("3. 기기에만 저장되는 정보", "언어, 진동 설정, 튜토리얼 완료 여부, 기법 도감에서 익힌 기법, 최고 콤보, 현재 퍼즐 자동 저장, 광고 간격을 조절하는 카운터는 기기에만 저장되며 서버로 전송되지 않습니다. 앱을 삭제하면 함께 삭제됩니다."),
                ("4. 처리 위탁 및 국외 처리", "Supabase(인증, 데이터베이스, 서버 함수), Google Firebase(푸시 알림, Crashlytics), Google AdMob·UMP(광고, 동의 관리), Apple·Google(로그인, 결제)을 이용합니다. 각 서비스에는 필요한 정보만 제공하며, 각 사업자는 이 방침과 같은 수준의 보호를 제공하는 자체 개인정보 처리방침과 보안 약정에 따라 정보를 처리합니다. 정보는 이용자의 국가 밖, 각 사업자가 운영하는 국가의 서버에서 관련 법령이 요구하는 보호조치에 따라 처리될 수 있습니다."),
                ("5. 보유 기간과 삭제", "앱에서 데이터를 삭제하거나 이메일로 삭제를 요청할 때까지 보유합니다. 로그인한 경우 설정 > Sudoku 탈퇴에서 이 게임의 데이터를 영구 삭제할 수 있으며, Apple 로그인 계정은 Apple 로그인 토큰도 철회합니다. 로그인 전 데이터는 기기의 익명 세션에만 연결되어 있어, 로그인하기 전에 앱을 삭제하면 복구하거나 이용자와 다시 연결할 수 없습니다. 법령상 보관 의무가 있는 거래 기록은 해당 기간 동안 보관할 수 있습니다. 충돌 보고는 Firebase Crashlytics의 보관 기간에 따릅니다."),
                ("6. 이용자 권리와 선택", "이용자는 dhalska2@gmail.com으로 개인정보 열람·정정·삭제·처리 제한 및 동의 철회를 요청할 수 있습니다. 광고 동의는 설정 > 광고 개인정보 설정(지역에 따라 표시)에서, 추적 허용은 기기 설정에서 변경할 수 있습니다. 알림은 설정에서 언제든 켜거나 끌 수 있습니다."),
                ("7. 아동, 보안 및 변경", "서비스는 아동을 대상으로 하지 않으며 필요한 보호자 동의 없이 아동 정보를 고의로 수집하지 않습니다. 접근 통제와 암호화 통신 등 합리적인 보호조치를 적용합니다. 변경 시 시행일을 갱신하고 중요한 변경을 알립니다."),
            ],
            "contact": "개인정보 문의",
        },
        "support": {
            "title": "Sudoku Pulse 도움말 및 지원",
            "intro": "Sudoku Pulse에 대해 자주 묻는 질문입니다. 더 도움이 필요하면 이메일로 문의해 주세요.",
            "faq": [
                ("힌트와 해설은 어떻게 작동하나요?", "빈 칸을 선택하고 힌트를 누르면 정답 숫자가 채워지고, 보드 위에 풀이 기법과 함께 그 숫자인 이유가 설명됩니다. 익힌 기법은 기법 도감에 모입니다. 선택한 칸을 풀려면 다른 칸이 먼저 필요하면 지금 풀 수 있는 칸을 강조해 주며, 이때는 힌트가 사용되지 않습니다. 매일 무료 힌트 3개를 쓸 수 있고(UTC 기준 자정에 초기화), 그 뒤에는 Pulse 상점의 힌트를 쓰거나 선택형 광고를 보고 힌트 1개를 받을 수 있습니다. 힌트를 쓰면 펄스 콤보가 끊깁니다."),
                ("꼭 로그인해야 하나요?", "아니요. 앱이 익명 세션을 자동으로 만들기 때문에 로그인하지 않아도 모든 퍼즐, 힌트, 구매를 이용할 수 있습니다. Apple(iOS) 또는 Google(Android) 로그인은 선택 사항이며 글로벌 랭킹에 참여할 때만 필요합니다. 로그인하면 그동안의 힌트 잔량, 광고 제거, 구매 기록, 플레이 기록이 계정에 연결됩니다. 로그인하기 전에 앱을 삭제하면 그 데이터는 복구할 수 없습니다."),
                ("랭킹은 어떻게 반영되나요?", [
                    "로그인해야 합니다. 로그아웃 또는 오프라인 상태에서 시작한 게임은 랭킹에 반영되지 않습니다.",
                    "힌트를 3개까지 사용한 퍼즐이 반영됩니다. 3개를 넘게 쓰면 반영되지 않습니다.",
                    "점수는 난이도별 속도(실수 1회당 +10초)와 펄스 콤보 보너스로 계산됩니다.",
                    "오늘의 퍼즐은 즐기기용이며 랭킹에 반영되지 않습니다.",
                    "이미 끝낸 같은 퍼즐을 다시 풀면 랭킹에 다시 반영되지 않습니다.",
                    "모든 결과는 서버에서 검증된 뒤 랭킹에 반영됩니다.",
                ]),
                ("구매를 복원하려면 어떻게 하나요?", "Pulse 상점에서 구매 복원을 누르세요. 광고 제거는 App Store 계정에서 복원되고, 힌트 잔량은 스토어에서 복원할 항목이 없더라도 서버에서 다시 불러옵니다. 이미 사용한 힌트는 복원되지 않습니다. 결제·환불 문의는 구매한 스토어로 해 주세요."),
                ("알림은 어떻게 켜고 끄나요?", "알림은 선택 사항이며 기본적으로 꺼져 있습니다. 설정 > 알림에서 켜거나 끌 수 있습니다. 켜면 순위 변동 알림과 리마인더를 보내 드립니다."),
                ("내 데이터를 삭제하려면 어떻게 하나요?", "로그인한 상태에서 설정 > Sudoku 탈퇴를 누르면 이 게임의 데이터가 영구 삭제됩니다. Apple 로그인 사용자는 Apple 로그인 화면에서 본인 확인을 거치며, Apple 로그인 토큰도 철회됩니다. 이메일로 삭제를 요청할 수도 있습니다. 자세한 내용은 {privacy}을 확인해 주세요."),
                ("문의하기", "제목에 Sudoku Pulse를 적어 dhalska2@gmail.com으로 앱 버전, 기기와 OS 버전, 문제가 생긴 과정을 보내 주세요. 비밀번호, 인증 코드, 결제 정보는 보내지 마세요."),
            ],
            "contact": "지원 문의",
        },
    },
    "en": {
        "ui": {"privacy": "Privacy Policy", "support": "Help & Support", "terms": "Terms of Service", "languages": "Choose language", "skip": "Skip to content", "updated": "Last updated October 3, 2026"},
        "privacy": {
            "title": "Sudoku Pulse Privacy Policy",
            "effective": "Effective October 3, 2026",
            "intro": "Next Studio (넥스트 스튜디오) operates Sudoku Pulse for iOS and Android. This policy explains what information the app processes, why, and the choices you have. It applies to the app and to this website.",
            "sections": [
                ("1. Accounts and sign-in", "When you first open the app, it automatically creates an anonymous Supabase session that has no name or email address. This lets purchases, hints and play statistics work without signing in. Signing in with Apple (iOS) or Google (Android) is optional and only needed to appear in the global ranking. When you sign in, the Sudoku data from your anonymous session (hint balance, ad removal, purchase records and play records) is linked to and merged into that account."),
                ("2. Information we collect and why", [
                    "Sign-in email address and provider identifier (only if you sign in): to identify your account. The leaderboard shows only a masked version of your email address.",
                    "Country code you choose: to show a flag on the leaderboard.",
                    "Play records: difficulty, completion time, mistakes, number of cells, hints used, Pulse combo bonus, whether it was the daily puzzle, a hash fingerprint of the puzzle, and the move log (cell, digit, game-clock seconds and entry type), plus the start and finish times of each play session. Our server uses these to verify results, calculate scores, prevent cheating and keep statistics.",
                    "Daily free hint count: the number of free hints you have used each day (up to 3 before an ad or a purchased hint is needed) is counted per server UTC date and stored with your Sudoku game profile on our server.",
                    "In-progress puzzle (signed-in players only): the puzzle you are playing may be saved to our server so you can resume it on another device.",
                    "Purchase information: product ID, transaction ID and verification status, used to grant hint packs and ad removal and to restore purchases. Ad removal is a non-consumable purchase and can move to another account that uses the same Apple ID. Payment details are handled by Apple or Google; we do not receive or store them.",
                    "Push notification information (only if you turn notifications on): FCM token, platform, language and notification setting, used to send ranking-change and reminder notifications. Notifications are off by default, and turning them off in Settings stops them.",
                    "Advertising: Google AdMob and the Google User Messaging Platform (UMP) consent SDK may process device identifiers, IP address and diagnostic information to show ads, manage ad frequency, prevent fraud and record consent. On iOS, the advertising identifier (IDFA) is used only if you allow it in the App Tracking Transparency (ATT) prompt. Rewarded ads are verified on our server with a random identifier generated by the app, not with your name or email address.",
                    "Crash reports: if the app crashes, Firebase Crashlytics collects the device model, OS version, app version, crash stack traces and an installation identifier so that we can fix the problem. Crash reports are not collected in debug builds.",
                ]),
                ("3. Information stored only on your device", "Language, haptics setting, tutorial completion, techniques learned in the technique book, best combo, the autosave of your current puzzle, and a counter used to space out ads are stored only on your device and are not sent to our server. They are removed when you delete the app."),
                ("4. Service providers and international processing", "We use Supabase (authentication, database and server functions), Google Firebase (push notifications and Crashlytics), Google AdMob and UMP (ads and consent), and Apple and Google (sign-in and payments). We share with each service only what it needs, and each provider processes the information under its own privacy policy and security commitments, which provide the same level of protection as this policy. Information may be processed on servers outside your country, where these providers operate, with the safeguards required by applicable law."),
                ("5. Retention and deletion", "We keep your data until you delete it in the app or ask us by email to delete it. If you are signed in, Settings > Leave Sudoku permanently deletes this game's data; for Apple sign-in, we also revoke the Apple sign-in token. Data created before you sign in is linked only to the anonymous session on your device, so if you delete the app before signing in, it can no longer be recovered or linked to you. Transaction records that we are legally required to keep may be retained for the required period. Crash reports are kept according to Firebase Crashlytics' retention period."),
                ("6. Your rights and choices", "You may request access, correction, deletion or restriction of processing, or withdraw consent, by emailing dhalska2@gmail.com. You can change ad consent in Settings > Ad privacy choices (shown where required in your region) and tracking permission in your device settings. You can turn notifications on or off in Settings at any time."),
                ("7. Children, security, and changes", "The service is not directed to children, and we do not knowingly collect children's information without required parental consent. We use reasonable safeguards, including access controls and encrypted communications. We update the effective date and provide appropriate notice of material changes."),
            ],
            "contact": "Privacy contact",
        },
        "support": {
            "title": "Sudoku Pulse Help & Support",
            "intro": "Answers to common questions about Sudoku Pulse. If you need more help, email us.",
            "faq": [
                ("How do hints and explanations work?", "Select an empty cell and tap Hint. The correct digit is filled in, and the board explains why it is right, together with the solving technique. Techniques you learn are collected in the Technique book. If the selected cell needs other cells to be filled first, the app highlights a cell you can solve now and no hint is used. You get 3 free hints each day (the count resets at 00:00 UTC); after that, you can use hints from the Pulse Shop or watch an optional ad for one hint. Using a hint breaks your Pulse combo."),
                ("Do I need to sign in?", "No. The app creates an anonymous session automatically, so you can play every puzzle, use hints and make purchases without signing in. Signing in with Apple (iOS) or Google (Android) is optional and only needed to join the global ranking. When you sign in, your earlier hint balance, ad removal, purchase records and play records are linked to your account. If you delete the app before signing in, that data cannot be recovered."),
                ("How does the ranking work?", [
                    "You must be signed in. Games started while signed out or offline are not ranked.",
                    "Puzzles solved with up to 3 hints count. Puzzles with more than 3 hints are not ranked.",
                    "Your score is speed for the difficulty (each mistake adds 10 seconds) plus the Pulse combo bonus.",
                    "The daily puzzle is for fun and is not ranked.",
                    "Finishing a puzzle you have already finished is not ranked again.",
                    "Every result is verified on our server before it is ranked.",
                ]),
                ("How do I restore purchases?", "Open the Pulse Shop and tap Restore. Ad removal is restored through your App Store account, and your hint balance is reloaded from our server even if the store has nothing to restore. Hints that have already been used cannot be restored. For billing or refunds, contact the store where you made the purchase."),
                ("How do I turn notifications on or off?", "Notifications are optional and off by default. Turn them on or off in Settings > Notifications. When they are on, we send ranking-change and reminder notifications."),
                ("How do I delete my data?", "While signed in, go to Settings > Leave Sudoku. This permanently deletes this game's data. Apple users confirm their identity on the Apple sign-in screen, and the Apple sign-in token is revoked. You can also request deletion by email. See the {privacy} for details."),
                ("Contact us", "Email dhalska2@gmail.com with Sudoku Pulse in the subject line, and include the app version, your device and OS version, and the steps that led to the problem. Never send passwords, verification codes or payment details."),
            ],
            "contact": "Support contact",
        },
    },
    "ja": {
        "ui": {"privacy": "プライバシーポリシー", "support": "ヘルプとサポート", "terms": "利用規約", "languages": "言語を選択", "skip": "本文へ移動", "updated": "最終更新：2026年10月3日"},
        "privacy": {
            "title": "Sudoku Pulse プライバシーポリシー",
            "effective": "施行日：2026年10月3日",
            "intro": "Next Studio（넥스트 스튜디오）は、iOS・Android向けのSudoku Pulseを運営しています。本ポリシーは、アプリが取り扱う情報、その目的、利用者が選択できる事項を説明するもので、アプリおよび本ウェブサイトに適用されます。",
            "sections": [
                ("1. アカウントとログイン", "アプリを初めて起動すると、名前やメールアドレスを含まない匿名のSupabaseセッションが自動的に作成されます。これにより、ログインしなくても購入、ヒント、プレイ統計を利用できます。Apple（iOS）またはGoogle（Android）でのログインは任意で、世界ランキングに表示される場合にのみ必要です。ログインすると、匿名セッションのSudokuデータ（ヒント残数、広告削除、購入記録、プレイ記録）がそのアカウントに紐付けられ、統合されます。"),
                ("2. 収集する情報と利用目的", [
                    "ログイン用メールアドレスとログインプロバイダの識別子（ログインした場合）：アカウントの識別に使用します。ランキングには一部を伏せたメールアドレスのみが表示されます。",
                    "利用者が選択した国コード：ランキングに国旗を表示するために使用します。",
                    "プレイ記録：難易度、クリア時間、ミス数、マス数、使用したヒント数、パルスコンボボーナス、今日のパズルかどうか、パズルのハッシュ指紋、入力履歴（マス、数字、ゲーム内時計の秒数、入力の種類）、プレイセッションの開始・終了時刻。サーバーはこれらを結果の検証、スコア計算、不正防止、統計に使用します。",
                    "1日の無料ヒント使用回数：広告の視聴や購入なしで1日3回まで使える無料ヒントの使用回数を、サーバーのUTC日付ごとに数え、サーバー上のSudokuゲームプロフィールに保存します。",
                    "プレイ中のパズル（ログインした利用者のみ）：別の端末で続きを遊べるよう、プレイ中のパズルをサーバーに保存する場合があります。",
                    "購入情報：商品ID、取引ID、検証状況。ヒントパックと広告削除の付与、購入の復元に使用します。非消耗型の広告削除は、同じApple IDを使う別のアカウントに移ることがあります。支払情報はAppleまたはGoogleが処理し、当社は受け取らず保存もしません。",
                    "プッシュ通知の情報（通知をオンにした場合のみ）：FCMトークン、プラットフォーム、言語、通知設定。ランキング変動とリマインダーの通知に使用します。通知は初期状態でオフで、設定でオフにすると送信されなくなります。",
                    "広告：Google AdMobとGoogle UMP（同意管理）SDKは、広告配信、表示頻度の管理、不正防止、同意の記録のため、端末識別子、IPアドレス、診断情報を処理する場合があります。iOSの広告識別子（IDFA）は、App Tracking Transparency（ATT）の確認で許可した場合にのみ使用されます。リワード広告は、名前やメールアドレスではなく、アプリが生成したランダムな識別子を用いてサーバーで報酬を検証します。",
                    "クラッシュレポート：アプリが異常終了した場合、Firebase Crashlyticsが端末モデル、OSバージョン、アプリバージョン、クラッシュのスタックトレース、インストール識別子を収集し、不具合の修正に使用します。デバッグビルドでは収集しません。",
                ]),
                ("3. 端末にのみ保存される情報", "言語、触覚フィードバックの設定、チュートリアルの完了状況、テクニック図鑑で覚えたテクニック、最高コンボ、現在のパズルの自動保存、広告の表示間隔を調整するカウンターは端末にのみ保存され、サーバーには送信されません。アプリを削除すると一緒に削除されます。"),
                ("4. 委託先および国外での処理", "Supabase（認証、データベース、サーバー関数）、Google Firebase（プッシュ通知、Crashlytics）、Google AdMob・UMP（広告、同意管理）、AppleおよびGoogle（ログイン、決済）を利用します。各サービスには必要な情報のみを提供し、各事業者は本ポリシーと同等の保護を提供する自社のプライバシーポリシーとセキュリティ上の約束に従って情報を処理します。情報は、利用者の国以外を含む、各事業者が運営する国のサーバーで、適用法令が求める保護措置のもとで処理される場合があります。"),
                ("5. 保有期間と削除", "アプリ内でデータを削除するか、メールで削除を依頼されるまで保有します。ログインしている場合は、設定 > Sudokuを退会 からこのゲームのデータを完全に削除でき、Appleでログインしたアカウントは Appleのログイントークンも取り消します。ログイン前のデータは端末の匿名セッションにのみ紐付いているため、ログインする前にアプリを削除すると、復元したり利用者に再び紐付けたりすることはできません。法令で保管が義務付けられた取引記録は、その期間保管する場合があります。クラッシュレポートはFirebase Crashlyticsの保管期間に従います。"),
                ("6. 利用者の権利と選択", "利用者は、dhalska2@gmail.com 宛てのメールで、アクセス、訂正、削除、処理の制限、同意の撤回を請求できます。広告の同意は 設定 > 広告のプライバシー設定（地域により表示）で、トラッキングの許可は端末の設定で変更できます。通知は設定でいつでもオン・オフできます。"),
                ("7. 子ども、セキュリティ、変更", "本サービスは子どもを対象としておらず、必要な保護者の同意なしに子どもの情報を意図的に収集しません。アクセス制御や暗号化通信などの合理的な保護措置を講じます。変更時には施行日を更新し、重要な変更を通知します。"),
            ],
            "contact": "プライバシーに関するお問い合わせ",
        },
        "support": {
            "title": "Sudoku Pulse ヘルプとサポート",
            "intro": "Sudoku Pulseについてよくある質問です。解決しない場合はメールでお問い合わせください。",
            "faq": [
                ("ヒントと解説はどのように機能しますか？", "空いているマスを選んでヒントをタップすると、正しい数字が入り、盤面上で解法テクニックとともにその数字になる理由が説明されます。覚えたテクニックはテクニック図鑑に集まります。選んだマスを解くのに先に他のマスが必要な場合は、今解けるマスを強調表示し、ヒントは消費されません。毎日3回まで無料でヒントを使え（UTCの0時にリセット）、その後はPulse ショップのヒントを使うか、任意の広告を見てヒントを1つもらえます。ヒントを使うとパルスコンボが途切れます。"),
                ("ログインは必要ですか？", "いいえ。アプリが匿名セッションを自動的に作成するため、ログインしなくてもすべてのパズル、ヒント、購入を利用できます。Apple（iOS）またはGoogle（Android）でのログインは任意で、世界ランキングに参加する場合にのみ必要です。ログインすると、それまでのヒント残数、広告削除、購入記録、プレイ記録がアカウントに紐付けられます。ログイン前にアプリを削除すると、そのデータは復元できません。"),
                ("ランキングのルールは？", [
                    "ログインが必要です。ログアウト中またはオフラインで始めたゲームはランキングに反映されません。",
                    "ヒントを3回まで使ったパズルが対象です。3回を超えて使うと反映されません。",
                    "スコアは難易度別のスピード（ミス1回につき+10秒）とパルスコンボボーナスで計算されます。",
                    "今日のパズルは楽しむためのもので、ランキングには反映されません。",
                    "すでにクリアした同じパズルをもう一度解いても、ランキングには再反映されません。",
                    "結果はすべてサーバーで検証されてからランキングに反映されます。",
                ]),
                ("購入を復元するには？", "Pulse ショップで「購入を復元」をタップしてください。広告削除はApp Storeアカウントから復元され、ヒント残数はストアから復元するものがなくてもサーバーから読み込み直されます。使用済みのヒントは復元できません。請求や返金については、購入したストアにお問い合わせください。"),
                ("通知のオン・オフは？", "通知は任意で、初期状態ではオフです。設定 > 通知 でオン・オフできます。オンにすると、ランキング変動とリマインダーの通知が届きます。"),
                ("データを削除するには？", "ログインした状態で 設定 > Sudokuを退会 をタップすると、このゲームのデータが完全に削除されます。Appleでログインしている場合は、Appleのサインイン画面で本人確認を行い、Appleのログイントークンも取り消されます。メールで削除を依頼することもできます。詳しくは{privacy}をご覧ください。"),
                ("お問い合わせ", "件名に「Sudoku Pulse」と記入し、アプリのバージョン、端末とOSのバージョン、問題が起きた手順を dhalska2@gmail.com までお送りください。パスワード、認証コード、支払情報は送らないでください。"),
            ],
            "contact": "サポートへのお問い合わせ",
        },
    },
    "zh-hans": {
        "ui": {"privacy": "隐私政策", "support": "帮助与支持", "terms": "服务条款", "languages": "选择语言", "skip": "跳到正文", "updated": "最后更新：2026年10月3日"},
        "privacy": {
            "title": "Sudoku Pulse 隐私政策",
            "effective": "生效日期：2026年10月3日",
            "intro": "Next Studio（넥스트 스튜디오）运营适用于 iOS 和 Android 的 Sudoku Pulse。本政策说明应用处理哪些信息、处理目的以及您可以做出的选择，适用于本应用及本网站。",
            "sections": [
                ("1. 账号与登录", "首次打开应用时，会自动创建一个不含姓名或邮箱的匿名 Supabase 会话，因此无需登录即可使用购买、提示和游戏统计。使用 Apple（iOS）或 Google（Android）登录是可选的，仅在希望出现在全球排名中时需要。登录后，匿名会话中的 Sudoku 数据（提示余额、移除广告、购买记录、游戏记录）将关联并合并到该账号。"),
                ("2. 收集的信息及使用目的", [
                    "登录邮箱和登录提供商标识符（仅在登录时）：用于识别账号。排行榜仅显示部分隐藏的邮箱。",
                    "用户选择的国家代码：用于在排行榜上显示国旗。",
                    "游戏记录：难度、完成时间、错误次数、格子数、使用的提示次数、脉冲连击奖励、是否为每日谜题、谜题的哈希指纹、落子记录（格子、数字、游戏计时秒数、输入类型），以及每局游戏的开始和结束时间。服务器使用这些信息验证成绩、计算得分、防止作弊并进行统计。",
                    "每日免费提示使用次数：每天最多可使用 3 次无需观看广告或购买的免费提示，使用次数按服务器 UTC 日期计算，并与您的 Sudoku 游戏档案一起保存在我们的服务器上。",
                    "进行中的谜题（仅限已登录玩家）：可能会将正在进行的谜题保存到服务器，以便在其他设备上继续。",
                    "购买信息：商品ID、交易ID和验证状态，用于发放提示包和移除广告以及恢复购买。移除广告为非消耗型商品，可转移到使用同一 Apple ID 的其他账号。支付信息由 Apple 或 Google 处理，我们不会接收或保存。",
                    "推送通知信息（仅在开启通知时）：FCM令牌、平台、语言和通知设置，用于发送排名变动和提醒通知。通知默认关闭，在设置中关闭后将不再发送。",
                    "广告：Google AdMob 和 Google UMP（同意管理）SDK 可能为投放广告、控制展示频次、防止欺诈和记录同意而处理设备标识符、IP地址和诊断信息。iOS 广告标识符（IDFA）仅在您通过“App 跟踪透明度”（ATT）提示允许后使用。激励广告使用应用生成的随机标识符（而非姓名或邮箱）在服务器上验证奖励。",
                    "崩溃报告：应用崩溃时，Firebase Crashlytics 会收集设备型号、操作系统版本、应用版本、崩溃堆栈跟踪和安装标识符，用于修复问题。调试版本不收集。",
                ]),
                ("3. 仅保存在设备上的信息", "语言、振动设置、教程完成状态、技巧图鉴中学会的技巧、最高连击、当前谜题的自动存档，以及用于控制广告间隔的计数器仅保存在设备上，不会发送到服务器。删除应用时这些信息会一并删除。"),
                ("4. 服务提供商及跨境处理", "我们使用 Supabase（身份验证、数据库和服务器函数）、Google Firebase（推送通知和 Crashlytics）、Google AdMob 和 UMP（广告和同意管理），以及 Apple 和 Google（登录和支付）。我们仅向各服务提供其所需的信息，各服务商依据其自身的隐私政策和安全承诺处理信息，提供与本政策同等水平的保护。信息可能在您所在国家或地区以外、这些服务商运营所在地的服务器上，按照适用法律要求的保障措施进行处理。"),
                ("5. 保存期限与删除", "我们会保存数据，直到您在应用中删除或通过电子邮件请求删除。已登录时，可在“设置 > 退出Sudoku”中永久删除本游戏的数据；使用 Apple 登录的账号还会撤销 Apple 登录令牌。登录前的数据仅与设备上的匿名会话关联，如果在登录前删除应用，这些数据将无法恢复或再次与您关联。法律要求保存的交易记录可能在规定期限内保留。崩溃报告按照 Firebase Crashlytics 的保存期限处理。"),
                ("6. 用户权利与选择", "您可以发送电子邮件至 dhalska2@gmail.com，请求访问、更正、删除、限制处理或撤回同意。广告同意可在“设置 > 广告隐私设置”（视地区显示）中更改，跟踪权限可在设备设置中更改。通知可随时在设置中开启或关闭。"),
                ("7. 儿童、安全与变更", "本服务不面向儿童，未经必要的监护人同意，我们不会故意收集儿童信息。我们采取合理的保护措施，包括访问控制和加密通信。政策变更时，我们将更新生效日期并对重大变更发出适当通知。"),
            ],
            "contact": "隐私咨询",
        },
        "support": {
            "title": "Sudoku Pulse 帮助与支持",
            "intro": "以下是关于 Sudoku Pulse 的常见问题。如需更多帮助，请发送电子邮件联系我们。",
            "faq": [
                ("提示和讲解如何使用？", "选择一个空格并点击“提示”，正确的数字会被填入，并在棋盘上结合解题技巧说明为什么是这个数字。学会的技巧会收录在技巧图鉴中。如果所选格子需要先填其他格子，应用会高亮显示一个现在就能解出的格子，此时不会消耗提示。每天可免费使用 3 次提示（按 UTC 零点重置），用完后可以使用 Pulse 商店中的提示，或观看可选广告获得 1 次提示。使用提示会中断脉冲连击。"),
                ("必须登录吗？", "不必。应用会自动创建匿名会话，无需登录即可玩所有谜题、使用提示和进行购买。使用 Apple（iOS）或 Google（Android）登录是可选的，仅在参加全球排名时需要。登录后，此前的提示余额、移除广告、购买记录和游戏记录会关联到账号。如果在登录前删除应用，这些数据将无法恢复。"),
                ("排名规则是什么？", [
                    "需要登录。在未登录或离线状态下开始的游戏不计入排名。",
                    "最多使用 3 次提示的谜题计入排名，超过 3 次则不计入。",
                    "得分 = 按难度计算的速度（每次失误 +10 秒）+ 脉冲连击奖励。",
                    "每日谜题仅供娱乐，不计入排名。",
                    "再次完成已完成过的同一谜题，不会再次计入排名。",
                    "所有成绩都会先在服务器上验证，再计入排名。",
                ]),
                ("如何恢复购买？", "在 Pulse 商店中点击“恢复购买”。移除广告会通过 App Store 账号恢复；即使商店中没有可恢复的项目，提示余额也会从服务器重新载入。已使用的提示无法恢复。账单或退款问题请联系您购买时使用的商店。"),
                ("如何开启或关闭通知？", "通知是可选的，默认关闭。可在“设置 > 通知”中开启或关闭。开启后，我们会发送排名变动和提醒通知。"),
                ("如何删除我的数据？", "登录状态下，在“设置 > 退出Sudoku”中可永久删除本游戏的数据。使用 Apple 登录的用户需在 Apple 登录界面验证身份，Apple 登录令牌也会被撤销。您也可以通过电子邮件请求删除。详情请参阅{privacy}。"),
                ("联系我们", "请在邮件主题中注明“Sudoku Pulse”，并将应用版本、设备与系统版本以及问题发生的步骤发送至 dhalska2@gmail.com。请勿发送密码、验证码或支付信息。"),
            ],
            "contact": "支持咨询",
        },
    },
    "es": {
        "ui": {"privacy": "Política de privacidad", "support": "Ayuda y soporte", "terms": "Términos del servicio", "languages": "Elegir idioma", "skip": "Ir al contenido", "updated": "Última actualización: 3 de octubre de 2026"},
        "privacy": {
            "title": "Política de privacidad de Sudoku Pulse",
            "effective": "En vigor desde el 3 de octubre de 2026",
            "intro": "Next Studio (넥스트 스튜디오) gestiona Sudoku Pulse para iOS y Android. Esta política explica qué información trata la app, con qué fines y qué opciones tienes. Se aplica a la app y a este sitio web.",
            "sections": [
                ("1. Cuentas e inicio de sesión", "Al abrir la app por primera vez, se crea automáticamente una sesión anónima de Supabase sin nombre ni correo electrónico. Gracias a ella, las compras, las pistas y las estadísticas de juego funcionan sin iniciar sesión. Iniciar sesión con Apple (iOS) o Google (Android) es opcional y solo es necesario para aparecer en la clasificación mundial. Al iniciar sesión, los datos de Sudoku de tu sesión anónima (saldo de pistas, eliminación de anuncios, registros de compra y registros de juego) se vinculan y se combinan con esa cuenta."),
                ("2. Información que recopilamos y finalidad", [
                    "Correo electrónico de inicio de sesión e identificador del proveedor (solo si inicias sesión): para identificar tu cuenta. La clasificación solo muestra el correo parcialmente oculto.",
                    "Código de país que eliges: para mostrar una bandera en la clasificación.",
                    "Registros de juego: dificultad, tiempo de resolución, errores, número de casillas, pistas usadas, bonus de combo Pulse, si era el puzle diario, una huella hash del puzle y el registro de jugadas (casilla, número, segundos del reloj de juego y tipo de entrada), además de la hora de inicio y fin de cada sesión de juego. El servidor los usa para verificar resultados, calcular puntuaciones, evitar trampas y elaborar estadísticas.",
                    "Recuento diario de pistas gratuitas: el número de pistas gratuitas que usas cada día (hasta 3 antes de necesitar un anuncio o una pista comprada) se cuenta por fecha UTC del servidor y se guarda con tu perfil de juego de Sudoku en nuestro servidor.",
                    "Puzle en curso (solo jugadores con sesión iniciada): el puzle que estás jugando puede guardarse en el servidor para continuarlo en otro dispositivo.",
                    "Información de compras: ID del producto, ID de la transacción y estado de verificación, para entregar paquetes de pistas y la eliminación de anuncios y para restaurar compras. La eliminación de anuncios es una compra no consumible y puede trasladarse a otra cuenta que use el mismo Apple ID. Los datos de pago los gestiona Apple o Google; no los recibimos ni los guardamos.",
                    "Información de notificaciones push (solo si las activas): token FCM, plataforma, idioma y ajuste de notificaciones, para enviar avisos de cambios en la clasificación y recordatorios. Las notificaciones están desactivadas por defecto y dejan de enviarse si las desactivas en Ajustes.",
                    "Publicidad: Google AdMob y el SDK de consentimiento Google UMP pueden tratar identificadores del dispositivo, la dirección IP y datos de diagnóstico para mostrar anuncios, controlar su frecuencia, prevenir el fraude y registrar el consentimiento. En iOS, el identificador publicitario (IDFA) solo se usa si lo permites en la solicitud de App Tracking Transparency (ATT). Las recompensas de los anuncios con recompensa se verifican en nuestro servidor mediante un identificador aleatorio generado por la app, no con tu nombre ni tu correo.",
                    "Informes de fallos: si la app se cierra inesperadamente, Firebase Crashlytics recopila el modelo del dispositivo, la versión del sistema operativo, la versión de la app, la traza de pila del fallo y un identificador de instalación para que podamos corregir el problema. No se recopilan en las versiones de depuración.",
                ]),
                ("3. Información guardada solo en tu dispositivo", "El idioma, el ajuste de respuesta háptica, si completaste el tutorial, las técnicas aprendidas en el libro de técnicas, el mejor combo, el guardado automático del puzle actual y un contador para espaciar los anuncios se guardan solo en tu dispositivo y no se envían a nuestro servidor. Se eliminan al borrar la app."),
                ("4. Proveedores y tratamiento internacional", "Usamos Supabase (autenticación, base de datos y funciones de servidor), Google Firebase (notificaciones push y Crashlytics), Google AdMob y UMP (publicidad y consentimiento), y Apple y Google (inicio de sesión y pagos). Solo compartimos con cada servicio lo que necesita, y cada proveedor trata la información conforme a sus propias políticas de privacidad y compromisos de seguridad, que ofrecen el mismo nivel de protección que esta política. La información puede tratarse en servidores situados fuera de tu país, donde operan estos proveedores, con las garantías que exija la ley aplicable."),
                ("5. Conservación y eliminación", "Conservamos tus datos hasta que los elimines en la app o nos pidas por correo que los eliminemos. Si has iniciado sesión, Ajustes > Salir de Sudoku elimina de forma permanente los datos de este juego; en las cuentas de Apple también revocamos el token de inicio de sesión de Apple. Los datos anteriores al inicio de sesión solo están vinculados a la sesión anónima de tu dispositivo: si eliminas la app antes de iniciar sesión, ya no podrán recuperarse ni vincularse contigo. Los registros de transacciones que la ley nos obligue a conservar podrán mantenerse durante el plazo exigido. Los informes de fallos se conservan según el plazo de retención de Firebase Crashlytics."),
                ("6. Tus derechos y opciones", "Puedes solicitar el acceso, la rectificación, la eliminación o la limitación del tratamiento de tus datos, o retirar tu consentimiento, escribiendo a dhalska2@gmail.com. Puedes cambiar el consentimiento publicitario en Ajustes > Privacidad de los anuncios (se muestra donde tu región lo exige) y el permiso de seguimiento en los ajustes del dispositivo. Puedes activar o desactivar las notificaciones en Ajustes en cualquier momento."),
                ("7. Menores, seguridad y cambios", "El servicio no está dirigido a menores y no recopilamos intencionadamente sus datos sin el consentimiento parental necesario. Aplicamos medidas razonables, como controles de acceso y comunicaciones cifradas. Actualizaremos la fecha y avisaremos de los cambios importantes."),
            ],
            "contact": "Contacto de privacidad",
        },
        "support": {
            "title": "Ayuda y soporte de Sudoku Pulse",
            "intro": "Respuestas a preguntas frecuentes sobre Sudoku Pulse. Si necesitas más ayuda, escríbenos por correo.",
            "faq": [
                ("¿Cómo funcionan las pistas y las explicaciones?", "Selecciona una casilla vacía y toca Pista. Se completa el número correcto y en el tablero se explica por qué es ese número, junto con la técnica de resolución. Las técnicas que aprendes se reúnen en el Libro de técnicas. Si la casilla elegida necesita que antes se resuelvan otras, la app resalta una casilla que puedes resolver ahora y no se gasta ninguna pista. Cada día dispones de 3 pistas gratuitas (el recuento se reinicia a las 00:00 UTC); después puedes usar pistas de la Tienda Pulse o ver un anuncio opcional para obtener una. Usar una pista corta el combo Pulse."),
                ("¿Tengo que iniciar sesión?", "No. La app crea automáticamente una sesión anónima, así que puedes jugar todos los puzles, usar pistas y hacer compras sin iniciar sesión. Iniciar sesión con Apple (iOS) o Google (Android) es opcional y solo es necesario para participar en la clasificación mundial. Al iniciar sesión, tu saldo de pistas, la eliminación de anuncios y tus registros de compra y de juego anteriores se vinculan a tu cuenta. Si eliminas la app antes de iniciar sesión, esos datos no se pueden recuperar."),
                ("¿Cómo funciona la clasificación?", [
                    "Debes haber iniciado sesión. Las partidas empezadas sin sesión o sin conexión no cuentan.",
                    "Cuentan los puzles resueltos con hasta 3 pistas; con más de 3 pistas no cuentan.",
                    "La puntuación es la velocidad según la dificultad (cada error suma 10 segundos) más el bonus de combo Pulse.",
                    "El puzle diario es para divertirse y no cuenta para la clasificación.",
                    "Si vuelves a completar un puzle que ya terminaste, no vuelve a contar.",
                    "Todos los resultados se verifican en nuestro servidor antes de entrar en la clasificación.",
                ]),
                ("¿Cómo restauro mis compras?", "Abre la Tienda Pulse y toca Restaurar. La eliminación de anuncios se restaura desde tu cuenta de App Store, y tu saldo de pistas se vuelve a cargar desde nuestro servidor aunque la tienda no tenga nada que restaurar. Las pistas ya usadas no se pueden restaurar. Para cobros o reembolsos, contacta con la tienda donde hiciste la compra."),
                ("¿Cómo activo o desactivo las notificaciones?", "Las notificaciones son opcionales y están desactivadas por defecto. Actívalas o desactívalas en Ajustes > Notificaciones. Si están activadas, te avisamos de cambios en la clasificación y te enviamos recordatorios."),
                ("¿Cómo elimino mis datos?", "Con la sesión iniciada, ve a Ajustes > Salir de Sudoku. Se eliminan de forma permanente los datos de este juego; los usuarios de Apple confirman su identidad en la pantalla de inicio de sesión de Apple y se revoca el token de Apple. También puedes solicitar la eliminación por correo. Consulta la {privacy} para más información."),
                ("Contacto", "Escribe a dhalska2@gmail.com con «Sudoku Pulse» en el asunto e incluye la versión de la app, tu dispositivo y la versión del sistema, y los pasos que llevaron al problema. Nunca envíes contraseñas, códigos de verificación ni datos de pago."),
            ],
            "contact": "Contacto de soporte",
        },
    },
    "fr": {
        "ui": {"privacy": "Politique de confidentialité", "support": "Aide et assistance", "terms": "Conditions d'utilisation", "languages": "Choisir la langue", "skip": "Aller au contenu", "updated": "Dernière mise à jour : 3 octobre 2026"},
        "privacy": {
            "title": "Politique de confidentialité de Sudoku Pulse",
            "effective": "Date d'entrée en vigueur : 3 octobre 2026",
            "intro": "Next Studio (넥스트 스튜디오) exploite Sudoku Pulse sur iOS et Android. Cette politique explique quelles informations l'application traite, dans quel but, et quels choix s'offrent à vous. Elle s'applique à l'application et à ce site web.",
            "sections": [
                ("1. Comptes et connexion", "À la première ouverture, l'application crée automatiquement une session Supabase anonyme, sans nom ni adresse e-mail. Elle permet d'utiliser les achats, les indices et les statistiques de jeu sans se connecter. La connexion avec Apple (iOS) ou Google (Android) est facultative et n'est nécessaire que pour figurer dans le classement mondial. Lorsque vous vous connectez, les données Sudoku de votre session anonyme (solde d'indices, suppression des publicités, historique d'achats et historique de parties) sont associées et fusionnées avec ce compte."),
                ("2. Données collectées et finalités", [
                    "Adresse e-mail de connexion et identifiant du fournisseur (uniquement si vous vous connectez) : identification de votre compte. Le classement n'affiche qu'une version masquée de l'adresse e-mail.",
                    "Code pays que vous choisissez : affichage d'un drapeau dans le classement.",
                    "Historique de parties : difficulté, temps de résolution, erreurs, nombre de cases, indices utilisés, bonus de combo Pulse, s'il s'agissait du défi quotidien, une empreinte (hash) de la grille et le journal des coups (case, chiffre, secondes de l'horloge de jeu et type de saisie), ainsi que les heures de début et de fin de chaque session de jeu. Le serveur les utilise pour vérifier les résultats, calculer les scores, empêcher la triche et établir des statistiques.",
                    "Compteur quotidien d'indices gratuits : le nombre d'indices gratuits utilisés chaque jour (jusqu'à 3 avant qu'une publicité ou un indice acheté soit nécessaire) est compté par date UTC du serveur et enregistré avec votre profil de jeu Sudoku sur notre serveur.",
                    "Grille en cours (joueurs connectés uniquement) : la grille en cours peut être enregistrée sur le serveur pour être reprise sur un autre appareil.",
                    "Informations d'achat : identifiant du produit, identifiant de transaction et état de vérification, pour attribuer les packs d'indices et la suppression des publicités et restaurer les achats. La suppression des publicités est un achat non consommable et peut être transférée vers un autre compte utilisant le même identifiant Apple. Les données de paiement sont traitées par Apple ou Google ; nous ne les recevons ni ne les conservons.",
                    "Informations de notification push (uniquement si vous les activez) : jeton FCM, plateforme, langue et réglage des notifications, pour envoyer des notifications de changement de classement et des rappels. Les notifications sont désactivées par défaut et ne sont plus envoyées si vous les désactivez dans les Réglages.",
                    "Publicité : Google AdMob et le SDK de consentement Google UMP peuvent traiter des identifiants de l'appareil, l'adresse IP et des données de diagnostic pour afficher des publicités, limiter leur fréquence, prévenir la fraude et enregistrer le consentement. Sur iOS, l'identifiant publicitaire (IDFA) n'est utilisé que si vous l'autorisez via la demande App Tracking Transparency (ATT). Les récompenses des publicités avec récompense sont vérifiées sur notre serveur à l'aide d'un identifiant aléatoire généré par l'application, et non de votre nom ou de votre adresse e-mail.",
                    "Rapports de plantage : en cas de plantage, Firebase Crashlytics collecte le modèle de l'appareil, la version du système, la version de l'application, la trace de pile du plantage et un identifiant d'installation afin que nous puissions corriger le problème. Ils ne sont pas collectés dans les versions de débogage.",
                ]),
                ("3. Informations conservées uniquement sur l'appareil", "La langue, le réglage du retour haptique, l'achèvement du tutoriel, les techniques apprises dans le carnet de techniques, le meilleur combo, la sauvegarde automatique de la grille en cours et un compteur servant à espacer les publicités sont conservés uniquement sur votre appareil et ne sont pas envoyés à notre serveur. Ils sont supprimés avec l'application."),
                ("4. Prestataires et traitement international", "Nous utilisons Supabase (authentification, base de données et fonctions serveur), Google Firebase (notifications push et Crashlytics), Google AdMob et UMP (publicité et consentement), ainsi qu'Apple et Google (connexion et paiements). Nous ne transmettons à chaque service que ce dont il a besoin, et chaque prestataire traite les informations selon ses propres politiques de confidentialité et engagements de sécurité, qui offrent le même niveau de protection que la présente politique. Les informations peuvent être traitées sur des serveurs situés hors de votre pays, là où ces prestataires opèrent, avec les garanties exigées par la loi applicable."),
                ("5. Conservation et suppression", "Nous conservons vos données jusqu'à ce que vous les supprimiez dans l'application ou nous demandiez leur suppression par e-mail. Si vous êtes connecté, Réglages > Quitter Sudoku supprime définitivement les données de ce jeu ; pour les comptes Apple, nous révoquons également le jeton de connexion Apple. Les données créées avant la connexion ne sont liées qu'à la session anonyme de votre appareil : si vous supprimez l'application avant de vous connecter, elles ne pourront plus être récupérées ni vous être rattachées. Les relevés de transactions que la loi nous oblige à conserver peuvent l'être pendant la durée requise. Les rapports de plantage sont conservés selon la durée de conservation de Firebase Crashlytics."),
                ("6. Vos droits et choix", "Vous pouvez demander l'accès, la rectification, la suppression ou la limitation du traitement de vos données, ou retirer votre consentement, en écrivant à dhalska2@gmail.com. Vous pouvez modifier le consentement publicitaire dans Réglages > Confidentialité des annonces (affiché lorsque votre région l'exige) et l'autorisation de suivi dans les réglages de l'appareil. Vous pouvez activer ou désactiver les notifications à tout moment dans les Réglages."),
                ("7. Enfants, sécurité et modifications", "Le service ne s'adresse pas aux enfants et nous ne recueillons pas sciemment leurs données sans le consentement parental requis. Nous appliquons des mesures raisonnables, notamment le contrôle d'accès et le chiffrement des communications. La date sera mise à jour et les changements importants seront signalés."),
            ],
            "contact": "Contact confidentialité",
        },
        "support": {
            "title": "Aide et assistance Sudoku Pulse",
            "intro": "Réponses aux questions fréquentes sur Sudoku Pulse. Pour toute autre aide, écrivez-nous par e-mail.",
            "faq": [
                ("Comment fonctionnent les indices et les explications ?", "Sélectionnez une case vide et touchez Indice. Le bon chiffre est placé et la grille explique pourquoi, avec la technique de résolution utilisée. Les techniques apprises sont rassemblées dans le Carnet de techniques. Si la case choisie nécessite d'abord d'autres cases, l'application met en évidence une case que vous pouvez résoudre maintenant, sans utiliser d'indice. Vous disposez chaque jour de 3 indices gratuits (le compteur repart à zéro à 00:00 UTC) ; ensuite, vous pouvez utiliser des indices de la Boutique Pulse ou regarder une publicité facultative pour en obtenir un. Utiliser un indice interrompt le combo Pulse."),
                ("Dois-je me connecter ?", "Non. L'application crée automatiquement une session anonyme : vous pouvez jouer à toutes les grilles, utiliser des indices et faire des achats sans vous connecter. La connexion avec Apple (iOS) ou Google (Android) est facultative et n'est nécessaire que pour participer au classement mondial. Lorsque vous vous connectez, votre solde d'indices, la suppression des publicités et vos historiques d'achats et de parties sont associés à votre compte. Si vous supprimez l'application avant de vous connecter, ces données ne peuvent pas être récupérées."),
                ("Comment fonctionne le classement ?", [
                    "Vous devez être connecté. Les parties commencées sans connexion ou hors ligne ne sont pas classées.",
                    "Les grilles résolues avec 3 indices maximum comptent ; au-delà de 3 indices, elles ne comptent pas.",
                    "Le score correspond à la vitesse selon la difficulté (chaque erreur ajoute 10 secondes) plus le bonus de combo Pulse.",
                    "Le défi quotidien est pour le plaisir et ne compte pas pour le classement.",
                    "Terminer à nouveau une grille déjà terminée ne compte pas une seconde fois.",
                    "Tous les résultats sont vérifiés sur notre serveur avant d'être classés.",
                ]),
                ("Comment restaurer mes achats ?", "Ouvrez la Boutique Pulse et touchez Restaurer. La suppression des publicités est restaurée via votre compte App Store, et votre solde d'indices est rechargé depuis notre serveur, même si la boutique n'a rien à restaurer. Les indices déjà utilisés ne peuvent pas être restaurés. Pour la facturation ou les remboursements, contactez la boutique où vous avez effectué l'achat."),
                ("Comment activer ou désactiver les notifications ?", "Les notifications sont facultatives et désactivées par défaut. Activez-les ou désactivez-les dans Réglages > Notifications. Une fois activées, nous vous envoyons des notifications de changement de classement et des rappels."),
                ("Comment supprimer mes données ?", "Une fois connecté, allez dans Réglages > Quitter Sudoku. Les données de ce jeu sont supprimées définitivement ; les utilisateurs Apple confirment leur identité sur l'écran de connexion Apple et le jeton Apple est révoqué. Vous pouvez aussi demander la suppression par e-mail. Consultez la {privacy} pour en savoir plus."),
                ("Nous contacter", "Écrivez à dhalska2@gmail.com avec « Sudoku Pulse » en objet, en indiquant la version de l'application, votre appareil et sa version du système, ainsi que les étapes ayant mené au problème. N'envoyez jamais de mot de passe, de code de vérification ni de données de paiement."),
            ],
            "contact": "Contact assistance",
        },
    },
    "de": {
        "ui": {"privacy": "Datenschutzerklärung", "support": "Hilfe & Support", "terms": "Nutzungsbedingungen", "languages": "Sprache wählen", "skip": "Zum Inhalt", "updated": "Zuletzt aktualisiert am 3. Oktober 2026"},
        "privacy": {
            "title": "Datenschutzerklärung für Sudoku Pulse",
            "effective": "Gültig ab 3. Oktober 2026",
            "intro": "Next Studio (넥스트 스튜디오) betreibt Sudoku Pulse für iOS und Android. Diese Erklärung beschreibt, welche Informationen die App verarbeitet, zu welchem Zweck und welche Wahlmöglichkeiten Sie haben. Sie gilt für die App und diese Website.",
            "sections": [
                ("1. Konten und Anmeldung", "Beim ersten Öffnen erstellt die App automatisch eine anonyme Supabase-Sitzung ohne Namen oder E-Mail-Adresse. Dadurch funktionieren Käufe, Hinweise und Spielstatistiken ohne Anmeldung. Die Anmeldung mit Apple (iOS) oder Google (Android) ist optional und nur erforderlich, um in der weltweiten Rangliste zu erscheinen. Wenn Sie sich anmelden, werden die Sudoku-Daten Ihrer anonymen Sitzung (Hinweisguthaben, Werbeentfernung, Kaufdaten und Spielaufzeichnungen) mit diesem Konto verknüpft und zusammengeführt."),
                ("2. Erhobene Daten und Zwecke", [
                    "E-Mail-Adresse und Anbieterkennung der Anmeldung (nur bei Anmeldung): zur Identifizierung Ihres Kontos. In der Rangliste wird nur eine maskierte E-Mail-Adresse angezeigt.",
                    "Von Ihnen gewählter Ländercode: Anzeige einer Flagge in der Rangliste.",
                    "Spielaufzeichnungen: Schwierigkeit, Lösungszeit, Fehler, Anzahl der Felder, verwendete Hinweise, Pulse-Combo-Bonus, ob es das Tagesrätsel war, ein Hash-Fingerabdruck des Rätsels und das Zugprotokoll (Feld, Ziffer, Sekunden der Spieluhr und Eingabeart) sowie Start- und Endzeit jeder Spielsitzung. Der Server nutzt diese Daten, um Ergebnisse zu prüfen, Punkte zu berechnen, Betrug zu verhindern und Statistiken zu führen.",
                    "Zähler der täglichen Gratis-Hinweise: Die Anzahl der Gratis-Hinweise, die Sie pro Tag verwenden (bis zu 3, bevor Werbung oder ein gekaufter Hinweis nötig ist), wird pro UTC-Datum des Servers gezählt und mit Ihrem Sudoku-Spielprofil auf unserem Server gespeichert.",
                    "Laufendes Rätsel (nur angemeldete Spieler): Das aktuelle Rätsel kann auf dem Server gespeichert werden, damit Sie es auf einem anderen Gerät fortsetzen können.",
                    "Kaufinformationen: Produkt-ID, Transaktions-ID und Prüfstatus, um Hinweispakete und die Werbeentfernung bereitzustellen und Käufe wiederherzustellen. Die Werbeentfernung ist ein nicht verbrauchbarer Kauf und kann auf ein anderes Konto mit derselben Apple-ID übergehen. Zahlungsdaten werden von Apple oder Google verarbeitet; wir erhalten oder speichern sie nicht.",
                    "Daten für Push-Mitteilungen (nur wenn Sie sie aktivieren): FCM-Token, Plattform, Sprache und Mitteilungseinstellung, um Mitteilungen über Ranglistenänderungen und Erinnerungen zu senden. Mitteilungen sind standardmäßig ausgeschaltet; wenn Sie sie in den Einstellungen ausschalten, werden keine mehr gesendet.",
                    "Werbung: Google AdMob und das Einwilligungs-SDK Google UMP können Gerätekennungen, die IP-Adresse und Diagnosedaten verarbeiten, um Werbung anzuzeigen, die Häufigkeit zu steuern, Betrug zu verhindern und Einwilligungen zu erfassen. Unter iOS wird die Werbe-ID (IDFA) nur verwendet, wenn Sie dies in der Abfrage zur App-Tracking-Transparenz (ATT) erlauben. Belohnungen aus Werbung mit Belohnung werden auf unserem Server mit einer von der App erzeugten Zufallskennung geprüft, nicht mit Ihrem Namen oder Ihrer E-Mail-Adresse.",
                    "Absturzberichte: Bei einem Absturz erfasst Firebase Crashlytics Gerätemodell, Betriebssystemversion, App-Version, Stacktrace des Absturzes und eine Installationskennung, damit wir den Fehler beheben können. In Debug-Builds werden keine Berichte erfasst.",
                ]),
                ("3. Nur auf dem Gerät gespeicherte Daten", "Sprache, Einstellung für haptisches Feedback, Abschluss des Tutorials, im Technikbuch gelernte Techniken, beste Combo, die automatische Speicherung des aktuellen Rätsels und ein Zähler für den Abstand zwischen Werbeanzeigen werden nur auf Ihrem Gerät gespeichert und nicht an unseren Server gesendet. Sie werden mit der App gelöscht."),
                ("4. Dienstleister und internationale Verarbeitung", "Wir nutzen Supabase (Anmeldung, Datenbank und Serverfunktionen), Google Firebase (Push-Mitteilungen und Crashlytics), Google AdMob und UMP (Werbung und Einwilligung) sowie Apple und Google (Anmeldung und Zahlungen). Wir geben jedem Dienst nur die Daten, die er benötigt; jeder Anbieter verarbeitet sie nach seinen eigenen Datenschutzrichtlinien und Sicherheitszusagen, die dasselbe Schutzniveau wie diese Erklärung bieten. Daten können auf Servern außerhalb Ihres Landes verarbeitet werden, in denen diese Anbieter tätig sind, mit den nach geltendem Recht erforderlichen Garantien."),
                ("5. Speicherdauer und Löschung", "Wir speichern Ihre Daten, bis Sie sie in der App löschen oder per E-Mail die Löschung verlangen. Wenn Sie angemeldet sind, löscht Einstellungen > Sudoku verlassen die Daten dieses Spiels dauerhaft; bei Apple-Konten widerrufen wir zusätzlich das Apple-Anmeldetoken. Daten aus der Zeit vor der Anmeldung sind nur mit der anonymen Sitzung auf Ihrem Gerät verknüpft: Wenn Sie die App vor der Anmeldung löschen, können sie nicht wiederhergestellt oder Ihnen erneut zugeordnet werden. Transaktionsdaten, die wir gesetzlich aufbewahren müssen, können für die vorgeschriebene Dauer gespeichert bleiben. Absturzberichte werden gemäß der Aufbewahrungsfrist von Firebase Crashlytics gespeichert."),
                ("6. Ihre Rechte und Wahlmöglichkeiten", "Sie können per E-Mail an dhalska2@gmail.com Auskunft, Berichtigung, Löschung oder Einschränkung der Verarbeitung verlangen oder Ihre Einwilligung widerrufen. Die Werbeeinwilligung können Sie unter Einstellungen > Datenschutz für Werbung (angezeigt, wo Ihre Region es erfordert) und die Tracking-Erlaubnis in den Geräteeinstellungen ändern. Mitteilungen können Sie jederzeit in den Einstellungen ein- oder ausschalten."),
                ("7. Kinder, Sicherheit und Änderungen", "Der Dienst richtet sich nicht an Kinder. Ohne erforderliche Zustimmung der Eltern erheben wir nicht wissentlich Daten von Kindern. Wir treffen angemessene Schutzmaßnahmen wie Zugriffskontrollen und verschlüsselte Verbindungen. Bei Änderungen aktualisieren wir das Datum und informieren über wesentliche Änderungen."),
            ],
            "contact": "Datenschutzkontakt",
        },
        "support": {
            "title": "Sudoku Pulse Hilfe & Support",
            "intro": "Antworten auf häufige Fragen zu Sudoku Pulse. Wenn Sie weitere Hilfe brauchen, schreiben Sie uns eine E-Mail.",
            "faq": [
                ("Wie funktionieren Hinweise und Erklärungen?", "Wählen Sie ein leeres Feld und tippen Sie auf Hinweis. Die richtige Ziffer wird eingetragen, und auf dem Spielfeld wird mit der passenden Lösungstechnik erklärt, warum sie stimmt. Gelernte Techniken werden im Technikbuch gesammelt. Wenn für das gewählte Feld zuerst andere Felder nötig sind, hebt die App ein Feld hervor, das Sie jetzt lösen können, und es wird kein Hinweis verbraucht. Jeden Tag stehen 3 Gratis-Hinweise bereit (der Zähler wird um 00:00 UTC zurückgesetzt); danach können Sie Hinweise aus dem Pulse-Shop nutzen oder sich optional eine Werbung für einen Hinweis ansehen. Ein Hinweis unterbricht die Pulse-Combo."),
                ("Muss ich mich anmelden?", "Nein. Die App erstellt automatisch eine anonyme Sitzung, sodass Sie alle Rätsel spielen, Hinweise nutzen und Käufe tätigen können, ohne sich anzumelden. Die Anmeldung mit Apple (iOS) oder Google (Android) ist optional und nur für die Teilnahme an der weltweiten Rangliste nötig. Bei der Anmeldung werden Ihr Hinweisguthaben, die Werbeentfernung sowie bisherige Kauf- und Spieldaten mit Ihrem Konto verknüpft. Wenn Sie die App vor der Anmeldung löschen, können diese Daten nicht wiederhergestellt werden."),
                ("Wie funktioniert die Rangliste?", [
                    "Sie müssen angemeldet sein. Spiele, die abgemeldet oder offline begonnen wurden, werden nicht gewertet.",
                    "Rätsel mit bis zu 3 Hinweisen zählen; mit mehr als 3 Hinweisen nicht.",
                    "Die Punkte ergeben sich aus dem Tempo je Schwierigkeit (jeder Fehler +10 Sekunden) plus dem Pulse-Combo-Bonus.",
                    "Das Tagesrätsel ist zum Spaß da und zählt nicht für die Rangliste.",
                    "Wenn Sie ein bereits gelöstes Rätsel erneut lösen, wird es nicht noch einmal gewertet.",
                    "Alle Ergebnisse werden vor der Wertung auf unserem Server geprüft.",
                ]),
                ("Wie stelle ich Käufe wieder her?", "Öffnen Sie den Pulse-Shop und tippen Sie auf Wiederherstellen. Die Werbeentfernung wird über Ihr App-Store-Konto wiederhergestellt, und Ihr Hinweisguthaben wird von unserem Server neu geladen, auch wenn es im Store nichts wiederherzustellen gibt. Bereits verbrauchte Hinweise können nicht wiederhergestellt werden. Bei Fragen zu Abrechnung oder Erstattung wenden Sie sich an den Store, in dem Sie gekauft haben."),
                ("Wie schalte ich Mitteilungen ein oder aus?", "Mitteilungen sind optional und standardmäßig ausgeschaltet. Sie können sie unter Einstellungen > Mitteilungen ein- oder ausschalten. Wenn sie aktiviert sind, senden wir Mitteilungen über Ranglistenänderungen und Erinnerungen."),
                ("Wie lösche ich meine Daten?", "Wenn Sie angemeldet sind, tippen Sie auf Einstellungen > Sudoku verlassen. Die Daten dieses Spiels werden dauerhaft gelöscht; Apple-Nutzer bestätigen ihre Identität über den Apple-Anmeldebildschirm, und das Apple-Token wird widerrufen. Sie können die Löschung auch per E-Mail beantragen. Weitere Informationen finden Sie in der {privacy}."),
                ("Kontakt", "Schreiben Sie an dhalska2@gmail.com mit „Sudoku Pulse“ im Betreff und nennen Sie App-Version, Gerät und Betriebssystemversion sowie die Schritte, die zum Problem geführt haben. Senden Sie niemals Passwörter, Bestätigungscodes oder Zahlungsdaten."),
            ],
            "contact": "Support-Kontakt",
        },
    },
    "pt-br": {
        "ui": {"privacy": "Política de Privacidade", "support": "Ajuda e suporte", "terms": "Termos de Serviço", "languages": "Escolher idioma", "skip": "Ir para o conteúdo", "updated": "Última atualização: 3 de outubro de 2026"},
        "privacy": {
            "title": "Política de Privacidade do Sudoku Pulse",
            "effective": "Em vigor desde 3 de outubro de 2026",
            "intro": "A Next Studio (넥스트 스튜디오) opera o Sudoku Pulse para iOS e Android. Esta política explica quais informações o app trata, para quê e quais escolhas você tem. Ela se aplica ao app e a este site.",
            "sections": [
                ("1. Contas e login", "Ao abrir o app pela primeira vez, uma sessão anônima do Supabase, sem nome nem e-mail, é criada automaticamente. Com ela, compras, dicas e estatísticas de jogo funcionam sem login. Entrar com Apple (iOS) ou Google (Android) é opcional e só é necessário para aparecer no ranking global. Ao entrar, os dados de Sudoku da sessão anônima (saldo de dicas, remoção de anúncios, registros de compra e registros de partidas) são vinculados e mesclados a essa conta."),
                ("2. Informações coletadas e finalidades", [
                    "E-mail de login e identificador do provedor (somente se você entrar): para identificar sua conta. O ranking mostra apenas o e-mail parcialmente oculto.",
                    "Código do país escolhido por você: para exibir uma bandeira no ranking.",
                    "Registros de partidas: dificuldade, tempo de conclusão, erros, número de casas, dicas usadas, bônus de combo Pulse, se era o desafio diário, uma impressão digital (hash) do quebra-cabeça e o registro de jogadas (casa, número, segundos do relógio do jogo e tipo de entrada), além dos horários de início e fim de cada sessão de jogo. O servidor usa esses dados para verificar resultados, calcular pontuações, evitar trapaças e manter estatísticas.",
                    "Contagem diária de dicas grátis: o número de dicas grátis que você usa por dia (até 3 antes de precisar de um anúncio ou de uma dica comprada) é contado por data UTC do servidor e salvo com o seu perfil de jogo de Sudoku no nosso servidor.",
                    "Quebra-cabeça em andamento (somente jogadores conectados): o quebra-cabeça em andamento pode ser salvo no servidor para você continuar em outro dispositivo.",
                    "Informações de compra: ID do produto, ID da transação e status de verificação, para entregar pacotes de dicas e a remoção de anúncios e restaurar compras. A remoção de anúncios é uma compra não consumível e pode passar para outra conta que use o mesmo ID Apple. Os dados de pagamento são tratados pela Apple ou pelo Google; não os recebemos nem armazenamos.",
                    "Informações de notificações push (somente se você ativá-las): token FCM, plataforma, idioma e configuração de notificações, para enviar avisos de mudança no ranking e lembretes. As notificações vêm desativadas e deixam de ser enviadas se você desativá-las em Configurações.",
                    "Publicidade: o Google AdMob e o SDK de consentimento Google UMP podem tratar identificadores do dispositivo, endereço IP e dados de diagnóstico para exibir anúncios, controlar a frequência, prevenir fraudes e registrar o consentimento. No iOS, o identificador de publicidade (IDFA) só é usado se você permitir na solicitação de Transparência de Rastreamento de Apps (ATT). As recompensas de anúncios premiados são verificadas no nosso servidor com um identificador aleatório gerado pelo app, não com seu nome ou e-mail.",
                    "Relatórios de falhas: se o app fechar inesperadamente, o Firebase Crashlytics coleta modelo do dispositivo, versão do sistema, versão do app, rastreamento de pilha da falha e um identificador de instalação para que possamos corrigir o problema. Não são coletados em versões de depuração.",
                ]),
                ("3. Informações guardadas somente no dispositivo", "Idioma, configuração de resposta tátil, conclusão do tutorial, técnicas aprendidas no livro de técnicas, melhor combo, o salvamento automático do quebra-cabeça atual e um contador usado para espaçar os anúncios ficam somente no seu dispositivo e não são enviados ao nosso servidor. Eles são apagados quando você exclui o app."),
                ("4. Prestadores e processamento internacional", "Usamos o Supabase (autenticação, banco de dados e funções de servidor), o Google Firebase (notificações push e Crashlytics), o Google AdMob e o UMP (publicidade e consentimento) e a Apple e o Google (login e pagamentos). Compartilhamos com cada serviço apenas o necessário, e cada prestador trata as informações conforme suas próprias políticas de privacidade e compromissos de segurança, que oferecem o mesmo nível de proteção desta política. As informações podem ser processadas em servidores fora do seu país, onde esses prestadores operam, com as salvaguardas exigidas pela lei aplicável."),
                ("5. Retenção e exclusão", "Mantemos seus dados até que você os exclua no app ou nos peça a exclusão por e-mail. Se você estiver conectado, Configurações > Sair do Sudoku exclui permanentemente os dados deste jogo; em contas Apple, também revogamos o token de login da Apple. Os dados anteriores ao login ficam vinculados apenas à sessão anônima do seu dispositivo: se você excluir o app antes de entrar, eles não poderão ser recuperados nem vinculados novamente a você. Registros de transações que a lei nos obriga a manter podem ser guardados pelo prazo exigido. Relatórios de falhas são mantidos conforme o prazo de retenção do Firebase Crashlytics."),
                ("6. Seus direitos e escolhas", "Você pode solicitar acesso, correção, exclusão ou restrição do tratamento dos seus dados, ou retirar o consentimento, pelo e-mail dhalska2@gmail.com. Você pode alterar o consentimento de anúncios em Configurações > Privacidade dos anúncios (exibido onde sua região exige) e a permissão de rastreamento nos ajustes do dispositivo. Você pode ativar ou desativar as notificações em Configurações a qualquer momento."),
                ("7. Crianças, segurança e alterações", "O serviço não é direcionado a crianças e não coletamos intencionalmente seus dados sem o consentimento necessário dos responsáveis. Adotamos medidas razoáveis, incluindo controle de acesso e comunicação criptografada. Atualizaremos a data e avisaremos sobre mudanças importantes."),
            ],
            "contact": "Contato de privacidade",
        },
        "support": {
            "title": "Ajuda e suporte do Sudoku Pulse",
            "intro": "Respostas para dúvidas frequentes sobre o Sudoku Pulse. Se precisar de mais ajuda, envie um e-mail.",
            "faq": [
                ("Como funcionam as dicas e as explicações?", "Selecione uma casa vazia e toque em Dica. O número correto é preenchido e o tabuleiro explica por que ele é o certo, com a técnica de resolução usada. As técnicas aprendidas ficam reunidas no Livro de técnicas. Se a casa escolhida depender de outras casas primeiro, o app destaca uma casa que você pode resolver agora, sem gastar dica. Todo dia você tem 3 dicas grátis (a contagem reinicia às 00:00 UTC); depois disso, pode usar dicas da Loja Pulse ou assistir a um anúncio opcional para ganhar uma. Usar uma dica interrompe o combo Pulse."),
                ("Preciso entrar com uma conta?", "Não. O app cria automaticamente uma sessão anônima, então você pode jogar todos os quebra-cabeças, usar dicas e fazer compras sem entrar. Entrar com Apple (iOS) ou Google (Android) é opcional e só é necessário para participar do ranking global. Ao entrar, seu saldo de dicas, a remoção de anúncios e seus registros de compra e de partidas anteriores são vinculados à sua conta. Se você excluir o app antes de entrar, esses dados não poderão ser recuperados."),
                ("Como funciona o ranking?", [
                    "É preciso estar conectado. Partidas iniciadas sem login ou offline não entram no ranking.",
                    "Contam os quebra-cabeças resolvidos com até 3 dicas; com mais de 3 dicas, não contam.",
                    "A pontuação é a velocidade por dificuldade (cada erro soma 10 segundos) mais o bônus de combo Pulse.",
                    "O desafio diário é para diversão e não conta para o ranking.",
                    "Concluir de novo um quebra-cabeça que você já terminou não conta outra vez.",
                    "Todos os resultados são verificados no nosso servidor antes de entrar no ranking.",
                ]),
                ("Como restauro minhas compras?", "Abra a Loja Pulse e toque em Restaurar. A remoção de anúncios é restaurada pela sua conta da App Store, e o saldo de dicas é recarregado do nosso servidor mesmo que a loja não tenha nada a restaurar. Dicas já usadas não podem ser restauradas. Para cobranças ou reembolsos, fale com a loja onde você fez a compra."),
                ("Como ativo ou desativo as notificações?", "As notificações são opcionais e vêm desativadas. Ative ou desative em Configurações > Notificações. Quando ativadas, enviamos avisos de mudança no ranking e lembretes."),
                ("Como excluo meus dados?", "Com a conta conectada, vá em Configurações > Sair do Sudoku. Os dados deste jogo são excluídos permanentemente; usuários Apple confirmam a identidade na tela de login da Apple e o token da Apple é revogado. Você também pode pedir a exclusão por e-mail. Veja a {privacy} para mais detalhes."),
                ("Fale conosco", "Envie um e-mail para dhalska2@gmail.com com “Sudoku Pulse” no assunto, informando a versão do app, o dispositivo e a versão do sistema, e os passos que levaram ao problema. Nunca envie senhas, códigos de verificação ou dados de pagamento."),
            ],
            "contact": "Contato de suporte",
        },
    },
}

PROVIDER_LINKS = [
    ("Supabase", "https://supabase.com/privacy"),
    ("Google", "https://policies.google.com/privacy"),
    ("Firebase", "https://firebase.google.com/support/privacy"),
    ("Apple", "https://www.apple.com/legal/privacy/"),
]


def rich(text, privacy_link=""):
    html = escape(text).replace(EMAIL, f'<a href="mailto:{EMAIL}">{EMAIL}</a>')
    return html.replace("{privacy}", privacy_link)


def block(content, privacy_link=""):
    if isinstance(content, list):
        return "<ul>" + "".join(f"<li>{rich(item, privacy_link)}</li>" for item in content) + "</ul>"
    return f"<p>{rich(content, privacy_link)}</p>"


def terms_href(prefix, folder):
    # terms.html is a single ko/en page; other languages land on the English part.
    return f"{prefix}terms.html" + ("" if folder == "ko" else "#en")


def render(folder, kind, prefix):
    """prefix: relative path from the output file back to the sudoku/ folder."""
    lang = next(l for l in LANGUAGES if l[0] == folder)[1]
    ui = PAGES[folder]["ui"]
    page = PAGES[folder][kind]
    title = page["title"]
    alternates = "\n".join(
        f'<link rel="alternate" hreflang="{hl}" href="{ROOT_URL}{f}/{kind}.html">' for f, hl, _, _ in LANGUAGES
    )
    languages = "".join(
        f'<a href="{prefix}{f}/{kind}.html" lang="{hl}" hreflang="{hl}"'
        + (' aria-current="true"' if f == folder else "")
        + f">{escape(label)}</a>"
        for f, hl, label, _ in LANGUAGES
    )
    nav = (
        f'<a href="{prefix}{folder}/privacy.html"' + (' aria-current="page"' if kind == "privacy" else "") + f'>{escape(ui["privacy"])}</a>'
        f'<a href="{prefix}{folder}/support.html"' + (' aria-current="page"' if kind == "support" else "") + f'>{escape(ui["support"])}</a>'
        f'<a href="{terms_href(prefix, folder)}">{escape(ui["terms"])}</a>'
    )
    privacy_link = f'<a href="{prefix}{folder}/privacy.html">{escape(ui["privacy"])}</a>'
    if kind == "privacy":
        body = f'<h1>{escape(title)}</h1><p class="effective">{escape(page["effective"])}</p><p class="intro">{escape(page["intro"])}</p>\n'
        body += "\n".join(f"<section><h2>{escape(h)}</h2>{block(c)}</section>" for h, c in page["sections"])
        body += '\n<p class="providers">' + " · ".join(f'<a href="{u}">{n} Privacy</a>' for n, u in PROVIDER_LINKS) + "</p>"
        subject = "Sudoku%20Pulse%20Privacy"
    else:
        body = f'<h1>{escape(title)}</h1><p class="effective">{escape(ui["updated"])}</p><p class="intro">{escape(page["intro"])}</p>\n'
        body += "\n".join(
            f"<section><h2>{i}. {escape(q)}</h2>{block(a, privacy_link)}</section>"
            for i, (q, a) in enumerate(page["faq"], 1)
        )
        subject = "Sudoku%20Pulse%20Support"
    body += (
        f'\n<div class="contact"><b>{escape(page["contact"])}</b><br>Next Studio · 넥스트 스튜디오<br>'
        f'<a href="mailto:{EMAIL}?subject={subject}">{EMAIL}</a></div>'
    )
    return f'''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="description" content="{escape(title)} · Next Studio">
<title>{escape(title)}</title>
<link rel="stylesheet" href="{prefix}style.css">
<link rel="canonical" href="{ROOT_URL}{folder}/{kind}.html">
{alternates}
<link rel="alternate" hreflang="x-default" href="{ROOT_URL}en/{kind}.html">
</head>
<body><a class="skip" href="#content">{escape(ui["skip"])}</a>
<main><header class="top"><a class="brand" href="{prefix}index.html">SUDOKU PULSE</a>
<nav class="languages" aria-label="{escape(ui["languages"])}">{languages}</nav></header>
<nav class="pages" aria-label="{escape(title)}">{nav}</nav>
<article id="content">{body}</article>
<footer>© 2026 Next Studio · 넥스트 스튜디오 · <a href="mailto:{EMAIL}">{EMAIL}</a></footer></main></body></html>
'''


def render_hub():
    rows = "".join(
        f'<li lang="{hl}"><span class="name">{escape(label)}</span>'
        f'<a href="{f}/privacy.html" hreflang="{hl}">{escape(PAGES[f]["ui"]["privacy"])}</a>'
        f'<a href="{f}/support.html" hreflang="{hl}">{escape(PAGES[f]["ui"]["support"])}</a>'
        f'<a href="{terms_href("", f)}">{escape(PAGES[f]["ui"]["terms"])}</a></li>'
        for f, hl, label, _ in LANGUAGES
    )
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="description" content="Sudoku Pulse privacy policy, help and support · Next Studio">
<title>Sudoku Pulse · Privacy &amp; Support</title>
<link rel="stylesheet" href="style.css">
<link rel="canonical" href="{ROOT_URL}index.html">
</head>
<body><main><header class="top"><span class="brand">SUDOKU PULSE</span></header>
<article id="content"><h1>Sudoku Pulse</h1><p class="intro">Choose your language · 언어를 선택하세요</p>
<ul class="hub">{rows}</ul>
<div class="contact"><b>Contact</b><br>Next Studio · 넥스트 스튜디오<br><a href="mailto:{EMAIL}?subject=Sudoku%20Pulse">{EMAIL}</a></div></article>
<footer>© 2026 Next Studio · 넥스트 스튜디오</footer></main></body></html>
'''


def main():
    count = 0
    for folder, _, _, legacy in LANGUAGES:
        (HERE / folder).mkdir(exist_ok=True)
        for kind in ("privacy", "support"):
            (HERE / folder / f"{kind}.html").write_text(render(folder, kind, "../"), encoding="utf-8")
            count += 1
        # Legacy URL kept for shipped app builds: same policy, links resolve from sudoku/.
        (HERE / legacy).write_text(render(folder, "privacy", ""), encoding="utf-8")
        count += 1
    (HERE / "index.html").write_text(render_hub(), encoding="utf-8")
    print(f"Generated {count + 1} pages.")


if __name__ == "__main__":
    main()
