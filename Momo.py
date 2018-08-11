from kivy.graphics import Rectangle
from kivy.core.window import Window


class Momo:

    def __init__(self, x, y, vx, vy, a, size, face, sad_face, sad_time, speed_lim):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.a = a
        self.size = size
        self.face = face
        self.sad_face = sad_face
        self.sad_time = sad_time
        self.speed_lim = speed_lim
        self.speed_lim_is_not_reached = True
        self.timer = 0
        self.image = Rectangle(pos=(x, y), size=(size, size), source=face)

    def limit_speed(self):
        if self.speed_lim_is_not_reached:
            v = (self.vx ** 2 + self.vy ** 2) ** 0.5
            if v > self.speed_lim:
                self.speed_lim_is_not_reached = False
                self.vx *= self.speed_lim / v
                self.vy *= self.speed_lim / v

    def move(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt
        self.image.pos = (self.x, self.y)
        self.do_if_bump()
        self.check_timer(dt)

    def do_if_bump(self):
        if self.x + self.size > Window.size[0]:
            self.vx = -self.vx * (1 + self.a * self.speed_lim_is_not_reached)
            self.vy = self.vy * (1 + self.a * self.speed_lim_is_not_reached)
            self.limit_speed()
            self.x = Window.size[0] - self.size
            self.image.source = self.sad_face
            self.timer = self.sad_time
        if self.x < 0:
            self.vx = -self.vx * (1 + self.a * self.speed_lim_is_not_reached)
            self.vy = self.vy * (1 + self.a * self.speed_lim_is_not_reached)
            self.limit_speed()
            self.x = 0
            self.image.source = self.sad_face
            self.timer = self.sad_time
        if self.y + self.size > Window.size[1]:
            self.vx = self.vx * (1 + self.a * self.speed_lim_is_not_reached)
            self.vy = -self.vy * (1 + self.a * self.speed_lim_is_not_reached)
            self.limit_speed()
            self.y = Window.size[1] - self.size
            self.image.source = self.sad_face
            self.timer = self.sad_time
        if self.y < 0:
            self.vx = self.vx * (1 + self.a * self.speed_lim_is_not_reached)
            self.vy = -self.vy * (1 + self.a * self.speed_lim_is_not_reached)
            self.limit_speed()
            self.y = 0
            self.image.source = self.sad_face
            self.timer = self.sad_time

    def check_timer(self, dt):
        if self.timer > 0:
            self.timer -= dt
            if self.timer <= 0:
                self.timer = 0
                self.image.source = self.face

    def is_hit(self, x, y, size):
        return (self.x + self.size / 2 - x - size / 2) ** 2 + (self.y + self.size / 2 - y - size / 2) ** 2 < \
               (self.size + size) ** 2 / 4