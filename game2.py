# Actor
from kivy.graphics import Rectangle
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.app import App


class Actor:

    def __init__(self, x, y, size, face):
        self.image = Rectangle(pos=(x, y), size=(size, size), source=face)


class Stage(Widget):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def add(self, actor):
        self.canvas.add(actor.image)


class Game(App):

    def build(self):
        Window.size = (600, 600)
        s = Stage()
        a1 = Actor(0, 0, 50, 'images/smiley.png')
        a2 = Actor(100, 100, 50, 'images/smiley_sad.png')
        s.add(a1)
        s.add(a2)
        return s


g = Game()
g.run()
