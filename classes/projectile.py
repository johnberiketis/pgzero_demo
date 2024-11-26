from utils import Object
from globals import WIDTH, HEIGHT, Type, Team

class Projectile(Object):

    def __init__(self, image = 'projectile', pos = (0,0), speed = 8, health = 1, direction = -1, spin = 0, angle = 0, bounds = (WIDTH, HEIGHT), damage = 1, source = None, team = Team.NEUTRAL):
        super().__init__(image, pos, speed=speed, health=health, direction=direction, timespan=10, spin=spin, angle=angle, bounds=bounds, source=source, team=team)
        self.damage: int = damage

    def update(self):
        self.y += self.speed*self.direction
        if self.y <= -10 or self.y >= self.bounds[1] + 10:
            self.kill()

    def collide(self, object):
        super().collide(object)
        if object.team != self.team:
            if object.type == Type.REFLECTOR:
                self.direction = -self.direction
                self.team = object.team
                self.angle += 180
            else:
                self.alive = False
    
    def copy(self):
        return Projectile( image=self.image, pos=self.pos, speed=self.speed, health=self.health, direction=self.direction, spin=self.spin, angle=self.angle)