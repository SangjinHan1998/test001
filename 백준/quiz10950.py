import sys

T = int(input())

for x in sys.stdin():
    print(x)
for i in range(T):
    A , B = map(int,input().split())
    print(A + B)