from classes.spaceship import Spaceship
from classes.weapon import Weapon
from classes.reflector import Reflector
from agent import Agent
from utils import team

# This is the laboratory where you can create your own custom 
# abilities, weapons and spaceships 

######################################
######### ABILITIES LAB ##############
######################################

def super_speed(spaceship : Spaceship):
    # Give character super speed
    spaceship.speed = 14

def invisibility(spaceship : Spaceship):
    # Make character invisible
    spaceship.image = 'spaceship_transparent'
    spaceship.collidable = False

def too_many_guns(spaceship : Spaceship):
    # Give character 4 weapons
    spaceship.weapon.set_barrels(4)

def machine_gun(spaceship: Spaceship):
    # Firerate boost
    spaceship.weapon.firerate = 16

def reflection(spaceship: Spaceship):
    # A reflective shield
    reflector = Reflector(image = 'metal_wall', pos = (spaceship.x, spaceship.y - 60), timespan = spaceship.ability_duration)
    spaceship.add_child( reflector )
    return reflector

######################################
############ GUN LAB #################
######################################

cannon = Weapon(firerate = 2, barrels = 1, damage = 8, speed = 3)
super_auto = Weapon(firerate = 6, barrels = 1, damage = 1, speed = 10)
automatic = Weapon(firerate = 4, barrels = 1, damage = 2, speed = 10) 
dual = Weapon(firerate = 4, barrels = 2, damage = 3, speed = 10) 

######################################
######### CHARACTERS LAB #############
######################################
#TODO implement point system?
mcqueen = Spaceship(image = 'spaceship_red', speed = 7, ability=super_speed, ability_duration = 6, weapon = super_auto)
casper = Spaceship(image = 'spaceship_yellow', speed = 6, ability=invisibility, ability_duration = 8, weapon = cannon)
gunner = Spaceship(image = 'spaceship_black', speed = 6, ability=too_many_guns, ability_duration = 6, weapon = dual)
rambo = Spaceship(image = 'spaceship_aqua_stripe', speed = 6, ability=machine_gun, ability_duration = 6, weapon = automatic)
turtle = Spaceship(image = 'spaceship_green', speed = 6, ability=reflection, ability_duration = 20, weapon = automatic)

agent = Agent("Enemy")
enemySpaceship = Spaceship(image = 'spaceship_black', speed = 6, ability=too_many_guns, ability_duration = 6, weapon = dual, team=team.TEAM2)
agent.take_control(enemySpaceship)

# characters_pool = [mcqueen, casper, gunner, rambo]
# character = random.choice(characters_pool)

character = enemySpaceship