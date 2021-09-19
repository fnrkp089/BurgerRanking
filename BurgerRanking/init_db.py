from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.project

mac = [
   {'burger_id': 1, 'name': '더블 에그 불고기 버거', 'img_url': 'https://www.mcdonalds.co.kr/upload/product/pcList/1631083489206.png',
  'like': 0, 'dislike': 0, 'status': '신선한 국내산 1+등급 계란 2개가 불고기 소스와 만나 푸짐하고 담백한 맛', 'brand': 'McDonald'},
   {'burger_id': 2,'name': '슈니언 버거', 'img_url': 'https://www.mcdonalds.co.kr/upload/product/pcList/1624844044781.png',
    'like': 0, 'dislike': 0, 'status': '탱~글한 통새우살과 바삭한 어니언의 조화!', 'brand': 'McDonald'},
   {'burger_id': 3, 'name': '트리플 치즈버거', 'img_url': 'https://www.mcdonalds.co.kr/upload/product/pcList/1621834836862.png',
    'like': 0, 'dislike': 0, 'status': '부드러운 치즈와 풍부한 육즙의 패티를 세배 더 진하게 즐길 수 있는맛!', 'brand': 'McDonald'},

   {'burger_id': 4, 'name': '빅맥', 'img_url': 'https://www.mcdonalds.co.kr/upload/product/pcList/1583727841393.png',
    'like': 0, 'dislike': 0, 'status': '100% 순 쇠고기 패티 두 장에 빅맥®만의 특별한 소스. 입안에서 살살 녹는 치즈와 신선한 양상추, 양파, 그리고 피클까지.', 'brand': 'McDonald'},
   {'burger_id': 5, 'name': '맥스파이시 상하이 버거', 'img_url': 'https://www.mcdonalds.co.kr/upload/product/pcList/1583728339451.png',
    'like': 0, 'dislike': 0, 'status': '겉은 바삭, 속은 부드러운 치킨 패티의 매콤함으로 입맛도 기분도 화끈하게!', 'brand': 'McDonald'},
   {'burger_id': 6, 'name': '1955 버거', 'img_url': 'https://www.mcdonalds.co.kr/upload/product/pcList/1599119588089.png',
    'like': 0, 'dislike': 0, 'status': '맥도날드가 처음 생긴 1955년의 맛을 담은 영원한 오리지널 1955 버거', 'brand': 'McDonald'},

   {'burger_id': 7, 'name': '더블 필레오피쉬', 'img_url': 'https://www.mcdonalds.co.kr/upload/product/pcList/1617176321703.png',
    'like': 0, 'dislike': 0, 'status': '맥도날드의 타르타르소스와 부드러운 스팀번이 조화로운 맛', 'brand': 'McDonald'},
   {'burger_id': 8, 'name': '필레오피쉬', 'img_url': 'https://www.mcdonalds.co.kr/upload/product/pcList/1617176321703.png',
    'like': 0, 'dislike': 0, 'status': '맥도날드의 타르타르소스와 부드러운 스팀번이 조화로운 맛', 'brand': 'McDonald'},
   {'burger_id': 9, 'name': '맥치킨 모짜렐라', 'img_url': 'https://www.mcdonalds.co.kr/upload/product/pcList/1583727633823.png',
    'like': 0, 'dislike': 0, 'status': '든든한 맥치킨에 골든 모짜렐라 치즈 스틱 2개와 매콤한 아라비아따 소스를 더해 강렬하게 재탄생한 맛!', 'brand': 'McDonald'},

   {'burger_id': 10, 'name': '맥치킨', 'img_url': 'https://www.mcdonalds.co.kr/upload/product/pcList/1583727841393.png',
    'like': 0, 'dislike': 0, 'status': '바삭한 치킨패티, 고소한 화이트 마요소스와 아삭한 양상추가 함께!', 'brand': 'McDonald'},
]

king = [
   {'burger_id': 11, 'name': '콰드로치즈와퍼', 'img_url': 'https://d1cua0vf0mkpiy.cloudfront.net/images/menu/normal/4713e253-3f67-45ff-a744-22e6f282c84b.png',
  'like': 0, 'dislike': 0, 'status': '진짜 불맛을 즐겨라! 4가지 고품격 치즈와 불에 직접 구운 와퍼 패티의 만남!', 'brand': 'BURGER KING'},
   {'burger_id': 12, 'name': '몬스터와퍼', 'img_url': 'https://d1cua0vf0mkpiy.cloudfront.net/images/menu/normal/4c47cb08-bc12-4457-b9b1-fbeb3ff1ad23.png',
    'like': 0, 'dislike': 0, 'status': '불맛 가득 순쇠고기,치킨,베이컨에 화끈한 디아블로 소스의 압도적인맛 ', 'brand': 'BURGER KING'},
   {'burger_id': 13, 'name': '기네스와퍼', 'img_url': 'https://d1cua0vf0mkpiy.cloudfront.net/images/menu/normal/b4c8ac6e-f947-4088-80b7-0f58657e90a1.png',
    'like': 0, 'dislike': 0, 'status': '기네스 번과 기네스 바비큐 소스의 풍미', 'brand': 'BURGER KING'},

   {'burger_id': 14, 'name': '기네스콰드로치즈와퍼', 'img_url': 'https://d1cua0vf0mkpiy.cloudfront.net/images/menu/normal/5e8d09ac-7835-40a4-8f4a-461a51fe9c94.png',
    'like': 0, 'dislike': 0, 'status': '콰드로치즈와퍼가 기네스를 만나다!', 'brand': 'BURGER KING'},
   {'burger_id': 15, 'name': '콰트로치즈X', 'img_url': 'https://d1cua0vf0mkpiy.cloudfront.net/images/menu/normal/1596e867-b80b-4376-99a4-e0cd309b39d0.png',
    'like': 0, 'dislike': 0, 'status': '더욱 더 풍성한 치즈와 소고기 번!', 'brand': 'BURGER KING'},
   {'burger_id': 16, 'name': '통새우X', 'img_url': 'https://d1cua0vf0mkpiy.cloudfront.net/images/menu/normal/18617ee5-b986-4ce5-8c27-fede613ae10b.png',
    'like': 0, 'dislike': 0, 'status': '육즙 가득 소고기와 통새우의 짜릿한 만남!', 'brand': 'BURGER KING'},

   {'burger_id': 17, 'name': '몬스터X', 'img_url': 'https://d1cua0vf0mkpiy.cloudfront.net/images/menu/normal/61144766-1be1-460f-b49f-01ad52f1ec4d.png',
    'like': 0, 'dislike': 0, 'status': '더욱 거대해진 와퍼의 맛있는 반란!', 'brand': 'BURGER KING'},
   {'burger_id': 18, 'name': '치즈렐라치킨버거', 'img_url': 'https://d1cua0vf0mkpiy.cloudfront.net/images/menu/normal/372496a5-5f24-48c6-bb21-52aecc256e69.png',
    'like': 0, 'dislike': 0, 'status': '모짜렐라 치즈가 통째로! 치즈렐라!', 'brand': 'BURGER KING'},
   {'burger_id': 19, 'name': '불고기와퍼', 'img_url': 'https://d1cua0vf0mkpiy.cloudfront.net/images/menu/normal/3ff9631a-cfa1-4566-b26a-89e9f8ba93e4.png',
    'like': 0, 'dislike': 0, 'status': '불에 직접 구운 순 쇠고기 패티가 들어간 와퍼에 달콤한 불고기 소스까지!', 'brand': 'BURGER KING'},

   {'burger_id': 20, 'name': '스태커4와퍼', 'img_url': 'https://d1cua0vf0mkpiy.cloudfront.net/images/menu/normal/93116ef9-43a4-451a-b45a-daa0aacfb631.png',
    'like': 0, 'dislike': 0, 'status': '믿고 먹을수 있는 와퍼! 4장의 패티로 더 크게 도전하세요!', 'brand': 'BURGER KING'},
]

lot = [
   {'burger_id': 21, 'name': '모짜렐라인더버거', 'img_url': 'http://www.lotteria.com/Data//Goods/231/ListImage.jpg',
  'like': 0, 'dislike': 0, 'status': '자연산 모짜렐라 치즈에 노릇노릇한 베이컨, 레터스소스가 어우러진 풍부한 맛!', 'brand': 'LOTTERIA'},
   {'burger_id': 22, 'name': '한우불고기버거', 'img_url': 'http://www.lotteria.com/Data//Goods/233/ListImage.jpg',
    'like': 0, 'dislike': 0, 'status': '한우로 만든 두춤한 패티와 부드럽고 촉촉한 포테이토번이 만나 더 맛있다! ', 'brand': 'LOTTERIA'},
   {'burger_id': 23, 'name': '불고기버거', 'img_url': '	http://www.lotteria.com/Data//Goods/68/ListImage.jpg',
    'like': 0, 'dislike': 0, 'status': '볼륨 가득한 패티와 불고기 소스가 잘 조화된 영양만점의 햄버거', 'brand': 'LOTTERIA'},

   {'burger_id': 24, 'name': '데리버거', 'img_url': 'http://www.lotteria.com/Data//Goods/26/ListImage.jpg',
    'like': 0, 'dislike': 0, 'status': '풍성한 레터스에 마요네즈, 독특한 데리소스가 포인트인 버거', 'brand': 'LOTTERIA'},
   {'burger_id': 25, 'name': '클래식치즈버거', 'img_url': '	http://www.lotteria.com/Data//Goods/238/ListImage.jpg',
    'like': 0, 'dislike': 0, 'status': '부드럽고 촉촉한 포테이토번과 풍부한 육즙의 두툼한 호주산 쇠고기 패티로 본연의 맛을 가득!', 'brand': 'LOTTERIA'},
   {'burger_id': 26, 'name': '폴드버거비프', 'img_url': 'http://www.lotteria.com/Data//Goods/327/ListImage.jpg',
    'like': 0, 'dislike': 0, 'status': '같은 것도 다르게 먹는다! 접어서 먹는 버거', 'brand': 'LOTTERIA'},

   {'burger_id': 27, 'name': 'T-Rex', 'img_url': 'http://www.lotteria.com/Data//Goods/290/ListImage.jpg',
    'like': 0, 'dislike': 0, 'status': '번스보다 큰 통다리살 치킨패티를 활용한 버거', 'brand': 'LOTTERIA'},
   {'burger_id': 28, 'name': '새우버거', 'img_url': 'http://www.lotteria.com/Data//Goods/296/ListImage.jpg',
    'like': 0, 'dislike': 0, 'status': '더 커지고 더 맛있어진 새우 패티로 고유의 맛을 강화한 오리지널 새우버거', 'brand': 'LOTTERIA'},
   {'burger_id': 29, 'name': '치킨버거', 'img_url': 'http://www.lotteria.com/Data//Goods/296/ListImage.jpg',
    'like': 0, 'dislike': 0, 'status': '육즙, 풍미 뛰어난 닭다리살 활용한 가성비 치킨버거', 'brand': 'LOTTERIA'},

   {'burger_id': 30, 'name': '핫크리스피버거', 'img_url': 'http://www.lotteria.com/Data//Goods/100/ListImage.jpg',
    'like': 0, 'dislike': 0, 'status': '토마토와 레터스등의 야채와 하바네로향이 가미된 가슴살 프리미엄 버거', 'brand': 'LOTTERIA'},
]

db.hamburger.drop()
db.hamburger.insert_many(mac)
db.hamburger.insert_many(king)
db.hamburger.insert_many(lot)
