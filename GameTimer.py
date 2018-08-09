from kivy.graphics import Rectangle
from kivy.core.text import Label


class GameTimer:

    def __init__(self, color):
        self.time = 0
        self.color = color
        lb = Label(text='00000', color=self.color)
        lb.refresh()
        self.image = Rectangle(pos=(0, 0), size=(100, 30), texture=lb.texture)

    def get_text_time(self):
        s = str(int(self.time * 10))
        if len(s) < 5:
            s = '0' * (5 - len(s)) + s
        return s

    def count_time(self, dt):
        self.time += dt
        lb = Label(text=self.get_text_time(), color=self.color)
        lb.refresh()
        self.image.texture = lb.texture