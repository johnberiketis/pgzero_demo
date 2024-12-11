import random

from library.spaceship import Spaceship
from library.blueprints import SpaceshipBlueprint
from library.blueprints import WeaponBlueprint
from library.projectile import Projectile
from library.agent import Agent
from library.utils import Team, world
from library.globals import IMAGES_SPACESHIPS

# This is the laboratory where you can create your own custom 
# abilities, weapons and spaceships 

######################################
######### ABILITIES LAB ##############
######################################

def super_speed(spaceship : Spaceship):
    ''' Super speed!!! '''
    spaceship.speed = 13

def invisibility(spaceship : Spaceship):
    '''Invisibility!!!'''
    spaceship.collidable = False

def too_many_guns(spaceship : Spaceship):
    '''Quad fire!!!'''
    spaceship.weapon.barrels = 4

def machine_gun(spaceship: Spaceship):
    '''Fire barraze!!!'''
    spaceship.weapon.firerate = 12

def reflection(spaceship: Spaceship):
    '''Reflector deployed!!!'''
    spaceship.deploy_reflector()

def buff_up(spaceship: Spaceship):
    '''Damage bonus!!!'''
    spaceship.weapon.damage = spaceship.weapon.damage + 2/spaceship.weapon.barrels

def hypervelocity(spaceship: Spaceship):
    '''Bullets super speed!!!'''
    spaceship.weapon.speed = 20

def fanfire(spaceship: Spaceship):
    '''Mines deployed!!!'''
    n = 10
    spread = 100
    for i in range(0,n+1):
        Projectile(image = 'others/bomb', pos = spaceship.pos, speed=2, damage = 12, health = 12, source=spaceship, team=spaceship.team, direction= -spread/2 + (i*spread/n) )

abilities = [
    super_speed,
    invisibility,
    too_many_guns,
    machine_gun,
    reflection,
    buff_up,
    hypervelocity,
    fanfire
    ]

######################################
############ WEAPON LAB ##############
######################################

# weapon points = (damage * barrels * firerate) + speed
cannon      = WeaponBlueprint(firerate = 2, barrels = 1, damage = 8, speed = 6)  # 22
super_auto  = WeaponBlueprint(firerate = 8, barrels = 1, damage = 1.5, speed = 13) # 25
automatic   = WeaponBlueprint(firerate = 4, barrels = 1, damage = 4, speed = 12) # 28
dual        = WeaponBlueprint(firerate = 2, barrels = 2, damage = 3, speed = 9)  # 21
dual_plasma = WeaponBlueprint(firerate = 1, barrels = 2, damage = 5, speed = 8)  # 18

gatling_gun = WeaponBlueprint(firerate = 12, barrels = 1, damage = 1, speed = 18, randomness=3 )
trident     = WeaponBlueprint(firerate = 2, barrels = 3, damage = 2, speed = 9,  spread_angle=45)
shotgun     = WeaponBlueprint(firerate = 1, barrels = 4, damage = 4, speed = 25, spread_angle=5, randomness=2 )

#Weapon for fun
malfunction = WeaponBlueprint(firerate = 12, barrels = 1, damage = 5, speed = 18, randomness=45 )

weapons = [
    cannon,
    super_auto,
    automatic,
    dual,
    dual_plasma,
    gatling_gun,
    trident,
    shotgun
]

######################################
######### CHARACTERS LAB #############
######################################

enemy_image = random.choice(IMAGES_SPACESHIPS)
enemy_ability = random.choice(abilities)
#enemy_ability = fanfire
enemy_weapon = random.choice(weapons)
# enemy_weapon = gatling_gun
enemy_speed = 4
enemy_blueprint = SpaceshipBlueprint(image = enemy_image, 
                                     health = 200, 
                                     speed = enemy_speed, 
                                     ability_function = enemy_ability, 
                                     ability_duration = 6, 
                                     cooldown_duration = 8, 
                                     weapon = enemy_weapon, 
                                     team=Team.ENEMY)

enemy_image2 = random.choice(IMAGES_SPACESHIPS)
enemy_ability2 = random.choice(abilities)
# enemy_ability2 = fanfire
enemy_weapon2 = random.choice(weapons)
# enemy_weapon2 = gatling_gun
enemy_speed2 = 4
enemy_blueprint2 = SpaceshipBlueprint(image = enemy_image2, 
                                     health = 200, 
                                     speed = enemy_speed2, 
                                     ability_function = enemy_ability2, 
                                     ability_duration = 6, 
                                     cooldown_duration = 8, 
                                     weapon = enemy_weapon2, 
                                     team=Team.ENEMY)

player_image = random.choice(IMAGES_SPACESHIPS)
player_ability = random.choice(abilities)
# player_ability = reflection
player_weapon = random.choice(weapons)
#player_weapon = gatling_gun
player_speed = random.choice([6,7,8])
player_blueprint = SpaceshipBlueprint(image = player_image, 
                                      health = 100, 
                                      speed = player_speed, 
                                      ability_function = player_ability, 
                                      ability_duration = 6, 
                                      cooldown_duration = 8, 
                                      weapon = player_weapon,
                                      team=Team.PLAYER)

agent = Agent("Enemy")