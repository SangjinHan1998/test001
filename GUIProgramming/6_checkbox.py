from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")
#root.geometry("640x480+300+100")      # 가로 x 세로 + x좌표 + y좌표

chkvar = IntVar()   # chkvar 에 int 형으로 값을 저장
chkbox = Checkbutton(root, text = "오늘 하루 보지 않기", variable = chkvar)     # 체크 해제했을때의 값
#chkbox.select() # 자동 선택 처리 
#chkbox.deselect()
chkbox.pack()

chkvar2 = IntVar()
chkbox2 = Checkbutton(root, text = "일주일동안 보지 않기", variable = chkvar2)
chkbox2.pack()

def btncmd():  
    print(chkvar.get()) # 0 : 체크해제, 1 : 체크
    print(chkvar2.get())
    pass

btn = Button(root, text = "클릭", command = btncmd)
btn.pack()

root.mainloop()