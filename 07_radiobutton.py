from tkinter import *

root = Tk()
root.title("Hello GUI") # 창 타이틀 설정
root.geometry("640x480+100+300") # 가로x세로+x좌표+y좌표

Label(root, text="메뉴를 선택하세요").pack()

burger_var = IntVar() # 여기에 int형으로 값 저장하며 RadioButton끼리 공유
btn_burger1 = Radiobutton(root, text="햄버거", value=1, variable=burger_var)
btn_burger2 = Radiobutton(root, text="치즈버거", value=2, variable=burger_var)
btn_burger3 = Radiobutton(root, text="치킨버거", value=3, variable=burger_var)

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()

drink_var = IntVar()
btn_drink1 = Radiobutton(root, text="콜라", value=1, variable=drink_var)
btn_drink2 = Radiobutton(root, text="사이다", value=2, variable=drink_var)
btn_drink3 = Radiobutton(root, text="환타", value=3, variable=drink_var)

btn_drink1.pack()
btn_drink2.pack()
btn_drink3.pack()

def btncmd():
    print(burger_var.get())
    print(drink_var.get())

btn = Button(root, text="order", command=btncmd)
btn.pack()

root.mainloop()

