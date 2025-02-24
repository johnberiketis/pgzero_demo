import game

from library.spaceship import SpaceshipBlueprint
from library.blueprints import WeaponBlueprint
from library.globals import Team

def ability(spaceship):
    '''Ability activated!'''
    spaceship.weapon.firerate = 12

weapon = WeaponBlueprint( firerate = 2, 
                          barrels = 1, 
                          damage = 3, 
                          speed = 6)

spaceship = SpaceshipBlueprint( image = 'spaceships/spaceship_red1', 
                                health = 10, 
                                speed = 7, 
                                ability_function = ability, 
                                ability_duration = 6, 
                                cooldown_duration = 2,
                                weapon = weapon,
           
                                team = Team.PLAYER )

#

game.play()