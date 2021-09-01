# Boolean --> True 또는 False 만 사용 가능 
a = True
print(type(a))
b = False
print(type(b))

day1 = 10000
day2 = 13000
print(((day2 - day1) == (day1 * 0.3)) or ((day2 - day1) > (day1 * 0.292)))

cur_price = 9980
print(cur_price >= 5000 and cur_price < 10000)

#  if 문
wikibooks_cur_price = 10500 
if wikibooks_cur_price >= 10000:
    print("Buy 10")
    print("Buy 10")
    print("Buy 10")
else:
    print("Holding")    # 들여쓰기 다르면 문법 에러 발생 


wikibooks1_cur_price = 8000
if wikibooks1_cur_price < 9000:
    print("Sell 10")

# if elif else
price = 7000
if price < 1000:
    bid = 1
elif price >= 1000 and price < 5000:
    bid = 5
elif price >= 5000 and price < 10000:
    bid = 10
elif price >= 10000 and price < 50000:
    bid = 50    
elif price >= 50000 and price < 100000:
    bid = 100
elif price >= 100000 and price < 500000:
    bid = 500
elif price >= 500000:
    bid = 1000
print(bid)

# for --> ~ 대한  반복문 사용
# 반복횟수가 정해짐 / 리스트, 튜플, 딕셔너리 와 같은 파이썬 자료구조와 함께 사용됨
for i in [0,1,2,3,4,5,6,7,8,9,10]:
    print(i)

# 리스트, 수정 가능
interest_stocks = ["naver", "Emart", "SKT"]

for company in interest_stocks:
    print("%s : Buy 10" % company)

# 튜플, 수정 불가능 
interest_stocks1 = ["KAKAO", "Coupang", "KT"]

for company in interest_stocks1: 
    print("%s Buy 10" % company)

# 딕셔너리 키-값 
interest_stocks = {"naver:" : 10, "Emart" : 5, "SKT" : 30} 

for company, stock_num in interest_stocks.items():
    print("%s : Buy %s" % (company, stock_num))

interest_stocks1 = {"KAKAO" : 100, "Coupang" : 200, "KT" : 300}
for company in interest_stocks1.keys():
    print("%s : Buy %s" % (company, interest_stocks1[company]))    

print("=======================while=====================")

# while 반복문 사용 
# 조건 충족시에만 실행됨 
i = 0
while i < 10: 
    print(i)
    i = i+1
# i = 11일때 조건식 만족 x 


wikibooks = 10000
day = 1
while day < 6:  
    wikibooks = wikibooks + wikibooks * 0.3
    day = day + 1

print(wikibooks)

# while 과 if
# 0 부터 10 까지 숫자중 홀수인 것 구하기(나머지 1이면 홀수)
num = 0 
while num <= 10:
    if num % 2 == 1:
        print(num)
    num += 1

while 1:
    print("Find stocks")
    break 

print("=======================================================================")
num1 = 0
while 1:
    print(num1)
    if num1 == 10: 
        break
    num1 += 1

num2 = 0
while num2 < 10:
    num2 += 1
    if num2 == 5:
        continue
    print(num2)



# 반복문 문장 최소 하나라도 있어야 문법 오류 x 

for i in [101, 102, 103, 104]:
    print("Newspaper delivery : ", i)

apart = [[101, 102, 103, 104] ,[201, 202, 203, 204] ,[301, 302, 303, 304] ,[401, 402, 403, 404]]

apart[0] == [101, 102, 103, 104] 
apart[1] == [201, 202, 203, 204] 
apart[2] == [301, 302, 303, 304]
apart[3] == [401, 402, 403, 404]
print(apart[2])

for floor in apart:
    for room in floor:
        print("Newspaper delivery : " , room) 


        
