for i in range(4):
    print("◆", end='')     # 문제 4-1

for i in range(4):
    print("", end = '\n')
    for j in range(5):
        print("□", end='')  # 문제 4-2

for i in range(5):
    print("", end = '\n')
    for j in range(5):
        if (j <= i):
            print("△", end='')  # 문제 4-3

for i in range(5):
    print("", end = '\n')
    for j in range(5):
        if (i <= j):
            print("▲", end='')  # 문제 4-3       

for i in range(5):
    print("", end = '\n')
    for j in range(5):
        if (j <= i):
            print("△", end='')  # 문제 4-4

# 문제 4-5
for j in range(5):
    for i in range(4-j):
        print('', end ='')
    for i in range(j + 1):
        print('*', end = '')
    print("")

# 문제 4-6
for j in range(5):
    for i in range(i):
        print('', end = '')
    for i in range(5-j):
        print('☆', end = '') 
    print("")

# 문제 4-7
for j in range(5):
    for i in range(4-j):
        print('', end='')
    for i in range(2*(j+1)-1):
        print('★', end = '')
    print("")

# 문제 4-8

# 문제 4-9



