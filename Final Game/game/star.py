#
# Description:
#   The stars that pass by during gameplay. 
#
# OOP Principles Used:
#   Abstraction
#   Encapsulation
#   Inheritance
#
# Reasoning:
#   Abstraction is used here to update the attributes each frame without worrying about 
#       what that entails when update() is called in the proper game event.
#   Encapsulation is used for most of the attributes of this class and are 
#       modified by method funcitons. These attributes are mostly those inherited from Actor.
#   Inheritance is used by actors. Anything that is drawn on the screen 
#       inherits default values from Actor. 
# 

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