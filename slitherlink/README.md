# Slitherlink policies

운영자: 넥스트 스튜디오 / Next Studio
문의: dhalska2@gmail.com
앱: `com.osj.slitherlink`
작성 기준: 2026-09-16 앱 구현 (광고·계정·서버 게임 진행 저장·분석 SDK·푸시 없음, iOS 구매 검증·환불 서버 연결, 실기기 검증은 진행 전).

## 공개 주소

- 한국어 홈: https://oh-seungjin.github.io/privacy-terms/slitherlink/
- 글로벌 안내: https://oh-seungjin.github.io/privacy-terms/slitherlink/index-en.html
- App Store Privacy Policy URL: https://oh-seungjin.github.io/privacy-terms/slitherlink/privacy-en.html
- Support URL: https://oh-seungjin.github.io/privacy-terms/slitherlink/support-en.html
- Terms URL: https://oh-seungjin.github.io/privacy-terms/slitherlink/terms-en.html
- Data Deletion URL: https://oh-seungjin.github.io/privacy-terms/slitherlink/delete-account-en.html

`privacy.html` 등 접미사 없는 파일은 한국어. 영어 `-en`, 일본어 `-ja`, 중국어 간체 `-zh-hans`, 스페인어 `-es`, 프랑스어 `-fr`, 독일어 `-de`, 브라질 포르투갈어 `-pt-br`.
각 언어에 홈·개인정보·약관·지원·삭제 페이지가 있으며 언어를 바꾸어도 현재 문서 종류를 유지한다. 언어 선택은 해당 언어의 정적 파일로 이동한다. 스크립트가 꺼져도 각 문서 전문과 언어 링크를 이용할 수 있다. 광고, 분석, 입력 폼, 쿠키를 추가하지 않는다.

## 유지보수

`translations.json`을 수정한 뒤 `python generate_pages.py`를 실행한다. iOS 구매 거래·환불 기록은 Supabase에서 처리하고 서버 검증 후 최대 24시간 오프라인 권한을 제공한다. 원본 영수증은 서버 DB에 저장하지 않는다. Android·웹 결제는 미지원이다. App Store 개인정보 표시도 실제 거래 데이터 처리에 맞춰 갱신한다.

문서 레이아웃·언어 선택·개별 언어 파일명은 기존 sudoku/nonogram 폴더를 기준으로 구성했다.
검토 자료: Apple App Review Guidelines 5.1.1, App Store Connect의 Manage app privacy, GitHub General Privacy Statement. 번역 지원은 특정 국가의 모든 배포 요건을 충족했다는 인증을 뜻하지 않는다.
