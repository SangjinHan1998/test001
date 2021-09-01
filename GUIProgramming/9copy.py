import time
import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("Nado GUI")  # 프로그레스 바 : 진행 상태 표시
root.geometry("640x480")

p_var2 = DoubleVar()
progressbar2 = ttk.Progressbar(root, maximum = 100, length = 250, variable =p_var2)
progressbar2.pack()

def btncmd2():
    for i in range(1, 101):
        time.sleep(0.01)    # 0.01 초 대기 

        p_var2.set(i)   # progress bar 의 값 결정
        progressbar2.update()   # ui 업데이트 
        print(p_var2.get())

btn = Button(root, text = "시작", command = btncmd2)
btn.pack()

root.mainloop()