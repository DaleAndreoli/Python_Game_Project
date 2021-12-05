import random
from game import constants
from game.actor import Actor
from game.point import Point

class Hull(Actor):
    def __init__(self, max_hull):
        super().__init__()

        self.set_position(Point(1, constants.MAX_Y - 1))
        self._init_color(7)

        self._init_text()

        self._max_hull = max_hull
        self._hull = max_hull
        
    def _init_text(self):
        text = ["[⊠ ]"]
        self._text = text

    def update(self):
        hull_segments = int( 30 * self._hull / self._max_hull )
        self._text[0] = "[⊠ ]" + "█" * hull_segments

    def remove_hull(self, damage):
        self._hull -= damage