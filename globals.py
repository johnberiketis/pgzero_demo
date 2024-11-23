from enum import Enum, IntEnum

WIDTH = 1000
HEIGHT = 800
ASTEROIDS_SPEED = 1
ASTEROIDS_PER_SECOND = 0.4

class Team(IntEnum):
    ENEMY = -1
    NEUTRAL = 0
    TEAM1 = 1
    TEAM2 = 2

class Type(IntEnum):
    SPACESHIP = 0
    ASTEROID = 1
    PROJECTILE = 2
    REFLECTOR = 3

class ProjectileImage(Enum):
    TYPE0 = 'projectile'
    TYPE1 = 'projectile_1'
    TYPE2 = 'projectile_2'
    TYPE3 = 'projectile_3'
    TYPE4 = 'projectile_4'
    TYPE5 = 'projectile_5'
    TYPE6 = 'projectile_bullet'
    TYPEBALL = 'projectile_ball'
 
asteroid_images = [
    'asteroid1',
    'asteroid2',
    'asteroid3',
    'asteroid4',
    'asteroid5',
    'asteroid6',
    'asteroid7'
]