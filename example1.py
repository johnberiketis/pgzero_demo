from game import play

speed = 2
health = 10
cooldown = 6
ability_duration = 2
image = 'spaceships/spaceship_orange7'

def update(spaceship):
    if spaceship.control.left:
        spaceship.x -= spaceship.speed
    elif spaceship.control.right:
        spaceship.x += spaceship.speed

    if spaceship.control.ability_key:
        spaceship.activate_ability()
    
    if spaceship.control.shooting_key:
        spaceship.weapon.shoot()   

def ability(spaceship):
    '''Ability activated'''
    spaceship.speed = 8

from library.weapon import Weapon
weapon = Weapon(firerate=2, barrels=1, damage=2, speed=6)

play() 