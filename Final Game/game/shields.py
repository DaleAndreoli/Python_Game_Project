import random
from game import constants
from game.actor import Actor
from game.point import Point

class Shields(Actor):
    def __init__(self, max_shields):
        super().__init__()

        self.set_position(Point(1, constants.MAX_Y - 2))
        self._init_color(2)

        self._init_text()

        self._max_shields = max_shields
        self._shields = max_shields
        
    def _init_text(self):
        text = ["[⊙ ]"]
        self._text = text

    def update(self):
        if self._shields < self._max_shields:
            self._shields += int(constants.SHIELD_REGEN / 100 * self._max_shields)
        shield_segments = int( 30 * self._shields / self._max_shields )
        self._text[0] = "[⊙ ]" + "█" * shield_segments

    def remove_shields(self, damage):
        self._shields -= damage

    def get_shields(self):
        return self._shields