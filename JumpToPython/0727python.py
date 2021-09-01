# ========================= [리스트] =====================================
com = ["콜라", "사이다" , "환타", "우유"]
print(com[1])
print(com[3])

# 리스트 --> 여러개의 데이터를 "순서대로" 저장하고 관리할 때 

# 바나나의 최근 5일치 가격 1000 1200 1100 1100 1000
banana = [1000, 1200, 1100, 1100, 1000]
print(banana)
# 실수도 가능
# banana = [1000.0, 1200.0, 1100.0, 1100.0, 1000.0]

# 내가 가진 바나나
myfruit = ['banana', 300]

myfruit = []    # 내가 가진 과일 없음 

# 리스트의 인덱싱은 문자열 인덱싱과 동일 음수 사용하면 뒤쪽부터 데이터 접근
print(banana[0])
print(banana[-1])

# 음료수 판매 10위
drink_top10 = ['코카콜라', '사이다', '핫식스', '코코팜', '환타', '카페라떼', '아메리카노', '딸기라떼', '초코우유', '카푸치노']
print("음료수 판매량 5위 : ", drink_top10[4])
print("음료수 판매량 3위 : ", drink_top10[2])

# 음료수 판매 5위까지 
drink_top5 = drink_top10[0:5]   # [시작 인덱스 : 끝 인덱스]
print(drink_top5)


# 음료수 판매 6위부터 나머지 
drink_bot5 = drink_top10[5:]    # 마지막 데이터의 경우 나타내는 숫자 생략 가능
print(drink_bot5)

print(drink_top10[5:8])

# 리스트에 데이터 추가 --> 1. append 리스트 맨 끝에만 추가됨
drink_top10.append('탄산수')
print(drink_top10)

drink_top11 = drink_top10
print(drink_top11)

# 2. insert --> 원하는 위치에 추가 
drink_top10.insert(3, '파워에이드')
print(drink_top10)

# 데이터 삭제
print(drink_top10[-1])
del drink_top10[-1]
print(drink_top10)

print(len(drink_top10))

# ======================= 튜플(tuple) ===========================
print("========================================튜플(tuple)==========================")
t = ('zero', 'one', 'two')
print(t)
print(t[1])

# 튜플 슬라이싱 
print(t[0:2])

print("=========================================딕셔너리============================")
# 딕셔너리
cur_price = {}
print(type(cur_price))

# 딕셔너리 키 - 값 쌍 하나 추가
cur_price['coffee'] = 1500  # 키(coffee) - 값()
cur_price['coke'] = 1200  # 키(coffee) - 값()
cur_price['juice'] = 1400  # 키(coffee) - 값()
cur_price['milk'] = 1000  # 데이터 추가
del cur_price['coke']   # 데이터 삭제
print(cur_price)

# 메서드 keys --> keys 값만 구할때
print(cur_price.keys()) # insert 나 append 처럼 메서드 호출
print(list(cur_price.keys()))
stock_list = list(cur_price.keys()) 
# stock_list 라는 이름의 변수로 list 의 반환값 바인딩
# 바인딩 : 결속. 특정객체에서 실행되게끔 고정시키는 역할 
# 객체 a, 전역함수 b 객체에 test() 메서드 b.test() 라고 쓰고 a객체에서 실행되게함

print(stock_list)
print("=====================================")

# 메서드 values --> values 값만 구할때
price_list = list(cur_price.values())   
print(price_list)

print('milk' in cur_price.keys())   # milk 가 cur_price 딕셔너리에 있는가?
print('soju' in cur_price.keys())   # soju 가 cur_price 딕셔너리에 있는가?

