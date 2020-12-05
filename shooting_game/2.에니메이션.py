from tkinter import *
from PIL import Image
from PIL import ImageTk

win=Tk()
x=0

def prev():
    global x 
    global img
    x -=1
    canvas.delete(ALL)    
    img=Image.open("./images/girl/"+str(x)+".png")
    img=ImageTk.PhotoImage(img)
    canvas.create_text(100,50, text=str(x)+".png", font=("Verdana", 50))
    canvas.create_image(300,300, image=img)
    win.update()

def next():
    global x 
    global img
    x +=1
    canvas.delete(ALL)    
    img=Image.open("./images/girl/"+str(x)+".png")
    img=ImageTk.PhotoImage(img)
    canvas.create_text(100,50, text=str(x)+".png", font=("Verdana", 50))
    canvas.create_image(300,300, image=img)
    win.update()

bt=Button(win, text="다음이미지", command=next)
bt2=Button(win, text="이전이미지", command=prev)

canvas=Canvas(win, bg="yellow", width=800, height=800)

next()
canvas.pack()
bt.pack()
bt2.pack()

win.mainloop()