#
# Description:
#   Holds variables that make a significant impact on gameplay.
#   Having these all in one file makes it easier to tune mechanics and balance 
#       difficulty without searching for where in the code those variables are set.
#
# OOP Principles Used:
#   Abstraction
#
# Reasoning:
#   Abstraction is used here by allowing significant changes to game settings 
#       without going under the hood to find them across various files. 
#   

import os
from game.point import Point

MAX_X = 260
MAX_Y = 80
FRAME_LENGTH = 0.05
PATH = os.path.dirname(os.path.abspath(__file__))
ARTIFACTS = 30

ENEMY_FIRE_DAMAGE = 40
ENEMY_COLLISION_DAMAGE = 10
ENEMY_FIRE_CHANCE = 10 # Percent chance per frame to fire
DISTANCE_BETWEEN_ENEMIES = 20
TOTAL_ENEMIES = 20

FIRE_COST = 10
THRUST_COST = 10
SHIELD_REGEN = 1 # Percent per frame

XWING_WEAPONS  = 150
XWING_ENGINES  = 100
XWING_THRUST   = Point(3, 1)
XWING_SHIELDS  = 150
XWING_HULL     = 300

AWING_WEAPONS  = 200
AWING_ENGINES  = 200
AWING_THRUST   = Point(6, 2)
AWING_SHIELDS  = 125
AWING_HULL     = 200

YWING_WEAPONS  = 200
YWING_ENGINES  = 75
YWING_THRUST   = Point(2, 1)
YWING_SHIELDS  = 150
YWING_HULL     = 500

FALCON_WEAPONS  = 100
FALCON_ENGINES  = 100
FALCON_THRUST   = Point(3, 1)
FALCON_SHIELDS  = 200
FALCON_HULL     = 400