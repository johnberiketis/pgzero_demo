from utils import Object, team
from globals import WIDTH, HEIGHT
from . import spaceship
from . import reflector

class Projectile(Object):

    def __init__(self, image = 'projectile', pos = (0,0), speed = 8, health = 1, direction = -1, spin = 0, angle = 0, bounds = (WIDTH, HEIGHT), damage = 1, source = None, team = team.NEUTRAL):
        super().__init__(image, pos, speed=speed, health=health, direction=direction, timespan=10, spin=spin, angle=angle, bounds=bounds, source=source, team=team)
        self.damage: int = damage

    def update(self):
        self.y += self.speed*self.direction
        if self.y <= -50 or self.y >= self.bounds[1] + 50:
            self.kill()

    def collide(self, object):
        #TODO don't forget to use the new attribute "team" in Object
        super().collide(object)
        if (self.source != object and self.source != object.parent and self.source != object.source) or (isinstance(object, spaceship.Spaceship) and self.source != object):
        # if not self.parent_hit(object) and self.source != object.source:
            self.alive = False
        elif (isinstance(object, reflector.Reflector) and self.source != object.parent):
            self.direction = -self.direction

    # def source_hit(self, obj):
    #     if self.source == obj:
    #         return True
    #     else:
    #         return False

    # def parent_hit(self, obj):
    #     if self.source.parent:
    #         if self.source.parent == obj:
    #             return True
    #         else:
    #             return self.source.
        
    # def child_hit(self, obj):
    
    def copy(self):
        return Projectile( image=self.image, pos=self.pos, speed=self.speed, health=self.health, direction=self.direction, spin=self.spin, angle=self.angle, )