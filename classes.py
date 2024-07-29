from pgzero.actor import Actor
from pgzero.clock import clock

class Projectile(Actor):

    def __init__(self, image, pos, speed = 8, direction = -1, timespan = 10, bounds = (1000, 800)):
        super().__init__(image, pos)
        self.speed = speed
        self.direction = direction
        self.timespan = timespan
        self.bounds = bounds
        self.alive = True
        clock.schedule_unique(self.kill, self.timespan)

    def update(self):
        self.y += self.speed*self.direction
        if self.y <= 0 or self.y >= self.bounds[1]:
            self.kill()

    def kill(self):
        self.alive = False

class Gun():

    def __init__(self, mount, firerate = 3, barrels = 1):
        self.mount = mount
        self.firerate = firerate
        barrels = 1 if barrels > 4 else barrels
        self.barrels = barrels
        self.muzzles_pos = []
        self.calc_muzzles_pos()
        self.gun_ready = True

    def shoot(self):
        if self.gun_ready:
            projectiles = []
            for i in range(self.barrels):
                projectiles.append(Projectile('projectile', tuple([sum(x) for x in zip(self.mount.pos, self.muzzles_pos[i])])))
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