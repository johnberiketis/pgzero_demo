import pygame
from spaceship import CustomActor

# This is the laboratory where you can create your own custom abilities and 
# your custom characters(spaceships) that can use those abilities

######################################
######### ABILITIES LAB ##############
######################################
def abilitySuperSpeed(object : CustomActor):
    # Give character super speed
    duration = 5 #the duration of the ability
    object.speed = 10
    return duration

def abilityInvisibility(object : CustomActor):
    # Make character invisible
    duration = 4 #the duration of the ability
    object.image = 'spaceship_transparent'
    return duration

# def abilityShrink(object : CustomActor):
#     # Shrink the character
#     duration = 7 #the duration of the ability
#     object._surf = pygame.transform.scale(object._surf, (object.width//2, object.width//2))
#     object.y += 50
#     object.width, object.height = object._surf.get_size()
#     return duration

def abiliotyTooManyGuns(object : CustomActor):
    # Give character 4 guns
    duration = 6
    object.gun.set_barrels(4)
    return duration

def abilityMachineGun(object):
    # Firerate boost
    duration = 5 #the duration of the ability
    object.gun.firerate = 10
    return duration

######################################
######### CHARACTERS LAB #############
######################################
mcqueen = CustomActor(image = 'spaceship_red', speed = 4, ability=abilitySuperSpeed)
casper = CustomActor(image = 'spaceship_yellow', speed = 7, ability=abilityInvisibility)
gunner = CustomActor(image = 'spaceship_green', speed = 5, ability=abiliotyTooManyGuns)
rambo = CustomActor(image = 'spaceship_aqua_stripe', speed = 5, ability=abilityMachineGun)

characters_pool = [mcqueen, casper, gunner, rambo]