from Stage import Stage
from kivy.core.window import Window
from kivy.app import App
from Layout import Layout


class Game(App):

    def build(self):

        Window.size = (600, 600)

        l = Layout()

        s = Stage(l, 'images1/')

        l.place_widget(s)

        return l
