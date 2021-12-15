#
# Description:
#   The parent class used by anything that needs to be drawn on the screen. 
#   Initializes default values such as position and text.
#   Creates the director and passes it the cast and script to start the game. 
#
# OOP Principles Used:
#   Abstraction
#   Encapsulation
#   Inheritance
#
# Reasoning:
#   Abstraction is used here to calculate things like the Actors length, width 
#       and hitbox.
#   Encapsulation is used for most of the attributes of this class and are 
#       modified by method funcitons.
#   Inheritance is used by actors. Anything that is drawn on the screen 
#       inherits default values from Actor. 
# 

from game import constants
from game.point import Point

class Actor:
    """A visible, moveable thing that participates in the game. The responsibility of Actor is to keep track of its appearance, position 
    and velocity in 2d space.

    Stereotype:
        Information Holder
    """

    def __init__(self):
        """The class constructor."""
        self._description = ""
        self._text = []
        self._position = Point(0, 0)
        self._velocity = Point(0, 0)
        self._base_hitbox = []
        self.current_hitbox = []
        self._color = 7 # 0:BLACK 1:RED 2:GREEN 3:YELLOW 4:BLUE 5:MAGENTA 6:CYAN 7:WHITE

    def _init_hitbox(self):
        for y in range(len(self._text)):
            for x in range(len(self._text[y])):
                if self._text[y][x] is not " ":
                    self._base_hitbox.append(Point(x, y))
        self.current_hitbox = self._base_hitbox

    def _init_color(self, color):
        self._color = color


    def get_description(self):
        """Gets the artifact's description.
        
        Returns:
            string: The artifact's description.
        """
        return self._description 

    def get_position(self):
        """Gets the actor's position in 2d space.
        
        Returns:
            Point: The actor's position in 2d space.
        """
        return self._position
    
    def get_text(self):
        """Gets the actor's textual representation.
        
        Returns:
            string: The actor's textual representation.
        """
        return self._text

    def get_velocity(self):
        """Gets the actor's speed and direction.
        
        Returns:
            Point: The actor's speed and direction.
        """
        return self._velocity
    
    def set_description(self, description):
        """Updates the actor's description to the given one.
        
        Args:
            description (string): The given description.
        """
        self._description = description

    def set_position(self, position):
        """Updates the actor's position to the given one.
        
        Args:
            position (Point): The given position.
        """
        self._position = position
    
    def set_text(self, text):
        """Updates the actor's text to the given value.
        
        Args:
            text (string): The given value.
        """
        self._text = text

    def set_velocity(self, velocity):
        """Updates the actor's velocity to the given one.
        
        Args:
            position (Point): The given velocity.
        """
        self._velocity = velocity
        
    def get_base_hitbox(self):
        return self._base_hitbox

    def get_width(self):
        width = 0
        for line in self._text:
            if len(line) > width:
                width = len(line)
        return width

    def get_length(self):
        return len(self._text)

    def get_color(self):
        return self._color