#
# Description:
#   An enemy ship that tries to fire at the player. 
#   Inherits from actor so that it may be drawn on the screen.
#   Initializes values specific to this type of ship.
#
# OOP Principles Used:
#   Abstraction
#   Encapsulation
#   Inheritance
#
# Reasoning:
#   Abstraction is used here to hold the ships ascii art and calculate the 
#       position to create an enemy_fire.
#   Encapsulation is used for most of the attributes of this class and are 
#       modified by method funcitons that can be called from other files.
#   Inheritance is used by actors. Anything that is drawn on the screen 
#       inherits default values from Actor. Some of these values are modified 
#       to fit the needs of this ship.
# 

import random
from game import constants
from game.actor import Actor
from game.point import Point

class Tie(Actor):
    def __init__(self, position):
        super().__init__()
        self.set_position(position)

        self._is_alive = True

        self._init_text()
        self._init_hitbox()
        self._init_velocity()
        self._init_color(7)
    
    def _init_text(self):
        text = []
        text.append("|         |")
        text.append("|___/‾\___|")
        text.append("|‾‾‾\_/‾‾‾|")
        text.append("|         |")

        self._text = text

    def _init_velocity(self):
        x = random.choice([-1, 1])
        y = -1

        self.set_velocity(Point(x, y))

    def get_fire_point(self):
        x = self.get_position().get_x() + random.choice([0, 10])
        y = self.get_position().get_y() + 2
        point = Point(x, y)
        return point

    def update(self):
        # Left or right screen edge
        if (self.get_position().get_x() < 1) or (self.get_position().get_x() > constants.MAX_X - 12):
            x = -self.get_velocity().get_x()
            y = self.get_velocity().get_y()
            self.set_velocity(Point(x,y))
        # bottom enemy boundary
        if (self.get_position().get_y() > int(constants.MAX_Y * 2 / 3) ):
            x = self.get_velocity().get_x()
            y = -self.get_velocity().get_y()
            self.set_velocity(Point(x,y))
        # Top screen edge    
        if (self.get_position().get_y() < 2 and self.get_position().get_x() > -10):
            x = self.get_velocity().get_x()
            y = 1
            self.set_velocity(Point(x,y))

        # if on screen, random chance to reverse a direction
        if (self.get_position().get_y() > 1):
            if random.randint(1, 100) <= 5:
                x = -self.get_velocity().get_x()
                y = self.get_velocity().get_y()
                self.set_velocity(Point(x,y))
            if random.randint(1, 100) <= 5:
                x = self.get_velocity().get_x()
                y = -self.get_velocity().get_y()
                self.set_velocity(Point(x,y))
    
    def kill(self):
        self.set_position(Point(-1000, -1000))
        self.set_velocity(Point(0,0))
        self._is_alive = False

    def is_alive(self):
        return self._is_alive
