from pathlib import Path
from html import escape
HERE = Path(__file__).resolve().parent

LANGUAGES = [
    ("ko", "한국어", "privacy.html"),
    ("en", "English", "privacy-en.html"),
    ("ja", "日本語", "privacy-ja.html"),
    ("zh-Hans", "简体中文", "privacy-zh-hans.html"),
    ("es", "Español", "privacy-es.html"),
    ("fr", "Français", "privacy-fr.html"),
    ("de", "Deutsch", "privacy-de.html"),
    ("pt-BR", "Português", "privacy-pt-br.html"),
]

PAGES = {
    "ko": {
        "title": "Nonogram Pulse 개인정보처리방침",
        "effective": "시행일: 2026년 9월 11일",
        "intro": "넥스트 스튜디오는 Nonogram Pulse 이용자의 개인정보를 보호하고 관련 법령을 준수합니다.",
        "sections": [
            ("1. 수집 정보와 이용 목적", [
                "Google·Apple 로그인 이메일 및 공급자 식별자: 로그인, 계정 구분, 이메일 마스킹 표시에 사용",
                "이용자가 선택한 국가 코드: 랭킹 국기 표시에 사용",
                "난이도, 완료 시간, 실수·정답 수, 랭킹 도전 및 기록: 통계, 랭킹, 부정 이용 방지에 사용",
                "상품 ID, 거래 ID, 구매 검증 상태: 번개 지급, 광고 제거, 구매 복원에 사용. 결제수단 정보는 스토어가 처리하며 회사는 저장하지 않음",
                "FCM 토큰, 플랫폼, 언어 및 알림 설정: 번개 충전 및 순위 하락 알림에 사용",
                "Google Mobile Ads 및 동의 SDK가 광고 제공, 빈도 관리, 부정행위 방지와 법정 동의를 위해 기기 식별자, IP 주소, 진단·이용 정보를 처리할 수 있음",
            ]),
            ("2. 처리 위탁 및 국외 처리", "Supabase(인증·DB), Google Firebase(푸시), Google AdMob(광고·동의), Apple·Google(로그인·결제)을 사용합니다. 정보는 각 사업자가 운영하는 국가의 서버에서 각 사업자의 정책과 적용 법령에 따라 처리될 수 있습니다."),
            ("3. 보유 기간", "계정과 게임 정보는 계정 삭제 시까지 보유합니다. 결제·분쟁 기록은 관련 법령상 기간 동안 보관할 수 있습니다. 푸시 토큰은 로그아웃, 갱신 또는 계정 삭제 시 삭제하거나 무효화하며, 비식별 통계는 보관될 수 있습니다."),
            ("4. 이용자 권리", "이용자는 열람·정정·삭제·처리 제한 및 동의 철회를 이메일로 요청할 수 있습니다. 광고 선택은 앱 또는 기기 설정에서 변경할 수 있습니다."),
            ("5. 아동, 보안 및 변경", "서비스는 아동을 대상으로 하지 않으며 필요한 보호자 동의 없이 아동 정보를 고의로 수집하지 않습니다. 접근 통제와 암호화 통신 등 합리적인 보호조치를 적용합니다. 변경 시 시행일을 갱신하고 중요한 변경을 알립니다."),
        ],
        "contact": "개인정보 문의", "company": "넥스트 스튜디오",
        "address": "인천광역시 서구 승학로495번길 7", "terms": "이용약관",
    },
    "en": {
        "title": "Nonogram Pulse Privacy Policy",
        "effective": "Effective September 11, 2026",
        "intro": "Next Studio protects the privacy of Nonogram Pulse users and complies with applicable privacy laws.",
        "sections": [
            ("1. Information we collect and why", [
                "Google or Apple sign-in email and provider identifier: sign-in, account identification, and masked email display",
                "Country code selected by the user: display of the ranking flag",
                "Difficulty, completion time, mistakes, correct entries, ranked attempts, and results: statistics, rankings, and abuse prevention",
                "Product ID, transaction ID, and purchase verification status: ticket grants, ad removal, and purchase restoration. The app stores process payment credentials; we do not store them",
                "FCM token, platform, language, and notification settings: ticket-full and rank-drop notifications",
                "Google Mobile Ads and consent SDKs may process device identifiers, IP address, diagnostics, and usage information for advertising, frequency management, fraud prevention, and legal consent",
            ]),
            ("2. Service providers and international processing", "We use Supabase for authentication and databases, Google Firebase for push notifications, Google AdMob for advertising and consent, and Apple and Google for sign-in and payments. Data may be processed in countries where these providers operate, under their policies and applicable safeguards."),
            ("3. Retention", "Account and gameplay data is retained until the account is deleted. Transaction and dispute records may be retained as required by law. Push tokens are removed or invalidated on logout, refresh, or account deletion. De-identified statistics may be retained."),
            ("4. Your rights", "You may request access, correction, deletion, restriction, or withdrawal of consent by email. Advertising choices may also be changed in the app or device settings."),
            ("5. Children, security, and changes", "The service is not directed to children, and we do not knowingly collect children's information without required parental consent. We use reasonable safeguards, including access controls and encrypted communications. We update the effective date and provide appropriate notice of material changes."),
        ],
        "contact": "Privacy contact", "company": "Next Studio",
        "address": "7, Seunghak-ro 495beon-gil, Seo-gu, Incheon, Republic of Korea", "terms": "Terms of Service",
    },
    "ja": {
        "title": "Nonogram Pulse プライバシーポリシー",
        "effective": "施行日：2026年9月11日",
        "intro": "Next Studioは、Nonogram Pulseの利用者のプライバシーを保護し、適用される法令を遵守します。",
        "sections": [
            ("1. 収集する情報と利用目的", [
                "Google・Appleログインのメールアドレスおよびプロバイダ識別子：ログイン、アカウント識別、メールアドレスのマスク表示",
                "利用者が選択した国コード：ランキングでの国旗表示",
                "難易度、クリア時間、ミス・正解数、ランキング挑戦および記録：統計、ランキング、不正利用の防止",
                "商品ID、取引ID、購入確認状況：挑戦権の付与、広告削除、購入の復元。支払情報はストアが処理し、当社は保存しません",
                "FCMトークン、プラットフォーム、言語、通知設定：挑戦権の満タンおよび順位低下の通知",
                "Google Mobile Adsおよび同意SDKは、広告配信、頻度管理、不正防止、法的同意のため、端末識別子、IPアドレス、診断・利用情報を処理する場合があります",
            ]),
            ("2. 委託先および国外での処理", "認証・データベースにSupabase、プッシュ通知にGoogle Firebase、広告・同意にGoogle AdMob、ログイン・決済にAppleおよびGoogleを使用します。情報は、各事業者の方針と適用法令に従い、事業者が運営する国のサーバーで処理される場合があります。"),
            ("3. 保有期間", "アカウントおよびゲーム情報は、アカウントが削除されるまで保有します。取引・紛争記録は、法令で定められた期間保管する場合があります。プッシュトークンは、ログアウト、更新、アカウント削除時に削除または無効化します。匿名化された統計は保有される場合があります。"),
            ("4. 利用者の権利", "利用者は、メールによりアクセス、訂正、削除、処理制限、同意撤回を請求できます。広告の選択は、アプリまたは端末の設定でも変更できます。"),
            ("5. 子ども、セキュリティ、変更", "本サービスは子どもを対象としておらず、必要な保護者の同意なしに子どもの情報を意図的に収集しません。アクセス制御や暗号化通信などの合理的な保護措置を講じます。変更時には施行日を更新し、重要な変更を通知します。"),
        ],
        "contact": "プライバシーに関するお問い合わせ", "company": "Next Studio",
        "address": "大韓民国 仁川広域市 西区 勝鶴路495番キル7", "terms": "利用規約",
    },
    "zh-Hans": {
        "title": "Nonogram Pulse 隐私政策",
        "effective": "生效日期：2026年9月11日",
        "intro": "Next Studio致力于保护Nonogram Pulse用户的隐私，并遵守适用的隐私法律。",
        "sections": [
            ("1. 收集的信息及使用目的", [
                "Google或Apple登录邮箱及提供商标识符：用于登录、区分账号及在排行榜中隐藏显示邮箱",
                "用户选择的国家代码：用于显示排行榜国旗",
                "难度、完成时间、错误与正确次数、排名挑战及记录：用于统计、排名和防止滥用",
                "商品ID、交易ID和购买验证状态：用于发放挑战次数、移除广告和恢复购买。支付信息由应用商店处理，我们不会保存",
                "FCM令牌、平台、语言及通知设置：用于挑战次数充满和排名下降通知",
                "Google Mobile Ads及同意SDK可能会为广告投放、频次管理、防欺诈和取得法定同意而处理设备标识符、IP地址、诊断及使用信息",
            ]),
            ("2. 服务提供商及跨境处理", "我们使用Supabase提供身份验证和数据库服务，使用Google Firebase发送推送通知，使用Google AdMob提供广告和同意管理，并使用Apple和Google提供登录与支付服务。信息可能根据各服务商的政策和适用保障措施，在其运营所在国家或地区处理。"),
            ("3. 保存期限", "账号和游戏数据将保存至账号删除。交易和争议记录可能根据法律要求保存。推送令牌会在退出登录、更新或删除账号时删除或失效。去标识化的统计数据可能会被保留。"),
            ("4. 用户权利", "用户可以通过电子邮件请求访问、更正、删除、限制处理或撤回同意。广告选项也可以在应用或设备设置中更改。"),
            ("5. 儿童、安全与变更", "本服务不面向儿童，未经必要的监护人同意，我们不会故意收集儿童信息。我们采取合理的保护措施，包括访问控制和加密通信。政策变更时，我们将更新生效日期并对重大变更发出适当通知。"),
        ],
        "contact": "隐私咨询", "company": "Next Studio",
        "address": "韩国仁川广域市西区胜鹤路495番街7号", "terms": "服务条款",
    },
    "es": {
        "title": "Política de privacidad de Nonogram Pulse",
        "effective": "En vigor desde el 11 de septiembre de 2026",
        "intro": "Next Studio protege la privacidad de los usuarios de Nonogram Pulse y cumple las leyes de privacidad aplicables.",
        "sections": [
            ("1. Información que recopilamos y finalidad", [
                "Correo e identificador del proveedor de Google o Apple: inicio de sesión, identificación de la cuenta y visualización enmascarada del correo",
                "Código de país elegido por el usuario: mostrar la bandera en la clasificación",
                "Dificultad, tiempo, errores, aciertos, intentos y resultados: estadísticas, clasificación y prevención de abusos",
                "ID del producto, ID de transacción y estado de verificación: entrega de intentos, eliminación de anuncios y restauración de compras. Las tiendas procesan los datos de pago; nosotros no los guardamos",
                "Token FCM, plataforma, idioma y ajustes de notificaciones: avisos de intentos recargados y descenso de posición",
                "Google Mobile Ads y sus SDK de consentimiento pueden tratar identificadores del dispositivo, dirección IP y datos de diagnóstico y uso para publicidad, control de frecuencia, prevención del fraude y consentimiento legal",
            ]),
            ("2. Proveedores y tratamiento internacional", "Usamos Supabase para autenticación y bases de datos, Google Firebase para notificaciones, Google AdMob para publicidad y consentimiento, y Apple y Google para inicio de sesión y pagos. Los datos pueden tratarse en los países donde operan estos proveedores, conforme a sus políticas y garantías aplicables."),
            ("3. Conservación", "Los datos de cuenta y juego se conservan hasta que se elimina la cuenta. Los registros de transacciones y disputas pueden conservarse según la ley. Los tokens se eliminan o invalidan al cerrar sesión, renovarse o eliminar la cuenta. Podrán conservarse estadísticas sin identificación."),
            ("4. Tus derechos", "Puedes solicitar acceso, rectificación, eliminación, limitación o retirada del consentimiento por correo electrónico. Las opciones de publicidad también se pueden cambiar en la app o en los ajustes del dispositivo."),
            ("5. Menores, seguridad y cambios", "El servicio no está dirigido a menores y no recopilamos intencionadamente sus datos sin el consentimiento parental necesario. Aplicamos medidas razonables, como controles de acceso y comunicaciones cifradas. Actualizaremos la fecha y avisaremos de los cambios importantes."),
        ],
        "contact": "Contacto de privacidad", "company": "Next Studio",
        "address": "7, Seunghak-ro 495beon-gil, Seo-gu, Incheon, República de Corea", "terms": "Términos del servicio",
    },
    "fr": {
        "title": "Politique de confidentialité de Nonogram Pulse",
        "effective": "Date d'entrée en vigueur : 11 septembre 2026",
        "intro": "Next Studio protège la vie privée des utilisateurs de Nonogram Pulse et respecte les lois applicables.",
        "sections": [
            ("1. Données collectées et finalités", [
                "Adresse e-mail et identifiant du fournisseur Google ou Apple : connexion, identification du compte et affichage masqué de l'adresse",
                "Code pays choisi par l'utilisateur : affichage du drapeau dans le classement",
                "Difficulté, temps, erreurs, réponses correctes, essais et résultats : statistiques, classement et prévention des abus",
                "Identifiant du produit, de la transaction et état de vérification : attribution des essais, suppression des publicités et restauration des achats. Les boutiques traitent les données de paiement ; nous ne les conservons pas",
                "Jeton FCM, plateforme, langue et réglages : notifications de recharge des essais et de baisse du classement",
                "Google Mobile Ads et les SDK de consentement peuvent traiter les identifiants de l'appareil, l'adresse IP et les données de diagnostic et d'utilisation pour la publicité, la gestion de fréquence, la prévention de la fraude et le consentement légal",
            ]),
            ("2. Prestataires et traitement international", "Nous utilisons Supabase pour l'authentification et la base de données, Google Firebase pour les notifications, Google AdMob pour la publicité et le consentement, ainsi qu'Apple et Google pour la connexion et les paiements. Les données peuvent être traitées dans les pays où ces prestataires opèrent, conformément à leurs politiques et garanties applicables."),
            ("3. Conservation", "Les données du compte et du jeu sont conservées jusqu'à la suppression du compte. Les opérations et litiges peuvent être conservés pendant la durée légale. Les jetons sont supprimés ou invalidés à la déconnexion, au renouvellement ou à la suppression du compte. Des statistiques désidentifiées peuvent être conservées."),
            ("4. Vos droits", "Vous pouvez demander l'accès, la rectification, la suppression, la limitation ou le retrait du consentement par e-mail. Les choix publicitaires peuvent aussi être modifiés dans l'application ou les réglages de l'appareil."),
            ("5. Enfants, sécurité et modifications", "Le service ne s'adresse pas aux enfants et nous ne recueillons pas sciemment leurs données sans le consentement parental requis. Nous appliquons des mesures raisonnables, notamment le contrôle d'accès et le chiffrement des communications. La date sera mise à jour et les changements importants seront signalés."),
        ],
        "contact": "Contact confidentialité", "company": "Next Studio",
        "address": "7, Seunghak-ro 495beon-gil, Seo-gu, Incheon, République de Corée", "terms": "Conditions d'utilisation",
    },
    "de": {
        "title": "Datenschutzerklärung für Nonogram Pulse",
        "effective": "Gültig ab 11. September 2026",
        "intro": "Next Studio schützt die Privatsphäre der Nutzer von Nonogram Pulse und beachtet die geltenden Datenschutzgesetze.",
        "sections": [
            ("1. Erhobene Daten und Zwecke", [
                "E-Mail-Adresse und Anbieterkennung von Google oder Apple: Anmeldung, Kontozuordnung und maskierte Anzeige der E-Mail-Adresse",
                "Vom Nutzer gewählter Ländercode: Anzeige der Flagge in der Rangliste",
                "Schwierigkeit, Lösungszeit, Fehler, richtige Eingaben, Ranglistenversuche und Ergebnisse: Statistiken, Ranglisten und Missbrauchsschutz",
                "Produkt-ID, Transaktions-ID und Prüfstatus: Gutschrift von Versuchen, Werbeentfernung und Wiederherstellung von Käufen. Zahlungsdaten werden vom Store verarbeitet und nicht von uns gespeichert",
                "FCM-Token, Plattform, Sprache und Benachrichtigungseinstellungen: Hinweise bei vollen Versuchen und Rangverlust",
                "Google Mobile Ads und Einwilligungs-SDKs können Gerätekennungen, IP-Adresse sowie Diagnose- und Nutzungsdaten für Werbung, Häufigkeitssteuerung, Betrugsprävention und rechtliche Einwilligungen verarbeiten",
            ]),
            ("2. Dienstleister und internationale Verarbeitung", "Wir verwenden Supabase für Anmeldung und Datenbank, Google Firebase für Push-Mitteilungen, Google AdMob für Werbung und Einwilligungen sowie Apple und Google für Anmeldung und Zahlungen. Daten können in Ländern verarbeitet werden, in denen diese Anbieter tätig sind, nach deren Richtlinien und den geltenden Schutzmaßnahmen."),
            ("3. Speicherdauer", "Konto- und Spieldaten werden bis zur Kontolöschung gespeichert. Transaktions- und Streitfalldaten können nach gesetzlichen Vorgaben aufbewahrt werden. Push-Token werden bei Abmeldung, Erneuerung oder Kontolöschung gelöscht oder ungültig gemacht. Anonymisierte Statistiken können gespeichert bleiben."),
            ("4. Ihre Rechte", "Sie können per E-Mail Auskunft, Berichtigung, Löschung, Einschränkung oder Widerruf der Einwilligung verlangen. Werbeoptionen lassen sich auch in der App oder den Geräteeinstellungen ändern."),
            ("5. Kinder, Sicherheit und Änderungen", "Der Dienst richtet sich nicht an Kinder. Ohne erforderliche Zustimmung der Eltern erheben wir nicht wissentlich Daten von Kindern. Wir treffen angemessene Schutzmaßnahmen wie Zugriffskontrollen und verschlüsselte Verbindungen. Bei Änderungen aktualisieren wir das Datum und informieren über wesentliche Änderungen."),
        ],
        "contact": "Datenschutzkontakt", "company": "Next Studio",
        "address": "Seunghak-ro 495beon-gil 7, Seo-gu, Incheon, Republik Korea", "terms": "Nutzungsbedingungen",
    },
    "pt-BR": {
        "title": "Política de Privacidade do Nonogram Pulse",
        "effective": "Em vigor desde 11 de setembro de 2026",
        "intro": "A Next Studio protege a privacidade dos usuários do Nonogram Pulse e cumpre as leis de privacidade aplicáveis.",
        "sections": [
            ("1. Informações coletadas e finalidades", [
                "E-mail e identificador do provedor Google ou Apple: login, identificação da conta e exibição mascarada do e-mail",
                "Código do país escolhido pelo usuário: exibição da bandeira no ranking",
                "Dificuldade, tempo, erros, respostas corretas, tentativas e resultados: estatísticas, ranking e prevenção de abuso",
                "ID do produto, ID da transação e status da verificação: concessão de tentativas, remoção de anúncios e restauração de compras. As lojas processam os dados de pagamento; nós não os armazenamos",
                "Token FCM, plataforma, idioma e preferências de notificação: avisos de tentativas recarregadas e queda no ranking",
                "O Google Mobile Ads e os SDKs de consentimento podem processar identificadores do dispositivo, endereço IP e dados de diagnóstico e uso para publicidade, controle de frequência, prevenção de fraude e consentimento legal",
            ]),
            ("2. Prestadores e processamento internacional", "Usamos o Supabase para autenticação e banco de dados, o Google Firebase para notificações, o Google AdMob para publicidade e consentimento e a Apple e o Google para login e pagamentos. Os dados podem ser processados nos países onde esses prestadores operam, conforme suas políticas e garantias aplicáveis."),
            ("3. Retenção", "Os dados da conta e do jogo são mantidos até a exclusão da conta. Registros de transações e disputas podem ser mantidos conforme exigido por lei. Tokens são removidos ou invalidados no logout, atualização ou exclusão da conta. Estatísticas sem identificação podem ser mantidas."),
            ("4. Seus direitos", "Você pode solicitar acesso, correção, exclusão, restrição ou retirada do consentimento por e-mail. As opções de publicidade também podem ser alteradas no aplicativo ou nos ajustes do dispositivo."),
            ("5. Crianças, segurança e alterações", "O serviço não é direcionado a crianças e não coletamos intencionalmente seus dados sem o consentimento necessário dos responsáveis. Adotamos medidas razoáveis, incluindo controle de acesso e comunicação criptografada. Atualizaremos a data e avisaremos sobre mudanças importantes."),
        ],
        "contact": "Contato de privacidade", "company": "Next Studio",
        "address": "7, Seunghak-ro 495beon-gil, Seo-gu, Incheon, República da Coreia", "terms": "Termos de Serviço",
    },
}

STYLE = """
:root{color-scheme:light;--navy:#34263f;--blue:#ff665c;--cloud:#fff8f3;--line:#dbe4ef}
*{box-sizing:border-box}body{margin:0;background:linear-gradient(180deg,#fff0ea 0,#fff 360px);font:16px/1.75 system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;color:var(--navy)}.sr-only{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0,0,0,0);white-space:nowrap;border:0}
main{max-width:900px;margin:0 auto;padding:32px 22px 72px}.top{display:flex;gap:16px;justify-content:space-between;align-items:center;flex-wrap:wrap;margin-bottom:38px}.brand{font-weight:850;letter-spacing:.04em}.language{padding:10px 36px 10px 12px;border:1px solid var(--line);border-radius:12px;background:#fff;color:var(--navy);font:inherit}
article{background:#fff;border:1px solid var(--line);border-radius:24px;padding:clamp(24px,5vw,56px);box-shadow:0 20px 60px #173a7412}h1{font-size:clamp(30px,5vw,48px);line-height:1.18;margin:0 0 8px}h2{font-size:23px;line-height:1.35;margin:38px 0 12px}.effective{color:#6e7c90;margin-top:0}.intro{font-size:18px}.contact{margin-top:42px;background:var(--cloud);border-radius:16px;padding:22px}.contact b{font-size:18px}a{color:var(--blue)}.links{margin-top:22px;text-align:center}.links a{margin:0 9px}@media(max-width:520px){main{padding:18px 12px 42px}.top{margin-bottom:18px}article{border-radius:18px;padding:24px 18px}h2{font-size:20px}}
"""

def render(code, data):
    options = "".join(
        f'<option value="{escape(filename)}"{" selected" if lang == code else ""}>{escape(label)}</option>'
        for lang, label, filename in LANGUAGES
    )
    sections = []
    for heading, content in data["sections"]:
        if isinstance(content, list):
            body = "<ul>" + "".join(f"<li>{escape(item)}</li>" for item in content) + "</ul>"
        else:
            body = f"<p>{escape(content)}</p>"
        sections.append(f"<section><h2>{escape(heading)}</h2>{body}</section>")
    return f'''<!doctype html>
<html lang="{escape(code)}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="description" content="{escape(data['title'])}"><title>{escape(data['title'])}</title><style>{STYLE}</style></head>
<body><main><div class="top"><div class="brand">NONOGRAM PULSE</div><label><span class="sr-only">Language</span><select class="language" aria-label="Language" onchange="location.href=this.value">{options}</select></label></div>
<article><h1>{escape(data['title'])}</h1><p class="effective">{escape(data['effective'])}</p><p class="intro">{escape(data['intro'])}</p>
{''.join(sections)}
<div class="contact"><b>{escape(data['contact'])}</b><br>{escape(data['company'])}<br>{escape(data['address'])}<br><a href="mailto:dhalska2@gmail.com">dhalska2@gmail.com</a></div>
<div class="links"><a href="terms.html">{escape(data['terms'])}</a></div></article></main></body></html>'''

for code, _, filename in LANGUAGES:
    (HERE / filename).write_text(render(code, PAGES[code]), encoding="utf-8")
