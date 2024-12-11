import math
import numpy

from pgzero.clock import clock

from library.projectile import Projectile
from library.globals import IMAGES_PROJECTILES, MIN_WEAPON_FIRERATE, MAX_WEAPON_FIRERATE, MIN_WEAPON_BARRELS, MAX_WEAPON_BARRELS
from library.globals import MIN_WEAPON_SPREAD_ANGLE, MAX_WEAPON_SPREAD_ANGLE, MIN_WEAPON_RANDOMNESS, MAX_WEAPON_RANDOMNESS
from library.utils import clamp_value
from library.blueprints import WeaponBlueprint

class Weapon():

    def __init__(self, blueprint: WeaponBlueprint):
        self.firerate = blueprint.firerate
        self.barrels = blueprint.barrels
        self.damage = blueprint.damage
        self.speed = blueprint.speed
        self.spread_angle = blueprint.spread_angle
        self.randomness = blueprint.randomness
        self._gun_ready = True
        self._points = (blueprint.damage * blueprint.barrels * blueprint.firerate) + blueprint.speed
        self._mount = None

    @property
    def firerate(self):
        return self._firerate
    
    @firerate.setter
    def firerate(self, value):
        self._firerate = clamp_value(value, MIN_WEAPON_FIRERATE, MAX_WEAPON_FIRERATE)

    @property
    def barrels(self):
        return self._barrels
    
    @barrels.setter
    def barrels(self, value):
        self._barrels = clamp_value(value, MIN_WEAPON_BARRELS, MAX_WEAPON_BARRELS)
        self._calc_muzzles_pos()

    @property
    def spread_angle(self):
        return self._spread_angle

    @spread_angle.setter
    def spread_angle(self, value):
        self._spread_angle = clamp_value(value, MIN_WEAPON_SPREAD_ANGLE, MAX_WEAPON_SPREAD_ANGLE) 

    @property
    def randomness(self):
        return self._randomness

    @randomness.setter
    def randomness(self, value):
        self._randomness = clamp_value(value, MIN_WEAPON_RANDOMNESS, MAX_WEAPON_RANDOMNESS) 

    def shoot(self):
        if self._gun_ready and self._mount:
            projectiles = []
            for i in range(self._barrels):
                if self.spread_angle and self.barrels > 1:
                    proj_direction = -self.spread_angle/2 + (i*self.spread_angle/(self.barrels-1))
                else:
                    proj_direction = 0
                if self.randomness:
                    proj_direction = proj_direction + numpy.random.normal(scale=self.randomness)
                proj_start_pos = tuple([sum(x) for x in zip(self._mount.pos, (self._muzzles_pos[i][0], self._muzzles_pos[i][1]*+self._mount.team.value))])
                projectiles.append( Projectile(self._get_image(), proj_start_pos, source = self._mount, damage = self.damage, speed = self.speed, team=self._mount.team, direction=proj_direction ) )
            self._gun_ready = False
            clock.schedule_unique(self.reload, 1/self.firerate)
            return projectiles
    
    def reload(self):
        self._gun_ready = True

    def _calc_muzzles_pos(self):
        barrels = self._barrels
        if barrels == 2:
            self._muzzles_pos = [(-8,-50), (+8,-50)]
        elif barrels == 3:
            self._muzzles_pos = [(-20,0), (0,-50), (+20,0)]
        elif barrels == 4:
            self._muzzles_pos = [(-20,0), (-8,-50), (+8,-50), (+20,0)]
        else:
            self._muzzles_pos = [(0,-50)]
    
    def _get_image(self):
        damage_index = math.ceil(self.damage)-1
        return IMAGES_PROJECTILES[damage_index] if (damage_index) < len(IMAGES_PROJECTILES) else IMAGES_PROJECTILES[-1]
