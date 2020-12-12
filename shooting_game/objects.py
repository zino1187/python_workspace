from PIL import Image
from PIL import ImageTk

class GameObject():
    def __init__(self, main, container, x, y , width, height, velX, velY):
        self.main=main
        self.container=container
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.velX=velX
        self.velY=velY

        # self.rect = self.container.create_rectangle(self.x, self.y, self.x+self.width , self.y+self.height, fill="red")
        print("w=", width, "h=", height)
        

class Hero(GameObject):
    def __init__(self, main, container,img, x, y , width, height, velX, velY):
        super().__init__(main, container, x, y , width, height, velX, velY)
        self.img=self.container.create_image(self.x, self.y, image=img)

    def tick(self):
        self.x+=self.velX
        self.y+=self.velY

    def render(self):
        # self.container.move(self.rect, self.velX ,self.velY)
        self.container.move(self.img, self.velX ,self.velY)


class BgImage(GameObject):
    def __init__(self, main, container, img, x, y , width, height, velX, velY):
        super().__init__(main , container, x, y , width, height, velX, velY)
        self.img=self.container.create_image(self.x, self.y, image=img, anchor="nw")

    def tick(self):
        pass

    def render(self):
        self.container.move(self.img, self.velX ,self.velY)


class Bullet(GameObject):                
    def __init__(self, main, container,img, x, y , width, height, velX, velY):
        super().__init__(main, container, x, y , width, height, velX, velY)
        self.img=self.container.create_image(self.x, self.y, image=img)

    def tick(self):
        self.x+=self.velX
        self.y+=self.velY
        #self.main.showInfo(str(len(self.main.bulletList)))
        self.main.showInfo(str(self.x))

        self.main.showInfo("pre :"+str(len(self.main.bulletList)))                
        if self.x > self.main.screenWidth-100:
            self.main.bulletList.remove(self) 
            self.container.delete(self.img)
            self.main.showInfo("post : "+str(len(self.main.bulletList)))                

    def render(self):
        self.container.move(self.img, self.velX ,self.velY)