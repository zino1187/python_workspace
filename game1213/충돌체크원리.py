from tkinter import Tk
from tkinter import Canvas
import time

class Main():
    def __init__(self):
        self.win=Tk()
        self.canvas = Canvas(self.win, width=800,height=600, bg="yellow")
        self.canvas.pack()
        self.objList=[] #게임에 등장한 오브젝트 리스트
        self.collisionSet=set()  #충돌객체 명단(중복 허용안함)

    def createRect(self):
        x1=100
        y1=100
        width1=100
        height1=100

        x2=300
        y2=300
        width2=100
        height2=100

        self.r1 = self.canvas.create_rectangle(x1, y1, x1+width1, y1+height1, fill="red")
        self.r2 = self.canvas.create_rectangle(x2, y2, x2+width2, y2+height2, fill="blue")
        self.box = self.canvas.create_rectangle(x1+20, y1+20, (x1+20)+30, (y1+20)+30, fill="black")
        #self.box = self.canvas.create_rectangle(x2+60, y2+60, (x2+60)+50, (y2+60)+50, fill="black")

    def collisionCheck(self):
        # objList=self.canvas.find_all()# 모든 오브젝트 구하기 
        # self.objList.append(self.r1)
        # self.objList.append(self.r2)

        # 충돌 체크용 오브젝트 
        
        # print(self.canvas.coords(self.box))
        # print(self.canvas.find_overlapping(*self.canvas.coords(self.r1)))
        # print(self.canvas.find_overlapping(*self.canvas.coords(self.r2)))
        # print(self.canvas.find_overlapping(*self.canvas.coords(self.box)))

        # size = len(self.canvas.find_overlapping(*self.canvas.coords(self.r2)))
        # print("size ",size)
        
        self.objList = self.canvas.find_all()

        for obj in self.objList:
            target= self.canvas.find_overlapping(*self.canvas.coords(obj))

            if len(target)>1 :
                print("size = ",target[0],"와 ", target[1]," 번째는 충돌중입니다")
                self.collisionSet.add(target[0])
                self.collisionSet.add(target[1])
            # if obj==target: 
            # print("발견")
        # obj = self.canvas.find_overlapping( self.canvas.coords(self.r1))
        # self.canvas.find_overlapping()
        
        print("충돌객체 명단 ", self.collisionSet)

        for item in self.collisionSet:
            self.canvas.delete(item)
            pass

    def gameLoop(self):
        pass
        time.sleep(1/1000)
        # self.collisionCheck()


main=Main()    
main.createRect()
main.collisionCheck()
main.gameLoop()
main.win.mainloop()