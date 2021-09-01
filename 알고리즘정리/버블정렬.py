data = [12, 53, 85, 36, 6, 47] # 정렬 데이터
sorted_data = []    # 정렬 결과 담는 리스트

# 1. 리스트 왼쪽부터 옆의 수와 비교해서 왼쪽이 클 경우 서로 자리 바꿈
# 2. 마지막까지 살아남는 리스트. 가장 큰 값을 정렬 리스트에 추가
# 3. 원래 리스트에 원소가 남지 않을 때까지 1 반복

while data: 
    large = data[0]
    for i in range((len(data) -1)):     # 0 ~ n-2 까지 
        if data[i] > data[i + 1]:
            large = data[i]
            data[i] = data[i + 1]
            data[i + 1] = large
        else:
            large = data[i + 1]
    sorted_data.append(large)
    data.remove(large)

    # 단계별 데이터 출력
    print("가장 큰 값 : {}".format(large))
    print("대상 리스트: {}".format(data))
    print("정렬 리스트: {}".format(sorted_data))
    print("\n")