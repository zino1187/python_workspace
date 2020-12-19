from tkinter import Tk
from tkinter import Canvas
from PIL import Image
from PIL import ImageTk
import time
from gameobject import BgImage
from gameobject import Hero
from gameobject import Enemy
from gameobject import Bullet
from gameobject import ObjectManager


class GameMain():
    def __init__(self):
        self.gameFlag=True
        self.enemyList=[]
        self.bulletList=[]

        self.win = Tk()
        self.canvas = Canvas(self.win, width=1200, height=800)
        self.canvas.pack()

        self.objectManager=ObjectManager(self.canvas)
        self.createBg()
        self.createHero()
        self.createEnemy()
        self.win.bind("<Key>", self.keyDown)
        self.win.bind("<KeyRelease>", self.keyUp)

        self.gameLoop()
        self.win.mainloop()


    def keyDown(self, event):
        if event.keycode==37:
            self.hero.velX=-5
        if event.keycode==39:
            self.hero.velX=5
        if event.keycode==38:
            self.hero.velY=-5
        if event.keycode==40:
            self.hero.velY=5
        if event.keycode==32:
            self.fire()    
            print("발사")

    def keyUp(self, event):
        if event.keycode==37:
            self.hero.velX=0
        if event.keycode==39:
            self.hero.velX=0
        if event.keycode==38:
            self.hero.velY=0
        if event.keycode==40:
            self.hero.velY=0


    def getImage(self, path, width, height):
        img=Image.open(path) 
        img=img.resize((width, height), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        return img

    def createBg(self):
        img=self.getImage("./images/desert.jpg",1200,800)
        self.bgImage=BgImage(self.canvas, img, 0, 0, 1200,800, 0,0)
        self.objectManager.addObject(self.bgImage)

    def createHero(self):
        img=self.getImage("./images/plane.png",100,60)
        self.hero=Hero(self.canvas, img, 100,100, 100,60, 0,0)
        self.objectManager.addObject(self.hero)

    def createEnemy(self):
        for i in range(0,5):
            img=self.getImage("./images/e"+str(i+1)+".png",80,80)
            en=Enemy(self.canvas, img, 1100, 100+(100*i), 80,80,-1,0)
            self.enemyList.append(en)
            self.objectManager.addObject(en)

    def createBullet(self):
        img=self.getImage("./images/ball.png",20,20)
        bullet=Bullet(self, self.canvas, img, self.hero.x, self.hero.y,  20,20, 20,0)
        self.bulletList.append(bullet)
        self.objectManager.addObject(bullet)

    def fire(self):
        self.createBullet()

    def gameLoop(self):
        while self.gameFlag:                
            self.objectManager.tick()
            self.objectManager.render()

            # print("loop..")
            self.win.update()
            time.sleep(1/1000)
            

main = GameMain()