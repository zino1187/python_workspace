from tkinter import *
from PIL import Image
from PIL import ImageTk
import time

import Bullet
import Hero

flag=True
velX=0 #스피드
velY=0 #스피드
x=0
y=0
w=50
targetX=700
a=0.05
bgX=0
hero=None
bullet=None

# 이미지선언
bgImg=None 
ballImg=None
heroImg=None
bulletList =[]

root=Tk()
canvas=Canvas(root, width=960, height=450)
canvas.pack(fill="both", expand=True)

# 배경이미지
def createBg():
    global bgImg
    bgImg=ImageTk.PhotoImage(Image.open("./images/desert.jpg"))

# 주인공 이미지
def createHero():
    global heroImg
    global canvas
    global hero

    img= Image.open("./images/plane.png")
    img = img.resize((120,75) , Image.ANTIALIAS)
    heroImg=ImageTk.PhotoImage(img)
    hero = Hero.Hero(canvas, heroImg, 300, 200, 120, 75, 0, 0) #주인공 생성

# 총알 이미지
def createBullet():
    global ballImg
    img= Image.open("./images/ball.png")
    img = img.resize((30,30) , Image.ANTIALIAS)
    ballImg=ImageTk.PhotoImage(img)

createBg()
createHero()
createBullet()

def pressDown(event):
	# print(event)
	if event.keycode == 37 :
		hero.velX=-5
	if event.keycode == 39 :
		hero.velX=5
	if event.keycode == 38 :
		hero.velY=-5
	if event.keycode == 40 :
		hero.velY=5
	if event.keycode == 32 :
		fire()


def pressUp(event):
	# print(event)
	if event.keycode == 37 :
		hero.velX=0
	if event.keycode == 39 :
		hero.velX=0
	if event.keycode == 38 :
		hero.velY=0
	if event.keycode == 40 :
		hero.velY=0

def fire():
    print("발사를 원해?")
    # 총알 클래스로 부터 총알을 생성하자!!
    global bullet
    global ballImg
    global canvas 
    bullet = Bullet.Bullet(canvas, ballImg, hero.x, hero.y, 30,30, 20,0)
    bulletList.append(bullet)



def tick():
    # print("tick() called...")
    # print(x)
    global hero
    global bullet

    if hero !=None:
        hero.tick()

    for bullet in bulletList:
        bullet.tick()

def render():    
    # print("render() called...")
    # canvas.create_image(100+x, 200+y, image=bg2)
    if hero !=None:
        hero.render()

    for bullet in bulletList:
        bullet.render()

def bgEffect():
    global bgX
    # bgX=bgX-2
    canvas.create_image(bgX,0, image=bgImg, anchor="nw")

#게임루프 함수
def gameLoop():
    while flag:
        # print("gameLoop()...")
        canvas.delete(ALL)
        bgEffect()
        tick()
        render()
        # move()
        time.sleep(10/1000)
        root.update()
	# for i in range(1,10000):
	# 	#print("gameLoop()...")
	# 	move()
	# 	time.sleep(10/1000)


# createRect(x,y, x+w, y+w,"red")



#<KeyUp> 으로 명시하면 방향키 위를 의미
root.bind("<Key>", pressDown)
root.bind("<KeyRelease>", pressUp)

gameLoop()
root.mainloop()