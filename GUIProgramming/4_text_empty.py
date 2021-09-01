from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")
#root.geometry("640x480+300+100")      # 가로 x 세로 + x좌표 + y좌표

txt = Text(root, width = 30, height= 5) # TEXT 여러줄
txt.pack()
txt.insert(END, "글자 입력:")
  
e = Entry(root, width = 30)             # ENTRY 한줄
e.pack()
e.insert(0, "한 줄만 입력:")

def btncmd():  
    # 내용 출력 
    print(txt.get("1.0", END))      # 1 : 첫번째 라인, 0 : 0번째 column 위치
    print(e.get())

    # 내용 삭제
    txt.delete("1.0", END)
    e.delete(0, END)

btn = Button(root, text = "클릭", command = btncmd)
btn.pack()

root.mainloop()