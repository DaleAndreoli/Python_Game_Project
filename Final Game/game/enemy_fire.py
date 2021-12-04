import random
from game.actor import Actor
from game.point import Point

class EnemyFire(Actor):
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
        self.set_velocity(Point(0, 2))
        self._init_color(2)

        self._init_text()
        self._init_hitbox()
    
    def _init_text(self):
        text = ["|"]

        self._text = text