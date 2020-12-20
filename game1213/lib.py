#모든 게임에 등장할 게임오브젝트의 최상위 클래스 
class GameObject():
    def __init__(self, canvas, x, y, width, height, velX, velY):
        self.canvas=canvas
        self.x=x
        self.y=y
        self.width=width 
        self.height=height
        self.velX=velX
        self.velY=velY

#게임에 등장할 오브젝트 중 , 배경 오브젝트 
class BgImage(GameObject):
    def __init__(self, canvas, img, x, y, width, height, velX, velY):
        super().__init__(canvas,x, y ,width, height, velX, velY)
        self.img=img
        self.image = self.canvas.create_image(self.x, self.y, image=self.img, anchor="nw")
        print("생성된 이미지 ", self.image )

    def tick(self):
        self.x = self.x + self.velX
        self.y = self.y + self.velY
        # print("BgImage tick()..", self.x)
    
    def render(self):
        self.canvas.move( self.image , self.velX, self.velY)

#주인공 클래스
class Hero(GameObject):
    def __init__(self, canvas, img, x, y, width, height, velX, velY):
        super().__init__(canvas,x, y ,width, height, velX, velY)
        self.img=img
        self.image = self.canvas.create_image(self.x, self.y, image=self.img)
        print("생성된 이미지 ", self.image )

    def tick(self):
        self.x = self.x + self.velX
        self.y = self.y + self.velY
    
    def render(self):
        self.canvas.move( self.image , self.velX, self.velY)


class Enemy(GameObject):
    def __init__(self, canvas, img, x, y, width, height, velX, velY):
        super().__init__(canvas,x, y ,width, height, velX, velY)
        self.img=img
        self.image = self.canvas.create_image(self.x, self.y, image=self.img)

    def tick(self):
        self.x = self.x + self.velX
        self.y = self.y + self.velY
    
    def render(self):
        self.canvas.move( self.image , self.velX, self.velY)


class Bullet(GameObject):
    def __init__(self, game_main, canvas, img, x, y, width, height, velX, velY):
        super().__init__(canvas,x, y ,width, height, velX, velY)
        self.game_main=game_main
        self.img=img
        self.image = self.canvas.create_image(self.x, self.y, image=self.img)

    def tick(self):
        self.x = self.x + self.velX
        self.y = self.y + self.velY

        # self.game_main.objectManager.createCollisionSet()
        # self.game_main.objectManager.removeObject(self)

    
    def render(self):
        self.canvas.move( self.image , self.velX, self.velY)



class ObjectManager():
    def __init__(self, canvas):
        self.canvas=canvas
        self.objectList=[] #게임에 등장할 오브젝트 리스트
        self.collisionSet=set()  #충돌객체 명단(중복 허용안함)

    #-----------------------------------------
    # 객체 추가
    #-----------------------------------------
    def addObject(self, gameObject):
        self.objectList.append(gameObject)
        print(self.objectList)


    #-----------------------------------------
    # tick , render
    #-----------------------------------------
    def tick(self):
        for obj in self.objectList:
            obj.tick()

    def render(self):
        for obj in self.objectList:
            obj.render()

    #-----------------------------------------
    # 충돌체크 명단 작성
    #-----------------------------------------
    def createCollisionSet(self):
        for obj in self.objectList:
            #켄버스내에 모든 객체를 대상으로 중첩되는 무언가가 있는지 체크
            target= self.canvas.find_overlapping(*self.canvas.coords(obj)) 

            if len(target)>1 :
                print("size = ",target[0],"와 ", target[1]," 번째는 서로 교차됩니다")
                self.collisionSet.add(target[0])
                self.collisionSet.add(target[1])

    #-----------------------------------------
    # 충돌 객체 제거 : gameObject에 지울 대상 객체를 인수로 넘긴다
    #-----------------------------------------
    def removeObject(self, gameObject):
        for item in self.collisionSet:
            if item==gameObject.image:
                self.canvas.delete(item)
