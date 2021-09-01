from tkinter import *

root = Tk()
root.title("Nado GUI")

btn1 = Button(root, text = "버튼 1")     # 어디에 넣을것인지
btn1.pack()

btn2 = Button(root, padx = 5, pady = 10, text = "버튼 2 녹차 피자 면도기")   # padx 는 너비조절 pady 는 높이조절  / 데이터 양 따라 버튼크기 달라짐
btn2.pack()

btn3 = Button(root, padx = 10, pady = 5, text = "버튼 3")
btn3.pack()

btn4 = Button(root, width = 10, height = 3, text = "버튼 4")      # width 와 height 의 크기는 고정 데이터 많아도 버튼 크기변화 x 
btn4.pack()

btn5 = Button(root, fg = "pink", bg = "brown", text = "버튼 5")
btn5.pack()

photo = PhotoImage(file = "GUIProgramming/icon1.png")
btn6 = Button(root, image = photo)
btn6.pack()

def btncmd():   # 버튼 7의 함수
    print("버튼이 클릭되었어요")

btn7 = Button(root, text = "동작하는 버튼", command = btncmd)
btn7.pack()

root.mainloop()