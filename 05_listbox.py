from tkinter import *

root = Tk()
root.title("Hello GUI") # 창 타이틀 설정
root.geometry("640x480+100+300") # 가로x세로+x좌표+y좌표

# selectmode=(extended 여러개 선택가능, single 하나만 선택가능), height=(0 리스트박스의 모든 내용 출력, n 리스트박스의 내용 n개발 출력)
listbox = Listbox(root, selectmode="extended", height=0)
listbox.insert(0, "사과")
listbox.insert(1, "딸기")
listbox.insert(2, "바나나")
listbox.insert(END, "수박")
listbox.insert(END, "포도")
listbox.pack()

def btncmd():
    # listbox.delete(END) #리스트박스 맨 뒤 삭제
    # listbox.delete(0) #리스트박스 맨 앞 삭제

    print("리스트 박스 아이템 개수 :", listbox.size())

    print("1번째 부터 3번째까지 항목 :", listbox.get(0,2))

    print("선택된 항목 확인 :", listbox.curselection()) # 인덱스 값 반환

    

btn = Button(root, text="click", command=btncmd)
btn.pack()

root.mainloop()

