from GameTimer import GameTimer
from Avatar import Avatar
from Stage import Stage
from Background import Background
from Momo import Momo
from kivy.core.window import Window
from kivy.app import App
from random import random
from math import sin, cos, pi


class Game(App):

    def build(self):

        Window.size = (600, 600)

        folder = 'images'

        gt = GameTimer(color=[1, 0, 1, 1])
        h = Avatar(x=275, y=275, v=300, size=50,
                   face=folder + '/avatar.png', moving_face=folder + '/move.png', hit_face=folder + '/catch.png')

        s = Stage(gt, h)
        s.set_background(Background(folder + '/background.png'))
        s.show_hero()

        for i in range(5):
            angle = random() * 2 * pi
            a = Momo(x=random() * 150, y=random() * 150, vx=100 * sin(angle), vy=100 * cos(angle), a=0.05, size=50,
                     happy_face=folder + '/momo.png', sad_face=folder + '/hit.png', sad_time=0.4, speed_lim=750)
            s.add(a)

        s.show_game_timer()
        s.start()

        return s