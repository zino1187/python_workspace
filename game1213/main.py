# 윈도우 창을 만들자!!
from tkinter import Tk #tkinter라는 파일에 들어있는 Tk 함수를 쓰겠다
from tkinter import Canvas #tkinter라는 파일에 들어있는 Canvas 함수를 쓰겠다

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
def gameLoop():
    while True:
        print("gameLoop 호출")


#금방 닫혀버리는 윈도우창을 계속 떠있게 하자 
win.mainloop()