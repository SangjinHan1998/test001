# BMI 측정
import sys

KG, HEIGHT = map(float,sys.stdin.readline().split())

BMI = KG / (HEIGHT ** 2)

if (BMI < 18.5):
    print("마른체형")
elif (18.5 <= BMI and BMI <25.0):
    print("표준")
elif (25.0 <= BMI and BMI <30.0):
    print("비만")    
else:
    print("고도비만")

# 삼각형의 넓이
def get_triangle_area(width,height2):
    return 0.5 * WIDTH * HEIGHT2

WIDTH, HEIGHT2 = map(float,sys.stdin.readline().split())
print(get_triangle_area(WIDTH, HEIGHT2))

# 시작과 끝을 나타내는 숫자를 받아 시작과 끝까지의 모든 정수값의 합 반환
def add_start_to_end(start,end):
    return sum(range(start, end+1))

start, end= map(int,sys.stdin.readline().split())
print(add_start_to_end(start, end))

# 문자열 앞 3글자만 출력
def get_abbr(data_list):
    result = []
    for x in data_list:
        result.append(x[:3])
    return result

print(get_abbr(['Seoul', 'Daegu', 'Kwangju', 'Jeju'])
