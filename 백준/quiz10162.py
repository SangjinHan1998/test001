T = int(input( ))

if (T % 10 != 0):
    print(-1) 
    
elif T < 60:
    print(T // 300)
    print(T // 60)
    print(T // 10)
elif T > 60 and T < 300:
    print(T // 300)
    print(T // 60)
    print((T % 60) // 10)
elif T > 300:
    print(T // 300)
    print((T % 300) // 60)
    print(((T % 300) % 60) // 10)

