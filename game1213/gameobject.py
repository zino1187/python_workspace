#우리가 지금 만든 파일을 파이썬에서는 모듈이라 부른다~!
#이 모듈안에 주인공, 총알, 적군, 아이템, 배경 등등..게임에 등장하는 모든 케릭터 및
#사물들을 정의해놓고 써먹을 꺼임..

#주인공을 만들자!!
#클래스란? 사물 자체가 아니라, 사물을 여러개 생성할 수 있는 틀이다(거푸집과 같다)
#it분에서는 틀을 가리켜 클래스라 한다!!
class Hero(): #Hero라는 이름의 클래스 선언 
    #어떤 켄버스에 부착할지,어떤이미지(img), 위치(x,y), 크기(width, height), 움직임속도(velX, velY)
    def __init__(self, canvas, img, x, y, width, height, velX, velY): #주인공이 탄생할때 작성하고 싶은 코드를 넣는 함수 영역
                          # 주인공의 색상이 빨간색으로 할지, 크기는 어떻게 할지 등등...  
        self.canvas=canvas
        self.img=img
        self.x=x
        self.y=y
        self.width=width 
        self.height=height
        self.velX=velX  #주인공의 x방향의 속도
        self.velY=velY #주인공의 y방향의 속도

    #주인공의 동작관 관련한 함수 정의 
    def tick(self): #주인공의 상태를 얼만큼 변화시킬지를 결정, 예) 2씩, 3씩 움직일지..
        self.x = self.x + self.velX
        self.y = self.y + self.velY

    def render(self):
        #주인공의 변경값을 켄버스에 다시 그리기!! (움직일대상이미지, x, y)
        self.canvas.move( self.img , self.velX, self.velY)


#총알을 만들자!!