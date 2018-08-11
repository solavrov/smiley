from Stage import Stage
from kivy.core.window import Window
from kivy.app import App


class Game(App):

    def build(self):
        Window.size = (600, 600)
        s = Stage('images1/')
        return s
