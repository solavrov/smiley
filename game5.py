from kivy.graphics import Ellipse, Color, Rectangle
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.app import App
from kivy.clock import Clock


class Actor:

    def __init__(self, x, y, vx, size, source):
        self.x = x
        self.y = y
        self.vx = vx
        self.image = Rectangle(pos=(x, y), size=(size, size), source=source)

    def move(self, dt):
        self.x += self.vx * dt
        self.image.pos = (self.x, self.y)


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
        a1 = Actor(0, 300, 10, 50, 'images/smiley.png')
        s.add(a1)
        Clock.schedule_interval(s.move, 1.0 / 60)
        return s


g = Game()
g.run()
