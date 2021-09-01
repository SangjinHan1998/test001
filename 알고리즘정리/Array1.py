# 배열(Array) 메모리 상에 같은 타입의 자료가 연속적으로 저장
# 정렬되어 있지 않다면, 탐색 시간이 걸린다. 
# 정렬되어 있다면 시간줄일 수 있음.
# 정렬을 위해 삽입 삭제하는데 배열을 한칸씩 밀거나 당기면 오버헤드가 생긴다. 

class ArrayList(BaseList):
    def __init__(self):
        self.list = []
        self.count = 0

    def append(self, data):
        self.list.append(data)
        self.count += 1
    
    def search(self, data):
        return[index for index, stored in enumerate(self.list)]