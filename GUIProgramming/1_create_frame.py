from tkinter import *

# tkinter 는 Tcl/Tk을 파이썬에 사용할 수 있도록 한 Lightweight GUI 모듈 
# Tcl(Tool Command Language) - 일종의 프로그래밍 언어
# Tk - 크로스 플랫폼에 사용되는 일종의 GUI 툴킷 
# tkinter는 파이썬 기본 내장되어있는 파이썬 표준 라이브러리
# 쉽고 간단한 GUI 프로그램 제작에 활용

root = Tk()
root.title("Nado GUI")
root.geometry("640 x 480")
#root.geometry("640x480+300+100")      # 가로 x 세로 + x좌표 + y좌표

root.resizable(False, False)    # x(너비), y(높이) 값 변경 불가 (창 크기 변경 불가)
                                # 크기 조절제한 
root.mainloop()