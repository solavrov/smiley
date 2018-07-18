# just figures
from kivy.graphics import Rectangle, Ellipse, Color
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.app import App


class Stage(Widget):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def draw_some(self):
        self.canvas.add(Color(1, 0, 0, 1))
        self.canvas.add(Rectangle(pos=(250, 250), size=(150, 20)))
        self.canvas.add(Color(0, 1, 0, 1))
        self.canvas.add(Rectangle(pos=(300, 200), size=(20, 200)))
        self.canvas.add(Color(0, 0, 1, 0.5))
        self.canvas.add(Ellipse(pos=(275, 225), size=(75, 100)))


class Game(App):

    def build(self):
        Window.size = (600, 600)
        s = Stage()
        s.draw_some()
        return s


g = Game()
g.run()
