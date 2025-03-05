from game import play
from library.spaceship import Spaceship
from library.weapon import Weapon
from library.globals import Team

def ability(spaceship):
    '''Ability activated!'''
    spaceship.weapon.firerate = 12

weapon = Weapon( firerate = 2, 
                 barrels = 1, 
                 damage = 3, 
                 speed = 6)

spaceship = Spaceship( image = 'spaceships/spaceship_red1', 
                       health = 100, 
                       speed = 7, 
                       ability_function = ability, 
                       ability_duration = 6, 
                       cooldown_duration = 2,
                       weapon = weapon,
                       team = Team.PLAYER )

play() 