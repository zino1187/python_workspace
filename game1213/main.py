# 윈도우 창을 만들자!!
from tkinter import Tk #tkinter라는 파일에 들어있는 Tk 함수를 쓰겠다
from tkinter import Canvas #tkinter라는 파일에 들어있는 Canvas 함수를 쓰겠다
import time #time이라는 모듈파일을 쓰겠다!!
from PIL import Image
from PIL import ImageTk 

# 이미지 생성 함수 : 이 함수를 호출하는 자는, 이미지를 얻어갈수 있도록...
def getImage():
    img=Image.open("./images/desert.jpg")  #Image 객체는 pillow 모듈파일에서 지원한다..따라서 현재 개발환경에
                            #설치가 되어 있어야 한다..
    #크기를 우리가 원하느 크기로 재조정하자!!!
    img=img.resize((1500,800), Image.ANTIALIAS) #재조정된 이미지를 다시변수로받기
    #크기가 재조정된 이미지를 켄버스에서 사용할 수 있도록 가공 
    img = ImageTk.PhotoImage(img) #img를 켄버스가 이해할수있는 이미지로 변환
    return img #함수 호출한 사람에게 결과를 반환하자!!

win=Tk() #윈도우 생성하고 win 변수에 담아둔다
#윈도우에 소속시킬 켄버스를 생성하고, 그 크기를 너비1500,높이 800
canvas = Canvas(win, width=1500,height=800, bg="yellow")

#내가 원하는 크기로 윈도우창을 늘리자!
win.geometry("1500x800") #너비 1000, 높이 800

#켄버스 부착 
canvas.pack()

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
        win.update() #윈도우창을 갱신

gameLoop() #게임루프를 호출
#금방 닫혀버리는 윈도우창을 계속 떠있게 하자 
win.mainloop()