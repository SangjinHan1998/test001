import stock

def cal_upper(price):
    increment = price * 0.3
    upper_price = price + increment
    return upper_price

def cal_lower(price):
    decrement = price * 0.3
    lower_price = price - decrement
    return lower_price 

author = "pystock"

print(stock.author)
print(cal_upper(10000)) # 상한가
print(cal_lower(10000)) # 하한가
print(__name__)

