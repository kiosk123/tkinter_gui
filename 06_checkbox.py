from tkinter import *

root = Tk()
root.title("Hello GUI") # 창 타이틀 설정
root.geometry("640x480+100+300") # 가로x세로+x좌표+y좌표

chkvar = IntVar() # chkvar에 int형으로 값을 저장
chkbox = Checkbutton(root, text="오늘 하루 보지 않기", variable=chkvar)

chkbox.select() # 선택 처리
chkbox.deselect() # 선택 해제 처리

chkbox.pack()

chkvar2 = IntVar() # chkvar에 int형으로 값을 저장
chkbox2 = Checkbutton(root, text="일주일동안 보지 않기", variable=chkvar2)
chkbox2.pack()

def btncmd():
    print(chkvar.get()) # 1 or 0
    print(chkvar2.get())

btn = Button(root, text="click", command=btncmd)
btn.pack()

root.mainloop()

