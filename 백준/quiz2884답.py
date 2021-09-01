x, y = map(int,input().split())

if y > 44:
    print(x, y - 45);
elif y < 45 and x > 0:
    print(x-1, y + 15)
else:
    print(23, y + 15)
