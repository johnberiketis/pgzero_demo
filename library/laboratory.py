import random

from library.spaceship import Spaceship
from library.weapon import Weapon
from library.projectile import Projectile
from library.agent import Agent
from library.utils import Team
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
    '''Bombs spread!!!'''
    n = 10
    spread = 100
    for i in range(0,n+1):
        Projectile(image = 'others/bomb', pos = spaceship.pos, speed=2, damage = 12, health = 8, source=spaceship, team=spaceship.team, direction= -spread/2 + (i*spread/n) )

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
cannon      = Weapon(firerate = 2, barrels = 1, damage = 8, speed = 6)  # 22
super_auto  = Weapon(firerate = 8, barrels = 1, damage = 1.5, speed = 13) # 25
automatic   = Weapon(firerate = 4, barrels = 1, damage = 4, speed = 12) # 28
dual        = Weapon(firerate = 2, barrels = 2, damage = 3, speed = 9)  # 21
dual_plasma = Weapon(firerate = 1, barrels = 2, damage = 5, speed = 8)  # 18
gatling_gun = Weapon(firerate = 2, barrels = 3, damage = 2, speed = 9)  # 21

test_cannon = Weapon(firerate = 8, barrels = 1, damage = 8, speed = 9)

weapons = [
    cannon,
    super_auto,
    automatic,
    dual,
    dual_plasma,
    gatling_gun
]

######################################
######### CHARACTERS LAB #############
######################################

enemy_image = random.choice(IMAGES_SPACESHIPS)
enemy_ability = random.choice(abilities)
enemy_weapon = random.choice(weapons)
enemy_speed = 4
enemy = Spaceship(image = enemy_image, health = 150, speed = enemy_speed, ability=enemy_ability, ability_duration = 8, cooldown = 4, weapon = enemy_weapon, team=Team.ENEMY)

player_image = random.choice(IMAGES_SPACESHIPS)
player_ability = random.choice(abilities)
player_weapon = random.choice(weapons)
player_speed = random.choice([6,7,8])
player = Spaceship(image = player_image, health = 100, speed = player_speed, ability=player_ability, ability_duration = 8, cooldown = 4, weapon = player_weapon)

agent = Agent("Enemy")
agent.take_control(enemy)