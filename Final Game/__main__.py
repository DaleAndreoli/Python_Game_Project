""" 
Bonus Features:
- Game Over Screen
- Score
- Lives
- Bigger Bricks
- Paddle region determines ball bounce direction
- Alternative controls:             (Tested on Windows)
    left/right arrow keys, lowercase a/d, uppercase A/D 
"""

import random
from asciimatics.screen             import Screen 

from game                           import constants

from game.input_service             import InputService
from game.output_service            import OutputService
from game.point                     import Point
from game.director                  import Director
from game.actor                     import Actor
from game.xwing                     import Xwing
from game.tie                       import Tie
from game.falcon                    import Falcon

from game.control_actors_action     import ControlActorsAction
from game.draw_actors_action        import DrawActorsAction
from game.handle_collisions_action  import HandleCollisionsAction
from game.move_actors_action        import MoveActorsAction


def main(screen):
    """Creates the various actors and adds them to the cast list. 
    Establishes the various actions that will comprise the script.
    Creates the director and passes it the cast and script to start the game.
    """
    # create the cast of Actors {key: string, value: list}
    cast = {}

    ties = []
    for x in range(10, 200, 20):
        tie = Tie(Point(x, 2))
        ties.append(tie)
    cast["enemy"] = ties

    falcon = Falcon()
    cast["player"] = [falcon]

    friendly_fire = []
    cast["friendly_fire"] = friendly_fire
    
    enemy_fire = []
    cast["enemy_fire"] = enemy_fire

    
    # create the script of Actions {key: string, value: list}
    script = {}

    input_service = InputService(screen)
    output_service = OutputService(screen)

    control_actors_action = ControlActorsAction(input_service)
    move_actors_action = MoveActorsAction()
    handle_collisions_acition = HandleCollisionsAction()
    draw_actors_action = DrawActorsAction(output_service)
    
    script["input"] = [control_actors_action]
    script["update"] = [move_actors_action, handle_collisions_acition]
    script["output"] = [draw_actors_action]

    # start the game
    director = Director(cast, script)
    director.start_game()


Screen.wrapper(main)