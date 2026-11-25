"""Generate Animal Grid marketing, privacy, and support pages in eight languages."""

from html import escape as esc
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SITE = "https://oh-seungjin.github.io/privacy-terms/animalgrid"
EMAIL = "dhalska2@gmail.com"
NAME = "Animal Grid"

LANGUAGES = {
    "ko": {
        "label": "한국어", "html": "ko", "nav": ["소개", "개인정보처리방침", "지원"],
        "tag": "동물을 칸에 맞춰 놓는 그리드 퍼즐", "intro": "동물이 가득한 격자 위에서 규칙에 맞게 칸을 채우는 퍼즐입니다. 클래식과 듀오 모드, 단계별 튜토리얼, 힌트, 30종 동물 도감을 제공합니다.",
        "features": ["단계별 튜토리얼과 규칙 설명 힌트", "클래식·듀오 두 가지 모드", "30종 동물 도감과 해금"],
        "offline": "계정이 필요 없으며 진행 기록은 기기에만 저장됩니다. 광고가 표시될 수 있습니다.",
        "privacy_title": "Animal Grid 개인정보처리방침", "date": "시행일: 2026년 11월 25일",
        "privacy_intro": "Animal Grid는 Next Studio가 제공하는 그리드 퍼즐 앱입니다. 만 13세 이상 이용자를 대상으로 하며 계정 없이 사용할 수 있습니다.",
        "privacy": [
            ("기기에서 처리하는 정보", "스테이지 진행 상황, 튜토리얼 진행 상황, 동물 도감과 해금 정보, 언어 설정은 기기에만 저장됩니다."),
            ("수집 및 제3자 제공", "Next Studio는 이 정보를 수집하거나 자체 서버로 전송하지 않습니다. 앱에는 계정, 클라우드 동기화, 분석 도구가 없습니다."),
            ("광고와 동의", "앱은 Google AdMob으로 전면 광고와 보상형 광고를 표시할 수 있습니다. Google과 광고 파트너는 광고 게재, 측정, 부정 사용 방지를 위해 광고 ID, IP 주소, 기기·앱 정보, 광고 상호작용 정보를 수집·사용할 수 있으며 이는 Google의 정책을 따릅니다. 유럽경제지역·영국 등에서는 Google 사용자 메시지 플랫폼(UMP)으로 동의 여부를 묻고, 가능한 경우 앱에서 선택을 변경할 수 있습니다. 광고 ID는 기기 설정에서 재설정하거나 맞춤 광고를 끌 수 있습니다."),
            ("연령", "Animal Grid는 만 13세 이상을 대상으로 하며 13세 미만 아동의 개인정보를 고의로 수집하지 않습니다."),
            ("삭제", "앱 데이터 삭제 또는 앱 제거로 기기 내 기록을 지울 수 있으며, 운영체제 백업·복원 정책의 영향을 받을 수 있습니다."),
            ("변경", "방침이 변경되면 이 페이지의 시행일을 갱신합니다."),
        ],
        "support_title": "Animal Grid 도움말 및 지원", "support_intro": "앱 사용 중 문제가 있다면 아래 내용을 확인하거나 이메일로 문의해 주세요.",
        "support": [
            ("진행 기록이 사라졌을 때", "기록은 계정 없이 기기에만 저장됩니다. 앱 데이터를 지우거나 앱을 삭제하면 기록도 삭제될 수 있습니다."),
            ("광고·동의 문제", "광고가 보이지 않거나 동의 메시지를 다시 보고 싶다면 앱 설정의 개인정보 옵션(제공되는 경우)을 확인하세요. 광고 ID는 기기 설정에서 관리할 수 있습니다."),
            ("데이터 삭제", "기기 설정에서 앱 데이터를 삭제하거나 앱을 제거하세요. Next Studio 서버에는 사용자 데이터가 없습니다."),
            ("문의할 때", "기기 종류, 운영체제 버전, 앱 버전과 문제를 재현하는 순서를 적어 보내 주세요."),
        ],
        "contact": "문의", "skip": "본문으로 이동", "choose": "언어 선택", "copyright": "© 2026 Next Studio · 넥스트 스튜디오",
    },
    "en": {
        "label": "English", "html": "en", "nav": ["Overview", "Privacy", "Support"],
        "tag": "A grid puzzle of animals", "intro": "Fill an animal-packed grid by following the rules. Play Classic and Duo modes with a step-by-step tutorial, hints, and a 30-animal collection.",
        "features": ["Step-by-step tutorial and rule hints", "Classic and Duo modes", "30-animal collection with unlocks"],
        "offline": "No account is needed and your progress stays on your device. Ads may be shown.",
        "privacy_title": "Animal Grid Privacy Policy", "date": "Effective November 25, 2026",
        "privacy_intro": "Animal Grid is a grid puzzle app provided by Next Studio. It is intended for users aged 13 and older and works without an account.",
        "privacy": [
            ("Information handled on your device", "Stage progress, tutorial progress, the animal collection and unlocks, and the language setting are stored only on your device."),
            ("Collection and sharing", "Next Studio does not collect this information or send it to its own servers. The app has no account, cloud sync, or analytics tool."),
            ("Ads and consent", "The app may show interstitial and rewarded ads through Google AdMob. Google and its ad partners may collect and use the advertising ID, IP address, device and app information, and ad interactions to serve and measure ads and prevent fraud, under Google's policies. In the European Economic Area, the UK and similar regions, the Google User Messaging Platform (UMP) asks for your consent, and you can change your choice in the app where available. You can reset your advertising ID or turn off ad personalization in device settings."),
            ("Age", "Animal Grid is intended for users aged 13 and older and does not knowingly collect personal information from children under 13."),
            ("Deletion", "Clear the app's data or uninstall the app to remove local records, subject to system backup and restore behavior."),
            ("Changes", "If this policy changes, the effective date on this page will be updated."),
        ],
        "support_title": "Animal Grid Help & Support", "support_intro": "Review these tips or email us if you need help using the app.",
        "support": [
            ("If your progress is gone", "Progress is stored only on your device, without an account. Clearing app data or uninstalling the app can remove it."),
            ("Ads and consent issues", "If ads do not appear or you want to see the consent message again, check the privacy options in the app settings where available. You can manage the advertising ID in device settings."),
            ("Delete data", "Clear the app's data in device settings or uninstall the app. Next Studio servers hold no user data."),
            ("When contacting us", "Include your device model, operating-system version, app version, and steps to reproduce the issue."),
        ],
        "contact": "Contact", "skip": "Skip to content", "choose": "Choose language", "copyright": "© 2026 Next Studio",
    },
    "ja": {
        "label": "日本語", "html": "ja", "nav": ["概要", "プライバシー", "サポート"],
        "tag": "動物を並べるグリッドパズル", "intro": "動物でいっぱいのマス目をルールに従って埋めるパズルです。クラシックとデュオの2モード、ステップ式チュートリアル、ヒント、30種類の動物図鑑があります。",
        "features": ["ステップ式チュートリアルとルール解説ヒント", "クラシック・デュオの2モード", "30種類の動物図鑑とアンロック"],
        "offline": "アカウントは不要で、進行状況は端末内に保存されます。広告が表示される場合があります。",
        "privacy_title": "Animal Grid プライバシーポリシー", "date": "施行日：2026年11月25日",
        "privacy_intro": "Animal GridはNext Studioが提供するグリッドパズルアプリです。13歳以上の方を対象とし、アカウントなしで利用できます。",
        "privacy": [
            ("端末内で扱う情報", "ステージの進行状況、チュートリアルの進行状況、動物図鑑とアンロック状況、言語設定は端末内だけに保存されます。"),
            ("収集と共有", "Next Studioはこれらの情報を収集せず、自社サーバーにも送信しません。アカウント、クラウド同期、分析ツールはありません。"),
            ("広告と同意", "本アプリはGoogle AdMobを通じてインタースティシャル広告とリワード広告を表示する場合があります。Googleと広告パートナーは、Googleのポリシーに従い、広告の配信・測定・不正防止のために広告ID、IPアドレス、端末・アプリ情報、広告の操作情報を収集・利用することがあります。欧州経済領域や英国などでは、Google User Messaging Platform（UMP）で同意を確認し、提供されている場合はアプリ内で選択を変更できます。広告IDのリセットや広告のパーソナライズ無効化は端末設定で行えます。"),
            ("年齢", "Animal Gridは13歳以上の方を対象としており、13歳未満の子どもの個人情報を意図的に収集しません。"),
            ("削除", "アプリのデータ消去またはアプリの削除で端末内の記録を削除できます。OSのバックアップ・復元の影響を受ける場合があります。"),
            ("変更", "方針を変更した場合は、このページの施行日を更新します。"),
        ],
        "support_title": "Animal Grid ヘルプとサポート", "support_intro": "問題がある場合は以下を確認するか、メールでお問い合わせください。",
        "support": [
            ("進行状況が消えた場合", "進行状況はアカウントなしで端末内にのみ保存されます。アプリのデータ消去やアプリの削除で失われることがあります。"),
            ("広告・同意の問題", "広告が表示されない場合や同意メッセージを再確認したい場合は、アプリ設定のプライバシーオプション（提供されている場合）をご確認ください。広告IDは端末設定で管理できます。"),
            ("データの削除", "端末設定でアプリのデータを消去するか、アプリを削除してください。Next Studioのサーバーにユーザーデータはありません。"),
            ("お問い合わせ", "端末、OS、アプリのバージョンと再現手順をお知らせください。")],
        "contact": "お問い合わせ", "skip": "本文へ移動", "choose": "言語を選択", "copyright": "© 2026 Next Studio",
    },
    "zh-hans": {
        "label": "简体中文", "html": "zh-Hans", "nav": ["简介", "隐私", "支持"],
        "tag": "把动物放进格子的网格谜题", "intro": "按照规则填满布满动物的网格。提供经典和双人模式、分步教程、提示以及30种动物图鉴。",
        "features": ["分步教程与规则提示", "经典与双人两种模式", "30种动物图鉴与解锁"],
        "offline": "无需账号，进度仅保存在设备上。可能会显示广告。",
        "privacy_title": "Animal Grid 隐私政策", "date": "生效日期：2026年11月25日",
        "privacy_intro": "Animal Grid是Next Studio提供的网格谜题应用，面向13岁及以上用户，无需账号即可使用。",
        "privacy": [
            ("设备上处理的信息", "关卡进度、教程进度、动物图鉴与解锁信息以及语言设置仅保存在设备上。"),
            ("收集与共享", "Next Studio不会收集这些信息，也不会发送到自己的服务器。应用不含账号、云同步或分析工具。"),
            ("广告与同意", "应用可能通过Google AdMob展示插页广告和激励广告。依据Google的政策，Google及其广告合作伙伴可能收集并使用广告ID、IP地址、设备与应用信息以及广告互动信息，用于投放和衡量广告及防止欺诈。在欧洲经济区、英国等地区，Google用户消息平台（UMP）会征求您的同意，并在提供时允许您在应用内更改选择。您可在设备设置中重置广告ID或关闭个性化广告。"),
            ("年龄", "Animal Grid面向13岁及以上用户，不会故意收集13岁以下儿童的个人信息。"),
            ("删除", "清除应用数据或卸载应用即可删除设备上的记录，但可能受系统备份与恢复影响。"),
            ("变更", "政策变更时将更新本页的生效日期。"),
        ],
        "support_title": "Animal Grid 帮助与支持", "support_intro": "如需帮助，请查看以下内容或发送电子邮件。",
        "support": [
            ("进度丢失时", "进度无需账号，仅保存在设备上。清除应用数据或卸载应用可能会删除进度。"),
            ("广告与同意问题", "如果没有显示广告，或想再次查看同意消息，请在应用设置中查看隐私选项（如有提供）。广告ID可在设备设置中管理。"),
            ("删除数据", "在设备设置中清除应用数据或卸载应用。Next Studio的服务器不保存用户数据。"),
            ("联系我们", "请提供设备型号、系统版本、应用版本和复现步骤。")],
        "contact": "联系", "skip": "跳到正文", "choose": "选择语言", "copyright": "© 2026 Next Studio",
    },
    "zh-hant": {
        "label": "繁體中文", "html": "zh-Hant", "nav": ["簡介", "隱私", "支援"],
        "tag": "把動物放進格子的網格謎題", "intro": "依照規則填滿布滿動物的網格。提供經典與雙人模式、分步教學、提示以及30種動物圖鑑。",
        "features": ["分步教學與規則提示", "經典與雙人兩種模式", "30種動物圖鑑與解鎖"],
        "offline": "無需帳號，進度僅儲存在裝置上。可能會顯示廣告。",
        "privacy_title": "Animal Grid 隱私權政策", "date": "生效日期：2026年11月25日",
        "privacy_intro": "Animal Grid是Next Studio提供的網格謎題應用程式，適用於13歲以上使用者，無需帳號即可使用。",
        "privacy": [
            ("裝置上處理的資訊", "關卡進度、教學進度、動物圖鑑與解鎖資訊以及語言設定僅儲存在裝置上。"),
            ("蒐集與分享", "Next Studio不會蒐集這些資訊，也不會傳送到自己的伺服器。應用程式沒有帳號、雲端同步或分析工具。"),
            ("廣告與同意", "應用程式可能透過Google AdMob顯示插頁式廣告與獎勵型廣告。依據Google的政策，Google及其廣告夥伴可能蒐集並使用廣告ID、IP位址、裝置與應用程式資訊以及廣告互動資訊，用於投放與衡量廣告及防止詐欺。在歐洲經濟區、英國等地區，Google使用者訊息平台（UMP）會徵求您的同意，並在提供時允許您於應用程式內變更選擇。您可在裝置設定中重設廣告ID或關閉個人化廣告。"),
            ("年齡", "Animal Grid適用於13歲以上使用者，不會故意蒐集13歲以下兒童的個人資料。"),
            ("刪除", "清除應用程式資料或解除安裝應用程式即可刪除裝置上的紀錄，但可能受系統備份與還原影響。"),
            ("變更", "政策變更時將更新本頁的生效日期。"),
        ],
        "support_title": "Animal Grid 說明與支援", "support_intro": "如需協助，請查看以下內容或寄送電子郵件。",
        "support": [
            ("進度遺失時", "進度無需帳號，僅儲存在裝置上。清除應用程式資料或解除安裝應用程式可能會刪除進度。"),
            ("廣告與同意問題", "若沒有顯示廣告，或想再次查看同意訊息，請在應用程式設定中查看隱私選項（若有提供）。廣告ID可在裝置設定中管理。"),
            ("刪除資料", "在裝置設定中清除應用程式資料或解除安裝應用程式。Next Studio的伺服器不保存使用者資料。"),
            ("聯絡我們", "請提供裝置型號、系統版本、應用程式版本與重現步驟。")],
        "contact": "聯絡", "skip": "跳到內容", "choose": "選擇語言", "copyright": "© 2026 Next Studio",
    },
    "es": {
        "label": "Español", "html": "es", "nav": ["Resumen", "Privacidad", "Soporte"],
        "tag": "Un rompecabezas de cuadrícula con animales", "intro": "Rellena una cuadrícula llena de animales siguiendo las reglas. Incluye los modos Clásico y Dúo, un tutorial paso a paso, pistas y una colección de 30 animales.",
        "features": ["Tutorial paso a paso y pistas de reglas", "Modos Clásico y Dúo", "Colección de 30 animales con desbloqueos"],
        "offline": "No necesitas cuenta y tu progreso se guarda solo en tu dispositivo. Puede haber anuncios.",
        "privacy_title": "Política de privacidad de Animal Grid", "date": "En vigor desde el 25 de noviembre de 2026",
        "privacy_intro": "Animal Grid es una aplicación de rompecabezas de cuadrícula ofrecida por Next Studio. Está dirigida a usuarios de 13 años o más y funciona sin cuenta.",
        "privacy": [
            ("Información tratada en tu dispositivo", "El progreso de los niveles, el progreso del tutorial, la colección de animales y los desbloqueos, y el ajuste de idioma se guardan solo en tu dispositivo."),
            ("Recopilación y uso compartido", "Next Studio no recopila esta información ni la envía a sus propios servidores. La aplicación no tiene cuentas, sincronización en la nube ni herramientas de análisis."),
            ("Anuncios y consentimiento", "La aplicación puede mostrar anuncios intersticiales y recompensados mediante Google AdMob. Según las políticas de Google, Google y sus socios publicitarios pueden recopilar y usar el ID de publicidad, la dirección IP, información del dispositivo y de la aplicación e interacciones con anuncios para mostrar y medir anuncios y prevenir el fraude. En el Espacio Económico Europeo, el Reino Unido y regiones similares, la Plataforma de mensajes de usuario (UMP) de Google solicita tu consentimiento y, cuando esté disponible, puedes cambiar tu elección en la aplicación. Puedes restablecer el ID de publicidad o desactivar la personalización de anuncios en los ajustes del dispositivo."),
            ("Edad", "Animal Grid está dirigida a usuarios de 13 años o más y no recopila a sabiendas datos personales de menores de 13 años."),
            ("Eliminación", "Borra los datos de la aplicación o desinstálala para eliminar los registros locales, según el comportamiento de copia de seguridad y restauración del sistema."),
            ("Cambios", "Si esta política cambia, se actualizará la fecha de entrada en vigor de esta página."),
        ],
        "support_title": "Ayuda y soporte de Animal Grid", "support_intro": "Consulta estos consejos o escríbenos si necesitas ayuda con la aplicación.",
        "support": [
            ("Si desaparece tu progreso", "El progreso se guarda solo en tu dispositivo, sin cuenta. Borrar los datos de la aplicación o desinstalarla puede eliminarlo."),
            ("Problemas con anuncios y consentimiento", "Si no aparecen anuncios o quieres volver a ver el mensaje de consentimiento, revisa las opciones de privacidad en los ajustes de la aplicación, cuando estén disponibles. El ID de publicidad se gestiona en los ajustes del dispositivo."),
            ("Eliminar datos", "Borra los datos de la aplicación en los ajustes del dispositivo o desinstálala. Los servidores de Next Studio no almacenan datos de usuarios."),
            ("Al contactarnos", "Indica el modelo del dispositivo, la versión del sistema operativo, la versión de la aplicación y los pasos para reproducir el problema.")],
        "contact": "Contacto", "skip": "Saltar al contenido", "choose": "Elegir idioma", "copyright": "© 2026 Next Studio",
    },
    "pt-br": {
        "label": "Português (Brasil)", "html": "pt-BR", "nav": ["Visão geral", "Privacidade", "Suporte"],
        "tag": "Um quebra-cabeça de grade com animais", "intro": "Preencha uma grade cheia de animais seguindo as regras. Tem os modos Clássico e Duo, tutorial passo a passo, dicas e uma coleção de 30 animais.",
        "features": ["Tutorial passo a passo e dicas de regras", "Modos Clássico e Duo", "Coleção de 30 animais com desbloqueios"],
        "offline": "Não é preciso conta e seu progresso fica apenas no dispositivo. Anúncios podem ser exibidos.",
        "privacy_title": "Política de Privacidade do Animal Grid", "date": "Em vigor desde 25 de novembro de 2026",
        "privacy_intro": "O Animal Grid é um app de quebra-cabeça de grade oferecido pela Next Studio. Destina-se a usuários com 13 anos ou mais e funciona sem conta.",
        "privacy": [
            ("Informações tratadas no dispositivo", "O progresso das fases, o progresso do tutorial, a coleção de animais e os desbloqueios, e a configuração de idioma ficam armazenados apenas no seu dispositivo."),
            ("Coleta e compartilhamento", "A Next Studio não coleta essas informações nem as envia aos seus próprios servidores. O app não tem conta, sincronização na nuvem nem ferramenta de análise."),
            ("Anúncios e consentimento", "O app pode exibir anúncios intersticiais e premiados pelo Google AdMob. Conforme as políticas do Google, o Google e seus parceiros de publicidade podem coletar e usar o ID de publicidade, o endereço IP, informações do dispositivo e do app e interações com anúncios para exibir e medir anúncios e prevenir fraudes. No Espaço Econômico Europeu, no Reino Unido e em regiões semelhantes, a Plataforma de Mensagens do Usuário (UMP) do Google solicita seu consentimento e, quando disponível, você pode alterar a escolha no app. Você pode redefinir o ID de publicidade ou desativar a personalização de anúncios nas configurações do dispositivo."),
            ("Idade", "O Animal Grid destina-se a usuários com 13 anos ou mais e não coleta intencionalmente dados pessoais de menores de 13 anos."),
            ("Exclusão", "Limpe os dados do app ou desinstale-o para remover os registros locais, sujeito ao comportamento de backup e restauração do sistema."),
            ("Alterações", "Se esta política mudar, a data de vigência desta página será atualizada."),
        ],
        "support_title": "Ajuda e suporte do Animal Grid", "support_intro": "Confira estas dicas ou envie um e-mail se precisar de ajuda com o app.",
        "support": [
            ("Se o progresso sumiu", "O progresso fica apenas no dispositivo, sem conta. Limpar os dados do app ou desinstalá-lo pode removê-lo."),
            ("Problemas com anúncios e consentimento", "Se os anúncios não aparecerem ou você quiser ver de novo a mensagem de consentimento, verifique as opções de privacidade nas configurações do app, quando disponíveis. O ID de publicidade é gerenciado nas configurações do dispositivo."),
            ("Excluir dados", "Limpe os dados do app nas configurações do dispositivo ou desinstale-o. Os servidores da Next Studio não guardam dados de usuários."),
            ("Ao entrar em contato", "Informe o modelo do dispositivo, a versão do sistema operacional, a versão do app e os passos para reproduzir o problema.")],
        "contact": "Contato", "skip": "Ir para o conteúdo", "choose": "Escolher idioma", "copyright": "© 2026 Next Studio",
    },
    "de": {
        "label": "Deutsch", "html": "de", "nav": ["Überblick", "Datenschutz", "Support"],
        "tag": "Ein Gitterrätsel mit Tieren", "intro": "Fülle ein Gitter voller Tiere nach den Regeln. Mit Klassik- und Duo-Modus, Schritt-für-Schritt-Tutorial, Hinweisen und einer Sammlung von 30 Tieren.",
        "features": ["Schritt-für-Schritt-Tutorial und Regelhinweise", "Klassik- und Duo-Modus", "Sammlung von 30 Tieren mit Freischaltungen"],
        "offline": "Kein Konto nötig, dein Fortschritt bleibt nur auf deinem Gerät. Es können Anzeigen erscheinen.",
        "privacy_title": "Datenschutzerklärung für Animal Grid", "date": "Gültig ab 25. November 2026",
        "privacy_intro": "Animal Grid ist eine Gitterrätsel-App von Next Studio. Sie richtet sich an Nutzer ab 13 Jahren und funktioniert ohne Konto.",
        "privacy": [
            ("Auf deinem Gerät verarbeitete Daten", "Level-Fortschritt, Tutorial-Fortschritt, Tiersammlung und Freischaltungen sowie die Spracheinstellung werden nur auf deinem Gerät gespeichert."),
            ("Erhebung und Weitergabe", "Next Studio erhebt diese Daten nicht und sendet sie nicht an eigene Server. Die App hat kein Konto, keine Cloud-Synchronisierung und kein Analysetool."),
            ("Anzeigen und Einwilligung", "Die App kann über Google AdMob Interstitial- und Prämienanzeigen zeigen. Gemäß den Richtlinien von Google können Google und seine Werbepartner die Werbe-ID, die IP-Adresse, Geräte- und App-Informationen sowie Anzeigeninteraktionen erfassen und nutzen, um Anzeigen auszuliefern, zu messen und Betrug zu verhindern. Im Europäischen Wirtschaftsraum, im Vereinigten Königreich und ähnlichen Regionen fragt die Google User Messaging Platform (UMP) deine Einwilligung ab; wo verfügbar, kannst du deine Auswahl in der App ändern. Die Werbe-ID kannst du in den Geräteeinstellungen zurücksetzen oder personalisierte Werbung deaktivieren."),
            ("Alter", "Animal Grid richtet sich an Nutzer ab 13 Jahren und erhebt nicht wissentlich personenbezogene Daten von Kindern unter 13 Jahren."),
            ("Löschung", "Lösche die App-Daten oder deinstalliere die App, um lokale Daten zu entfernen; Backup- und Wiederherstellungsfunktionen des Systems können dies beeinflussen."),
            ("Änderungen", "Ändert sich diese Erklärung, wird das Datum auf dieser Seite aktualisiert."),
        ],
        "support_title": "Hilfe und Support für Animal Grid", "support_intro": "Sieh dir diese Tipps an oder schreibe uns eine E-Mail, wenn du Hilfe brauchst.",
        "support": [
            ("Wenn dein Fortschritt weg ist", "Der Fortschritt wird ohne Konto nur auf deinem Gerät gespeichert. Das Löschen der App-Daten oder das Deinstallieren kann ihn entfernen."),
            ("Probleme mit Anzeigen und Einwilligung", "Erscheinen keine Anzeigen oder möchtest du die Einwilligungsmeldung erneut sehen, prüfe die Datenschutzoptionen in den App-Einstellungen, sofern verfügbar. Die Werbe-ID verwaltest du in den Geräteeinstellungen."),
            ("Daten löschen", "Lösche die App-Daten in den Geräteeinstellungen oder deinstalliere die App. Auf den Servern von Next Studio liegen keine Nutzerdaten."),
            ("Bei Kontakt", "Nenne Gerätemodell, Betriebssystemversion, App-Version und die Schritte zur Reproduktion des Problems.")],
        "contact": "Kontakt", "skip": "Zum Inhalt springen", "choose": "Sprache wählen", "copyright": "© 2026 Next Studio",
    },
}

STYLE = (ROOT / "style.css").read_text(encoding="utf-8")
KINDS = ("index", "privacy", "support")


def nav(data, current):
    return "".join(f'<a href="{kind}.html"' + (' aria-current="page"' if kind == current else "") + f'>{esc(data["nav"][i])}</a>' for i, kind in enumerate(KINDS))


def language_options(current, kind):
    return "".join(f'<option value="../{code}/{kind}.html"' + (' selected' if code == current else "") + f'>{esc(d["label"])}</option>' for code, d in LANGUAGES.items())


def alternates(kind):
    links = "\n".join(f'<link rel="alternate" hreflang="{d["html"]}" href="{SITE}/{code}/{kind}.html">' for code, d in LANGUAGES.items())
    return links + f'\n<link rel="alternate" hreflang="x-default" href="{SITE}/en/{kind}.html">'


def page(code, kind, data):
    if kind == "index":
        title = NAME
        content = f'<p class="muted">PUZZLE · ANIMALS · GRID</p><h1>{esc(data["tag"])}</h1><p class="lead">{esc(data["intro"])}</p><ul class="features">' + "".join(f'<li>{esc(i)}</li>' for i in data["features"]) + f'</ul><p class="lead">{esc(data["offline"])}</p><div class="cards"><a class="card" href="privacy.html">{esc(data["nav"][1])} →</a><a class="card" href="support.html">{esc(data["nav"][2])} →</a></div>'
    else:
        title = data[f"{kind}_title"]
        content = f'<h1>{esc(title)}</h1>' + (f'<p class="date">{esc(data["date"])}</p>' if kind == "privacy" else "") + f'<p class="lead">{esc(data[f"{kind}_intro"])}</p>'
        content += "".join(f'<section><h2>{i}. {esc(h)}</h2><p>{esc(t)}</p></section>' for i, (h, t) in enumerate(data[kind], 1))
        subject = "Animal%20Grid%20" + ("Privacy" if kind == "privacy" else "Support")
        content += f'<aside class="contact"><h2>{esc(data["contact"])}</h2><p>Next Studio · 넥스트 스튜디오<br><a href="mailto:{EMAIL}?subject={subject}">{EMAIL}</a></p></aside>'
    return f'''<!doctype html>
<html lang="{data['html']}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="description" content="{NAME} · {esc(title)} · Next Studio"><title>{NAME} · {esc(title)}</title>
<link rel="stylesheet" href="../style.css"><link rel="icon" href="../icon.png"><link rel="canonical" href="{SITE}/{code}/{kind}.html">
{alternates(kind)}</head><body><a class="skip" href="#content">{esc(data['skip'])}</a><main>
<header class="top"><a class="brand" href="index.html"><img src="../icon.png" width="42" height="42" alt=""> {NAME}</a><label><span class="skip">{esc(data['choose'])}</span><select class="language" aria-label="{esc(data['choose'])}" onchange="location.href=this.value">{language_options(code, kind)}</select></label></header>
<nav aria-label="{NAME}">{nav(data, kind)}</nav><article id="content">{content}</article><footer>{esc(data['copyright'])}<br><a href="mailto:{EMAIL}">{EMAIL}</a></footer></main></body></html>'''


for locale, strings in LANGUAGES.items():
    destination = ROOT / locale
    destination.mkdir(exist_ok=True)
    for kind in KINDS:
        (destination / f"{kind}.html").write_text(page(locale, kind, strings), encoding="utf-8")

links = "".join(f'<a class="card" href="{code}/index.html" hreflang="{d["html"]}">{esc(d["label"])}</a>' for code, d in LANGUAGES.items())
(ROOT / "index.html").write_text(f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="{NAME} official website"><title>{NAME} · Next Studio</title><link rel="stylesheet" href="style.css"><link rel="icon" href="icon.png"></head><body><main><header class="top"><span class="brand"><img src="icon.png" width="42" height="42" alt=""> {NAME}</span></header><article><p class="muted">PUZZLE · ANIMALS · GRID</p><h1>A grid puzzle of animals</h1><p class="lead">Choose your language.</p><div class="cards languages">{links}</div></article><footer>© 2026 Next Studio · 넥스트 스튜디오</footer></main></body></html>''', encoding="utf-8")
print(f"Generated {len(LANGUAGES) * len(KINDS) + 1} pages.")
