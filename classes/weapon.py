from globals import ProjectileImage
from .projectile import Projectile
from pgzero.clock import clock

class Weapon():

    def __init__(self, firerate = 3, barrels = 1, damage = 1, speed = 8):
        self.mount = None,
        self.firerate = firerate
        self.barrels = 4 if barrels > 4 else barrels
        self.damage = damage
        self.speed = speed
        self.muzzles_pos = []
        self.calc_muzzles_pos()
        self.gun_ready = True

    def copy(self):
        return Weapon(firerate=self.firerate, barrels=self.barrels, damage=self.damage, speed=self.speed)

    def shoot(self):
        if self.gun_ready and self.mount:
            projectiles = []
            for i in range(self.barrels):
                projectiles.append(Projectile(self.get_image(), tuple([sum(x) for x in zip(self.mount.pos, self.muzzles_pos[i])]), source = self.mount, damage = self.damage, speed = self.speed, team=self.mount.team))
            self.gun_ready = False
            clock.schedule_unique(self.reload, 1/self.firerate)
            return projectiles
    
    def reload(self):
        self.gun_ready = True
    
    def set_mount(self, obj):
        self.mount = obj

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
        match self.damage:
            case 1:
                return ProjectileImage.TYPE0.value
            case 2:
                return ProjectileImage.TYPE1.value
            case 3:
                return ProjectileImage.TYPE2.value
            case 4:
                return ProjectileImage.TYPE3.value
            case 5:
                return ProjectileImage.TYPE4.value
            case 6:
                return ProjectileImage.TYPE5.value
            case _:
                return ProjectileImage.TYPE6.value