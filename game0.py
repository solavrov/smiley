from kivy.graphics import Ellipse, Color, Rectangle
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.app import App


class Stage(Widget):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Game(App):

    def build(self):
        # Window.size = (600, 600)
        stage = Stage()
        return stage


Game().run()
