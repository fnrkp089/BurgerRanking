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
  https://youtu.be/XI3LMycx6Sc
  
