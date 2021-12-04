import random
from game.actor import Actor
from game.point import Point

class Falcon(Actor):
    """Points earned. The responsibility of Score is to keep track of the player's points.

    Stereotype:
        Information Holder

    Attributes: 
        _points (integer): The number of points the score is worth.
    """
    def __init__(self):
        """The class constructor. Invokes the superclass constructor, initializes points to zero, 
        sets the position and updates the text.
        
        Args:
            self (Score): an instance of Score.
        """
        super().__init__()
        self._thrust = Point(3, 1)

        position = Point(100, 20)
        self.set_position(position)

        self._init_text()
        self._init_hitbox()
        self._init_color(4)
    
    def _init_text(self):
        text = []
        text.append("    /‾‾|  |‾‾\\")
        text.append("   / o |  | o \\")
        text.append("  / o  |__|  o \/‾\\")
        text.append(" /               _/")
        text.append("|   U   ||       |")
        text.append("|==    <||>    ==|")
        text.append("|    o      o    |")
        text.append(" \     o  o     /")
        text.append("   \__________/")

        self._text = text

    def get_thrust(self):
        return self._thrust

    def get_fire_point(self):
        x = self.get_position().get_x() + random.randint(8, 9)
        y = self.get_position().get_y() + 5
        point = Point(x, y)
        return point
