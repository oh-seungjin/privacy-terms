"""Current cross-platform disclosure overrides (2026-10-17)."""
UPDATES = {
'ko': ('스캔과 OCR은 기기 안에서 처리합니다. 클라우드 백업, 문서 변환, AI, 공유 링크는 선택한 문서를 서버로 전송하는 구독 기능입니다.', '광고는 없습니다. Firebase Analytics로 화면·기능 사용, 구매 이벤트, 앱 설치 식별자, 기기 정보 및 IP로 추정한 대략적 위치를 분석합니다. 문서 내용·이름·검색어는 분석 이벤트에 넣지 않습니다. 광고 식별자 수집과 광고 개인화는 비활성화합니다.'),
'en': ('Scanning and OCR run on your device. Optional subscription features—cloud backup, document conversion, AI and share links—send selected documents to servers.', 'There are no ads. Firebase Analytics measures screen and feature use, purchase events, app installation identifiers, device information and approximate location derived from IP. Document content, names and search text are not included in analytics events. Advertising identifier collection and ad personalization are disabled.'),
'ja': ('スキャンとOCRは端末内で処理します。任意の購読機能であるクラウドバックアップ、文書変換、AI、共有リンクは、選択した文書をサーバーに送信します。', '広告はありません。Firebase Analyticsで画面・機能の利用、購入イベント、アプリのインストール識別子、端末情報、IPから推定したおおよその位置を分析します。文書の内容・名前・検索語は分析イベントに含めません。広告識別子の収集と広告のパーソナライズは無効です。'),
'de': ('Scannen und OCR laufen auf dem Gerät. Optionale Abo-Funktionen wie Cloud-Backup, Dokumentumwandlung, KI und Freigabelinks senden ausgewählte Dokumente an Server.', 'Keine Werbung. Firebase Analytics erfasst Bildschirm- und Funktionsnutzung, Kaufereignisse, App-Installationskennungen, Geräteinformationen und den aus der IP abgeleiteten ungefähren Standort. Dokumentinhalt, Namen und Suchtext sind nicht in Analyseereignissen enthalten. Werbe-ID-Erfassung und personalisierte Werbung sind deaktiviert.'),
'fr': ('La numérisation et l’OCR fonctionnent sur l’appareil. Les fonctions facultatives sur abonnement — sauvegarde cloud, conversion, IA et liens de partage — envoient les documents choisis aux serveurs.', 'Aucune publicité. Firebase Analytics analyse l’utilisation des écrans et fonctions, les achats, les identifiants d’installation, les informations de l’appareil et la position approximative déduite de l’IP. Le contenu, le nom des documents et les recherches ne figurent pas dans ces événements. La collecte d’identifiants publicitaires et la personnalisation publicitaire sont désactivées.'),
'es': ('El escaneo y OCR se procesan en el dispositivo. Las funciones opcionales de suscripción — copia en la nube, conversión, IA y enlaces compartidos — envían documentos seleccionados a servidores.', 'Sin anuncios. Firebase Analytics analiza el uso de pantallas y funciones, compras, identificadores de instalación, información del dispositivo y ubicación aproximada derivada de la IP. No incluimos contenido, nombres de documentos ni búsquedas en los eventos. La recopilación del identificador publicitario y la personalización de anuncios están desactivadas.'),
'pt-br': ('Digitalização e OCR ocorrem no aparelho. Recursos opcionais de assinatura — backup na nuvem, conversão, IA e links de compartilhamento — enviam documentos selecionados aos servidores.', 'Sem anúncios. O Firebase Analytics analisa uso de telas e recursos, compras, identificadores de instalação, informações do aparelho e localização aproximada derivada do IP. Conteúdo, nomes de documentos e pesquisas não entram nos eventos. A coleta de identificadores publicitários e a personalização de anúncios estão desativadas.'),
'zh-hant': ('掃描與 OCR 在裝置內處理。雲端備份、文件轉換、AI 與分享連結是選用的訂閱功能，會將所選文件傳送至伺服器。', '沒有廣告。Firebase Analytics 分析畫面與功能使用、購買事件、應用程式安裝識別碼、裝置資訊及由 IP 推估的大致位置。分析事件不含文件內容、名稱或搜尋文字。廣告識別碼收集與廣告個人化均已停用。'),
'zh-hans': ('扫描与 OCR 在设备内处理。云端备份、文档转换、AI 与分享链接是可选的订阅功能，会将所选文档发送至服务器。', '没有广告。Firebase Analytics 分析页面与功能使用、购买事件、应用安装标识符、设备信息及由 IP 推估的大致位置。分析事件不含文档内容、名称或搜索文字。广告标识符收集与广告个性化均已停用。'),
}

def apply_updates(languages):
    for lang, data in languages.items():
        summary, analytics = UPDATES[lang]
        data['offline'] = summary
        data['privacy_intro'] = summary
        data['date'] = '2026-10-17'
        # The existing ads/tracking section follows crash reporting in each locale.
        sections = data['privacy']
        for i, (title, body) in enumerate(sections):
            if 'IDFA' in body:
                sections[i] = (title, analytics)
