import random
from game import constants
from game.action import Action
from game.point import Point
from game.enemy_fire import EnemyFire

class MoveActorsAction(Action):
    """A code template for moving actors. The responsibility of this class of
    objects is move any actor that has a velocity more than zero.
    
    Stereotype:
        Controller

    Attributes:
        _input_service (InputService): An instance of InputService.
    """

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        for enemy in cast["enemy"]:
            enemy.update()
            if enemy.get_position().get_y() > 2 and random.randint(1, 100) <= constants.ENEMY_FIRE_CHANCE:
                fire = EnemyFire(enemy.get_fire_point())
                cast["enemy_fire"].append(fire)

        for star in cast["background"]:
            star.update()

        cast["shields"][0].update()
        cast["engines"][0].update()
        cast["weapons"][0].update()
        cast["hull"][0].update()

        for group in cast.values():
            for actor in group:
                if not actor.get_velocity().is_zero():
                    self._move_actor(actor)

    def _move_actor(self, actor):
        """Moves the given actor to its next position according to its 
        velocity. Will wrap the position from one side of the screen to the 
        other when it reaches the edge in either direction.
        
        Args:
            actor (Actor): The actor to move.
        """
        position = actor.get_position()
        velocity = actor.get_velocity()
        x1 = position.get_x()
        y1 = position.get_y()
        x2 = velocity.get_x()
        y2 = velocity.get_y()

        x = 1 + (x1 + x2 - 1)
        y = 1 + (y1 + y2 - 1)

        position = Point(x, y)

        actor.set_position(position)