import os
from tkinter import *

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

root = Tk()         # label 은 글자나 이미지를 보여준다. 
root.title("Nado GUI")
root.geometry("640x480")


label1 = Label(root, text = "안녕하세요")
label1.pack()

photo = PhotoImage(file = resource_path("GUIProgramming/icon1.png"))
label2 = Label(root, image = photo)
label2.pack() 

def change():
    label1.config(text="또 만나요")

    global photo2   # 전역변수니 함수가 끝내도 없애지 않음
    photo2 = PhotoImage(file = resource_path("GUIProgramming/icon2.png"))
    label2.config(image = photo2) 

    # garbage Collection  변수를 쓰레기로 인식하고 지울 수 있다. 

btn = Button(root, text = "클릭", command = change)
btn.pack()

root.mainloop()