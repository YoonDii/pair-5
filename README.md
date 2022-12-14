# pair-5(음악리뷰게시판-배포까지)
https://halloweenk2y.herokuapp.com/
## 참여자

- 윤혜진 [깃허브](https://github.com/hyejinny97)
- 김병우 [깃허브](https://github.com/BuildEnough)
- 김윤지 [깃허브](https://github.com/YoonDii)

## 목표

페어 프로그래밍을 통한 영화 리뷰 커뮤니티 서비스를 개발

- **CRUD** 구현(구현 방법 제한 없음)
- **Staticfiles** 활용 정적 파일(이미지, CSS, JS) 다루기
- Django **Auth** 활용 회원 관리(회원 가입 / 회원 조회 / 로그인 / 로그아웃)
- Media 활용 동적 파일 다루기
- 모델간 **1 : N / M : N 관계** 매핑

## 구현기능

### 기능 View

**> 리뷰 reviews**

데이터 목록 조회

데이터 정보 조회

데이터 생성

데이터 수정

데이터 삭제

리뷰 좋아요 / 좋아요 취소

**> 댓글 comments**

리뷰의 댓글 목록 조회

댓글 생성

댓글 삭제

**> 회원 관리 accounts**

회원 가입

회원 목록 조회

회원 정보 조회

로그인

로그아웃

팔로우

### 화면 Template

**> 네비게이션바, Bootstrap <nav>**

- 서비스 로고
- 리뷰 목록 페이지 이동 버튼
- 리뷰 작성 페이지 이동 버튼
- 로그인 상태에 따라 다른 화면을 출력합니다.
  1. 로그인 상태
     - 로그인한 사용자의 username
     - 로그아웃 버튼
  2. 비 로그인 상태
     - 로그인 페이지 이동 버튼
     - 회원 가입 페이지 이동 버튼

**> 메인 페이지**

**> 목록 페이지**

**> 리뷰 정보 페이지**

**>리뷰 작성 페이지**

**> 리뷰 수정 페이지**

**> 회원 가입 페이지**

**> 회원 조회 페이지(프로필 페이지)**

**> 로그인 페이지**

**> 팔로우 버튼**
