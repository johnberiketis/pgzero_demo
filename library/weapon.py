import math
import numpy

from pgzero.clock import clock

from library.projectile import Projectile
from library.globals import IMAGES_PROJECTILES
from library.utils import clamp_value

class Weapon():

    def __init__(self, firerate = 3, barrels = 1, damage = 1, speed = 8, mount = None, spread_angle = 0, randomness = 0):
        self.firerate = firerate
        self.barrels = barrels
        self.damage = damage
        self.speed = speed
        self.spread_angle = spread_angle
        self.randomness = randomness
        self._gun_ready = True
        self._points = (damage * barrels * firerate) + speed
        self._mount = mount

    @property
    def randomness(self):
        return self._randomness

    @randomness.setter
    def randomness(self, value):
        self._randomness = clamp_value(value, 0, 45) 

    @property
    def firerate(self):
        return self._firerate
    
    @firerate.setter
    def firerate(self, value):
        self._firerate = clamp_value(value, 1, 12)

    @property
    def barrels(self):
        return self._barrels
    
    @barrels.setter
    def barrels(self, value):
        self._barrels = clamp_value(value, 1, 4)
        self._calc_muzzles_pos()
        
    @property
    def damage(self):
        return self._damage
    
    @damage.setter
    def damage(self, value):
        self._damage = clamp_value(value, 0, 10)

    @property
    def speed(self):
        return self._speed
    
    @speed.setter
    def speed(self, value):
        self._speed = clamp_value(value, 0, 25)

    def assemble(self, mount):
        return Weapon(firerate=self._firerate, barrels=self._barrels, damage=self._damage, speed=self._speed, mount=mount, spread_angle=self.spread_angle, randomness=self.randomness)

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
