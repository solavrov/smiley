from kivy.graphics import Rectangle
from kivy.core.window import Window


class Background:

    def __init__(self, picture):
        self.image = Rectangle(pos=(0, 0), size=(Window.size[0], Window.size[1]), source=picture)
