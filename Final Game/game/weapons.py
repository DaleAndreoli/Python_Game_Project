import random
from game import constants
from game.actor import Actor
from game.point import Point

class Weapons(Actor):
    def __init__(self, max_weapons):
        super().__init__()

        self.set_position(Point(1, constants.MAX_Y - 4))
        self._init_color(1)

        self._init_text()

        self._max_weapons = max_weapons
        self._weapons = max_weapons
        
    def _init_text(self):
        text = ["[ᗕ ]"]
        self._text = text

    def update(self):
        if self._weapons < self._max_weapons:
            self._weapons += 1
        weapons_segments = int( 30 * self._weapons / self._max_weapons )
        self._text[0] = "[ᗕ ]" + "█" * weapons_segments

    def remove_weapons(self, damage):
        self._weapons -= damage

    def get_weapons(self):
        return self._weapons