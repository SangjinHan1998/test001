import time
print(time.ctime()) # 현재 시간 출력

cur_time = time.ctime()
print(cur_time.split(' ')[-1])  # cur_time 을 ' ' 로 나눈 뒤 뒤에서 첫번째 값 출력

for i in range(10):
    print(i)
    time.sleep(1)   # print number every second

print(dir(time))    # check what functions or variables are in the module.

