import GameObject

class Hero(GameObject.GameObject):
    def __init__(self, container, img, x, y, width, height, velX, velY):
        super().__init__(container, img, x, y, width, height,velX, velY)

    def tick(self):
        self.x = self.x + self.velX
        self.y = self.y + self.velY

    def render(self):
        self.container.create_image(self.x, self.y, image=self.img)
        # print(self.img)