import pygame
from spaceship import CustomActor

# This is the laboratory where you can create your own custom abilities and 
# your custom characters(spaceships) that can use those abilities

######################################
######### ABILITIES LAB ##############
######################################
def abilitySuperSpeed(object):
    # Give character super speed
    duration = 5 #the duration of the ability
    object.speed = 10
    return duration

def abilityInvisibility(object):
    # Make character invisible
    duration = 4 #the duration of the ability
    object.y = -100
    return duration

def abilityShrink(object):
    # Shrink the character
    duration = 7 #the duration of the ability
    object._surf = pygame.transform.scale(object._surf, (object.width//2, object.width//2))
    object.y += 50
    object.width, object.height = object._surf.get_size()
    return duration


######################################
######### CHARACTERS LAB #############
######################################
mcqueen = CustomActor(image = 'spaceship_red', speed = 4, ability=abilitySuperSpeed)
casper = CustomActor(image = 'spaceship_yellow', speed = 7, ability=abilityInvisibility)
antman = CustomActor(image = 'spaceship_green', speed = 5, ability=abilityShrink)


characters_pool = [mcqueen, casper, antman]