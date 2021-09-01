a = int(input())
b = int(input())

z = a*((b %100)%10)
y = a*((b %100)//10)
x = a*(b // 100)
i = a * b
print(z)
print(y)
print(x)
print(i)