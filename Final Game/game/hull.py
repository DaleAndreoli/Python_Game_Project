#
# Description:
#   UI element that displays the players hull.
#
# OOP Principles Used:
#   Abstraction
#   Encapsulation
#   Inheritance
#
# Reasoning:
#   Abstraction is used here to hold and update the UI element's ascii art.
#   Encapsulation is used for most of the attributes of this class and are 
#       modified by method funcitons.
#   Inheritance is used by actors. Anything that is drawn on the screen 
#       inherits default values from Actor. Some of these values are modified 
#       to fit the needs of this UI element.
# 

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

    def get_hull(self):
        return self._hull

    def get_hint(self):
        return ["Taking fire or colliding with an enemy while the shields are depleted will damage the hull. The hull does not regenerate. When the hull is fully damaged, your ship will be destroyed and the game will be over."]