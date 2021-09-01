import sys

# 011 use variable
SAMSUNG = int(sys.stdin.readline())
evaluated_price = SAMSUNG * 10

print(evaluated_price)

# 012 use variable
Capitalization =298000000000000
current = int(sys.stdin.readline())
PER = 15.79
print(Capitalization,type(Capitalization))
print(current, type(current))
print(PER, type(PER))

# 013 print STRING
s = "hello! "
t = "python"
print(s + t)

# 014 calculation with python
print(2 + 2 * 3)

# 015 (function type)
a = "132"
print(type(a))

# 016 (convert string to integer)
num_str = input()
print(type(num_str))
print(int(num_str))

# 017 (covert integer to stirng 100)
num = 100
result = str(num)
print(result, type(result))

# 018 (convert string to float)
num1 = "15.79"
print(type(num1))
print(num1, float(num1))

# 019
year = "2020"
year = int(year)
print(year, type(year))

# 020
money, month = map(int,input().split())
air = money * month
print(air)