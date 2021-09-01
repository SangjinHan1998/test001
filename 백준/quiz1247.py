import sys
 
answer = []
 
for answer in range(3):
    N = int(sys.stdin.readline())
    sum = 0
    for i in range(N):
        a = int(sys.stdin.readline())
        sum += a
    
    if sum > 0:
        answer.append("+")
    elif sum < 0:
        answer.append("-")
    else:
        answer.append("0")
 
for b in answer:
    print(b)