#
# Description:
#   The game loop event that handles output.
#   Draws each actor onto the screen.
#   Displays the game over screen if the conditions are met.
#   Establishes the execute method that is specific to this event.
#
# OOP Principles Used:
#   Polymorphism
#
# Reasoning:
#   Polymorphism is used by this event as it inherits from Action, but changes
#       the .execute() method to perform its specific action.
# 

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
        hull = cast["hull"][0].get_hull()

        enemies_remaining = 0

        for enemy in cast["enemy"]:
            if enemy.is_alive():
                enemies_remaining += 1

        # if still alive and still enemies
        if hull > 0 and enemies_remaining > 0:
            self.output_service.clear_screen()
            for i in cast.values():
                self.output_service.draw_actors(i)
            self.output_service.flush_buffer()

        # if all enemies are destroyed
        elif enemies_remaining <= 0:
            game_over_text = "You have destroyed " + str(constants.TOTAL_ENEMIES) + " enemies! Mission successful."
            game_over = Actor()
            game_over.set_text([game_over_text])
            x = int((constants.MAX_X / 2) - len(game_over_text) / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)
            game_over.set_position(position)

            self.output_service.clear_screen()
            self.output_service.draw_actor(game_over)
            self.output_service.flush_buffer()


        # if dead
        else:
            game_over_text = "Your hull has taken too much damage! You have been destroyed."
            game_over = Actor()
            game_over.set_text([game_over_text])
            x = int((constants.MAX_X / 2) - len(game_over_text) / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)
            game_over.set_position(position)

            self.output_service.clear_screen()
            self.output_service.draw_actor(game_over)
            self.output_service.flush_buffer()
