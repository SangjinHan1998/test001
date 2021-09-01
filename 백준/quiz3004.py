t = int(input())


for i in range(2, 101):
    if i % 2 == 0:
        print(int(((t / 2) + 1)**2))
    else:
        print(int(t**2))