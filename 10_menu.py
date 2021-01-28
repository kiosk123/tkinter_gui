import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("Hello GUI") # 창 타이틀 설정
root.geometry("640x480+100+300") # 가로x세로+x좌표+y좌표

def create_new_file():
    print("create new file")

menu = Menu(root);

# File Menu
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="New File", command=create_new_file)
menu_file.add_command(label="New Window")
menu_file.add_separator()
menu_file.add_command(label="Open File...")
menu_file.add_separator()
menu_file.add_command(label="Save All", state="disable") # 비활성화
menu_file.add_separator()
menu_file.add_command(label="Exit", command=root.quit)

menu.add_cascade(label="File", menu=menu_file)

# Edit Menu
menu.add_cascade(label="Edit")

# Language Menu
menu_lang = Menu(menu, tearoff=0)
menu_lang.add_radiobutton(label="Python")
menu_lang.add_radiobutton(label="Java")
menu_lang.add_radiobutton(label="C++")
menu.add_cascade(label="Language", menu=menu_lang)

# View Menu
menu_view = Menu(menu, tearoff=0)
menu_view.add_checkbutton(label="Show Minimap")
menu.add_cascade(label="View", menu=menu_view)




root.config(menu=menu)
root.mainloop()

