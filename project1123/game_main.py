import tkinter
from PIL import Image
from PIL import ImageTk

root = tkinter.Tk()
root.title("나의 슈팅게임")
can = tkinter.Canvas(root, width=1490, height=1096)

img1= Image.open("./images/sky.png")

img1 = img1.resize((1490,1095) , Image.ANTIALIAS)

bg1=ImageTk.PhotoImage(img1)
can.create_image(0,0, image=bg1)


img2= Image.open("./images/tree.png")
img2 = img2.resize((313,260) , Image.ANTIALIAS)
bg2=ImageTk.PhotoImage(img2)
can.create_image(100,460, image=bg2)

img3= Image.open("./images/skeleton.png")
img3 = img3.resize((150,51) , Image.ANTIALIAS)
bg3=ImageTk.PhotoImage(img3)
can.create_image(1180,900, image=bg3)


can.pack()

root.mainloop()