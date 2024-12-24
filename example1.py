'''
Here is your main workplace. A simple interface module to affect the game's
functionality. All objects, functions and variables from here get transfered to
the game's code. Examples include the spaceship's ability to move and shoot,
it's attributes like speed, health, ability and more. Here you can create
objects such as powerups, weapons, abilities, projectiles and even enemies. You
can design and create the spaceship you dreamed but also unleash the final boss
to challenge you and your friends. Want to do something for fun? Ofcourse your
weapon can shoot sideways! Your imagination is the limit! (But also RAM and CPU)
'''

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

from library.blueprints import WeaponBlueprint
weapon = WeaponBlueprint(firerate=2, barrels=1, damage=2, speed=6)

powerup = None

play() 