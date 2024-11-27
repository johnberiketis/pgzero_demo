from enum import IntEnum
from pgzero.actor import Actor

WIDTH = 1000
HEIGHT = 800
ASTEROIDS_SPEED = 1
ASTEROIDS_PER_SECOND = 0.4
ASTEROIDS_DAMAGE = 10
OBJECTS_LIMIT = 80
ABILITY_DURATION_LIMIT = 20

PLAYER_START_POS = (WIDTH//2, HEIGHT-50)
ENEMY_START_POS = (WIDTH//2, 60)

class Team(IntEnum):
    ENEMY = -1
    NEUTRAL = 0
    PLAYER = 1

class Type(IntEnum):
    SPACESHIP = 0
    ASTEROID = 1
    PROJECTILE = 2
    REFLECTOR = 3

WIN_GRAPHIC = Actor('win', (WIDTH//2, HEIGHT//2))
LOSE_GRAPHIC = Actor('lose', (WIDTH//2, HEIGHT//2))

IMAGES_PROJECTILES = [
    'projectile',
    'projectile_1',
    'projectile_2',
    'projectile_3',
    'projectile_4',
    'projectile_5',
    'projectile_ball',
    'projectile_bullet'
]

IMAGES_SPACESHIPS = [
    'spaceship_aqua_stripe',
    'spaceship_black',
    'spaceship_blue',
    'spaceship_green',
    'spaceship_purple',
    'spaceship_red_stripe',
    'spaceship_red',
    'spaceship_yellow'
]
 
IMAGES_ASTEROIDS = [
    'asteroid1',
    'asteroid2',
    'asteroid3',
    'asteroid4',
    'asteroid5',
    'asteroid6',
    'asteroid7'
]