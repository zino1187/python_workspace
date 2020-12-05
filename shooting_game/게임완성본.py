from tkinter import *
from tkinter import Tk
from PIL import Image
from PIL import ImageTk
import time
import Hero
import BG
import Enemy
import Bullet

win = Tk()

# 이미지 생성해주는 함수
def getImage(path, width, height):
    img = Image.open(path)
    img = img.resize((width,height), Image.ANTIALIAS)    
    return ImageTk.PhotoImage(img)

def tick():
    for bg in bgList:
        bg.tick()

    for enemy in enemyList:
        enemy.tick()
    for bullet in bulletList:
        bullet.tick()
    hero.tick()

def render():    
    for bg in bgList:
        bg.render()
    for enemy in enemyList:
        enemy.render()
    for bullet in bulletList:
        bullet.render()
    hero.render()

def fire():
    print("발사")
    bulletList.append(Bullet.Bullet(canvas, getImage("./images/ball.png", 20, 20), hero.x, hero.y , 20,20,10,0)) 

def keyDown(event):
    print("keyDown")
    if event.keycode==37:
        hero.velX=-5
    if event.keycode==39:
        hero.velX=5
    if event.keycode==38:
        hero.velY=-5
    if event.keycode==40:
        hero.velY=5
    if event.keycode==32:
        fire()

def keyUp(event):
    print("keyUp")
    if event.keycode==37:
        hero.velX=0
    if event.keycode==39:
        hero.velX=0
    if event.keycode==38:
        hero.velY=0
    if event.keycode==40:
        hero.velY=0


# 게임루프
def gameLoop():
    while gameFlag:
        # 여기서 순서가 중요하다, 캔버스지우기 > 배경 그리기> 게임오브젝트 올리기 > 윈도우 갱신
        canvas.delete(ALL)
        tick()
        render()
        time.sleep(1/1000)
        win.update()
        # print("gameLoop called..")

#----------------------------------------------------------------------
# 생성 
#---------------------------------------------------------------------- 
gameFlag=True
canvas = Canvas(win,bg="red", width=1280, height=960) #캔버스
bgImg = getImage("./images/desert.jpg", 1280, 960)#배경이미지
heroImg = getImage("./images/plane.png", 90,45)#주인공 이미지
enemyList=[] #적군리스트
enemyPath=["e1.png","e2.png","e3.png","e4.png","e5.png"]
bulletList=[] #총알 리스트
bgList=[] #배경 리스트

# 배경생성
bgList.append(BG.BG(canvas, bgImg, 0, 0 ,1280,960,-10,0))
bgList.append(BG.BG(canvas, bgImg, 1280, 0 ,1280,960,-10,0))

# 적군생성
for i in range(0, len(enemyPath)-1):
    enemyList.append(Enemy.Enemy(canvas, getImage("./images/"+enemyPath[i], 65, 60), 1000, 200+(100*i) , 65,60,-1,0))

#주인공 생성    
hero = Hero.Hero(canvas, heroImg, 100, 100, 90, 45, 0, 0) #주인공 생성

#스타일

# 조립
canvas.pack()

#이벤트 연결 
win.bind("<Key>", keyDown)
win.bind("<KeyRelease>", keyUp)

gameLoop()
win.mainloop()