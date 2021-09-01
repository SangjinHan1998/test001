import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

values = [str(i) + "일" for i in range(1, 32)]  # 1 ~ 31 까지의 숫자
combobox = ttk.Combobox(root, height = 5, values = values)  # height 를 통해 목록이 5개까지만 보여진다. 
combobox.pack() # 아이디 가입할 때 리스트 나오는 박스 만들기 
combobox.set("카드 결제일") # 최초 목록 제목 설정

readonly_combobox = ttk.Combobox(root, height = 8, values = values, state = "readonly") # 박스 내용 못바꿈. 
readonly_combobox.current(0) # 0번째 인덱스 값 선택
readonly_combobox.pack()     

def btncmd():  
    print(combobox.get())
    print(readonly_combobox.get())
    pass

btn = Button(root, text = "선택", command = btncmd)
btn.pack()

root.mainloop()