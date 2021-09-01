import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")


# showerror 경고 표시 
# #askokcancel 확인 과 취소 나타냄
#기차 예매 시스템 가정
def info():
    msgbox.showinfo("알림","정상적으로 예매 완료")  # (상태 창 , 메세지 창)

def warn():
    msgbox.showwarning("경고","해당 좌석 매진")

def error():
    msgbox.showerror("에러","오류 발생")

def okcancel():
    msgbox.askokcancel("확인 / 취소","해당 좌석은 유아동반석입니다. 예매하시겠습니까?") 

def retrycancel():
    msgbox.askretrycancel("재시도 / 취소","일시적 오류. 다시 시도하시겠습니까?") 

def yesno():
    msgbox.askyesno("yes / no ","해당 좌석은 역방향입니다. 예매하시겠습니까?")

def yesnocancel():
    response = msgbox.askyesnocancel(title = None, message = "예매 내역이 저장되지 않았습니다. \n저장 후 프로그램을 다시 실행하십니까?")
    # 네 : 저장 후 종료
    # 아니오 : 저장하지 않고 종료
    # 취소 : 프로그램 종료 취소
    print("응답:", response) # True, False, None --> 예 1 , 아니오 0 그외
    if response == 1: # 네, ok
        print("예")
    elif response == 0: # 아니오
        print("아니오")
    else:
        print("취소")


Button(root, command = info, text = "알림").pack()  # 버튼의 이름 설정 
Button(root, command = warn, text = "경고").pack()
Button(root, command = error, text = "에러").pack()

Button(root, command = okcancel, text = "확인 취소").pack()
Button(root, command = retrycancel, text = "재시도 취소").pack()
Button(root, command = yesno, text = "예 아니오").pack()
Button(root, command = yesnocancel, text = "예 아니오 취소").pack()


root.mainloop()