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

from library.spaceship import Spaceship, default_update
from library.pilot import Pilot, Player1, Player2

enemy_spaceship = SpaceshipBlueprint(image = 'spaceships/spaceship_black1', 
                                            health = 50, 
                                            speed = 4, 
                                            ability_function = ability,
                                            ability_duration = 6, 
                                            cooldown_duration = 6, 
                                            weapon = weapon, 
                                            team=Team.ENEMY)

  
pilot = Pilot("Enemy")
enemy_spaceship = Spaceship( enemy_spaceship )
pilot.take_control( enemy_spaceship )


game.play()