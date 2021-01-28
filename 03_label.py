from tkinter import *

root = Tk()
root.title("Hello GUI") 

label = Label(root, text="안녕하세요")
label.pack()

photo = PhotoImage(file="image/check.png")
label2 = Label(root, image=photo)
label2.pack()

def change():
    label.config(text="또 만나요")
    
    global photo2 # garbage collection 방지
    photo2 = PhotoImage(file="image/cancel.png")
    label2.config(image=photo2)

btn = Button(root, text="클릭", command=change)
btn.pack()



root.mainloop()

