from dataclasses import dataclass
from typing import Callable, Optional

from library.globals import Team

@dataclass 
class WeaponBlueprint():
        
    firerate: float = 1   
    barrels: int = 1     
    damage: float = 0       
    speed: float = 0       
    spread_angle: float = 0
    randomness: float = 0 

    def copy(self):
        return WeaponBlueprint( self.firerate, self.barrels, self.damage, self.speed, self.spread_angle, self.randomness)

@dataclass
class SpaceshipBlueprint():

    image: str = 'spaceships/spaceship_orange1'
    health: float = 1
    speed: int = 0
    ability_duration: float = 0
    cooldown_duration: float = 0
    update_function: Callable = None
    ability_function: Callable = None
    weapon: Optional[WeaponBlueprint] = None
    team: Team = Team.NEUTRAL

    @property
    def weapon(self):
        return self._weapon
    
    @weapon.setter
    def weapon(self, weapon_blueprint: WeaponBlueprint):
        self._weapon = weapon_blueprint.copy() if weapon_blueprint else None

      
