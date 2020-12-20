from tkinter import Tk  #tkinter라는 파일에서 Tk() 함수가져오기
from tkinter import Canvas #tkinter라는 파일에서 Canvas가져오기
from lib import BgImage # lib.py에서 BgImage 클래스를 가져오기
from lib import Hero  # lib.py에서 BgImage 클래스를 가져오기

#지난 시간에 거푸집을 프로그래밍 분야에서는 클래스라 한다.
class GameMain():
    def __init__(self): #모든 클래스가 반드시 가져야할 함수를 가리켜 생성자라한다..
                                #생성자는 거푸집으로부터 물건을 생성해 낼때 어떤 모양, 색상, 특징을 
                                #갖는지를 결정짓는 함수다..    
        self.win=Tk() #윈도우창 호출하고, 그 윈도우를 가리킬 변수 선언
        self.canvas = Canvas(self.win, width=1400, height=800, bg="yellow") #켄버스 생성
        self.canvas.pack() #윈도우에 부착하기!!

        self.win.mainloop() #윈도우가 사라지지않고 계속 유지될 수 있게 루프실행

GameMain() #거푸집으로부터, 물체 하나를 생성한다.. 
                    #주의) 클래스명에 함수표시를 한 함수가 바로 __init__을 의미 