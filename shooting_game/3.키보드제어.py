from tkinter import *
from PIL import Image
from PIL import ImageTk

x=100
y=50

# 함수정의 
def moveLeft():
    print("Left")
    

def moveRight():
    print("Right")
    global x
    global y
    x+=5
    canvas.delete(ALL) 
    canvas.create_image(x,y, image=heroImg)
    
def moveUp():
    print("Up")
def moveDown():
    print("Down")

# 생성
win = Tk()
frame = Frame(win)
leftBt=Button(frame, text="Left", command=moveLeft)
upBt=Button(frame, text="Up", command=moveUp)
downBt=Button(frame, text="Down", command=moveDown)
rightBt=Button(frame, text="Right", command=moveRight)
canvas = Canvas(win, bg="yellow", width=800, height=650)

img=Image.open("./images/plane.png")
img  = img.resize((120,70), Image.ANTIALIAS)
heroImg=ImageTk.PhotoImage(img)


# 스타일 
win.geometry("800x700")

# 조립 
leftBt.grid(row=0, column=0)
rightBt.grid(row=0, column=1)
upBt.grid(row=0, column=2)
downBt.grid(row=0, column=3)

def render():
    canvas.create_image(100,50,image=heroImg)

frame.pack()
canvas.pack()
render()

win.mainloop()