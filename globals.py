from enum import IntEnum
from pgzero.actor import Actor

# WIDTH = 1000
# HEIGHT = 800
WIDTH = 1920
HEIGHT = 1080
FPS = 60
ASTEROIDS_SPEED = 1
ASTEROIDS_PER_SECOND = 0.4
ASTEROIDS_DAMAGE = 10
POWERUPS_PER_SECOND = 0.03
OBJECTS_LIMIT = 80
ABILITY_DURATION_LIMIT = 20
MIN_COOLDOWN = 1
MAX_COOLDOWN = 30

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
    POWERUP = 4

WIN_GRAPHIC = Actor('others/win', (WIDTH//2, HEIGHT//2))
LOSE_GRAPHIC = Actor('others/lose', (WIDTH//2, HEIGHT//2))

IMAGES_PROJECTILES = [
    'projectiles/projectilered',
    'projectiles/projectileyellow',
    'projectiles/projectilegreen',
    'projectiles/projectileblue',
    'projectiles/projectilepurple',
    'projectiles/projectilewhite',
    'projectiles/projectilemissile1',
    'projectiles/projectilemissile2',
    'projectiles/projectilemissile3',
    'projectiles/projectilemissile4'
]

IMAGES_SPACESHIPS = [
    'spaceships/spaceship_black1',
    'spaceships/spaceship_black2',
    'spaceships/spaceship_black3',
    'spaceships/spaceship_black4',
    'spaceships/spaceship_black5',
    'spaceships/spaceship_blue1',
    'spaceships/spaceship_blue2',
    'spaceships/spaceship_blue3',
    'spaceships/spaceship_blue4',
    'spaceships/spaceship_blue5',
    'spaceships/spaceship_blue6',
    'spaceships/spaceship_blue7',
    'spaceships/spaceship_blue8',
    'spaceships/spaceship_green1',
    'spaceships/spaceship_green2',
    'spaceships/spaceship_green3',
    'spaceships/spaceship_green4',
    'spaceships/spaceship_green5',
    'spaceships/spaceship_green6',
    'spaceships/spaceship_green7',
    'spaceships/spaceship_green8',
    'spaceships/spaceship_orange1',
    'spaceships/spaceship_orange2',
    'spaceships/spaceship_orange3',
    'spaceships/spaceship_orange4',
    'spaceships/spaceship_orange5',
    'spaceships/spaceship_orange6',
    'spaceships/spaceship_orange7',
    'spaceships/spaceship_orange8',
    'spaceships/spaceship_red1',
    'spaceships/spaceship_red2',
    'spaceships/spaceship_red3',
    'spaceships/spaceship_red4',
    'spaceships/spaceship_red5',
    'spaceships/spaceship_red6',
    'spaceships/spaceship_red7',
    'spaceships/spaceship_red8',
]

IMAGES_POWERUPS = {
    "repair" : 'powerups/powerup_repair',
    "projectile_upgrade" : 'powerups/powerup_projectile_upgrade',
    "weapon_plus" : 'powerups/powerup_weapon_plus',
}
 
IMAGES_ASTEROIDS = [
    'asteroids/asteroid_big1',
    'asteroids/asteroid_big2',
    'asteroids/asteroid_big3',
    'asteroids/asteroid_big4',
    'asteroids/asteroid_med1',
    'asteroids/asteroid_med2',
    'asteroids/asteroid_small1',
    'asteroids/asteroid_small2'
]