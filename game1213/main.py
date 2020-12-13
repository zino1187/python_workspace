# 윈도우 창을 만들자!!
from tkinter import Tk #tkinter라는 파일에 들어있는 Tk 함수를 쓰겠다

win=Tk() #윈도우 생성하고 win 변수에 담아둔다

#내가 원하는 크기로 윈도우창을 늘리자!
win.geometry("1500x800") #너비 1000, 높이 800

#금방 닫혀버리는 윈도우창을 계속 떠있게 하자 
win.mainloop()