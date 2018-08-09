from kivy.config import Config
Config.set('graphics', 'resizable', False)
from Game import Game

g = Game()
g.run()
