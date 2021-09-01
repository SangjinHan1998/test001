x, y = map(int,input().split())
a = (x * 60)
c = a + y - 45
if (x == 0):
    print((int(c / 60) + 23), (c % 60)) 
if (y >= 0 and y <= 59):
    print(int(c / 60), (c % 60))


