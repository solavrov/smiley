from kivy.graphics import Ellipse, Color, Rectangle
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.app import App
from kivy.clock import Clock
from random import random


class Ball:

    def __init__(self, pos, size, vx):
        self.image = Rectangle(source='smiley.png', pos=pos, size=size)
        self.vx = vx

    def draw(self, canvas):
        canvas.add(self.image)

    def move(self, dt):
        self.image.pos = (self.image.pos[0] + self.vx * dt, self.image.pos[1])
        if self.image.pos[0] + self.image.size[0] >= Window.size[0] or self.image.pos[0] <= 0:
            self.image.source = 'smiley_sad.png'
            self.vx = -self.vx


class Box(Widget):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ball = Ball((0, 300), (50, 50), 100)

    def draw(self):
        self.ball.draw(self.canvas)

    def move(self, dt):
        self.ball.move(dt)


class Game(App):

    def build(self):
        Window.size = (600, 600)
        box = Box()
        box.draw()
        Clock.schedule_interval(box.move, 1.0 / 60)
        return box


Game().run()
