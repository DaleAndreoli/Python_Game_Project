#
# Description:
#   UI element that displays the players engines' energy level.
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

class Engines(Actor):
    def __init__(self, max_engines):
        super().__init__()

        self.set_position(Point(1, constants.MAX_Y - 3))
        self._init_color(6)

        self._init_text()

        self._max_engines = max_engines
        self._engines = max_engines
        
    def _init_text(self):
        text = ["[ᚅ ]"]
        self._text = text

    def update(self):
        if self._engines < self._max_engines:
            self._engines += 1
        engines_segments = int( 30 * self._engines / self._max_engines )
        self._text[0] = "[ᚅ ]" + "█" * engines_segments

    def remove_engines(self, damage):
        self._engines -= damage

    def get_engines(self):
        return self._engines

    def get_hint(self):
        return ["Tap a WASD key to accelerate in that direction. This will consume some of your engines' energy. This resource will recharge over time."]