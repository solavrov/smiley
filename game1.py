# just pictures
from kivy.graphics import Rectangle
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.app import App


class Stage(Widget):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def add(self, x, y, size, source):
        self.canvas.add(Rectangle(pos=(x, y), size=(size, size), source=source))


class Game(App):

    def build(self):
        Window.size = (600, 600)
        s = Stage()
        s.add(0, 0, 50, 'images/smiley.png')
        s.add(100, 100, 50, 'images/smiley_sad.png')
        return s


g = Game()
g.run()
