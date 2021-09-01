from tkinter import Label, Tk
import time

app_window = Tk()   # 함수 정의
app_window.title("My Digital Time")    # 제목
app_window.geometry("350x150")  # 창의 크기 
app_window.resizable(0,0)   # 창 크기 변할 때 디자인 이상하지 않게 함 

# 사용자 정의 4가지 1. 디지털 숫자의 글꼴 2. 시계의 배경색 3. 텍스트의 테두리 너비 4. 숫자와 배경 동일 색상인가? 

text_font = ("LG PC", 68, 'bold')
background = "#f2e750"
foreground = "#363529"
border_width = 25

# 시간 보여주는 텍스트 
label = Label(app_window, font = text_font, bg = background, fg = foreground, bd = border_width)
label.grid(row = 0, column = 1) 

# 디지털 시계 기능 정의 
def digital_clock():
    time_live = time.strftime("%H:%M:%S")
    label.config(text=time_live) 
    label.after(200, digital_clock) 

digital_clock()
app_window.mainloop() 



