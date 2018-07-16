# static emotion
from kivy.graphics import Rectangle
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.app import App
from kivy.clock import Clock


class Actor:

    def __init__(self, x, y, vx, vy, size, happy_face, sad_face):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.size = size
        self.happy_face = happy_face
        self.sad_face = sad_face
        self.image = Rectangle(pos=(x, y), size=(size, size), source=happy_face)

    def move(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt
        self.image.pos = (self.x, self.y)
        self.do_if_bump()

    def do_if_bump(self):
        if self.x + self.size > Window.size[0]:
            self.vx = -self.vx
            self.x = Window.size[0] - self.size
            self.image.source = self.sad_face
        if self.x < 0:
            self.vx = -self.vx
            self.x = 0
            self.image.source = self.sad_face
        if self.y + self.size > Window.size[0]:
            self.vy = -self.vy
            self.y = Window.size[0] - self.size
            self.image.source = self.sad_face
        if self.y < 0:
            self.vy = -self.vy
            self.y = 0
            self.image.source = self.sad_face


class Stage(Widget):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.actors = []

    def add(self, actor):
        self.canvas.add(actor.image)
        self.actors.append(actor)

    def move(self, dt):
        for a in self.actors:
            a.move(dt)


class Game(App):

    def build(self):
        Window.size = (600, 600)
        s = Stage()
        a1 = Actor(x=0, y=300, vx=100, vy=100, size=50,
                   happy_face='images/smiley.png', sad_face='images/smiley_sad.png')
        s.add(a1)
        # s.add(a2)
        Clock.schedule_interval(s.move, 1/60)
        return s


g = Game()
g.run()
