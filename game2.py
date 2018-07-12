from kivy.graphics import Ellipse, Color, Rectangle
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.app import App


class Actor:

    def __init__(self, x, y, size, source):
        self.image = Rectangle(pos=(x, y), size=(size, size), source=source)

    def draw(self, canvas):
        canvas.add(self.image)


class Stage(Widget):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.actors = []

    def add(self, actor):
        self.actors.append(actor)

    def draw(self):
        for e in self.actors:
            e.draw(self.canvas)


class Game(App):

    def build(self):
        Window.size = (600, 600)
        stage = Stage()
        stage.add(Actor(0, 0, 50, 'images/smiley.png'))
        stage.add(Actor(200, 200, 50, 'images/smiley_sad.png'))
        stage.draw()
        return stage


Game().run()
