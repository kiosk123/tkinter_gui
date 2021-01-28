from tkinter import *

root = Tk()
root.title("Hello GUI") # 창 타이틀 설정
root.geometry("640x480+100+300") # 가로x세로+x좌표+y좌표

txt = Text(root, width=30, height=5)
txt.pack()

# txt.insert(END, "글자를 입력하세요")
txt.insert(index=END, chars="글자를 입력하세요")

e = Entry(root, width=30) # 한줄에 입력받을 때 사용
e.pack()
e.insert(0, "한 줄만 입력해요")

def btncmd():
    print(txt.get("1.0", END)) # 첫번째줄(1).0번째컬럼(0) 부터 끝까지 텍스트 가져오기
    print(e.get())

    # 내용 삭제
    txt.delete("1.0", END)
    e.delete(0, END)

btn = Button(root, text="click", command=btncmd)
btn.pack()

root.mainloop()

