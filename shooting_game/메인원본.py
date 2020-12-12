from tkinter import Tk
from PIL import Image 
from PIL import ImageTk
import time
from tkinter import Canvas
from objects import Hero
from objects import BgImage
from objects import Bullet
import objects

# from mymodule import getMsg
# from mymodule import Dog

# 전역변수 
gameFlag=True
screenWidth=1600
screenHeight=800
back=[] #리스트 선언
bulletList=[] #총알 리스트
textId=None #정보텍스트 아이디

# 이미지 생성 함수 
def getImage(path, width, height):
    img = Image.open(path)
    img = img.resize((width, height), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    return img

# ----------------------------------------------------------------
# 객체 생성
# ----------------------------------------------------------------
win=Tk()
canvas = Canvas(win, width=screenWidth,height=screenHeight)

bgImg=getImage("./images/bg.png", screenWidth,screenHeight)
back.append(BgImage(canvas, bgImg, 0, 0, screenWidth, screenHeight, -0.4, 0))
back.append(BgImage(canvas, bgImg , screenWidth, 0, screenWidth, screenHeight, -0.4, 0))

heroImg=getImage("./images/plane.png", 100,65)
hero = Hero(canvas, heroImg, 100,100, 100, 65, 0, 0)

bulletImg=getImage("./images/ball.png", 20, 20)


# ----------------------------------------------------------------
# 스타일
# ----------------------------------------------------------------


# ----------------------------------------------------------------
# 부착
# ----------------------------------------------------------------
canvas.pack()


# ----------------------------------------------------------------
# 함수 정의
# ----------------------------------------------------------------
def tick():
    for i in range(0, len(back)):
        back[i].tick()
    
    hero.tick()

    for i in range(0, len(bulletList)):
        bulletList[i].tick()

def render():
    for i in range(0, len(back)):
        back[i].render()

    hero.render()

    for i in range(0, len(bulletList)):
        bulletList[i].render()

def keyDown(event):
    if event.keycode==37:
        hero.velX=-10
    if event.keycode==39:
        hero.velX=10
    if event.keycode==38:
        hero.velY=-10
    if event.keycode==40:
        hero.velY=10
    if event.keycode==32:
        fire()    

def keyUp(event):
    if event.keycode==37:
        hero.velX=0
    if event.keycode==39:
        hero.velX=0
    if event.keycode==38:
        hero.velY=0
    if event.keycode==40:
        hero.velY=0

def fire():
    bulletList.append(Bullet(canvas, bulletImg, hero.x+(hero.width/2), hero.y , 20,20, 27, 0))

def showInfo():
    global textId
    textId = canvas.create_text(50,25, fill="red",font="verdana 30" , text=str(len(bulletList)))

# GameLoop
def gameLoop():
    while gameFlag:
        tick()
        render()
        canvas.delete(textId)
        showInfo()
        time.sleep(1/1000)
        win.update()

# 키보드 제어 
win.bind("<Key>", keyDown)
win.bind("<KeyRelease>", keyUp)

# 실행
gameLoop()    
win.mainloop()