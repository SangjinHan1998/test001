t = int(input())

if t == 1:
    print(2 * t)
elif t % 2 == 0:
    print(int(((t / 2) + 1)**2))
else:
    print(int((t // 2 + 1)*(t // 2 + 2)))