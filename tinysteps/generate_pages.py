"""Generate TinySteps marketing, privacy, and support pages in eight languages."""

from html import escape as esc
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SITE = "https://oh-seungjin.github.io/privacy-terms/tinysteps"
EMAIL = "dhalska2@gmail.com"

ALL_TRANSLATIONS = {
    "ko": {
        "label": "한국어", "html": "ko", "nav": ["소개", "개인정보처리방침", "지원"],
        "tag": "작은 습관이 자라나는 정원", "intro": "매일의 습관과 집중 시간을 기록하고, 30일 동안 식물을 키워 보세요.",
        "features": ["요일과 시간을 정하는 습관 및 로컬 알림", "15·25·45·60분 집중 타이머", "30일 성장 과정과 100종 식물 도감"],
        "offline": "계정, 광고, 분석 도구, 구독 없이 모든 기록을 기기에만 저장합니다.",
        "privacy_title": "TinySteps 개인정보처리방침", "date": "시행일: 2026년 10월 9일",
        "privacy_intro": "TinySteps는 Next Studio가 제공하는 오프라인 습관·집중 앱입니다. 계정이나 서버 연결 없이 사용할 수 있도록 설계했습니다.",
        "privacy": [
            ("기기에서 처리하는 정보", "습관 이름·일정·아이콘·색상·알림 시간, 습관 완료 기록, 집중 타이머 기록, 식물 성장·선택·수집 진행 정보, 언어 및 화면 모드 설정을 기기에만 저장합니다."),
            ("수집 및 제3자 제공", "Next Studio는 이 정보를 수집하거나 서버로 전송하지 않습니다. 앱에는 계정, 클라우드 동기화, 광고, 분석 도구 또는 추적 SDK가 없습니다."),
            ("알림", "사용자가 허용하면 기기에서 로컬 알림을 예약합니다. 알림 내용과 시간은 서버로 전송되지 않으며 기기 설정에서 권한을 해제할 수 있습니다."),
            ("내보내기와 삭제", "데이터 내보내기는 사용자의 요청에 따라 습관 및 집중 기록의 JSON 사본을 클립보드에 저장합니다. 운영체제 정책에 따라 다른 앱이 클립보드를 읽을 수 있습니다. 설정의 모든 데이터 초기화 또는 앱 삭제로 기록을 제거할 수 있으며, 운영체제 백업·복원 정책의 영향을 받을 수 있습니다."),
            ("아동 및 변경", "TinySteps는 일반 사용자를 위한 앱이며 아동의 개인정보를 고의로 수집하지 않습니다. 방침이 변경되면 이 페이지의 시행일을 갱신합니다."),
        ],
        "support_title": "TinySteps 도움말 및 지원", "support_intro": "앱 사용 중 문제가 있다면 아래 내용을 확인하거나 이메일로 문의해 주세요.",
        "support": [
            ("알림이 오지 않을 때", "기기 설정에서 TinySteps 알림 권한을 허용했는지 확인하고, 습관의 요일과 시간이 현재 일정에 맞는지 확인하세요. 알림은 서버가 아닌 기기에서 예약됩니다."),
            ("데이터 백업", "설정의 데이터 내보내기로 JSON을 클립보드에 복사할 수 있습니다. TinySteps는 계정이나 클라우드 동기화를 제공하지 않습니다."),
            ("데이터 삭제", "설정의 모든 데이터 초기화를 사용하세요. 이 작업은 습관, 집중 기록, 정원 및 도감 진행 상태를 기기에서 삭제합니다."),
            ("문의할 때", "기기 종류, 운영체제 버전, 앱 버전과 문제를 재현하는 순서를 적어 보내 주세요. 습관 내용처럼 공개하고 싶지 않은 정보는 포함하지 않아도 됩니다."),
        ],
        "contact": "문의", "skip": "본문으로 이동", "choose": "언어 선택", "copyright": "© 2026 Next Studio · 넥스트 스튜디오",
    },
    "en": {
        "label": "English", "html": "en", "nav": ["Overview", "Privacy", "Support"],
        "tag": "A garden where small habits grow", "intro": "Track daily habits and focus sessions while your plant grows over 30 days.",
        "features": ["Flexible schedules and on-device reminders", "15, 25, 45, and 60-minute focus timer", "30-day growth cycle and 100-plant collection"],
        "offline": "No account, ads, analytics, or subscription. Your records stay on your device.",
        "privacy_title": "TinySteps Privacy Policy", "date": "Effective October 9, 2026",
        "privacy_intro": "TinySteps is an offline habit and focus app provided by Next Studio. It is designed to work without an account or server connection.",
        "privacy": [
            ("Information handled on your device", "Habit names, schedules, icons, colors and reminder times; completion history; focus history; plant growth, selection and collection progress; and language and appearance preferences are stored only on your device."),
            ("Collection and sharing", "Next Studio does not collect or transmit this information to a server. The app has no account, cloud sync, advertising, analytics, or tracking SDK."),
            ("Notifications", "If you grant permission, TinySteps schedules reminders locally on your device. Reminder content and times are not sent to a server. You can revoke permission in device settings."),
            ("Export and deletion", "At your request, Data Export places a JSON copy of habit and focus records on the clipboard. Other apps may read clipboard contents under operating-system rules. Use Reset All Data or uninstall the app to remove local records, subject to system backup and restore behavior."),
            ("Children and changes", "TinySteps is a general-audience app and does not knowingly collect children's personal information. If this policy changes, the effective date on this page will be updated."),
        ],
        "support_title": "TinySteps Help & Support", "support_intro": "Review these tips or email us if you need help using the app.",
        "support": [
            ("If reminders do not arrive", "Confirm that notification permission is enabled for TinySteps and that the habit's selected days and time match your schedule. Reminders are scheduled on the device, not by a server."),
            ("Data backup", "Data Export copies JSON to the clipboard. TinySteps does not provide accounts or cloud sync."),
            ("Delete data", "Use Reset All Data in Settings. This removes habits, focus history, garden state, and collection progress from the device."),
            ("When contacting us", "Include your device model, operating-system version, app version, and steps to reproduce the issue. You do not need to include private habit details."),
        ],
        "contact": "Contact", "skip": "Skip to content", "choose": "Choose language", "copyright": "© 2026 Next Studio",
    },
    "ja": {
        "label": "日本語", "html": "ja", "nav": ["概要", "プライバシー", "サポート"],
        "tag": "小さな習慣が育つ庭", "intro": "毎日の習慣と集中時間を記録し、30日間で植物を育てましょう。",
        "features": ["曜日・時間を設定できる習慣と端末内通知", "15・25・45・60分の集中タイマー", "30日間の成長と100種類の植物図鑑"],
        "offline": "アカウント、広告、分析、サブスクリプションはなく、記録は端末内に保存されます。",
        "privacy_title": "TinySteps プライバシーポリシー", "date": "施行日：2026年10月9日",
        "privacy_intro": "TinyStepsはNext Studioが提供するオフラインの習慣・集中アプリです。アカウントやサーバー接続なしで動作します。",
        "privacy": [("端末内で扱う情報", "習慣名、予定、アイコン、色、通知時刻、達成履歴、集中履歴、植物の成長・選択・収集状況、言語・表示設定を端末内だけに保存します。"), ("収集と共有", "Next Studioはこれらの情報を収集せず、サーバーへ送信しません。アカウント、クラウド同期、広告、分析、トラッキングSDKはありません。"), ("通知", "許可された場合、通知は端末内で予約されます。内容と時刻はサーバーへ送信されず、端末設定で許可を解除できます。"), ("書き出しと削除", "データ書き出しは習慣・集中記録のJSONをクリップボードへ保存します。OSの規則により他のアプリが読み取る場合があります。全データのリセットまたはアプリ削除で端末内の記録を削除できますが、OSのバックアップ・復元の影響を受ける場合があります。"), ("子どもと変更", "一般利用者向けのアプリで、子どもの個人情報を意図的に収集しません。方針変更時は施行日を更新します。")],
        "support_title": "TinySteps ヘルプとサポート", "support_intro": "問題がある場合は以下を確認するか、メールでお問い合わせください。",
        "support": [("通知が届かない場合", "TinyStepsの通知許可と、習慣に設定した曜日・時刻を確認してください。通知は端末内で予約されます。"), ("データのバックアップ", "データ書き出しでJSONをクリップボードへコピーできます。アカウントやクラウド同期はありません。"), ("データの削除", "設定の全データのリセットで、習慣、集中履歴、庭、図鑑の進行状況を削除できます。"), ("お問い合わせ", "端末、OS、アプリのバージョンと再現手順をお知らせください。非公開にしたい習慣内容は不要です。")],
        "contact": "お問い合わせ", "skip": "本文へ移動", "choose": "言語を選択", "copyright": "© 2026 Next Studio",
    },
    "zh-hans": {
        "label": "简体中文", "html": "zh-Hans", "nav": ["简介", "隐私", "支持"],
        "tag": "让小习惯长成一座花园", "intro": "记录每日习惯和专注时间，在30天内培育植物。",
        "features": ["自定义日期、时间与设备本地提醒", "15、25、45和60分钟专注计时器", "30天成长过程与100种植物图鉴"],
        "offline": "无需账号，没有广告、分析或订阅；记录仅保存在设备上。",
        "privacy_title": "TinySteps 隐私政策", "date": "生效日期：2026年10月9日",
        "privacy_intro": "TinySteps是Next Studio提供的离线习惯与专注应用，无需账号或服务器连接。",
        "privacy": [("设备上处理的信息", "习惯名称、计划、图标、颜色、提醒时间、完成记录、专注记录、植物成长与收集进度以及语言和外观偏好仅保存在设备上。"), ("收集与共享", "Next Studio不会收集这些信息或将其发送到服务器。应用不含账号、云同步、广告、分析或跟踪SDK。"), ("通知", "获得许可后，提醒在设备本地安排，内容和时间不会发送到服务器。您可在设备设置中撤销权限。"), ("导出与删除", "数据导出会按您的要求将习惯和专注记录的JSON副本放入剪贴板。其他应用可能依照操作系统规则读取剪贴板。您可使用“重置所有数据”或卸载应用删除本地记录，但可能受系统备份与恢复影响。"), ("儿童与变更", "本应用面向一般用户，不会故意收集儿童个人信息。政策变更时将更新本页日期。")],
        "support_title": "TinySteps 帮助与支持", "support_intro": "如需帮助，请查看以下内容或发送电子邮件。",
        "support": [("未收到提醒", "请确认TinySteps的通知权限已开启，并检查习惯的日期和时间。提醒在设备本地安排。"), ("数据备份", "数据导出可将JSON复制到剪贴板。本应用不提供账号或云同步。"), ("删除数据", "使用设置中的“重置所有数据”，可删除习惯、专注记录、花园和图鉴进度。"), ("联系我们", "请提供设备型号、系统版本、应用版本和复现步骤，无需发送私人习惯内容。")],
        "contact": "联系", "skip": "跳到正文", "choose": "选择语言", "copyright": "© 2026 Next Studio",
    },
    "es": {
        "label": "Español", "html": "es", "nav": ["Inicio", "Privacidad", "Soporte"],
        "tag": "Un jardín donde crecen pequeños hábitos", "intro": "Registra hábitos y sesiones de concentración mientras tu planta crece durante 30 días.",
        "features": ["Horarios flexibles y recordatorios locales", "Temporizador de 15, 25, 45 y 60 minutos", "Ciclo de 30 días y colección de 100 plantas"],
        "offline": "Sin cuenta, anuncios, analíticas ni suscripción. Los registros permanecen en el dispositivo.",
        "privacy_title": "Política de privacidad de TinySteps", "date": "En vigor desde el 9 de octubre de 2026",
        "privacy_intro": "TinySteps es una aplicación sin conexión de hábitos y concentración de Next Studio. Funciona sin cuenta ni conexión a un servidor.",
        "privacy": [("Información tratada en el dispositivo", "Los hábitos, horarios, iconos, colores, recordatorios, historial, progreso de plantas y preferencias se guardan únicamente en el dispositivo."), ("Recopilación y uso compartido", "Next Studio no recopila ni transmite esta información. No hay cuenta, sincronización, publicidad, analíticas ni SDK de seguimiento."), ("Notificaciones", "Con permiso, los recordatorios se programan localmente. El contenido y la hora no se envían a un servidor y el permiso puede revocarse en los ajustes."), ("Exportación y eliminación", "La exportación copia un JSON al portapapeles; otras aplicaciones podrían leerlo según las reglas del sistema. Restablecer todos los datos o desinstalar elimina los registros locales, sujeto a las copias de seguridad del sistema."), ("Menores y cambios", "La aplicación es para el público general y no recopila intencionadamente datos de menores. Actualizaremos la fecha si cambia esta política.")],
        "support_title": "Ayuda y soporte de TinySteps", "support_intro": "Consulta estos consejos o escríbenos si necesitas ayuda.",
        "support": [("Si no llegan recordatorios", "Comprueba el permiso de notificaciones y los días y la hora del hábito. Se programan en el dispositivo."), ("Copia de datos", "La exportación copia un JSON al portapapeles. No hay cuenta ni sincronización en la nube."), ("Eliminar datos", "Usa Restablecer todos los datos para borrar hábitos, historial, jardín y colección."), ("Al contactarnos", "Indica dispositivo, versión del sistema y de la app, y pasos para reproducir el problema. No incluyas hábitos privados.")],
        "contact": "Contacto", "skip": "Ir al contenido", "choose": "Elegir idioma", "copyright": "© 2026 Next Studio",
    },
    "fr": {
        "label": "Français", "html": "fr", "nav": ["Présentation", "Confidentialité", "Assistance"],
        "tag": "Un jardin où poussent les petites habitudes", "intro": "Suivez vos habitudes et vos séances de concentration pendant que votre plante grandit en 30 jours.",
        "features": ["Planning flexible et rappels locaux", "Minuteur de 15, 25, 45 et 60 minutes", "Croissance sur 30 jours et collection de 100 plantes"],
        "offline": "Sans compte, publicité, analyse ni abonnement. Les données restent sur l’appareil.",
        "privacy_title": "Politique de confidentialité de TinySteps", "date": "En vigueur le 9 octobre 2026",
        "privacy_intro": "TinySteps est une application hors ligne d’habitudes et de concentration fournie par Next Studio, sans compte ni serveur.",
        "privacy": [("Informations traitées sur l’appareil", "Habitudes, plannings, icônes, couleurs, rappels, historiques, progression des plantes et préférences sont stockés uniquement sur l’appareil."), ("Collecte et partage", "Next Studio ne collecte ni ne transmet ces informations. Aucun compte, cloud, publicité, outil d’analyse ou SDK de suivi n’est intégré."), ("Notifications", "Avec votre autorisation, les rappels sont programmés localement. Leur contenu et leur heure ne sont pas envoyés à un serveur. L’autorisation peut être retirée dans les réglages."), ("Exportation et suppression", "L’export place une copie JSON dans le presse-papiers, que d’autres apps peuvent lire selon le système. Réinitialiser les données ou désinstaller supprime les données locales, sous réserve des sauvegardes système."), ("Enfants et modifications", "L’application s’adresse au grand public et ne collecte pas sciemment les données d’enfants. La date sera mise à jour en cas de modification.")],
        "support_title": "Aide et assistance TinySteps", "support_intro": "Consultez ces conseils ou envoyez-nous un e-mail.",
        "support": [("Rappels absents", "Vérifiez l’autorisation de notification ainsi que les jours et l’heure de l’habitude. Les rappels sont locaux."), ("Sauvegarde", "L’export copie un JSON dans le presse-papiers. Il n’existe ni compte ni synchronisation cloud."), ("Supprimer les données", "Utilisez Réinitialiser toutes les données pour effacer habitudes, historique, jardin et collection."), ("Nous contacter", "Indiquez l’appareil, les versions du système et de l’app, et les étapes de reproduction. N’envoyez pas d’habitudes privées.")],
        "contact": "Contact", "skip": "Aller au contenu", "choose": "Choisir la langue", "copyright": "© 2026 Next Studio",
    },
    "de": {
        "label": "Deutsch", "html": "de", "nav": ["Übersicht", "Datenschutz", "Support"],
        "tag": "Ein Garten, in dem kleine Gewohnheiten wachsen", "intro": "Halte Gewohnheiten und Fokuszeiten fest, während deine Pflanze 30 Tage lang wächst.",
        "features": ["Flexible Zeitpläne und lokale Erinnerungen", "Fokus-Timer für 15, 25, 45 und 60 Minuten", "30 Tage Wachstum und 100 Pflanzen"],
        "offline": "Ohne Konto, Werbung, Analyse oder Abo. Deine Daten bleiben auf dem Gerät.",
        "privacy_title": "Datenschutzerklärung für TinySteps", "date": "Gültig ab 9. Oktober 2026",
        "privacy_intro": "TinySteps ist eine Offline-App für Gewohnheiten und Fokus von Next Studio. Sie funktioniert ohne Konto oder Serververbindung.",
        "privacy": [("Auf dem Gerät verarbeitete Daten", "Gewohnheiten, Zeitpläne, Symbole, Farben, Erinnerungen, Verläufe, Pflanzenfortschritt und Einstellungen werden nur auf dem Gerät gespeichert."), ("Erhebung und Weitergabe", "Next Studio erhebt oder überträgt diese Daten nicht. Die App enthält kein Konto, keine Cloud-Synchronisierung, Werbung, Analyse oder Tracking-SDKs."), ("Mitteilungen", "Nach Erlaubnis werden Erinnerungen lokal geplant. Inhalt und Zeit werden nicht an einen Server gesendet; die Erlaubnis kann in den Geräteeinstellungen widerrufen werden."), ("Export und Löschung", "Der Export legt eine JSON-Kopie in der Zwischenablage ab, die andere Apps nach Systemregeln lesen können. Alle Daten zurücksetzen oder Deinstallieren entfernt lokale Daten, vorbehaltlich Systemsicherungen."), ("Kinder und Änderungen", "Die App richtet sich an die Allgemeinheit und erhebt nicht wissentlich Daten von Kindern. Bei Änderungen aktualisieren wir das Datum.")],
        "support_title": "TinySteps Hilfe & Support", "support_intro": "Prüfe diese Hinweise oder sende uns eine E-Mail.",
        "support": [("Keine Erinnerung", "Prüfe die Mitteilungsberechtigung sowie Tage und Uhrzeit der Gewohnheit. Erinnerungen werden lokal geplant."), ("Datensicherung", "Der Export kopiert JSON in die Zwischenablage. Konto und Cloud-Synchronisierung gibt es nicht."), ("Daten löschen", "Alle Daten zurücksetzen löscht Gewohnheiten, Fokusverlauf, Garten und Sammlung."), ("Kontakt", "Nenne Gerät, System- und App-Version sowie Schritte zur Reproduktion. Private Gewohnheitsinhalte sind nicht nötig.")],
        "contact": "Kontakt", "skip": "Zum Inhalt", "choose": "Sprache wählen", "copyright": "© 2026 Next Studio",
    },
    "pt-br": {
        "label": "Português (Brasil)", "html": "pt-BR", "nav": ["Visão geral", "Privacidade", "Suporte"],
        "tag": "Um jardim onde pequenos hábitos crescem", "intro": "Registre hábitos e sessões de foco enquanto sua planta cresce por 30 dias.",
        "features": ["Rotinas flexíveis e lembretes locais", "Temporizador de 15, 25, 45 e 60 minutos", "Ciclo de 30 dias e coleção de 100 plantas"],
        "offline": "Sem conta, anúncios, análise ou assinatura. Seus registros ficam no aparelho.",
        "privacy_title": "Política de Privacidade do TinySteps", "date": "Em vigor desde 9 de outubro de 2026",
        "privacy_intro": "TinySteps é um app offline de hábitos e foco da Next Studio, projetado para funcionar sem conta ou servidor.",
        "privacy": [("Informações tratadas no aparelho", "Hábitos, horários, ícones, cores, lembretes, históricos, progresso das plantas e preferências ficam somente no aparelho."), ("Coleta e compartilhamento", "A Next Studio não coleta nem transmite essas informações. Não há conta, sincronização em nuvem, anúncios, análise ou SDK de rastreamento."), ("Notificações", "Com permissão, os lembretes são agendados localmente. Conteúdo e horário não são enviados a servidores, e a permissão pode ser retirada nos ajustes."), ("Exportação e exclusão", "A exportação coloca uma cópia JSON na área de transferência, que outros apps podem ler conforme o sistema. Redefinir todos os dados ou desinstalar remove os registros locais, sujeito a backups do sistema."), ("Crianças e alterações", "O app é para o público geral e não coleta intencionalmente dados de crianças. Atualizaremos a data se a política mudar.")],
        "support_title": "Ajuda e suporte do TinySteps", "support_intro": "Consulte estas dicas ou envie um e-mail se precisar de ajuda.",
        "support": [("Lembretes não chegam", "Confira a permissão de notificações e os dias e horário do hábito. Os lembretes são agendados no aparelho."), ("Backup", "A exportação copia JSON para a área de transferência. Não há conta nem sincronização em nuvem."), ("Excluir dados", "Use Redefinir todos os dados para apagar hábitos, histórico, jardim e coleção."), ("Ao entrar em contato", "Informe aparelho, versões do sistema e do app e passos para reproduzir. Não inclua hábitos privados.")],
        "contact": "Contato", "skip": "Ir ao conteúdo", "choose": "Escolher idioma", "copyright": "© 2026 Next Studio",
    },
}

# TinySteps 1.0 supports Korean and English only. Keep public pages aligned with
# the locales that users can actually select in the app.
LANGUAGES = {code: ALL_TRANSLATIONS[code] for code in ("ko", "en")}

STYLE = """:root{--bg:#f6f3eb;--card:#fffdf8;--ink:#1c2a22;--muted:#657067;--green:#496c56;--soft:#dce8dd;--line:#d6ddd5}*{box-sizing:border-box}body{margin:0;background:radial-gradient(circle at 90% 0,#dce9dd 0,transparent 32rem),var(--bg);color:var(--ink);font:16px/1.65 system-ui,-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif}a{color:var(--green)}main{max-width:980px;margin:auto;padding:22px 18px 64px}.skip{position:absolute;left:-9999px}.skip:focus{left:12px;top:12px;background:#fff;padding:10px;z-index:5}.top{display:flex;align-items:center;justify-content:space-between;gap:16px}.brand{display:flex;align-items:center;gap:10px;color:var(--ink);font-weight:900;letter-spacing:.04em;text-decoration:none}.brand img{border-radius:11px}.language{font:inherit;color:var(--ink);background:var(--card);border:1px solid var(--line);border-radius:12px;padding:9px 30px 9px 11px}nav{display:flex;gap:18px;flex-wrap:wrap;margin:24px 0}nav a{font-weight:700;text-decoration:none}nav a[aria-current=page]{text-decoration:underline;text-underline-offset:6px}article{background:var(--card);border:1px solid var(--line);border-radius:28px;padding:clamp(24px,6vw,58px);box-shadow:0 24px 60px #233d2c12}h1{font-size:clamp(2.25rem,6vw,4.2rem);line-height:1.05;letter-spacing:-.045em;margin:.15em 0 .35em}h2{font-size:1.25rem;margin:2em 0 .35em}.lead{font-size:1.15rem;max-width:42rem}.date,.muted{color:var(--muted)}.features{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;padding:0;margin:34px 0;list-style:none}.features li{background:var(--soft);border-radius:18px;padding:20px;font-weight:700}.cards{display:grid;grid-template-columns:repeat(2,1fr);gap:14px;margin-top:32px}.card{border:1px solid var(--line);border-radius:16px;padding:18px;text-decoration:none;font-weight:800}.contact{margin-top:40px;background:var(--soft);border-radius:18px;padding:20px}footer{text-align:center;color:var(--muted);margin-top:30px}.languages{display:flex;flex-wrap:wrap;gap:12px}@media(max-width:680px){main{padding:16px 12px 42px}.features,.cards{grid-template-columns:1fr}article{border-radius:20px;padding:26px 19px}}"""

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
        title = "TinySteps"
        content = f'<p class="muted">HABIT · FOCUS · GARDEN</p><h1>{esc(data["tag"])}</h1><p class="lead">{esc(data["intro"])}</p><ul class="features">' + "".join(f'<li>{esc(item)}</li>' for item in data["features"]) + f'</ul><p class="lead">{esc(data["offline"])}</p><div class="cards"><a class="card" href="privacy.html">{esc(data["nav"][1])} →</a><a class="card" href="support.html">{esc(data["nav"][2])} →</a></div>'
    else:
        title = data[f"{kind}_title"]
        content = f'<h1>{esc(title)}</h1><p class="date">{esc(data["date"])}</p><p class="lead">{esc(data[f"{kind}_intro"])}</p>'
        content += "".join(f'<section><h2>{i}. {esc(heading)}</h2><p>{esc(text)}</p></section>' for i, (heading, text) in enumerate(data[kind], 1))
        subject = "TinySteps%20Privacy" if kind == "privacy" else "TinySteps%20Support"
        content += f'<aside class="contact"><h2>{esc(data["contact"])}</h2><p>Next Studio · 넥스트 스튜디오<br><a href="mailto:{EMAIL}?subject={subject}">{EMAIL}</a></p></aside>'
    return f'''<!doctype html>
<html lang="{data['html']}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="description" content="TinySteps · {esc(title)} · Next Studio"><title>TinySteps · {esc(title)}</title>
<link rel="stylesheet" href="../style.css"><link rel="icon" href="../icon.png"><link rel="canonical" href="{SITE}/{code}/{kind}.html">
{alternates(kind)}</head><body><a class="skip" href="#content">{esc(data['skip'])}</a><main>
<header class="top"><a class="brand" href="index.html"><img src="../icon.png" width="42" height="42" alt=""> TinySteps</a><label><span class="skip">{esc(data['choose'])}</span><select class="language" aria-label="{esc(data['choose'])}" onchange="location.href=this.value">{language_options(code, kind)}</select></label></header>
<nav aria-label="TinySteps">{nav(data, kind)}</nav><article id="content">{content}</article><footer>{esc(data['copyright'])}<br><a href="mailto:{EMAIL}">{EMAIL}</a></footer></main></body></html>'''


for locale, strings in LANGUAGES.items():
    destination = ROOT / locale
    destination.mkdir(exist_ok=True)
    for page_kind in KINDS:
        (destination / f"{page_kind}.html").write_text(page(locale, page_kind, strings), encoding="utf-8")

(ROOT / "style.css").write_text(STYLE, encoding="utf-8")
links = "".join(f'<a href="{code}/index.html" hreflang="{data["html"]}">{esc(data["label"])}</a>' for code, data in LANGUAGES.items())
(ROOT / "index.html").write_text(f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="TinySteps official website"><title>TinySteps · Next Studio</title><link rel="stylesheet" href="style.css"><link rel="icon" href="icon.png"></head><body><main><header class="top"><span class="brand"><img src="icon.png" width="42" height="42" alt=""> TinySteps</span></header><article><p class="muted">HABIT · FOCUS · GARDEN</p><h1>A garden where small habits grow</h1><p class="lead">Choose your language.</p><div class="cards languages">{links}</div></article><footer>© 2026 Next Studio · 넥스트 스튜디오</footer></main></body></html>''', encoding="utf-8")
print(f"Generated {len(LANGUAGES) * len(KINDS) + 1} pages.")
