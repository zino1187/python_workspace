from tkinter import Tk
from PIL import Image 
from PIL import ImageTk
import time
from tkinter import Canvas
from objects import Hero
from objects import BgImage
from objects import Bullet
import objects

class Main():
    def __init__(self):
        self.gameFlag=True
        self.screenWidth=1600
        self.screenHeight=800
        self.backList=[] #리스트 선언
        self.bulletList=[] #총알 리스트
        self.textId=None #정보텍스트 아이디

        # ----------------------------------------------------------------
        # 객체 생성
        # ----------------------------------------------------------------
        self.win=Tk()
        self.canvas = Canvas(self.win, width=self.screenWidth,height=self.screenHeight)
        self.bgImg=self.getImage("./images/bg.png", self.screenWidth, self.screenHeight)
        self.backList.append(BgImage(self, self.canvas, self.bgImg, 0, 0, self.screenWidth, self.screenHeight, -0.4, 0))
        self.backList.append(BgImage(self, self.canvas, self.bgImg , self.screenWidth, 0, self.screenWidth, self.screenHeight, -0.4, 0))
        self.heroImg=self.getImage("./images/plane.png", 100,65)
        self.hero = Hero(self, self.canvas, self.heroImg, 100,100, 100, 65, 0, 0)
        self.bulletImg=self.getImage("./images/ball.png", 20, 20)

        self.canvas.pack()
        # 키보드 제어 
        self.win.bind("<Key>", self.keyDown)
        self.win.bind("<KeyRelease>", self.keyUp)

        # 실행
        self.gameLoop()    
        self.win.mainloop()

        # 이미지 생성 메서드
    def getImage(self, path, width, height):
        img = Image.open(path)
        img = img.resize((width, height), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        return img

    def tick(self):
        for back in self.backList:
            back.tick()
        
        self.hero.tick()
        self.showInfo("num "+str(len(self.bulletList)))

        for bullet in self.bulletList:
            self.showInfo(bullet)
            bullet.tick()

    def render(self):
        for back in self.backList:
            back.render()

        self.hero.render()

        for bullet in self.bulletList:
            bullet.render()

    def keyDown(self, event):
        if event.keycode==37:
            self.hero.velX=-10
        if event.keycode==39:
            self.hero.velX=10
        if event.keycode==38:
            self.hero.velY=-10
        if event.keycode==40:
            self.hero.velY=10
        if event.keycode==32:
            self.fire()    

    def keyUp(self, event):
        if event.keycode==37:
            self.hero.velX=0
        if event.keycode==39:
            self.hero.velX=0
        if event.keycode==38:
            self.hero.velY=0
        if event.keycode==40:
            self.hero.velY=0

    def fire(self):
        self.bulletList.append(Bullet(self, self.canvas, self.bulletImg, self.hero.x+(self.hero.width/2), self.hero.y , 20,20, 27, 0))

    def showInfo(self, info):
        self.canvas.delete(self.textId)
        self.textId = self.canvas.create_text(100,25, fill="red",font="verdana 30" , text=info)

    # GameLoop
    def gameLoop(self):
        while self.gameFlag:
            self.tick()
            self.render()
            time.sleep(1/1000)
            self.win.update()


main = Main()