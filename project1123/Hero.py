class Hero:
    def __init__(self, container, img, x, y, width, height, velX, velY):
        self.container=container
        self.img=img
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.velX=velX
        self.velY=velY

    def tick(self):
        self.x = self.x + self.velX
        self.y = self.y + self.velY

    def render(self):
        self.container.create_image(self.x, self.y, image=self.img)