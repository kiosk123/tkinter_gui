from tkinter import *
import tkinter.ttk as ttk

root = Tk()
root.title("Hello GUI") # 창 타이틀 설정
root.geometry("640x480+100+300") # 가로x세로+x좌표+y좌표

# mode="indeterminate" 로딩중등을 표시할 때 사용
progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate")
progressbar.start(10) # 10ms 마다 움직음
progressbar.pack()

# mode="determinate" 진행상황을 표시할때 사용
progressbar1 = ttk.Progressbar(root, maximum=100, mode="determinate")
progressbar1.start(10) # 10ms 마다 움직음
progressbar1.pack()

p_var2 = DoubleVar()
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar2.pack()

def btncmd():
    # progressbar1.stop() # 프로그래스바 멈춤
    for i in range(101):
        import time
        time.sleep(0.01)
        p_var2.set(i) # 0 ~ 100까지 올라가도록 값설정
        progressbar2.update() # 프로그레스바 진행 상황(ui) 업데이트
        print("현재 {}%까지 진행됨".format(p_var2.get()))

btn = Button(root, text="click", command=btncmd)
btn.pack()

root.mainloop()

