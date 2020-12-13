# 윈도우 창을 만들자!!
from tkinter import Tk #tkinter라는 파일에 들어있는 Tk 함수를 쓰겠다
from tkinter import Canvas #tkinter라는 파일에 들어있는 Canvas 함수를 쓰겠다
import time #time이라는 모듈파일을 쓰겠다!!
from PIL import Image
from PIL import ImageTk 
from gameobject import Hero #gameobject 모듈안에 있는 클래스 중에서 Hero 쓰겠다

# 이미지 생성 함수 : 이 함수를 호출하는 자는, 이미지를 얻어갈수 있도록...
def getImage(path, width, height): #함수를 호출하는 자가 path변수의 값을 결정할 수 있게 하자
    img=Image.open(path)  #Image 객체는 pillow 모듈파일에서 지원한다..따라서 현재 개발환경에
                            #설치가 되어 있어야 한다..
    #크기를 우리가 원하느 크기로 재조정하자!!!
    img=img.resize((width, height), Image.ANTIALIAS) #재조정된 이미지를 다시변수로받기
    #크기가 재조정된 이미지를 켄버스에서 사용할 수 있도록 가공 
    img = ImageTk.PhotoImage(img) #img를 켄버스가 이해할수있는 이미지로 변환
    return img #함수 호출한 사람에게 결과를 반환하자!!



#------------------------------------------------------------------
# 생성하기  
#------------------------------------------------------------------
win=Tk() #윈도우 생성하고 win 변수에 담아둔다
#윈도우에 소속시킬 켄버스를 생성하고, 그 크기를 너비1500,높이 800
canvas = Canvas(win, width=1500,height=800, bg="yellow")


# 배경 그리기 
bgImg = getImage("./images/desert.jpg", 1500, 800) #생성된 이미지를 다시 bgImg변수에 담음
#anchor="nw" 옵션을 추가해야, 이미지가 켄버스에 가득 채워진다
canvas.create_image(0, 0 , image=bgImg, anchor="nw")

#주인공 생성하기 
#canvas, img, x, y, width, height, velX, velY
heroImg = getImage("./images/plane.png", 100, 65)
hero=Hero(canvas, heroImg,100, 200,100,65,1,1) #거푸집(틀)로부터 주인공 탄생시키기

#------------------------------------------------------------------
# 그림 그리기 (켄버스에...)
#------------------------------------------------------------------


#주인공 그리기 
#heroImg = getImage("./images/plane.png", 100, 65)
#canvas.create_image(100, 100, image=heroImg)



#내가 원하는 크기로 윈도우창을 늘리자!
win.geometry("1500x800") #너비 1000, 높이 800

#켄버스 부착 
canvas.pack()


#게임의 정보를 출력하는 함수(점수, 적군수, 위치)
def showInfo():
    canvas.create_text(100,25, fill="red", font="verdana", text="Hello")

#게임루프를 실행하는 함수 정의 
#gameLoop() 라는 이름의 코드를 선언하고, 그 영역의 범위를 
# 들여쓰기(tab)를 통해 알린다
# def라고 불리는 영역을 함수라고 하는데, 함수는 반드시 호출해야
# 즉 이름을 불러줘야 일한다!!
# while문은 게임루프를 만드는데 사용하지만, 그 속도가 너무 빨라서
# 컴퓨터가 감당할 수 없다..우리가 원하는 것은 while문의 속도를
# 늦추는 것이다...해결책? 시간 간격을 만들어서 while문을 호출
def gameLoop():
    while True:
        print("gameLoop 호출")
        time.sleep(1/1000)  # 1/1000초까지 시간을 간격을 둘수있음
        #주인공의 움직임관련 함수를 호출하자
        hero.tick()
        hero.render()
        showInfo()
        win.update() #윈도우창을 갱신


gameLoop() #게임루프를 호출
#금방 닫혀버리는 윈도우창을 계속 떠있게 하자 
win.mainloop()