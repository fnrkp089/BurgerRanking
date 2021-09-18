# 미니 프로젝트 <BurgerRanking>
  
# Team
  이병관, 김효진, 박상수, 오성현
  
# Stack
  * Python
  * Flask
  * MongoDB
  * JWT
  * Html, css, Jquery
  
  # What is BurgerRanking
  > 당신의 버거는 어떤 버거인가요? 그리고 다른 사람들이 좋아하는 버거는 무엇일까요?
  
  # Wire Frame
  ![](https://images.velog.io/images/fnrkp089/post/a24e0b89-b9e9-41a5-ba09-15bcb8a2f9f2/KakaoTalk_20210913_145859026.jpg)
  
  ## 💡필요한 API
  
  > **회원가입 api**  
  <span style="color:olivedrab">POST</span>  
  **URL :**  /register  
  **request :** {'id':id, 'password':password, 'name':name}  
  **response :** '회원가입 완료 메세지'  

  > **로그인 api**  
  <span style="color:olivedrab">POST</span>  
  **URL :** /login  
  **request :** {'id':id, 'password':password}  
  **response :** '로그인 완료/실패메세지'  

  > **버거조회 api**  
  **<span style="color:indianred">GET</span>**  
  **URL :** /mainpage  
  **request : ** {'burger_id':burger_id ,'name':name, 'like':like, 'dislike': dislike, 'status':status}  
  **response :** '버거에 대한 상세 정보 리스트 표시'  

  > **리뷰작성 api**  
  **<span style="color:olivedrab">POST</span>**  
  **URL :**/comment  
  **request :**{'burger_id':burger_id, 'user':user', 'comment':comment}  
  **response :** '로그인 한 유저만 리뷰 작성'  
  
  > **리뷰삭제 api**  
  **<span style="color:olivedrab">POST</span>**  
  **URL :**/comment_delete  
  **request :**{'burger_id':burger_id, 'comment_id':comment_id', 'user':user}  
  **response :** '해당 리뷰 작성자일경우에만 삭제'  

  >**좋아요 api**  
  **<span style="color:olivedrab">POST</span>**  
  **URL :**/like  
  **request :**{'burger_id':burger_id, 'like':like}  
  **response :** '좋아요한 버거의 메세지'  

  ***
  # 화면 구성
  ![](https://images.velog.io/images/fnrkp089/post/f32d9751-9c6c-492c-9845-dee450dbf158/%EB%B2%84%EA%B1%B01.PNG)  
  ***로그인 페이지***  
    
  
  ![](https://images.velog.io/images/fnrkp089/post/9bdbd0e2-4fb8-4f56-b148-e2e6947d8e29/%EB%B2%84%EA%B1%B02.PNG)  
  ***회원 가입 페이지***  
  
  ![](https://images.velog.io/images/fnrkp089/post/a9c5025c-8cef-449f-bfe2-d3a847fca4f4/%EB%B2%84%EA%B1%B03.gif)  
  ***버튼클릭, 리뷰작성 모습(33fps라 화질이 깨짐)***  
 
  ## 관련 링크
  https://youtu.be/Z0_9t-phu5E  
    
  # Solved Problems
  > 버거데이터 베이스에 필요한 속성들은 무엇으로 할것인가?
  * 각 브랜드별 상위 10개의 버거를 추린다.
  * 해당 버거의 이름, 설명, 좋아요, 버거의 브랜드,  고유 버거 아이디를 추가한다.  
    
  ***
  > 버거별 조회를 어떻게 할것인가?
  * 버거의 브랜드를 담아줄 전역변수를 하나 설정하여, 해당 변수에 브랜드를 넣어준다.
  * 브랜드가 담겨있지 않은채 실행하면 모든 버거를 가져오게하는 이벤트로 인식하게 한다.  
    
  ***
  > 리뷰를 보여주는 버튼을 어떻게 할것인가?
  * 버거 조회시 해당 이벤트에 관한 html을 같이 append 시킨다
  * for문을 통해 배열의 index에 따라 동작하므로 id값에 index를 추가한다
  * 특정 버거를 눌렀을 경우 id값의 index를 통해 해당 위치의 리뷰만 열리게 한다.  
    
  ***
  > 리뷰 작성을 어떻게 구현할것인가?
  * 리뷰버튼에 해당 버거의 아이디 값을 부여한다.
  * 누를 경우 버거의 아이디와 현재 사용자의 아이디와 현재 리뷰의 인덱스 값을 넘긴다
  * 리뷰 작성이 완료될 경우 사용자의 아이디와 버거의 아이디, 그리고 리뷰의 고유 아이디 값을 생성하여 서버로 넘긴다  
    
  
  ***
  > 리뷰 삭제를 어떻게 구현할 것인가?
  * 현재 접속한 사용자의 아이디를 비교한다.
  * 작성된 리뷰와 사용자의 아이디가 동일할 경우 해당 div에 '삭제' 버튼이 보이도록 한다.  
    
  ***
  > 리뷰 삭제시 어떤 리뷰인지 어떻게 구분할 것인가?
  * ObjectId Type을 String으로 형변환 후 클라이언트로 전송한다
  * 클라이언트는 해당 Object Type을 비교하여 올바른 요청일 경우 삭제 요청을 전송한다
  * 해당 리뷰의 고유 아이디로 조회 후, 삭제한다.
    
  ***
  > 좋아요를 어떻게 구현할 것인가?
  * 버거의 이름을 조회하여 해당 버거의 좋아요 숫자를 증가
  * 브랜드를 담아준 전역변수를 비교하여 사용자가 눌렀던 브랜드,혹은 전체 버거를 재조회한다.  
    
  ***
  > 사용자가 현재 어떤 브랜드를 눌렀는지 보여주게 할것인가?
  * 첫 화면에서는 모든 브랜드를 조회하는 버튼에만 색을 부여
  * 버튼 클릭마다 버튼에 각각 Addclass와 removeClass를 사용하여 css 변화  
    
  
  
  
