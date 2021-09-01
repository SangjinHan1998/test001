import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("Nado GUI")  # 프로그레스 바 : 진행 상태 표시
root.geometry("640x480")

#progressbar = ttk.Progressbar(root, maximum = 100, mode = "indeterminate")  # indeterminate 언제끝나는지 미정. 
progressbar = ttk.Progressbar(root, maximum = 100, mode = "determinate") 
progressbar.start(10)   # 10 ms 마다 움직임.
progressbar.pack()

def btncmd():  
    progressbar.stop()  # 작동 중지
    pass

btn = Button(root, text = "중지", command = btncmd)
btn.pack()

root.mainloop()