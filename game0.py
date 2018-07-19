# just window
from kivy.uix.widget import Widget
from kivy.app import App


class Stage(Widget):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Game(App):

    def build(self):
        s = Stage()
        return s


g = Game()
g.run()
