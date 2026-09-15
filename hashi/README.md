# Hashi 정책 및 지원 페이지

- 운영자: 넥스트 스튜디오 / Next Studio (대한민국)
- 문의·삭제 요청: dhalska2@gmail.com
- 앱 식별자: `com.osj.hashi`
- 기준일: 2026-09-15

기존 Slitherlink와 같은 정적 페이지 구조로 홈(마케팅), 개인정보처리방침, 이용약관, 지원, 데이터 삭제 안내를 8개 언어로 제공합니다. 모바일 AdMob·선택형 FCM과 현재 비활성화된 계정·구매의 실제 구현 상태를 구분했습니다. 별도의 광고·분석 스크립트나 제출 폼을 이 웹사이트에 추가하지 않았습니다.

## 스토어 입력용 기본 URL

- 마케팅: https://oh-seungjin.github.io/privacy-terms/hashi/
- 개인정보: https://oh-seungjin.github.io/privacy-terms/hashi/privacy.html
- 이용약관: https://oh-seungjin.github.io/privacy-terms/hashi/terms.html
- 지원: https://oh-seungjin.github.io/privacy-terms/hashi/support.html
- 삭제 요청 안내: https://oh-seungjin.github.io/privacy-terms/hashi/delete-account.html

## 언어별 개인정보 URL

| 언어 | URL |
|---|---|
| 한국어 | https://oh-seungjin.github.io/privacy-terms/hashi/privacy.html |
| 영어 | https://oh-seungjin.github.io/privacy-terms/hashi/privacy-en.html |
| 일본어 | https://oh-seungjin.github.io/privacy-terms/hashi/privacy-ja.html |
| 중국어 간체 | https://oh-seungjin.github.io/privacy-terms/hashi/privacy-zh-hans.html |
| 스페인어 | https://oh-seungjin.github.io/privacy-terms/hashi/privacy-es.html |
| 프랑스어 | https://oh-seungjin.github.io/privacy-terms/hashi/privacy-fr.html |
| 독일어 | https://oh-seungjin.github.io/privacy-terms/hashi/privacy-de.html |
| 포르투갈어(브라질) | https://oh-seungjin.github.io/privacy-terms/hashi/privacy-pt-br.html |

다른 문서는 위 URL의 `privacy`를 `index`, `terms`, `support`, `delete-account`로 변경합니다. 언어 선택은 현재 문서 종류를 유지하며, JavaScript가 꺼져도 전문과 언어별 링크를 이용할 수 있습니다.

## 유지보수와 출시 시 갱신

`translations.json` 수정 후 `python generate_pages.py`로 40개 HTML을 재생성합니다. 앱의 실제 아이콘을 사용했습니다.

- 현재 로그인·실제 결제와 자동 푸시 발송은 비활성화되어 있다는 안내가 포함됩니다. 활성화 시 모든 언어의 해당 문구를 갱신합니다.
- 앱 내 계정 삭제는 미구현입니다. 이메일 삭제 안내를 게시한 것만으로 앱 내 계정 삭제 구현이 완료되지는 않습니다. 계정 기능 공개 전에 이를 구현하고 안내도 갱신합니다.
- 서버 삭제 요청은 Hashi 범위로 처리하고, 공유 서버의 다른 게임 계정·기록에 영향을 주기 전에 범위를 확인합니다. 서버 보유 기간·국외 이전의 구체적인 운영 조건은 실제 제공업체 계약 및 배포 설정과 함께 관리합니다.
- 스토어 개인정보 응답은 배포할 SDK·동의 설정·활성 기능 기준으로 별도 작성해야 합니다. 이 앱에 '데이터 수집 없음'을 그대로 선택하지 않습니다.

## 검토 자료

- [AdMob 데이터 공개](https://developers.google.com/admob/android/privacy/play-data-disclosure)
- [Google UMP](https://developers.google.com/admob/flutter/privacy)
- [Firebase 개인정보 및 보안](https://firebase.google.com/support/privacy)
- [Supabase 개인정보](https://supabase.com/privacy)
- [Apple 심사 지침](https://developer.apple.com/app-store/review/guidelines/#privacy)

제공업체 링크는 각 개인정보 페이지에도 있습니다. 번역 제공 자체가 모든 국가의 법적 요건 충족을 인증하지는 않습니다.
