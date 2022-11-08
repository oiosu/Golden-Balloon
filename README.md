# 🟡 누런풍선
### 여행 상품 소개 및 리뷰 커뮤니티 서비스
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

### Figma 화면 설계
![1](./readme.assets/1.png)
![2](./readme.assets/2.png)
![3](./readme.assets/3.png)
![4](./readme.assets/4.png)
![5](./readme.assets/5.png)
![6](./readme.assets/6.png)
![7](./readme.assets/7.png)

---

### Keep 
> 🎉 프로젝트를 진행하며 만족스러웠던, 성취감을 느꼈던 부분을 작성한 부분입니다. 

- 팀원 모두 소통하는 자세와 의견을 수용하는 자세로 프로젝트에 임하여 각자의 역할 분담과 이에 맞는 기능 구현을 원활하게 진행할 수 있었습니다.
- 노션을 통해 각자 어제 한 일, 오늘 할 일을 적어 각 팀원들의 업무를 가시성 높게 확인할 수 있어 프로젝트 진행이 수월하였습니다.
- 전체적인 프로세스를 처음부터 끝까지 진행할 수 있어 좋았습니다. 칸반보드나 스크럼 등 커뮤니케이션에 도움이 되는 여러 방법을 사용하면서 더 적극적으로 참여할 수 있었습니다.
- 화면 디자인 부터 기능 설계까지 계획하면서 개발을 구현하는 과정을 통해 프로젝트를 완성하기 까지 시간 분배와 기능 구현을 할 수 있었던 것 같습니다.
- 팀 분위기가 너무 좋았어서.. 저 스스로 나름 120%의 힘을 쥐어 짜낼수 있었지 않았나.. 생각해봅니다

### Problem
> 🤔 프로젝트를 진행하며 마주한 문제점이나 아쉬운 점을 작성한 부분입니다. 

- 더 많은 기능 구현을 하고 싶었지만 시간이 짧아 아쉬웠습니다.
- JS을 더 적극적으로 활용하면서 사용자들이 더 매끄럽게 서비스를 사용할 수 있도록 프론트에서의 화면 기능을 더 구현해 보고 싶었지만 시간이 짧아 아쉬웠습니다.
- 몇번 브랜치를 만드는 것을 깜박해서 master에 바로 올리는 실수를 하였습니다. 기능을 구현하기 전 신중하게 과정을 생각하는 습관을 길러야겠습니다.
- 저 스스로의 실력적 한계를 적나라하게 볼 수 있었던 시간이었습니다. 이전에 조금 더 열심히 배웠다면, 조금 더 체력이 좋았다면 등등..더 좋은 결과를 만들어내지 못한 저 스스로에게 좀 많이 아쉬웠습니다.

### Try 
> 🛠 앞서 정의한 Problem을 해결하기 위한 시도와, 별도 시도가 없었다면 어떠한 시도를 하면 좋을지 작성한 부분입니다. 

- 프로젝트 진행 시 규칙을 더욱 세부적으로 정한다면 앞으로 업무 진행에 있어 실수하는 부분 없이 진행될 것 같습니다.
- 기능을 구현하기 전 디스코드에 브랜치 생성 보고하는 시도를 하였습니다.
- 기능 구현을 위해 효율적으로 진행하도록 시간 분배의 필요성을 느꼈습니다.
- CSS와 장고와의 연결이 되지 않아 처음에 많이 당황스러웠지만 검색을 통해 쿠기 삭제 설정과 팀원들과 CSS LINK 연결 태그를 하나씩 살펴보며 해결해 나갈 수 있었습니다.
- 부족한 부분에 대해서 추가 공부를 조금 더 해야겠네요.. JS도 그렇고.. DB도 그렇고.. 특히 비동기부분은 다시 꼭 봐야겠구나라고 생각하였습니다.

### Others

- 자기 역할 뿐만 아니라 자기 몫보다 더 넘치게 열정적으로 프로젝트에 임하셔서 처음으로 제대로된 프로젝트를 경험할 수 있었습니다. 소통 뿐만 아니라 프로젝트에 참여하는 자세를 배울 수 있어서 정말 정말 귀한 경험이었다고 생각합니다! 우리 팀원들을 최종 프젝에서 만났어야 했는데,,,, 백엔드 기능 담담자로서, 팀장으로서 훌륭한 팀원들에 비해 부족한 실력이었다고 생각합니다. 그래도 다들 감싸주셔서 정말 감사하구 더 오래오래 봤음 좋겠습니다!!!!
- 다들 적극적으로 참여해주어서 보다 완성도 있는 프로젝트를 완성했다고 생각합니다. 좋은 팀원들을 만났는데 하필 제일 짧은 프로젝트라 너무 아쉽습니다 ㅠㅠㅠ 시간만 더 있었다면 부족한 부분을 더 채울 수 있었을텐데 그러지 못한 것 또한 아쉽습니다.
- 팀원 모두 정해진 기간동안 적극적으로 프로젝트에 참여해주셔서 많은 것들을 배울 수 있는 시간이였고 힘낼 수 있었습니다. 최종때도 정말 만나서 또 완성도 있는 프로젝트 같이 만들어 가고 싶습니다!!!
- 부족한 저를 많이 다독여주시고 힘내게 해주셔서 너무 감사한 시간이었고.. 오늘 다른분들의 작품을 보면서 아 내가 저기있었으면 나도 저 정도 수준이었을텐데..라고 생각하며, 저희 팀원분들을 만나 제가 참여했다라고 말을 할 수 있는 결과물중 가장 훌륭하고 멋진 결과물을 만들수 있었구나..라고 생각합니다. 정말 너무 감사합니다 모두






