#
# Description:
#   The game loop event that reads input and affects the player ship accordingly.
#   Establishes the execute method that is specific to this event.
#
# OOP Principles Used:
#   Polymorphism
#
# Reasoning:
#   Polymorphism is used by this event as it inherits from Action, but changes
#       the .execute() method to perform its specific action.
# 

from game import constants
from game.action import Action
from game.point import Point
from game.friendly_fire import FriendlyFire

class ControlActorsAction(Action):
    """A code template for controlling actors. The responsibility of this
    class of objects is translate user input into some kind of intent.
    
    Stereotype:
        Controller

    Attributes:
        _input_service (InputService): An instance of InputService.
    """

    def __init__(self, input_service):
        """The class constructor.
        
        Args:
            input_service (InputService): An instance of InputService.
        """
        self._input_service = input_service

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        # Adjust the player's velocity according to WASD input
        acceleration = self._input_service.get_direction()
        fire = self._input_service.get_fire()
        player = cast["player"][0]
        friendly_fire = cast["friendly_fire"]
        weapons = cast["weapons"][0]
        engines = cast["engines"][0]

        if engines.get_engines() > constants.THRUST_COST and not acceleration.equals(Point(0,0)):
            engines.remove_engines(constants.THRUST_COST)

            velocity = player.get_velocity()
            thrust = player.get_thrust()

            x1 = velocity.get_x()
            x2 = acceleration.get_x()
            x3 = thrust.get_x()
            
            y1 = velocity.get_y()
            y2 = acceleration.get_y()
            y3 = thrust.get_y()

            x = x1 + (x2 * x3)
            y = y1 + (y2 * y3)

            new_velocity = Point(x, y)

            player.set_velocity(new_velocity)

        # fire if Space is pressed
        if fire == 1 and weapons.get_weapons() > constants.FIRE_COST:
            fire = FriendlyFire(player.get_fire_point())
            friendly_fire.append(fire)
            weapons.remove_weapons(constants.FIRE_COST)