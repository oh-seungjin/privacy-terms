# Chess 정책 및 지원 페이지

- 운영자: 넥스트 스튜디오 / Next Studio (대한민국)
- 문의·삭제 요청: dhalska2@gmail.com
- 앱 식별자: `com.osj.chess`
- 기준일: 2026-09-29

Hashi/Slitherlink와 같은 정적 페이지 구조로 홈(마케팅), 개인정보처리방침, 이용약관, 지원, 데이터 삭제 안내를 제공합니다. **언어 목록은 플레이북 기본 8개 언어가 아니라 Chess 앱이 실제 지원하는 10개 언어**(`lib/l10n/app_*.arb` 기준: ko/en/de/es/fr/hi/id/pt/ru/tr)를 그대로 따릅니다.

앱의 실제 구현 상태를 반영했습니다: 익명 로그인 기본 + Apple 로그인(선택, 이메일 공유), 실제 인앱결제/구독(Apple 결제, 서버는 상태만 확인), 온라인 랭크 대전/친구 초대(Supabase), Apple 로그인 시 전적·업적·퍼즐 기록 등 진행상황 서버 동기화, AdMob 광고, 코치 음성 해설(기기 내 TTS만 사용, 녹음/전송 없음). Firebase는 사용하지 않습니다. 계정 삭제는 아직 앱 내 버튼이 없어 이메일 요청 방식입니다.

## 스토어 입력용 기본 URL

- 마케팅: https://oh-seungjin.github.io/privacy-terms/chess/
- 개인정보: https://oh-seungjin.github.io/privacy-terms/chess/privacy.html
- 이용약관: https://oh-seungjin.github.io/privacy-terms/chess/terms.html
- 지원: https://oh-seungjin.github.io/privacy-terms/chess/support.html
- 삭제 요청 안내: https://oh-seungjin.github.io/privacy-terms/chess/delete-account.html

## 언어별 개인정보 URL

| 언어 | URL |
|---|---|
| 한국어 | https://oh-seungjin.github.io/privacy-terms/chess/privacy.html |
| 영어 | https://oh-seungjin.github.io/privacy-terms/chess/privacy-en.html |
| 독일어 | https://oh-seungjin.github.io/privacy-terms/chess/privacy-de.html |
| 스페인어 | https://oh-seungjin.github.io/privacy-terms/chess/privacy-es.html |
| 프랑스어 | https://oh-seungjin.github.io/privacy-terms/chess/privacy-fr.html |
| 힌디어 | https://oh-seungjin.github.io/privacy-terms/chess/privacy-hi.html |
| 인도네시아어 | https://oh-seungjin.github.io/privacy-terms/chess/privacy-id.html |
| 포르투갈어 | https://oh-seungjin.github.io/privacy-terms/chess/privacy-pt.html |
| 러시아어 | https://oh-seungjin.github.io/privacy-terms/chess/privacy-ru.html |
| 튀르키예어 | https://oh-seungjin.github.io/privacy-terms/chess/privacy-tr.html |

다른 문서는 위 URL의 `privacy`를 `index`, `terms`, `support`, `delete-account`로 변경합니다. 언어 선택은 현재 문서 종류를 유지하며, JavaScript가 꺼져도 전문과 언어별 링크를 이용할 수 있습니다.

## 앱 UI 문구와의 용어 통일

마케팅 페이지의 기능 목록(`translations.json`의 `features`)은 앱 내 `AppLocalizations` 문구(`analysisBoard`, `lessons`, `drillsSectionTitle`, `puzzleRushNav`, `openingExplorerTitle`, `storeSubscriptionSectionTitle`)와 언어별로 직접 대조해 맞췄습니다. 특히:
- `Puzzle Rush`는 앱이 실제로 번역하지 않는 언어(de/es/fr/pt/ru/tr/id)에서는 라틴 문자 그대로 두고, 힌디어는 앱과 동일하게 음역(`पज़ल रश`)을 썼습니다.
- 힌디어 구독 용어는 앱과 동일한 `प्रीमियम सदस्यता`(초안에서 쓰던 `सब्सक्रिप्शन`을 앱 표기에 맞게 교체).
- 러시아어/튀르키예어/인도네시아어 오프닝 익스플로러 명칭을 앱의 `Обозреватель дебютов`/`Açılış Gezgini`/`Penjelajah Pembukaan`에 맞춰 교체.
- **분석 보드**(Analysis Board)는 이전 스토어 문안 초안에는 빠져 있었는데, 실제로는 자체 제한(하루 3회, 구독 시 무제한)이 있는 독립 기능이라 마케팅 페이지 기능 목록에 별도 항목으로 추가했습니다.

## 유지보수와 출시 시 갱신

`translations.json` 수정 후 `python generate_pages.py`로 50개 HTML을 재생성합니다. 앱의 실제 아이콘(`assets/branding/icon-master.png`)을 축소해 사용했습니다.

- 온라인 대전(랭크 매칭 + 친구 초대), 구매/구독, 진행상황 동기화는 **실제로 켜져 있는 기능**입니다(게임 저장소 `game-launch-playbook/games/chess/launch.md` 기준). 서버 킬 스위치로 랜덤 매칭을 다시 끄게 되면 이 페이지들의 관련 문구도 갱신해야 합니다.
- 앱 내 계정 삭제 버튼은 아직 없습니다. 이메일 삭제 안내를 게시한 것만으로 앱 내 계정 삭제 구현이 완료되지는 않습니다 — 구현 시 이 페이지도 갱신합니다.
- 서버 삭제 요청은 Chess 범위로 처리하고, 공유 서버의 다른 게임 계정·기록에 영향을 주기 전에 범위를 확인합니다.
- 스토어 개인정보 응답(App Privacy)은 배포할 SDK·동의 설정·활성 기능 기준으로 별도 작성해야 합니다.

## 검토 자료

- [AdMob iOS 데이터 공개](https://developers.google.com/admob/ios/privacy/data-disclosure)
- [Google 개인정보처리방침](https://policies.google.com/privacy)
- [Apple 개인정보](https://www.apple.com/legal/privacy/)
- [Apple 심사 지침 — 개인정보](https://developer.apple.com/app-store/review/guidelines/#privacy)
- [Supabase 개인정보](https://supabase.com/privacy)

제공업체 링크는 각 개인정보 페이지에도 있습니다. 번역 제공 자체가 모든 국가의 법적 요건 충족을 인증하지는 않습니다.
