#
# Description:
#   UI element that displays the players weapons' energy level.
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

    def get_hint(self):
        return ["Hold spacebar to fire your blasters. This will consume your weapons' energy. This resource will recharge over time."]