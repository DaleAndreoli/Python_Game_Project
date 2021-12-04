import random
from game import constants
from game.actor import Actor
from game.point import Point

class Star(Actor):
    def __init__(self, position):
        super().__init__()

        self.set_position(position)
        self.set_velocity(Point(0, 0))
        self._init_color(3)

        self._init_text()
        self._init_hitbox()

        self._count = 0
        
    def _init_text(self):
        text = [random.choice([".", "*"])]

        self._text = text

    def update(self):
        if self._count % 2 == 0:
            x = self.get_position().get_x()
            y = self.get_position().get_y() + 1
            self.set_position(Point(x,y))
        self._count += 1

        if self.get_position().get_y() > constants.MAX_Y - 1:
            self.set_position(Point(-20, -20))