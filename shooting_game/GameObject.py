class GameObject:
    def __init__(self, container, img, x, y, width, height, velX, velY):
        self.container = container
        self.img=img
        self.x =x
        self.y = y 
        self.width =width
        self.height = height
        self.velX=velX
        self.velY=velY
        
        print("자식에 의해 호출됨 ", self.x)