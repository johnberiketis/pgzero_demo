from .projectile import Projectile
from pgzero.clock import clock
from globals import IMAGES_PROJECTILES
import math

class Weapon():

    def __init__(self, firerate = 3, barrels = 1, damage = 1, speed = 8, mount = None):
        self.mount = None,
        self.firerate = firerate
        self.barrels = 4 if barrels > 4 else barrels
        self.damage = damage
        self.speed = speed
        self.muzzles_pos = []
        self.calc_muzzles_pos()
        self.gun_ready = True
        self.points = (damage * barrels * firerate) + speed
        self.mount = mount

    def assemble(self, mount):
        return Weapon(firerate=self.firerate, barrels=self.barrels, damage=self.damage, speed=self.speed, mount=mount)

    def shoot(self):
        if self.gun_ready and self.mount:
            projectiles = []
            for i in range(self.barrels):
                projectiles.append(Projectile(self.get_image(), tuple([sum(x) for x in zip(self.mount.pos, (self.muzzles_pos[i][0], self.muzzles_pos[i][1]*-self.mount.direction))]), source = self.mount, damage = self.damage, speed = self.speed, team=self.mount.team, direction=self.mount.direction))
            self.gun_ready = False
            clock.schedule_unique(self.reload, 1/self.firerate)
            return projectiles
    
    def reload(self):
        self.gun_ready = True
    
    # def set_mount(self, obj):
    #     self.mount = obj

    def set_barrels(self, barrels):
        self.barrels = barrels
        self.calc_muzzles_pos()

    def calc_muzzles_pos(self):
        barrels = self.barrels
        if barrels == 2:
            self.muzzles_pos = [(-8,-50), (+8,-50)]
        elif barrels == 3:
            self.muzzles_pos = [(-20,0), (0,-50), (+20,0)]
        elif barrels == 4:
            self.muzzles_pos = [(-20,0), (-8,-50), (+8,-50), (+20,0)]
        else:
            self.muzzles_pos = [(0,-50)]
    
    def get_image(self):
        damage_index = math.ceil(self.damage)-1
        return IMAGES_PROJECTILES[damage_index] if (damage_index) < len(IMAGES_PROJECTILES) else IMAGES_PROJECTILES[-1]