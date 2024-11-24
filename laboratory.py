from classes.spaceship import Spaceship
from classes.weapon import Weapon
from classes.reflector import Reflector
from agent import Agent
from utils import Team
import random
from globals import spaceship_images

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
    # Give character 4 weapons
    spaceship.weapon.set_barrels(4)

def machine_gun(spaceship: Spaceship):
    # Firerate boost
    spaceship.weapon.firerate = 14

def reflection(spaceship: Spaceship):
    # A reflective shield
    reflector = Reflector(image = 'metal_wall', pos = (spaceship.x, spaceship.y + 60*spaceship.direction), timespan = spaceship.ability_duration, team=spaceship.team)
    spaceship.collidable = False
    spaceship.add_child( reflector )

abilities = [
    super_speed,
    invisibility,
    too_many_guns,
    machine_gun,
    reflection
    ]

######################################
############ GUN LAB #################
######################################

cannon = Weapon(firerate = 2, barrels = 1, damage = 8, speed = 3)
super_auto = Weapon(firerate = 7, barrels = 1, damage = 2, speed = 12)
automatic = Weapon(firerate = 5, barrels = 1, damage = 3, speed = 12) 
dual = Weapon(firerate = 4, barrels = 2, damage = 3, speed = 10) 
dual_plasma = Weapon(firerate = 2, barrels = 2, damage = 6, speed = 6)

weapons = [
    cannon,
    super_auto,
    automatic,
    dual,
    dual_plasma
]

######################################
######### CHARACTERS LAB #############
######################################
#TODO implement point system?
# mcqueen = Spaceship(image = 'spaceship_red', health = 80, speed = 7, ability=super_speed, ability_duration = 6, weapon = super_auto)
# casper = Spaceship(image = 'spaceship_yellow', health = 80, speed = 6, ability=invisibility, ability_duration = 8, weapon = cannon)
# gunner = Spaceship(image = 'spaceship_black', health = 80, speed = 6, ability=too_many_guns, ability_duration = 6, weapon = dual)
# rambo = Spaceship(image = 'spaceship_aqua_stripe', health = 80, speed = 6, ability=machine_gun, ability_duration = 6, weapon = automatic)
# turtle = Spaceship(image = 'spaceship_green', health = 80, speed = 6, ability=reflection, ability_duration = 20, weapon = automatic)
# malware = Spaceship(image = 'spaceship_black', health = 50, speed = 4, ability=reflection, ability_duration = 8, weapon = dual_plasma)

enemy_pos = (500, 60)

enemy_image = 'spaceship_black'
enemy_ability = random.choice(abilities)
# enemy_ability = invisibility
enemy_weapon = random.choice(weapons)
enemy_speed = 4
enemy = Spaceship(image = enemy_image, pos=enemy_pos, health = 80, speed = enemy_speed, ability=enemy_ability, ability_duration = 6, weapon = enemy_weapon, team=Team.TEAM2, direction=1)

player_image = random.choice(spaceship_images)
player_ability = random.choice(abilities)
# player_ability = machine_gun
player_weapon = random.choice(weapons)
# player_weapon = dual_plasma
player_speed = random.choice([5,6,7])
player = Spaceship(image = player_image, health = 80, speed = player_speed, ability=player_ability, ability_duration = 6, weapon = player_weapon)

agent = Agent("Enemy")
agent.take_control(enemy)