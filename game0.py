# just window
from kivy.uix.widget import Widget
from kivy.app import App


class Stage(Widget):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Game(App):

    def build(self):
        # Window.size = (600, 600)
        s = Stage()
        return s


g = Game()
g.run()
