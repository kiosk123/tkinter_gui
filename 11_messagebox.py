import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()
root.title("Hello GUI") # 창 타이틀 설정
root.geometry("640x480+100+300") # 가로x세로+x좌표+y좌표

def info():
    msgbox.showinfo("알림", "정상적으로 예매 완료되었습니다.")

Button(root, command=info, text="알림").pack()

root.mainloop()

