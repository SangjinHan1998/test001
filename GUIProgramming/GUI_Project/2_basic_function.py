import tkinter.ttk as ttk
import tkinter.messagebox as msgbox     # 메세지박스 생성 
from tkinter import *   # *을 통해 tkinter의 모든 모듈 사용 __all__(이곳에 정의하지 않으면 사용 x?)
from tkinter import filedialog # 서브모듈이라 별도로 해야함 + 파일/디렉터리 선택 창을 만들기위한 클래스와 팩토리 함수를 제공

root = Tk()
root.title("Nado GUI")

# 파일 추가
def add_file(): # askopenfilenames = 복수갤의 파일 선택 
    files = filedialog.askopenfilenames(title = "이미지 파일을 선택하세요.", \
        filetypes =(("PNG 파일", "*.png"), ("모든 파일", "*.*")), \
        initialdir = r"C:\Users\sangj\Downloads")
        # r 추가해서 경로 그대로 사용한다는 의미 
        # 최초의 사용자 지정 경로를 보여줌 
        # 이미지는 png형식 이름은 .png로 남는다. 

    # 사용자가 선택한 파일 목록 
    for file in files:
        list_file.insert(END, file) # 파일 목록 출력

# 선택 삭제
def del_file():
    # print(list_file.curselection())  curselection() 선택 항목 튜플로 반환 
    for index in reversed(list_file.curselection()):    
    # 역으로 출력 
        list_file.delete(index)

# 저장 경로 (폴더) 
def browse_dest_path():
    folder_selected = filedialog.askdirectory()   # 폴더 선택 창
    if folder_selected == '':   # 사용자가 취소를 누를 때 
        return 
    # print(folder_selected)
    txt_dest_path.delete(0, END)
    txt_dest_path.insert(0, folder_selected)

# 시작
def start(): 
    # 각 옵션들 값을 확인 
    print("가로넓이 : ", cmb_width.get())
    print("간격 : ", cmb_space.get())
    print("포맷 : ", cmb_format.get())

    # 파일 목록 확인 
    if list_file.size() == 0: 
        msgbox.showwarning("경고", "이미지 파일 추가할것")
        return

    # 저장 경로 확인 
    if len(txt_dest_path.get()) == 0:   
        # 문자열의 길이가 0일때
        msgbox.showwarning("경고", "저장 경로 추가할것")
        return

# 파일 프레임 (파일 추가, 선택 삭제)

file_frame = Frame(root) 
file_frame.pack(fill = "x", padx = 5, pady = 5) # 파일추가 선택삭제 사이 벌어지게함 간격 띄우기 추가 

btn_add_file = Button(file_frame, padx = 5, pady = 5, width = 12, text="파일추가", command = add_file)
btn_add_file.pack(side="left") 

# command 함수 -->  이벤트가 발생하면 실행한다. 

btn_del_file = Button(file_frame, padx = 5, pady = 5, width = 12, text="선택삭제", command = del_file)
btn_del_file.pack(side="right")

# 리스트 프레임 
list_frame = Frame(root) 
list_frame.pack(fill = "both", padx = 5, pady = 5) 

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side = "right", fill = "y")

list_file = Listbox(list_frame, selectmode = "extended", height = 15, yscrollcommand = scrollbar.set)  
list_file.pack(side = "left", fill = "both", expand = True)
scrollbar.config(command = list_file.yview)

# 저장 경로 프레임 
path_frame = LabelFrame(root, text = "저장경로")
path_frame.pack(fill = "x", padx=5, pady=5, ipady = 5) # 경로의 칸을 최대한 늘려주었음 

txt_dest_path = Entry(path_frame)   # "1.0" END
txt_dest_path.pack(side = "left", fill = "x", expand = True, padx=5, pady=5, ipady=4) # ipad 높이 조절

btn_dest_path = Button(path_frame, text = "찾아보기", width=10 ,command = browse_dest_path)
btn_dest_path.pack(side = "right", padx=5, pady=5)

# 옵션 프레임 
frame_option = LabelFrame(root, text = "옵션") 
frame_option.pack(padx = 5, pady = 5, ipady = 5) 

# 1. 가로 넓이 옵션 
# 가로 넓이 레이블
lbl_width = Label(frame_option, text = "가로넓이", width = 8)
lbl_width.pack(side = "left", padx = 5, pady = 5)

# 가로 넓이 콤보
opt_width = ["원본유지", "1024", "800", "640"]
cmb_width = ttk.Combobox(frame_option, state = "readonly", values = opt_width, width = 10)
cmb_width.current(0)
cmb_width.pack(side="left", padx = 5, pady = 5)

# 2. 간격 옵션
# 간격 옵션 레이블  
lbl_space = Label(frame_option, text = "간격", width = 8)
lbl_space.pack(side = "left", padx = 5, pady = 5)

# 간격 옵션 콤보 

opt_space = ["없음", "좁게", "보통", "넓게"]
cmb_space = ttk.Combobox(frame_option, state = "readonly", values = opt_space, width = 10)
cmb_space.current(0)
cmb_space.pack(side="left", padx = 5, pady = 5)

# 3. 파일 포멧 옵션 
# 파일 포맷 옵션 레이블 

lbl_format = Label(frame_option, text = "포맷", width = 8)
lbl_format.pack(side = "left", padx = 5, pady = 5)

# 파일 포맷 옵션 콤보 

opt_format = ["PNG", "JPG", "BMP"]
cmb_format = ttk.Combobox(frame_option, state = "readonly", values = opt_format, width = 10)
cmb_format.current(0)
cmb_format.pack(side="left", padx = 5, pady = 5)

# 진행 상황 Progress Bar
frame_progress = LabelFrame(root, text = "진행상황") 
frame_progress.pack(fill = "x", padx = 5, pady = 5, ipady = 5)  

p_var = DoubleVar()
progress_bar = ttk.Progressbar(frame_progress, maximum = 100, variable = p_var) 
progress_bar.pack(fill = "x", padx = 5, pady = 5)

# 실행 프레임 
frame_run = Frame(root) 
frame_run.pack(fill = "x", padx = 5, pady = 5) 

btn_close = Button(frame_run, padx = 5, pady = 5, text = "닫기", width = 12, command = root.quit)
btn_close.pack(side = "right", padx = 5, pady = 5) # 오 -> 왼 기준으로 가장 첫번째이자 가장 오른쪽(stack) 

btn_start = Button(frame_run, padx = 5, pady = 5, text = "시작", width = 12, command = start)
btn_start.pack(side = "right", padx = 5, pady = 5) # 오 -> 왼 기준으로 가장 첫번째이자 가장 오른쪽(stack) 


root.resizable(False, False)    # x(너비), y(높이) 값 변경 불가 (창 크기 변경 불가)
                                # 크기 조절제한 
root.mainloop()