from tkinter import Tk  #tkinter라는 파일에서 Tk() 함수가져오기
from tkinter import Canvas #tkinter라는 파일에서 Canvas가져오기
from PIL import Image #pillow 라는 모듈파일에서 Image 가져오기 
from PIL import ImageTk #pillow 라는 모듈파일에서 ImageTk 가져오기 
import time #time 모듈 가져오기 (일정 시간 간격으로 실행루프를 생성하기 위해)

from lib import ObjectManager # lib.py에서 ObjectManager 클래스를 가져오기
from lib import BgImage # lib.py에서 BgImage 클래스를 가져오기
from lib import Hero  # lib.py에서 BgImage 클래스를 가져오기
from lib import Enemy # lib.py에서 Enemy 클래스를 가져오기

#지난 시간에 거푸집을 프로그래밍 분야에서는 클래스라 한다.
class GameMain():
    def __init__(self): #모든 클래스가 반드시 가져야할 함수를 가리켜 생성자라한다..
                                #생성자는 거푸집으로부터 물건을 생성해 낼때 어떤 모양, 색상, 특징을 
                                #갖는지를 결정짓는 함수다..    
        self.gameFlag=True           
        self.enemyList=[] #적군을 차곡 차곡 쌓아놓을 상자 선언
                                   #이 상자는 배열이라 부르며, 첫번째 방이 0으로 인식됨 

        self.win=Tk() #윈도우창 호출하고, 그 윈도우를 가리킬 변수 선언
        self.canvas = Canvas(self.win, width=1400, height=800, bg="yellow") #켄버스 생성
        self.canvas.pack() #윈도우에 부착하기!!

        #ObjectManager 거푸집으로부터 ObjectManager 하나를 생성하자!!
        # 이때, ObjectManager 그림을 그릴 켄버스를 넘겨줘야 한다!!
        self.objectManager = ObjectManager(self.canvas)
        self.createBg()
        self.createHero()
        self.createEnemy()

        self.gameLoop() # 게임 엔진 가동시작!!
        self.win.mainloop() #윈도우가 사라지지않고 계속 유지될 수 있게 루프실행

    #게임에 사용할 이미지를 생성해주는 함수
    # 아래의 함수는 현재 GameMain이라는 클래스 안에 작성하고 있으므로, 
    # GameMain 클래스 소속임을 알려주기 위해 self 를 전달해줘야 한다..
    def getImage(self, path, width, height):
        img=Image.open(path) #Image객체의 open함수 호출
        #켄버스 크기에 맞도록 이미지 조정 
        img=img.resize((width, height) , Image.ANTIALIAS)
        #크기를 조정해서 만들어진 이미지를 켄버스에 사용할 수 있도록 가공 
        img=ImageTk.PhotoImage(img)
        return img #함수 호출한 사람이 그 결과를 가지고 갈수 있도록 결과 반환

    #배경을 탄생시킨다!!
    def createBg(self):
        img=self.getImage("./images/desert.jpg", 1400, 800) #배경에 사용할 이미지 얻기완료!!
        
        #BgImage라는 클래스 즉 거푸집으로부터 , 배경 객체 하나 만들기!!
        self.bgImage=BgImage(self.canvas, img, 0, 0 ,1400,800,0,0)
        
        #ObjectManager에게 지금 생성된 배경이미지 객체를 등록요청한다!!
        self.objectManager.addObject(self.bgImage)

    #주인공을 탄생시킨다!!
    def createHero(self):
        #너비100,높이60인 주인공 이미지 얻기
        img = self.getImage("./images/plane.png", 100,60) 
        #주인공 거푸집에서 주인공 한명을 탄생시켜보자!!
        self.hero = Hero(self.canvas, img, 100,100, 100, 60, 0, 0)
        #생성된 주인공을 켄버스에 그리도록 ObjectManager 등록요청
        self.objectManager.addObject(self.hero)

        # img = self.getImage("./images/plane.png", 200,120 )
        # self.hero2 = Hero(self.canvas,img, 600,200, 200,120,0,0)
        # self.objectManager.addObject(self.hero2)

    #적군을 등장시키는 함수
    def createEnemy(self):  
        #너비와 높이가 각각 80인 적군 이미지 가져오기!!
        for i in range(0,5):  # 0,1,2,3,4      
            img=self.getImage("./images/e"+str(i+1)+".png", 80, 80) 
            self.en = Enemy(self.canvas, img, 1300, 100+(i*100),80,80,-0.2,0)
            self.objectManager.addObject(self.en) #적군 등록을 요청
            #방금 생성된 적군을 상자에 순서대로 채워넣기!!
            self.enemyList.append(self.en)


    #게임루프 정의하기!!(게임의 심장박동, 즉 엔진과 같다)
    def gameLoop(self):
        #while문이 True인 동안 끝없이  엄청난 속도로 실행이 됨
        #속도가 너무 빠르면, 화면에 그림을 그리는 작업에 무리가 갈 수 있기 때문에
        #속도를 조절할 필요가 있다..time 모듈을 이용하여 우리가 원하는 시간 간격
        #으로 속도를 조절하겟다...1/1000초까지 표현가능하다
        while self.gameFlag:
            print("gameLoop 실행중..")

            #ObjectManager로 하여금 게임에 등장하는 모든 객체가 움직이도록 요청
            self.objectManager.tick() #변화량을 체크 
            self.objectManager.render() #화면에 다시 그려라

            self.win.update()#윈도우 화면을 다시 그리자!(변경 사항 반영)
            time.sleep(1/1000) #실행부를 1000분의 1초간격으로 실행되게..

GameMain() #거푸집으로부터, 물체 하나를 생성한다.. 
                    #주의) 클래스명에 함수표시를 한 함수가 바로 __init__을 의미 