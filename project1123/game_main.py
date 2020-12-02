import tkinter
import time
from PIL import Image
from PIL import ImageTk
from threading import Thread 

root = tkinter.Tk()

flag=True #게임 루프 실행 여부를 결정짓는 변수
interval=0
x=0
y=0
velX=0
velY=0

root.title("나의 슈팅게임")
can = tkinter.Canvas(root, width=1920 , height=900)

img1= Image.open("./images/bg.png")
bg1=ImageTk.PhotoImage(img1)
can.create_image(0,0, image=bg1, anchor="nw")


img2= Image.open("./images/tree.png")
img2 = img2.resize((213,160) , Image.ANTIALIAS)
bg2=ImageTk.PhotoImage(img2)
can.create_image(100,460, image=bg2)

img3= Image.open("./images/skeleton.png")
img3 = img3.resize((150,51) , Image.ANTIALIAS)
bg3=ImageTk.PhotoImage(img3)
can.create_image(1180,900, image=bg3)

can.pack(fill="both", expand=True)

def tick():
    # print("tick() called...")
    global x
    x += 3
    print(x)

def render():    
    # print("render() called...")
    can.create_image(0,0, image=bg1, anchor="nw")
    can.create_image(100+x,460, image=bg2)

def gameLoop(): 
    while flag:        
            tick()
            render()
            time.sleep(1/1000)
            print("gameLoop()..")

control_thread = Thread(target=gameLoop, daemon=True)
control_thread.start()
root.protocol("WM_DELETE_WINDOW", quit)

root.mainloop()
control_thread.join()