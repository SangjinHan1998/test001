import sys

num = int(sys.stdin.readline())
max = 0
avg = 0
Test = list(map(float,sys.stdin.readline().split()))
for i in range(num):
    if max < Test[i]:
        max = Test[i]

for i in range(num):
    Test[i] = Test[i] / max * 100
    avg += Test[i]

print(round(avg / num, 2))