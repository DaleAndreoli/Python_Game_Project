import random
import sys
from game import constants
from game.action import Action
from game.point import Point

class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        # Calculate this frame's current hitbox for each Actor
        for group in cast.values():
            for actor in group:
                actor_base_hitbox = actor.get_base_hitbox()
                actor_position = actor.get_position()
                actor_current_hitbox = []

                for point in actor_base_hitbox:
                    x = point.get_x() + actor_position.get_x()
                    y = point.get_y() + actor_position.get_y()
                    point = Point(x, y)
                    current_point = Point(x, y)
                    actor_current_hitbox.append(current_point)
                actor.current_hitbox = actor_current_hitbox

        # Bring in the cast
        enemies = cast["enemy"]
        player = cast["player"][0]
        friendly_fires = cast["friendly_fire"]
        enemy_fires = cast["enemy_fire"]
        shields = cast["shields"][0]

        player_hitbox = player.current_hitbox

        # Player / Screen collisions
        for point in player_hitbox:
            # Right Edge
            if point.get_x() > constants.MAX_X:
                player.set_position( Point( constants.MAX_X - player.get_width(), player.get_position().get_y() ) )
                player.set_velocity( Point( 0, player.get_velocity().get_y() ) )
            # Left Edge    
            if point.get_x() < 0:
                player.set_position( Point( 1, player.get_position().get_y() ) )
                player.set_velocity( Point( 0, player.get_velocity().get_y() ) )
            # Bottom Edge    
            if point.get_y() > constants.MAX_Y:
                player.set_position( Point( player.get_position().get_x(), constants.MAX_Y - player.get_length()) )
                player.set_velocity( Point( player.get_velocity().get_x(), 0 ) )       
            # Top Edge
            if point.get_y() < 0:
                player.set_position( Point( player.get_position().get_x(), 1 ) ) 
                player.set_velocity( Point( player.get_velocity().get_x(), 0 ) )               

        # Player / Enemy collision
        for enemy in enemies:
            enemy_hitbox = enemy.current_hitbox     # list of Points
            for enemy_point in enemy_hitbox:
                for player_point in player_hitbox:
                    if player_point.equals(enemy_point):
                        enemy.set_position(Point(-1000, -1000))
                        enemy.set_velocity(Point(0,0))
                        shields.remove_shields(20)

        # Player / Enemy Fire Collision
        for fire in enemy_fires:
            fire_point = fire.get_position()
            for player_point in player_hitbox:
                if player_point.equals(fire_point):
                    fire.set_position(Point(-10, -10))
                    fire.set_velocity(Point(0, 0))
                    shields.remove_shields(10)

        # Enemy / Friendly Fire collision
        for enemy in enemies:
            enemy_hitbox = enemy.current_hitbox
            for enemy_point in enemy_hitbox:
                for fire in friendly_fires:
                    fire_hitbox = fire.current_hitbox
                    for fire_point in fire_hitbox:
                        if enemy_point.equals(fire_point):
                            enemy.set_position(Point(-1000, -1000))
                            enemy.set_velocity(Point(0,0))
                            fire.set_position(Point(-10, -10))
                            fire.set_velocity(Point(0, 0))

        # Friendly Fire / Screen collisions
        for fire in friendly_fires:
            if fire.get_position().get_y() < 1:
                fire.set_position(Point(-10, -10))
                fire.set_velocity(Point(0, 0))
                
        # Enemy Fire / Screen collisions
        for fire in enemy_fires:
            if fire.get_position().get_y() > constants.MAX_Y - 1:
                fire.set_position(Point(-10, -10))
                fire.set_velocity(Point(0, 0))

