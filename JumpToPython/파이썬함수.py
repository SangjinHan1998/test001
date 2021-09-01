def print_ntimes(n): # 변수 --> 함수 파라미터 또는 함수 인자. 
    for i in range(n):
        print("red")

print(print_ntimes(5))

#===============================반환값===================================
def cal_upper(price):
    increment = price * 0.3
    upper_price = price + increment
    return upper_price  
    # 함수 외부로 보냄

print(cal_upper(10000))

def cal_lower(price):
    decrement = price * 0.3
    lower_price = price - decrement 
    return lower_price

print(cal_lower(1000))
print(cal_lower(5000))

def cal_upper_lower(price):
    offset = price * 0.3
    upper = price + offset
    lower = price - offset
    return (upper, lower)

(upper, lower) = cal_upper_lower(3000)  # 상한가 하한가 튜플 구성 반환
print(upper, lower)

#=============================Bulit-In Functions==================================
# abs(return absolute value / only integer type values and real number)
print(abs(-44))
print(abs(-7.2))
# chr(i) (input UniCode and return String)
print(chr(97))
print(chr(66))
# enumerate (input sequence form and return object / print data and index at the same time)
for i,stock in enumerate(['Naver', 'KAKAO', 'LG']):
    print(i, stock)
# NO enumerate (No index -> separately caluculate index)
t = 0
for stock in ['SAMSUNG', 'APPLE', 'GOOGLE']:
    print(t, stock)
    t += 1
# id(object) (Take an object return its eigenvalue. eigenvalue --> usually address of memeory
hd = 1
mi = 2
print(id(hd))
print(id(mi))

# len(s) (input list, tuple, string, dictionary and ruturn element number)
print(len(['a','b']))
print(len('english'))
print(len({1:'blue',2:'red'}))

# list (input string or tuple next make list object and return list)
print(list('lemon'))
print(list((1,2,3)))

# max (return maximum) min (return minimum)
print(max(12,13,445))
print(min(143,23,56))

# sorted (sort input data and return result data)
print(sorted((3,4,65,19)))
print(sorted([35,21,22,145,90]))
print(sorted(['b','d','a']))

# int(x) input string and return integer type
# str(x) input object and return s




