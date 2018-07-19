# new keyboard
from kivy.graphics import Rectangle
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.app import App
from kivy.clock import Clock
from random import random
from math import sin, cos, pi
from kivy.core.text import Label


class Background:

    def __init__(self, picture):
        self.image = Rectangle(pos=(0, 0), size=(Window.size[0], Window.size[1]), source=picture)


class Hero:

    def __init__(self, x, y, size, face, moving_face, hit_face):
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.size = size
        self.face = face
        self.moving_face = moving_face
        self.hit_face = hit_face
        self.v = 200
        self.image = Rectangle(pos=(x, y), size=(size, size), source=face)

    def move(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt
        if self.is_out():
            self.x -= self.vx * dt
            self.y -= self.vy * dt
            self.vx = self.vy = 0
        self.image.pos = (self.x, self.y)

    def is_out(self):
        return self.x < 0 or self.x + self.size > Window.size[0] or \
               self.y < 0 or self.y + self.size > Window.size[1]


class Actor:

    def __init__(self, x, y, vx, vy, a, size, happy_face, sad_face, sad_time):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.a = a
        self.size = size
        self.happy_face = happy_face
        self.sad_face = sad_face
        self.sad_time = sad_time
        self.timer = 0
        self.image = Rectangle(pos=(x, y), size=(size, size), source=happy_face)

    def move(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt
        self.image.pos = (self.x, self.y)
        self.do_if_bump()
        self.check_timer(dt)

    def do_if_bump(self):
        if self.x + self.size > Window.size[0]:
            self.vx = -self.vx * self.a
            self.vy = self.vy * self.a
            self.x = Window.size[0] - self.size
            self.image.source = self.sad_face
            self.timer = self.sad_time
        if self.x < 0:
            self.vx = -self.vx * self.a
            self.vy = self.vy * self.a
            self.x = 0
            self.image.source = self.sad_face
            self.timer = self.sad_time
        if self.y + self.size > Window.size[1]:
            self.vx = self.vx * self.a
            self.vy = -self.vy * self.a
            self.y = Window.size[1] - self.size
            self.image.source = self.sad_face
            self.timer = self.sad_time
        if self.y < 0:
            self.vx = self.vx * self.a
            self.vy = -self.vy * self.a
            self.y = 0
            self.image.source = self.sad_face
            self.timer = self.sad_time

    def check_timer(self, dt):
        if self.timer > 0:
            self.timer -= dt
            if self.timer <= 0:
                self.timer = 0
                self.image.source = self.happy_face

    def is_hit(self, x, y, size):
        return (self.x + self.size / 2 - x - size / 2) ** 2 + (self.y + self.size / 2 - y - size / 2) ** 2 < \
               (self.size + size) ** 2 / 4


class GameTimer:

    def __init__(self):
        self.time = 0
        lb = Label(text='00000')
        lb.refresh()
        self.image = Rectangle(pos=(0, 0), size=(100, 30), texture=lb.texture)

    def get_text_time(self):
        s = str(int(self.time * 10))
        if len(s) < 5:
            s = '0' * (5 - len(s)) + s
        return s

    def count_time(self, dt):
        self.time += dt
        lb = Label(text=self.get_text_time())
        lb.refresh()
        self.image.texture = lb.texture


class Stage(Widget):

    def __init__(self, game_timer, hero, **kwargs):
        super().__init__(**kwargs)
        self.game_timer = game_timer
        self.hero = hero
        self.actors = []
        self.clock = None
        self.is_running = True
        self.keyboard = Window.request_keyboard(self.close_keyboard, self)
        self.keyboard.bind(on_key_down=self.move_on_key)
        self.keyboard.bind(on_key_up=self.do_on_key_up)

    def set_background(self, background):
        self.canvas.add(background.image)

    def show_hero(self):
        self.canvas.add(self.hero.image)

    def show_game_timer(self):
        self.canvas.add(self.game_timer.image)

    def add(self, actor):
        self.canvas.add(actor.image)
        self.actors.append(actor)

    def move(self, dt):
        self.game_timer.count_time(dt)
        self.hero.move(dt)
        for a in self.actors:
            a.move(dt)
        # self.do_if_hit_hero()

    def do_if_hit_hero(self):
        for a in self.actors:
            if a.is_hit(self.hero.x, self.hero.y, self.hero.size):
                self.hero.image.source = self.hero.hit_face
                self.stop()
                break

    def close_keyboard(self):
        self.keyboard.unbind(on_key_down=self.move_on_key)
        self.keyboard = None

    def move_on_key(self, keyboard, keycode, text, modifiers):
        if self.is_running:
            self.hero.image.source = self.hero.moving_face
            if keycode[1] == 'up':
                self.hero.vx = 0
                self.hero.vy = self.hero.v
            if keycode[1] == 'down':
                self.hero.vx = 0
                self.hero.vy = -self.hero.v
            if keycode[1] == 'left':
                self.hero.vx = -self.hero.v
                self.hero.vy = 0
            if keycode[1] == 'right':
                self.hero.vx = self.hero.v
                self.hero.vy = 0

    def do_on_key_up(self, keyboard, keycode):
        if self.is_running:
            self.hero.vx = 0
            self.hero.vy = 0
            self.hero.image.source = self.hero.face

    def start(self):
        self.clock = Clock.schedule_interval(self.move, 1 / 60)

    def stop(self):
        self.clock.cancel()
        self.is_running = False


class Game(App):

    def build(self):

        Window.size = (600, 600)

        gt = GameTimer()
        h = Hero(275, 275, 50, 'images/smiley.png', 'images/smiley_amazed.png', 'images/smiley_hit.png')

        s = Stage(gt, h)
        s.set_background(Background('images/space.png'))
        s.show_game_timer()
        s.show_hero()

        for i in range(5):
            angle = random() * 2 * pi
            a = Actor(x=random() * 150, y=random() * 150, vx=50 * sin(angle), vy=50 * cos(angle), a=1.1, size=50,
                      happy_face='images/smiley.png', sad_face='images/smiley_crazy.png', sad_time=0.4)
            s.add(a)

        s.start()

        return s


g = Game()
g.run()


