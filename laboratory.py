from classes import Spaceship

# This is the laboratory where you can create your own custom abilities and 
# your spacehips that can use those abilities

######################################
######### ABILITIES LAB ##############
######################################
def super_speed(spaceship : Spaceship):
    # Give character super speed
    duration = 5 #the duration of the ability
    spaceship.speed = 10
    return duration

def invisibility(spaceship : Spaceship):
    # Make character invisible
    duration = 4 #the duration of the ability
    spaceship.image = 'spaceship_transparent'
    return duration

def too_many_guns(spaceship : Spaceship):
    # Give character 4 guns
    duration = 6
    spaceship.gun.set_barrels(4)
    return duration

def machine_gun(spaceship: Spaceship):
    # Firerate boost
    duration = 5 #the duration of the ability
    spaceship.gun.firerate = 10
    return duration

######################################
######### CHARACTERS LAB #############
######################################
mcqueen = Spaceship(image = 'spaceship_red', speed = 4, ability=super_speed)
casper = Spaceship(image = 'spaceship_yellow', speed = 7, ability=invisibility)
gunner = Spaceship(image = 'spaceship_green', speed = 5, ability=too_many_guns)
rambo = Spaceship(image = 'spaceship_aqua_stripe', speed = 5, ability=machine_gun)

characters_pool = [mcqueen, casper, gunner, rambo]

# character = random.choice(characters_pool)

# Use the below line to avoid a random character selection
character = characters_pool[3]