# [✈ 누런풍선](https://pacific-reaches-80736.herokuapp.com/)
### 여행 상품 소개 및 리뷰 커뮤니티 서비스
> 여행을 준비하는 사람들에게 설레임과 밝은 기운을 전달하고 싶은 서비스 Golden Balloon
<br>

## 업무분담
* `백솔비`: 프론트엔드

* `임수경`: 프론트엔드

* `이동현`: 백엔드

* `김예린`: 백엔드, 팀장
<br>

## 사용 기술 및 개발 계획
* Django, HTML, CSS

* `협업 Tool`: Figma, Notion, Discord, GitHub

* `2022.10.31 ~ 2022.11.07`
<br>

## DB 모델링
![ERD](./readme.assets/%EB%88%84%EB%9F%B0%ED%92%8D%EC%84%A0%20ERD.png)
<br>

## 핵심기능

<br>

#### 1. 여행 상품 소개 
* selenium, BeautifulSoup을 이용하여 마이리얼트립의 여행 상품 제목과 이미지 크롤링 및 템플릿에 출력

* Tab menu 구현, carousel 구현

*  위시리스트 기능 구현

<br>

#### 2. 리뷰 작성 커뮤니티 및 공지사항
* 게시글 CRUD 구현
    * 게시글 좋아요 / 평점 / 이미지 업로드 / 댓글 생성 및 수정 / 작성 시간 및 수정 시간 
        * 이미지 클릭 시 사진 확대 기능 구현 

* 사용자가 작성한 제목, 내용을 기반으로 검색 기능 구현

<br>

#### 3. 유저 프로필 
* 회원가입 및 로그인

* 유저 정보 업데이트 

* 프로필 이미지 업로드 및 수정

* 사용자간의 팔로우

* 위시리스트 목록 출력

* 팔로우 및 팔로잉 목록 출력 
<br>


---


🟡 좋은 서비스를 만들기 위해 저희는 세세한 부분까지도 자세하고 빈틈없이 꼼꼼하게 기능을 구현하고자 결정했습니다. 
서비스의 시스템을 개발 구현 시 만약 내가 사용자라면 어떤 내용이 들어가면 더 좋을까라는 고민을 하며 개발했습니다. 또한 프로젝트 기간동안 최대한 기획한 대로 구현하고자 노력했습니다.

![image](https://user-images.githubusercontent.com/99783474/203452713-f515477b-521c-44f1-bb8a-3204c0bbbd70.png)


벡엔드 개발 담당은 2명, 프론트엔드 개발 담당은 총 2명으로 역할 분담을 나눠 진행했습니다. 그리고 자신의 업무 담당이 일찍 끝났을 경우 다른 담당자와 함께 프로젝트를 마치기 위해 서로 도와가며 진행했습니다. 저희 팀이 구현하고자 하는 화면과 데이터가 제대로 기능이 연결이 되지 않을 경우 그때마다 데이터 수정 및 레이아웃 수정을 진행했습니다.

---


### 🟡 "누런풍선" 팀 전체적인 프로세스 : 기획부터 개발까지

![image](https://user-images.githubusercontent.com/99783474/203452763-18104734-de31-46ca-a48f-ec09738995e3.png)



### ✈ 여행 서비스를 선택한 이유

많고 많은 주제들 중에 우리 팀이 선택한 주제는 "여행" 이라는 주제였습니다.. 다들 왜? 라는 질문 없이뭐든 해도 좋다, 다 잘 할 수 있을 것 같다 라는 마음으로 자신감 있게 출발한 이유이기도 했습니다. 여행이라는 단어는 많은 이들을 설레게 해주는 단어인 것 같습니다. 동시에 어떤 것을 준비해야 할지 모르는 이들에게 어떻게 하면 우리 서비스가 잘 보여줄 수 있을까 라는 고민과 함께 관련 여행 서비스를 벤치 마킹을 했습니다. 벤치 마킹을 한 서비스는 총 마이 리얼 트립, airbnb, 트립어드바이저, 스투비 플래너를 살펴보았습니다. 그중에도 우리 팀이 가장 맘에 들었던 마이 리얼 트립 서비스를 통해 다음과 같이 분석하고 계획했습니다.

◼ [My Real Trip](https://www.myrealtrip.com/)

![image](https://user-images.githubusercontent.com/99783474/203452879-62da673c-596b-477a-84c1-b6b56b86fee9.png)

---

### 💡 서비스마다 컨셉이 있는 것 같아요 그렇다면 우리는 색감으로 중심을 잡아갈까요?

