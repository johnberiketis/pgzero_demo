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

# speed = 5
# health = 100
# cooldown = 6
# ability_duration = 8

# def move(spaceship):
#     if spaceship.keyboard.left:
#         spaceship.x = spaceship.x - spaceship.speed
#     elif spaceship.keyboard.right:
#         spaceship.x = spaceship.x + spaceship.speed

# def shoot(spaceship):
#     if spaceship.keyboard.space:
#         spaceship.weapon.shoot()

# def ability(spaceship):
#     '''Quad fire!!!'''
#     spaceship.weapon.barrels = 4

# from library.weapon import Weapon
# weapon = Weapon(firerate=5, barrels=3, damage=4, speed=5, spread_angle=10, randomness=3)

play() 