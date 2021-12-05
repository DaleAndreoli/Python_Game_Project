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
from game.awing                     import Awing
from game.ywing                     import Ywing
from game.tie                       import Tie
from game.falcon                    import Falcon
from game.star                      import Star
from game.shields                   import Shields
from game.engines                   import Engines
from game.weapons                   import Weapons
from game.hull                      import Hull

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

    background = []
    for i in range( constants.MAX_Y, -1000, -1):
        x = random.randint(1, constants.MAX_X)
        y = i
        star = Star(Point(x,y))
        background.append(star)
    cast["background"] = background

    ties = []
    for y in range(0, -(constants.DISTANCE_BETWEEN_ENEMIES * constants.TOTAL_ENEMIES), -constants.DISTANCE_BETWEEN_ENEMIES):
        tie = Tie( Point( random.randint(2, constants.MAX_X - 20), y ) )
        ties.append(tie)
    cast["enemy"] = ties

    ywing = Ywing()
    awing = Awing()
    xwing = Xwing()
    falcon = Falcon()
    ships = [xwing, awing, ywing, falcon]

    hangar_input = InputService(screen)
    hangar_output = OutputService(screen)
    cast["player"] = [ships[choose_ship(hangar_input, hangar_output)]]

    # Initialize Blaster Fire
    friendly_fire = []
    cast["friendly_fire"] = friendly_fire
    enemy_fire = []
    cast["enemy_fire"] = enemy_fire

    # Initialize Ship Systems
    shields = Shields( cast["player"][0].get_max_shields() )
    cast["shields"] = [shields]
    engines = Engines( cast["player"][0].get_max_engines() )
    cast["engines"] = [engines]
    weapons = Weapons( cast["player"][0].get_max_weapons() )
    cast["weapons"] = [weapons]
    hull = Hull( cast["player"][0].get_max_hull() )
    cast["hull"] = [hull]

    
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

def choose_ship(input_service, output_service):
    hangar_y = int(constants.MAX_Y / 3)

    xwing = Xwing()
    x = int(constants.MAX_X * 1 / 5) - xwing.get_width()
    y = hangar_y
    xwing.set_position(Point(x,y))
    x_stats = Actor()
    x_stats.set_text(xwing.get_stats())
    x_stats.set_position(Point(x, y + 10))

    awing = Awing()
    x = int(constants.MAX_X * 2 / 5) - awing.get_width()
    y = hangar_y
    awing.set_position(Point(x,y))
    a_stats = Actor()
    a_stats.set_text(awing.get_stats())
    a_stats.set_position(Point(x, y + 10))

    ywing = Ywing()
    x = int(constants.MAX_X * 3 / 5) - ywing.get_width()
    y = hangar_y
    ywing.set_position(Point(x,y))
    y_stats = Actor()
    y_stats.set_text(ywing.get_stats())
    y_stats.set_position(Point(x, y + 10))

    falcon = Falcon()
    x = int(constants.MAX_X * 4 / 5) - falcon.get_width()
    y = hangar_y
    falcon.set_position(Point(x,y))
    f_stats = Actor()
    f_stats.set_text(falcon.get_stats())
    f_stats.set_position(Point(x, y + 10))

    ships = [xwing, awing, ywing, falcon]
    stats = [f_stats, x_stats, a_stats, y_stats]

    output_service.clear_screen()
    output_service.draw_actors(ships)
    output_service.draw_actors(stats)
    output_service.flush_buffer()

    choice = input_service.get_ship()
    return choice

Screen.wrapper(main)