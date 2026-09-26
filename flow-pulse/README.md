# StreamLine Pulse (Flow Pulse) 정책 및 지원 페이지

- 운영자: 넥스트 스튜디오 / Next Studio (대한민국)
- 문의·삭제 요청: dhalska2@gmail.com
- 앱 식별자: `com.osj.flowpulse` (스토어 표시 이름: StreamLine Pulse)
- 기준일: 2026-09-26

앱이 영어·한국어 2개 언어만 지원하기로 확정돼서(플레이북 `games/flow-pulse/intake.md` 참고),
다른 게임들의 8개 언어 대신 **한국어·영어 2개 언어**로만 홈(마케팅), 개인정보처리방침, 이용약관,
지원, 데이터 삭제 안내 정적 페이지를 제공한다. 실제 앱 구현(Supabase 익명 로그인 기본, AdMob
전면·보상형 광고, iOS StoreKit 인앱결제, Firebase·푸시 없음)과 내용을 맞췄다.

## 스토어 입력용 기본 URL

- 마케팅: https://oh-seungjin.github.io/privacy-terms/flow-pulse/
- 개인정보: https://oh-seungjin.github.io/privacy-terms/flow-pulse/privacy.html
- 이용약관: https://oh-seungjin.github.io/privacy-terms/flow-pulse/terms.html
- 지원: https://oh-seungjin.github.io/privacy-terms/flow-pulse/support.html
- 삭제 요청 안내: https://oh-seungjin.github.io/privacy-terms/flow-pulse/delete-account.html

## 언어별 개인정보 URL

| 언어 | URL |
|---|---|
| 한국어 | https://oh-seungjin.github.io/privacy-terms/flow-pulse/privacy.html |
| 영어 | https://oh-seungjin.github.io/privacy-terms/flow-pulse/privacy-en.html |

다른 문서는 위 URL의 `privacy`를 `index`, `terms`, `support`, `delete-account`로 변경한다.
언어 선택은 현재 문서 종류를 유지하며, JavaScript가 꺼져도 `<noscript>` 언어별 링크를 이용할 수
있다.

## 유지보수와 출시 시 갱신

`translations.json` 수정 후 `python3 generate_pages.py`로 10개 HTML을 재생성한다. 앱의 실제
아이콘(`flow-pulse/assets/branding/icon-master.svg`에서 내보낸 PNG)을 사용했다.

- 이 게임은 Firebase/FCM 푸시 알림을 전혀 쓰지 않는다(빌드 실패 문제로 2026-09-26에 완전히
  제거함). 나중에 푸시를 추가하면 개인정보처리방침에 그 사실을 반영해야 한다.
- 인앱 구매는 현재 iOS에서만 지원된다(`PurchaseService.supported`가 iOS 전용). Android 구매를
  지원하게 되면 이용약관·개인정보처리방침의 관련 문구를 갱신한다.
- 앱 내 계정 삭제(`AppBackend.deleteGameData`, 공용 `delete-account` Edge Function)가 실제로
  구현돼 있다 — 이메일 요청만 가능하다고 쓰지 않았다.
- 언어 지원 범위(현재 en/ko만)가 바뀌면 `generate_pages.py`의 `LANGS`와 `translations.json`을
  함께 갱신한다.
- 스토어 개인정보 응답은 배포할 SDK·동의 설정·활성 기능 기준으로 별도 작성해야 한다. 이 앱에
  '데이터 수집 없음'을 그대로 선택하지 않는다.

## 검토 자료

- [AdMob 데이터 공개](https://developers.google.com/admob/android/privacy/play-data-disclosure)
- [Google UMP](https://developers.google.com/admob/flutter/privacy)
- [Supabase 개인정보](https://supabase.com/privacy)
- [Apple 심사 지침](https://developer.apple.com/app-store/review/guidelines/#privacy)

제공업체 링크는 개인정보 페이지에도 있다. 번역 제공 자체가 모든 국가의 법적 요건 충족을
인증하지는 않는다.
