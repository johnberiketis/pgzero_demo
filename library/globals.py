from enum import IntEnum

from pgzero.actor import Actor
from pgzero import loaders

# Game constants
WIDTH = 1920
HEIGHT = 1080
FPS = 60
OBJECTS_LIMIT = 80
TUTORIAL = True
TUTORIAL_MESSAGE = "Controls:\nLEFT and RIGHT arrows to move\nSPACE to shoot\nLEFT SHIFT to activate ability\nESC to quit"
TUTORIAL_MESSAGE_P2 = "Player 2 controls:\nKEYPAD 6 for to move right\nKEYPAD 4 to move left\nKEYPAD 0 to shoot\nKEYPAD ENTER to activate ability\nESC to quit"
MAX_SPACESHIP_POINTS = 200
USE_INSPECTOR = False #Broken
MAX_ABILITY_MSG_LENGTH = 30
WIN_GRAPHIC = Actor('others/win', (WIDTH//2, HEIGHT//2))
LOSE_GRAPHIC = Actor('others/lose', (WIDTH//2, HEIGHT//2))
NUMBER_OF_PLAYERS = 1
NUMBER_OF_ENEMIES = 1

# Enviroment constants
ASTEROIDS_SPEED = 1
ASTEROIDS_PER_SECOND = 0.4
ASTEROIDS_DAMAGE = 10
POWERUPS_PER_SECOND = 0.03

# Spaceship constants:
MIN_COOLDOWN = 1
MAX_COOLDOWN = 30
MIN_ABILITY_DURATION = 1
MAX_ABILITY_DURATION = 20
PLAYER_START_POS = (WIDTH//2-500, HEIGHT-50)
ENEMY_START_POS = (WIDTH//2+500, 60)

# Spaceship inspector weights
MAX_HEALTH_WEIGHT       = 0.25
HEALTH_WEIGHT           = 0.25
SPEED_WEIGHT            = 2.0
ABILITY_DURATION_WEIGHT = 2.0
COOLDOWN_WEIGHT         = 2.0
COLLIDABLE_WEIGHT       = 20.0
SPACESHIP_CHILDS_LENGTH_WEIGHT = 10.0  

# Weapon constants:
MIN_WEAPON_FIRERATE = 1
MAX_WEAPON_FIRERATE = 12
MIN_WEAPON_BARRELS = 1
MAX_WEAPON_BARRELS = 4
MIN_WEAPON_SPREAD_ANGLE = 0
MAX_WEAPON_SPREAD_ANGLE = 120
MIN_WEAPON_RANDOMNESS = 0
MAX_WEAPON_RANDOMNESS = 30

# Projectile constants
MIN_PROJECTILE_DAMAGE = 1
MAX_PROJECTILE_DAMAGE = 10
MIN_PROJECTILE_SPEED = 1
MAX_PROJECTILE_SPEED = 25

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

EXPLOSION_FRAMES = [
        {"frame_number" : 0, "image" : loaders.images.load("effects/explosion1")},
        {"frame_number" : 3, "image" : loaders.images.load("effects/explosion2")},
        {"frame_number" : 5, "image" : loaders.images.load("effects/explosion3")},
        {"frame_number" : 8, "image" : loaders.images.load("effects/explosion4")},
        {"frame_number" : 10, "image" : loaders.images.load("effects/explosion5")}
]