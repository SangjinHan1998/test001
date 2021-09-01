subway1 = ["테이프", "휴대폰", "달력", 20, 30]


#볼펜을 추가할때
subway1.append("볼펜")
print(subway1)

#수첩을 휴대폰과 달력 사이 넣는다. 
subway1.insert(2,"수첩")
print(subway1)

#하나씩 뒤에서 꺼냄
print(subway1.pop())
print(subway1)
print(subway1)
#같은 값 몇개 있는가? 

subway1.append("휴대폰")
print(subway1)
print(subway1.count("휴대폰"))

#정렬

num_list = [5,2,4,3,1]


