# step moving
from kivy.graphics import Rectangle
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.app import App


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


class Stage(Widget):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def add(self, actor):
        self.canvas.add(actor.image)


class Game(App):

    def build(self):
        Window.size = (600, 600)
        s = Stage()
        a1 = Actor(0, 300, 20, 50, 'images/smiley.png')
        s.add(a1)
        a1.move(1)
        return s


g = Game()
g.run()
