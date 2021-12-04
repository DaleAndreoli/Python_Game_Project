import random
from game import constants
from game.actor import Actor
from game.point import Point

class Tie(Actor):
    """Points earned. The responsibility of Score is to keep track of the player's points.

    Stereotype:
        Information Holder

    Attributes: 
        _points (integer): The number of points the score is worth.
    """
    def __init__(self, position):
        """The class constructor. Invokes the superclass constructor, initializes points to zero, 
        sets the position and updates the text.
        
        Args:
            self (Score): an instance of Score.
        """
        super().__init__()
        self.set_position(position)

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
        x = random.randint(-1, 1)
        y = random.randint(-1, 1)

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
        if  (self.get_position().get_y() > int(constants.MAX_Y * 2 / 3) ):
            x = self.get_velocity().get_x()
            y = -self.get_velocity().get_y()
            self.set_velocity(Point(x,y))
            
        if  (self.get_position().get_y() < 2 ):
            x = self.get_velocity().get_x()
            y = 1
            self.set_velocity(Point(x,y))

    
