from inspect import signature
import re

from library.spaceship import Spaceship
from library.weapon import Weapon
from library.globals import MAX_SPACESHIP_POINTS, MAX_HEALTH_WEIGHT, HEALTH_WEIGHT, SPEED_WEIGHT, ABILITY_DURATION_WEIGHT, COOLDOWN_WEIGHT, COLLIDABLE_WEIGHT, SPACESHIP_CHILDS_LENGTH_WEIGHT

class DummyControl():

    def __init__(self, name, puppet = None):
        self.name = name
        self.puppet = puppet
        
        self.right = False
        self.left = False
        self.ability_key = False
        self.shooting_key = False

    def take_control(self, puppet):
        self.puppet = puppet
        puppet._control = self

dummyControl = DummyControl("Dummy")
dummyWeaponBlueprint = Weapon( 3, 1, 2, 6 )
dummySpaceship = Spaceship(
    health=50,
    speed=5,
    cooldown_duration=6,
    ability_duration=6,
    weapon=dummyWeaponBlueprint
)

class InspectorResult():
     
     def __init__(self, status, message = None):
          self.status = status
          self.message = message

def calculate_ability_points(ability):
    if callable(ability):
        sig = signature(ability)
        if len(sig.parameters) == 1:
            spaceship = Spaceship(dummySpaceship, dummy=True)
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
        return spaceship.max_health*       MAX_HEALTH_WEIGHT\
             + spaceship.health*           HEALTH_WEIGHT\
             + spaceship.speed*            SPEED_WEIGHT\
             + spaceship.ability_duration* ABILITY_DURATION_WEIGHT\
             - spaceship.cooldown*         COOLDOWN_WEIGHT\
             - int(spaceship.collidable)*  COLLIDABLE_WEIGHT\
             + len(spaceship.childs)*      SPACESHIP_CHILDS_LENGTH_WEIGHT       
        
    return 0


def calculate_points(spaceship: Spaceship):
    ability_weight = (spaceship.ability_duration/spaceship.cooldown)
    return calculate_spaceship_points(spaceship) + \
           calculate_weapon_points(spaceship.weapon) + \
           calculate_ability_points(spaceship._ability)*ability_weight

def update_function_pass(update_func):
    
    if not callable(update_func):
        return InspectorResult(False, "Update function provided is not a funtion")
    else:
        sig = signature(update_func)
        if len(sig.parameters) != 1:
            return InspectorResult(False, "Update function must take 1 argument")
        else:
            erroneous_keys = []
            erroneous_update_no_key = False
            spaceship = Spaceship(dummySpaceshipBlueprint, dummy=True)
            dummyControl.take_control(spaceship)
            points_before = calculate_spaceship_points(spaceship) + calculate_weapon_points(spaceship.weapon)

            update_func(spaceship)
            points_after_no_key = calculate_spaceship_points(spaceship) + calculate_weapon_points(spaceship.weapon)
            points_difference_no_key = points_after_no_key - points_before
            if points_difference_no_key:
                erroneous_update_no_key = True

            dummyControl.left = True
            spaceship = Spaceship(dummySpaceshipBlueprint, dummy=True)
            dummyControl.take_control(spaceship)
            update_func(spaceship)
            points_after_left = calculate_spaceship_points(spaceship) + calculate_weapon_points(spaceship.weapon)
            points_difference_left = points_after_left - points_before
            if points_difference_left:
                erroneous_keys.append("left")
            dummyControl.left = False

            dummyControl.right = True
            spaceship = Spaceship(dummySpaceshipBlueprint, dummy=True)
            dummyControl.take_control(spaceship)
            update_func(spaceship)
            points_after_right = calculate_spaceship_points(spaceship) + calculate_weapon_points(spaceship.weapon)
            points_difference_right = points_after_right - points_before
            if points_difference_right:
                erroneous_keys.append("right")
            dummyControl.right = False

            dummyControl.ability_key = True
            spaceship = Spaceship(dummySpaceshipBlueprint, dummy=True)
            dummyControl.take_control(spaceship)
            update_func(spaceship)
            points_after_ability = calculate_spaceship_points(spaceship) + calculate_weapon_points(spaceship.weapon)
            points_difference_ability = points_after_ability - points_before
            if points_difference_ability:
                erroneous_keys.append("ability")
            dummyControl.ability_key = False

            dummyControl.shooting_key = True
            spaceship = Spaceship(dummySpaceshipBlueprint, dummy=True)
            dummyControl.take_control(spaceship)
            update_func(spaceship)
            points_after_shoot = calculate_spaceship_points(spaceship) + calculate_weapon_points(spaceship.weapon)
            points_difference_shoot = points_after_shoot - points_before
            if points_difference_shoot:
                erroneous_keys.append("shoot")
            dummyControl.shooting_key = False

            if len(erroneous_keys) > 0 or erroneous_update_no_key:
                msg_suffix = ''
                if len(erroneous_keys) > 0:
                    msg_suffix = "\nThe following actions inside update alter the spaceship: " + str.join(', ', erroneous_keys)
                return InspectorResult(False, "Update function should not alter spaceship's capabilities" + msg_suffix)
            else:
                return InspectorResult(True)
            
def run_inspection(spaceship_blueprint: SpaceshipBlueprint):
    inspector_results = [] 
    spaceship_points = calculate_points(spaceship_blueprint)
    print("Spaceship points = ", spaceship_points)
    if spaceship_points > MAX_SPACESHIP_POINTS:
        inspector_results.append( InspectorResult(False, f"The spaceship is overpowered!\nPoints: {spaceship_points} of max: {MAX_SPACESHIP_POINTS}") )
    inspector_results.append( update_function_pass(spaceship_blueprint.update_function) )

    inspection_message = ""
    for result in inspector_results:
        if result.status == False:
            inspection_message += result.message + "\n"

    return inspection_message
    
def run_source_code_inspection(source_code):
    return re.findall(r'\b_\w+', source_code)