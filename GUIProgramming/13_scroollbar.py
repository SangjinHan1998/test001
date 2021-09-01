from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)    # 스크롤바 위젯
scrollbar.pack(side = "right", fill = "y")

# set 이 없으면 스크롤을 내려도 다시 올라온다. 
listbox = Listbox(frame, selectmode = "extended", height = 5, yscrollcommand = scrollbar.set)

for i in range(1, 32):  # 1 ~ 31
    listbox.insert(END, str(i) + "일")
listbox.pack(side = "left")

scrollbar.config(command = listbox.yview)   # yview 상하로 움직이는 목록

root.mainloop()   