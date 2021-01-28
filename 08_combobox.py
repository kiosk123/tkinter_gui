from tkinter import *
import tkinter.ttk as ttk

root = Tk()
root.title("Hello GUI") # 창 타이틀 설정
root.geometry("640x480+100+300") # 가로x세로+x좌표+y좌표

values = [str(i) + "일" for i in range(1, 32)]
combobox = ttk.Combobox(root, height=5, values=values, state="readonly")
combobox.pack()
combobox.set("카드 결제일") # 최초 목록 제목 설정

def btncmd():
    print(combobox.get()) # 선택된 값 출력

btn = Button(root, text="select", command=btncmd)
btn.pack()

root.mainloop()

