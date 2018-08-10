from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.clock import Clock


class Stage(Widget):

    def __init__(self, game_timer, hero, **kwargs):
        super().__init__(**kwargs)
        self.game_timer = game_timer
        self.hero = hero
        self.actors = []
        self.clock = None
        self.is_running = True
        self.keyboard = Window.request_keyboard(self.close_keyboard, self)
        self.keyboard.bind(on_key_down=self.on_key_down)
        self.keyboard.bind(on_key_up=self.on_key_up)
        self.keys = {'up': 'up', 'down': 'down', 'left': 'left', 'right': 'right'}
        self.pressed_keys = []

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
        self.do_if_hit_hero()

    def do_if_hit_hero(self):
        for a in self.actors:
            if a.is_hit(self.hero.x, self.hero.y, self.hero.size):
                self.hero.image.source = self.hero.hit_face
                self.stop()
                break

    def close_keyboard(self):
        self.keyboard.unbind(on_key_down=self.on_key_down)
        self.keyboard.unbind(on_key_up=self.on_key_up)
        self.keyboard = None

    def act_on_key(self):
        if len(self.pressed_keys) > 0:
            if self.pressed_keys[-1] == self.keys['up']:
                self.hero.vx = 0
                self.hero.vy = self.hero.v
                self.hero.image.source = self.hero.moving_face
            if self.pressed_keys[-1] == self.keys['down']:
                self.hero.vx = 0
                self.hero.vy = -self.hero.v
                self.hero.image.source = self.hero.moving_face
            if self.pressed_keys[-1] == self.keys['left']:
                self.hero.vx = -self.hero.v
                self.hero.vy = 0
                self.hero.image.source = self.hero.moving_face
            if self.pressed_keys[-1] == self.keys['right']:
                self.hero.vx = self.hero.v
                self.hero.vy = 0
                self.hero.image.source = self.hero.moving_face
        else:
            self.hero.vx = 0
            self.hero.vy = 0
            self.hero.image.source = self.hero.face

    def on_key_down(self, keyboard, keycode, text, modifiers):
        if self.is_running:
            if keycode[1] not in self.pressed_keys and keycode[1] in self.keys.values():
                self.pressed_keys.append(keycode[1])
            self.act_on_key()
            # print(self.pressed_keys)

    def on_key_up(self, keyboard, keycode):
        if self.is_running:
            if keycode[1] in self.keys.values():
                self.pressed_keys.remove(keycode[1])
            self.act_on_key()
            # print(self.pressed_keys)

    def start(self):
        self.clock = Clock.schedule_interval(self.move, 1 / 60)

    def stop(self):
        self.clock.cancel()
        self.is_running = False
