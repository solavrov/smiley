# keyboard (game3)
from kivy.graphics import Rectangle
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.app import App


class Hero:

    def __init__(self, x, y, size, face):
        self.x = x
        self.y = y
        self.size = size
        self.image = Rectangle(pos=(x, y), size=(size, size), source=face)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        self.image.pos = (self.x, self.y)


class Stage(Widget):

    def __init__(self, hero, **kwargs):
        super().__init__(**kwargs)
        self.hero = hero
        self.canvas.add(hero.image)
        self.keyboard = Window.request_keyboard(self.close_keyboard, self)
        self.keyboard.bind(on_key_down=self.move_on_key)

    def close_keyboard(self):
        self.keyboard.unbind(on_key_down=self.move_on_key)
        self.keyboard = None

    def move_on_key(self, keyboard, keycode, text, modifiers):
        if keycode[1] == 'w':
            self.hero.move(0, 10)
        if keycode[1] == 's':
            self.hero.move(0, -10)
        if keycode[1] == 'a':
            self.hero.move(-10, 0)
        if keycode[1] == 'd':
            self.hero.move(10, 0)


class Game(App):

    def build(self):
        Window.size = (600, 600)
        h = Hero(300, 300, 50, 'images/smiley.png')
        s = Stage(h)
        return s


g = Game()
g.run()