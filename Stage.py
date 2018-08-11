from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.graphics import Rectangle
from GameTimer import GameTimer
from Momo import Momo
from Avatar import Avatar
from random import random
from math import sin, cos, pi
from os import path


class Stage(Widget):

    def __init__(self, layout, folder, **kwargs):
        super().__init__(**kwargs)
        self.layout = layout
        self.folder = folder
        self.game_timer = GameTimer(color=[1, 0, 1, 1])
        self.avatar = Avatar(x=275, y=275, v=300, size=50,
                             face=folder + 'avatar.png', moving_face=folder + 'move.png', hit_face=folder + 'catch.png')
        self.momos = []
        self.clock = None
        self.is_running = True
        self.keyboard = Window.request_keyboard(self.close_keyboard, self)
        self.keyboard.bind(on_key_down=self.on_key_down)
        self.keyboard.bind(on_key_up=self.on_key_up)
        self.keys = {'up': 'up', 'down': 'down', 'left': 'left', 'right': 'right'}
        self.pressed_keys = []
        self.background = Rectangle(pos=(0, 0), size=(Window.size[0], Window.size[1]), source=folder + 'back.png')
        self.canvas.add(self.background)
        self.show_hero()
        for i in range(5):
            angle = random() * 2 * pi
            a = Momo(x=random() * 150, y=random() * 150, vx=100 * sin(angle), vy=100 * cos(angle), a=0.05, size=50,
                     happy_face=folder + 'momo.png', sad_face=folder + 'hit.png', sad_time=0.4, speed_lim=750)
            self.add(a)
        self.show_game_timer()
        self.start()

    def show_hero(self):
        self.canvas.add(self.avatar.image)

    def show_game_timer(self):
        self.canvas.add(self.game_timer.image)

    def add(self, momo):
        self.canvas.add(momo.image)
        self.momos.append(momo)

    def move(self, dt):
        self.game_timer.count_time(dt)
        self.avatar.move(dt)
        for a in self.momos:
            a.move(dt)
        self.do_if_hit_hero()

    def do_if_hit_hero(self):
        for a in self.momos:
            if a.is_hit(self.avatar.x, self.avatar.y, self.avatar.size):
                self.avatar.image.source = self.avatar.hit_face
                self.stop()
                break

    def close_keyboard(self):
        self.keyboard.unbind(on_key_down=self.on_key_down)
        self.keyboard.unbind(on_key_up=self.on_key_up)
        self.keyboard = None

    def act_on_key(self):
        if len(self.pressed_keys) > 0:
            if self.pressed_keys[-1] == self.keys['up']:
                self.avatar.vx = 0
                self.avatar.vy = self.avatar.v
                self.avatar.image.source = self.avatar.moving_face
            if self.pressed_keys[-1] == self.keys['down']:
                self.avatar.vx = 0
                self.avatar.vy = -self.avatar.v
                self.avatar.image.source = self.avatar.moving_face
            if self.pressed_keys[-1] == self.keys['left']:
                self.avatar.vx = -self.avatar.v
                self.avatar.vy = 0
                self.avatar.image.source = self.avatar.moving_face
            if self.pressed_keys[-1] == self.keys['right']:
                self.avatar.vx = self.avatar.v
                self.avatar.vy = 0
                self.avatar.image.source = self.avatar.moving_face
        else:
            self.avatar.vx = 0
            self.avatar.vy = 0
            self.avatar.image.source = self.avatar.face

    def on_key_down(self, keyboard, keycode, text, modifiers):
        if self.is_running:
            if keycode[1] not in self.pressed_keys and keycode[1] in self.keys.values():
                self.pressed_keys.append(keycode[1])
            self.act_on_key()
        else:
            if keycode[1] == 'enter':
                self.layout.place_widget(Stage(self.layout, self.folder))
        if path.isdir('images' + keycode[1]):
            self.change_theme('images' + keycode[1] + '/')

    def on_key_up(self, keyboard, keycode):
        if self.is_running:
            if keycode[1] in self.keys.values():
                self.pressed_keys.remove(keycode[1])
            self.act_on_key()

    def change_theme(self, folder):
        self.folder = folder
        self.background.source = folder + 'back.png'
        self.avatar.face = folder + 'avatar.png'
        self.avatar.image.source = self.avatar.face
        self.avatar.moving_face = folder + 'move.png'
        self.avatar.hit_face = folder + 'catch.png'
        for e in self.momos:
            e.happy_face = folder + 'momo.png'
            e.image.source = e.happy_face
            e.sad_face = folder + 'hit.png'

    def start(self):
        self.clock = Clock.schedule_interval(self.move, 1 / 60)

    def stop(self):
        self.clock.cancel()
        self.is_running = False
