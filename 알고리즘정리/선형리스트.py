class BaseList:
      # 데이터의 추가
  def append(self, data):
      raise NotImplemented
  # 데이터의 탐색
  def search(self, data):
      raise NotImplemented
  # 데이터의 참조하기
  def get(self, index):
      raise NotImplemented
  # 데이터의 꺼내오기
  def pop(self):
      raise NotImplemented
  # 데이터의 삭제
  def remove(self, index):
      raise NotImplemented
  # 리스트 전체 출력
  def display(self):
      raise NotImplemented

class ArrayList(BaseList):
  def __init__(self):
      self.list = []
      self.count = 0

  def append(self, data):
      self.list.append(data)
      self.count += 1

  def search(self, data):
      return [index for index, stored in enumerate(self.list) if stored == data]

  def get(self, index):
      if 0 <= index < self.count:
          return self.list[index]
      else:
          raise IndexError

  def pop(self):
      val = self.list[self.count - 1]
      self.remove(self.count - 1)
      return val

  def remove(self, index):
      for _index in range(index, self.count - 1):
          self.list[_index] = self.list[_index + 1]

      del self.list[self.count - 1]
      self.count -= 1

  def display(self):
      for index in range(self.count):
          print(self.list[index])


class Node:
    def __init__(self, data, next):
        # 데이터 저장
        self.data = data
        # 다음 노드를 가리킴
        self.next = next

class LinkedList(BaseList):
    def __init__(self, sort = None):
        self.head = Node(None, None)
        self.tail = None
        self.count = 0
        self.sort = sort if sort else lambda x, y : x > y
# lambda 
# 인자 : 표현식 코드의 간결함과 메모리의 절약
# return 키워드 없이 자동으로 return 
# def 함수이름 (매개변수): / return 결과  --> lambda 매개변수 : 결과
# (lambda x, y : x + y)(10, 20) 결과 30

    def append(self, data): # 추가
        new_node = Node(data, self.head.next)
        self.head.next = new_node
        if not self.tail:
            self.tail = new_node
        self.count += 1
        return new_node
    
    def append_with_sort(self, data):
        new_node = Node(data, None)
        prev = self.head
        while prev.next:
            current = prev.next
            if self.sort(current.data, data):
                break
            prev = prev.next
        
        new_node.next = prev.next
        prev.next = new_node
    
    def search(self, data):
        hits = []
        current = self.head
        while current.next:
            current = current.next
            if current.data == data:
                hits.append(current)

        return hits
    
    def get(self, index):
        if 0 <= index < self.count:
            current = self.head.next
            for _index in range(self.count):
                if _index == index:
                    return current
                current = current.next 
        else:
            raise IndexError

        def pop(self):
            node = self.head.next 
            self.head.next = node.next 
            self.count -= 1
            return node

        def remove(self, index):
            before = None
            current = self.head.next 
            for _index in range(self.count):
                if _index == index:
                    if _index == 0:
                        self.head.next = current.next 
                    else:
                        before.next = current.next 

                before = current 
                current = current.next 
            self.count -= 1

        def display(self):
            current = self.head 
            while current.next:
                current = current.next
                print(current.data)


    
                
    