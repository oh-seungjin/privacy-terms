"""Add the signed rewarded-ad verification disclosure in every locale."""
import json
from pathlib import Path

path = Path(__file__).resolve().parent / "translations.json"
data = json.loads(path.read_text(encoding="utf-8"))
copy = {
    "ko": (
        "보상형 광고 힌트는 Google의 서명된 서버 알림을 확인한 뒤 지급합니다. 중복 지급을 막기 위해 익명 요청 토큰, 광고 거래 ID와 시간을 서버에 보관합니다.",
        "광고 시청 완료만으로 힌트가 지급되지는 않으며, 서버 확인이 끝난 뒤 지급됩니다.",
        "시행 / 수정: 2026년 9월 16일",
    ),
    "en": (
        "Rewarded hints are issued after our server verifies Google's signed callback. We store a pseudonymous request token, ad transaction ID and time to prevent duplicate rewards.",
        "Watching an ad alone does not issue a hint; the server confirms the reward first.",
        "Effective / updated September 16, 2026",
    ),
    "ja": (
        "報酬型広告のヒントは、Googleの署名付きサーバー通知を確認してから付与します。重複付与を防ぐため、匿名のリクエストトークン、広告取引ID、時刻をサーバーに保存します。",
        "広告の視聴だけではヒントは付与されず、サーバーで確認した後に反映されます。",
        "施行・更新日：2026年9月16日",
    ),
    "zh-hans": (
        "奖励广告提示仅在服务器验证 Google 的签名回调后发放。为防止重复发放，我们会保存匿名请求令牌、广告交易 ID 和时间。",
        "仅观看广告不会立即获得提示；服务器确认奖励后才会发放。",
        "生效／更新日期：2026年9月16日",
    ),
    "es": (
        "Las pistas por anuncios se entregan tras verificar en nuestro servidor la respuesta firmada de Google. Guardamos un identificador de solicitud seudónimo, el ID de transacción del anuncio y la hora para evitar duplicados.",
        "Ver el anuncio no basta para recibir la pista; primero debe confirmarla el servidor.",
        "Vigente / actualizado: 16 de septiembre de 2026",
    ),
    "fr": (
        "Les indices issus des publicités sont accordés après vérification du rappel signé de Google par notre serveur. Nous conservons un jeton de demande pseudonyme, l’identifiant de transaction publicitaire et l’heure pour éviter les doublons.",
        "Le visionnage seul ne donne pas l’indice : le serveur confirme d’abord la récompense.",
        "Entrée en vigueur / mise à jour : 16 septembre 2026",
    ),
    "de": (
        "Hinweise aus Belohnungsanzeigen werden erst nach Prüfung der signierten Google-Rückmeldung durch unseren Server vergeben. Zur Vermeidung doppelter Gutschriften speichern wir ein pseudonymes Anfragetoken, die Werbetransaktions-ID und den Zeitpunkt.",
        "Das Ansehen der Anzeige allein vergibt noch keinen Hinweis; zuerst bestätigt der Server die Belohnung.",
        "Gültig / aktualisiert am 16. September 2026",
    ),
    "pt-br": (
        "As dicas por anúncios são concedidas após nosso servidor verificar o retorno assinado do Google. Guardamos um token de solicitação pseudônimo, o ID da transação do anúncio e o horário para evitar créditos duplicados.",
        "Assistir ao anúncio não libera a dica por si só; o servidor confirma a recompensa primeiro.",
        "Vigente / atualizado em 16 de setembro de 2026",
    ),
}
old_reward_copy = {
    "ko": "보상 광고는 완료 보상을 받은 경우 힌트 1개를 제공합니다.",
    "en": "A rewarded ad grants one hint when its reward is earned.",
    "ja": "リワード広告の報酬獲得時にヒント1個を付与します。",
    "zh-hans": "激励广告成功获得奖励时提供1个提示。",
    "es": "Un anuncio con recompensa concede una pista al obtener la recompensa.",
    "fr": "Une publicité avec récompense accorde un indice lorsque la récompense est obtenue.",
    "de": "Eine Belohnungsanzeige gewährt bei Erhalt der Belohnung einen Hinweis.",
    "pt-br": "Um anúncio com recompensa concede uma dica quando a recompensa é obtida.",
}
deletion_scope = {
    "ko": "현재 일반 빌드에는 로그인·실제 구매가 활성화되어 있지 않습니다. 계정 기능이 활성화된 버전에서는 설정의 ‘하시 탈퇴’에서 하시의 진행 상황, 힌트, 구매 권한과 게임별 계정 연결을 삭제할 수 있습니다. 공용 로그인과 다른 게임의 데이터는 유지됩니다. 테스트 데이터의 삭제나 앱을 설치하지 않은 상태의 삭제는 아래 이메일로 요청할 수 있습니다.",
    "en": "Sign-in and real purchases are disabled in the current standard build. In an account-enabled version, Settings > Leave Hashi deletes Hashi progress, hints, purchase access and the game-specific account link. The shared sign-in and other games' data remain. You can request deletion of test data or data without the app by email below.",
    "ja": "現在の通常版ではログインと実際の購入は無効です。アカウント機能を有効にした版では、設定の「ハシを退会」からハシの進行状況、ヒント、購入権限、ゲーム別のアカウント連携を削除できます。共通ログインと他のゲームのデータは残ります。テストデータやアプリを利用できない場合の削除は、以下のメールで依頼できます。",
    "zh-hans": "当前普通版本未启用登录或实际购买。启用账号功能后，可在设置中选择“注销数桥”，删除数桥进度、提示、购买权益及该游戏的账号关联。共用登录和其他游戏的数据会保留。测试数据或无法使用应用时，可通过以下邮箱请求删除。",
    "es": "La versión normal actual no habilita cuentas ni compras reales. Cuando se active la cuenta, Ajustes > Eliminar cuenta de Hashi borrará el progreso, las pistas, el acceso a compras y el vínculo de Hashi. El inicio de sesión compartido y los datos de otros juegos seguirán intactos. Puedes solicitar por correo la eliminación de datos de prueba o sin usar la app.",
    "fr": "La version standard actuelle ne permet pas la connexion ni les achats réels. Une fois les comptes activés, Réglages > Supprimer le compte Hashi effacera la progression, les indices, l’accès aux achats et le lien propre à Hashi. La connexion commune et les données des autres jeux resteront intactes. Vous pouvez demander par e-mail la suppression des données de test ou sans utiliser l’app.",
    "de": "Im aktuellen Standard-Build sind Anmeldung und echte Käufe deaktiviert. Nach Aktivierung der Konten löscht Einstellungen > Hashi-Konto löschen den Hashi-Fortschritt, Hinweise, Kaufzugang und die spielbezogene Kontoverknüpfung. Die gemeinsame Anmeldung und Daten anderer Spiele bleiben erhalten. Testdaten oder Daten ohne App-Zugriff kannst du per E-Mail löschen lassen.",
    "pt-br": "A versão padrão atual não ativa contas nem compras reais. Quando as contas forem ativadas, Configurações > Excluir conta do Hashi apagará o progresso, as dicas, o acesso a compras e o vínculo específico do jogo. O login compartilhado e os dados dos outros jogos serão mantidos. Você pode solicitar por e-mail a exclusão de dados de teste ou sem usar o app.",
}
for locale, (privacy, support, date) in copy.items():
    item = data[locale]
    if privacy not in item["privacy"][2][1]:
        item["privacy"][2][1] += " " + privacy
    item["support"][1][1] = item["support"][1][1].replace(
        old_reward_copy[locale], support
    )
    item["delete-account"][0][1] = deletion_scope[locale]
    item["date"] = date
path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
