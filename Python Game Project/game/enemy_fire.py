#
# Description:
#   The lasers fired by enemies toward the player.  
#
# OOP Principles Used:
#   Encapsulation
#   Inheritance
#
# Reasoning:
#   Encapsulation is used for most of the attributes of this class and are 
#       modified by method funcitons. These attributes are mostly those inherited from Actor.
#   Inheritance is used by actors. Anything that is drawn on the screen 
#       inherits default values from Actor. 
# 

import random
from game.actor import Actor
from game.point import Point

class EnemyFire(Actor):
    def __init__(self, position):
        super().__init__()

        self.set_position(position)
        self.set_velocity(Point(0, 2))
        self._init_color(2)

        self._init_text()
        self._init_hitbox()
    
    def _init_text(self):
        text = ["|"]

        self._text = text