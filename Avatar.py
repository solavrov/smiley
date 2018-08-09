from kivy.graphics import Rectangle
from kivy.core.window import Window


class Avatar:

    def __init__(self, x, y, v, size, face, moving_face, hit_face):
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.size = size
        self.face = face
        self.moving_face = moving_face
        self.hit_face = hit_face
        self.v = v
        self.image = Rectangle(pos=(x, y), size=(size, size), source=face)

    def move(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt
        if self.is_out():
            self.x -= self.vx * dt
            self.y -= self.vy * dt
            self.vx = self.vy = 0
        self.image.pos = (self.x, self.y)

    def is_out(self):
        return self.x < 0 or self.x + self.size > Window.size[0] or \
               self.y < 0 or self.y + self.size > Window.size[1]
