import game

from library.spaceship import SpaceshipBlueprint
from library.blueprints import WeaponBlueprint
from library.globals import Team

def ability(spaceship):
    spaceship.speed = 5

weapon = WeaponBlueprint( firerate = 2, 
                          barrels = 3, 
                          damage = 1, 
                          speed = 6 )

spaceship = SpaceshipBlueprint( image = 'spaceships/spaceship_orange6', 
                                health = 50, 
                                speed = 7, 
                                ability_function = ability, 
                                ability_duration = 6, 
                                cooldown_duration = 2,
                                weapon = weapon,
                                team = Team.PLAYER )

game.play()