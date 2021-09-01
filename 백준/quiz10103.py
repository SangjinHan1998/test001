n = int(input())  # 테스트케이스 개수 입력
a_score=100  # 초기 점수
b_score=100  # 초기 점수
for i in range(n):  # 테스트케이스 횟수만큼 반복
    a,b = map(int,input().split(" "))  # 1판마다 주사위 점수를 받아 a,b에 저장
    if a>b:  # a가 이겼으면
        b_score-=a  # 그만큼 b의 점수에서 차감
    elif a<b:  # b가 이겼으면
        a_score-=b  # 그만큼 a의 점수에서 차감
    else:  # 무승부일 경우
        pass  # 패~쓰
print(a_score)  #결과 출력
print(b_score)