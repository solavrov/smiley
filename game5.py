# x_bump
from kivy.graphics import Rectangle
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.app import App
from kivy.clock import Clock


class Actor:

    def __init__(self, x, y, vx, size, face):
        self.x = x
        self.y = y
        self.vx = vx
        self.size = size
        self.image = Rectangle(pos=(x, y), size=(size, size), source=face)

    def move(self, dt):
        self.x += self.vx * dt
        self.image.pos = (self.x, self.y)
        self.do_if_bump()

    def do_if_bump(self):
        if self.x + self.size > Window.size[0]:
            self.vx = -self.vx
            self.x = Window.size[0] - self.size
        if self.x < 0:
            self.vx = -self.vx
            self.x = 0


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
        a1 = Actor(x=0, y=300, vx=100, size=50, face='images/smiley.png')
        # a2 = Actor(x=0, y=200, vx=50, size=50, source='images/smiley.png')
        s.add(a1)
        # s.add(a2)
        Clock.schedule_interval(s.move, 1/60)
        return s


g = Game()
g.run()
