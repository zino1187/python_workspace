from tkinter import * 

win = Tk()

x=0
   
def setCount():
    global x
    x+=1
    print("증가된 x는 ", x)
    canvas.delete(ALL)
    canvas.create_text(100,100,text=x , font=("Verdana", 30))

# frame = Frame(win, width=600,height=50)
bt = Button(win, text="카운터 증가", command=setCount)
canvas = Canvas(win, bg="yellow",width=600, height=550)

bt.pack()
canvas.pack()

win.mainloop()

