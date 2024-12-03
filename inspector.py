from inspect import signature
from classes.spaceship import Spaceship
from classes.weapon import Weapon

def calculate_ability_points(ability):
    if callable(ability):
        sig = signature(ability)
        if len(sig.parameters) == 1:
            spaceship = Spaceship()
            points_before = calculate_spaceship_points(spaceship) + calculate_weapon_points(spaceship.weapon)
            ability(spaceship)
            points_after = calculate_spaceship_points(spaceship) + calculate_weapon_points(spaceship.weapon)
            return points_after - points_before
        
    return 0

def calculate_weapon_points(weapon: Weapon):
    if isinstance(weapon, Weapon):
        return (weapon.firerate*weapon.barrels*weapon.damage) + weapon.speed
    else:
        return 0

def calculate_spaceship_points(spaceship: Spaceship):
    if isinstance(spaceship, Spaceship):
        return spaceship.max_health*                           0.5\
             + spaceship.speed*                                1.0\
             + spaceship.ability_duration*                     1.0\
             - spaceship.cooldown*                             1.0\
             - int(spaceship.collidable)*                      10.0\
             + len(spaceship.childs)*                          10.0       
        
    return 0


def calculate_points(spaceship: Spaceship):
    return calculate_spaceship_points(spaceship) + \
           calculate_weapon_points(spaceship.weapon) + \
           calculate_ability_points(spaceship.ability)