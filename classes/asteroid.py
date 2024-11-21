from utils import Object
from globals import WIDTH, HEIGHT
from . import spaceship
from . import projectile
from . import reflector

class Asteroid(Object):

    def __init__(self, image, pos, speed = 1, health = 10, direction = 1, timespan = 30, spin = 0, angle = 0, bounds = (WIDTH, HEIGHT), source = None):
        super().__init__(image, pos, speed=speed, health=health, direction=direction, timespan=timespan, spin=spin, angle=angle, bounds=bounds, source=source)

    def update(self):
        self.angle = self.angle + self.spin
        self.y += self.speed*self.direction
        if self.y <= -50 or self.y >= self.bounds[1] + 50 or self.health <= 0:
            self.kill()

    def collide(self, object):
        super().collide(object)
        if isinstance(object, spaceship.Spaceship):
            self.alive = False
        if isinstance(object, reflector.Reflector):
            self.direction = -self.direction
        elif isinstance(object, projectile.Projectile):
            self.damage( object.damage )
