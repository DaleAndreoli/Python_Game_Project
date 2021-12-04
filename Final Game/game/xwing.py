import random
from game.actor import Actor
from game.point import Point

class Xwing(Actor):
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
        self._points = 0
        position = Point(1, 1)
        self.set_position(position)
        self.set_text()
    
    def set_text(self):
        text = []
        text.append("        /‾\\")
        text.append("       |   |")
        text.append("       |   |")
        text.append("||     | _ |     ||")
        text.append("||     |/_\|     ||")
        text.append("||————|| o ||————||")
        text.append("||____||___||____||")

        self._text = text