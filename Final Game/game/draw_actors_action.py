from game.action import Action
from game.output_service import OutputService
from game.actor import Actor
from game import constants
from game.point import Point

class DrawActorsAction(Action):
    """A script action for drawing actors. The responsibility of this
    class of objects is to send actors to the output service to be
    displayed.
    
    Stereotype:
        Displayer

    Attributes:
        _output_service (OutputService): An instance of OutputService.
    """
    def __init__(self, output_service):
        """The class constructor.
        
        Args:
            output_service (OutputService): An instance of OutputService.
        """
        self.output_service = output_service

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        self.output_service.clear_screen()
        for i in cast.values():
            self.output_service.draw_actors(i)
        self.output_service.flush_buffer()