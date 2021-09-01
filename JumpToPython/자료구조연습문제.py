naver_closing_price = {}    # 문제 3-1

naver_closing_price['월'] = 474500
naver_closing_price['화'] = 461500
naver_closing_price['수'] = 501000
naver_closing_price['목'] = 500500
naver_closing_price['금'] = 488500


print(naver_closing_price) # 문제 3-1

print_list = list(naver_closing_price.values()) 
print(print_list)   # 문제 3-1
print(max(print_list))  # 문제 3-2
print(min(print_list))  # 문제 3-3
print("가격차 : " , max(print_list) - min(print_list))    # 문제 3-4
print("수요일 종가: ", print_list[2])    # 문제 3-5

naver_closing_price2 = {}    # 문제 3-1

naver_closing_price2['09/07'] = 474500
naver_closing_price2['09/08'] = 461500
naver_closing_price2['09/09'] = 501000
naver_closing_price2['09/10'] = 500500
naver_closing_price2['09/11'] = 488500

print(naver_closing_price2)
print("==== = = === =")
print_list2 = list(naver_closing_price2.values())
print(print_list[2])