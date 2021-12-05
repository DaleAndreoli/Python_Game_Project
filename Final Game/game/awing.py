import random
from game.actor import Actor
from game.point import Point
from game import constants

class Awing(Actor):
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
        self._thrust  = constants.AWING_THRUST
        self._shields = constants.AWING_SHIELDS
        self._engines = constants.AWING_ENGINES
        self._weapons = constants.AWING_WEAPONS
        self._hull    = constants.AWING_HULL

        position = Point( int(constants.MAX_X / 2), constants.MAX_Y - (self.get_length() + 1))
        self.set_position(position)

        self._stats = []

        self._init_text()
        self._init_stats()
        self._init_hitbox()
        self._init_color(4)
    
    def _init_text(self):
        text = []
        text.append("    /‾|‾\\")
        text.append("   /⠀⠀|⠀⠀\\")
        text.append("| /⠀⠀⠀_⠀⠀⠀\ |")
        text.append("||⠀⠀⠀/_\⠀⠀⠀||")
        text.append("||__⠀| |⠀__||")
        text.append("  ||_____||")
        text.append("  ||     ||")
        self._text = text

    def _init_stats(self):
        text = []
        text.append("Interceptor")
        text.append("")
        text.append("Weapons: ★ ★ ★ ★ ★")
        text.append("Engines: ★ ★ ★ ★ ★")
        text.append("Shields: ★ ★") 
        text.append("Hull:    ★ ★")
        text.append("")
        text.append("Press A to select")
        self._stats = text

    def get_stats(self):
        return self._stats
        
    def get_thrust(self):
        return self._thrust

    def get_max_shields(self):
        return self._shields

    def get_max_engines(self):
        return self._engines

    def get_max_weapons(self):
        return self._weapons

    def get_max_hull(self):
        return self._hull

    def get_fire_point(self):
        x = self.get_position().get_x() + random.choice([0,12])
        y = self.get_position().get_y() + 3
        point = Point(x, y)
        return point