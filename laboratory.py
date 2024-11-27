from classes.spaceship import Spaceship
from classes.weapon import Weapon
from classes.reflector import Reflector
from agent import Agent
from utils import Team
import random
from globals import IMAGES_SPACESHIPS

# This is the laboratory where you can create your own custom 
# abilities, weapons and spaceships 

######################################
######### ABILITIES LAB ##############
######################################

def super_speed(spaceship : Spaceship):
    # Give character super speed
    spaceship.speed = 13

def invisibility(spaceship : Spaceship):
    #TODO fix bug that show the inv image looking up on the enemy
    # Make character invisible
    spaceship.set_image('spaceship_transparent')
    spaceship.collidable = False

def too_many_guns(spaceship : Spaceship):
    # Give character 4 weapon barrels
    spaceship.weapon.set_barrels(4)

def machine_gun(spaceship: Spaceship):
    # Firerate boost
    spaceship.weapon.firerate = 14

def reflection(spaceship: Spaceship):
    # A reflective shield
    reflector = Reflector(image = 'metal_wall', pos = (spaceship.x, spaceship.y + 60*spaceship.direction), timespan = spaceship.ability_duration, team=spaceship.team)
    spaceship.collidable = False
    spaceship.add_child( reflector )

def buff_up(spaceship: Spaceship):
    # Increase weapon damage
    spaceship.weapon.damage = spaceship.weapon.damage + 2/spaceship.weapon.barrels

abilities = [
    super_speed,
    invisibility,
    too_many_guns,
    machine_gun,
    reflection,
    buff_up
    ]

######################################
############ WEAPON LAB ##############
######################################

#TODO implement point system weapon.points = (damage * barrels * firerate) + speed
cannon      = Weapon(firerate = 2, barrels = 1, damage = 8, speed = 5)  # 21
super_auto  = Weapon(firerate = 9, barrels = 1, damage = 1, speed = 12) # 21
automatic   = Weapon(firerate = 5, barrels = 1, damage = 4, speed = 11) # 31
dual        = Weapon(firerate = 3, barrels = 2, damage = 3, speed = 8)  # 26
dual_plasma = Weapon(firerate = 2, barrels = 2, damage = 5, speed = 5)  # 25
gatling_gun = Weapon(firerate = 3, barrels = 3, damage = 2, speed = 7)  # 25

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
# TODO implement point system?
# Spaceship cost = {cost_of(spaceship in normal mode) * cooldown_duration} + {cost_of(spaceship in ability mode) * ability_duration}
# mcqueen = Spaceship(image = 'spaceship_red', health = 80, speed = 7, ability=super_speed, ability_duration = 6, weapon = super_auto)
# casper = Spaceship(image = 'spaceship_yellow', health = 80, speed = 6, ability=invisibility, ability_duration = 8, weapon = cannon)
# gunner = Spaceship(image = 'spaceship_black', health = 80, speed = 6, ability=too_many_guns, ability_duration = 6, weapon = dual)
# rambo = Spaceship(image = 'spaceship_aqua_stripe', health = 80, speed = 6, ability=machine_gun, ability_duration = 6, weapon = automatic)
# turtle = Spaceship(image = 'spaceship_green', health = 80, speed = 6, ability=reflection, ability_duration = 20, weapon = automatic)
# malware = Spaceship(image = 'spaceship_black', health = 50, speed = 4, ability=reflection, ability_duration = 8, weapon = dual_plasma)

enemy_image = 'spaceship_black'
# enemy_ability = random.choice(abilities)
enemy_ability = invisibility
enemy_weapon = random.choice(weapons)
# enemy_weapon = super_auto
enemy_speed = 4
enemy = Spaceship(image = enemy_image, health = 80, speed = enemy_speed, ability=enemy_ability, ability_duration = 6, weapon = enemy_weapon, team=Team.ENEMY, direction=1)

player_image = random.choice(IMAGES_SPACESHIPS)
# player_ability = random.choice(abilities)
player_ability = invisibility
# player_weapon = random.choice(weapons)
player_weapon = gatling_gun
player_speed = random.choice([5,6,7])
player = Spaceship(image = player_image, health = 80, speed = player_speed, ability=player_ability, ability_duration = 6, weapon = player_weapon)

agent = Agent("Enemy")
agent.take_control(enemy)