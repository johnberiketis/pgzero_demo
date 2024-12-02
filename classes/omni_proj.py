from utils import Object, OmniObject
from globals import WIDTH, HEIGHT, Type, Team
from effects import explosion
import math

class OmniProjectile(OmniObject):

    def __init__(self, image = 'projectiles/projectilemissile1', pos = (0,0), speed = 8, health = 1, spin = 0, damage = 1, source = None, team = Team.NEUTRAL, direction = 0):
        if team == Team.ENEMY:
            direction += 180
        
        super().__init__(image, pos, speed=speed, health=health, direction=direction, timespan=10, spin=spin, angle=-direction, source=source, team=team)
        self.damage: int = damage

    def update(self):
        self.move_to(*self.next_pos())
        if self.y <= -10 or self.y >= self.bounds[1] + 10 or self.health <= 0:
            self.kill()

    def collide(self, object):
        super().collide(object)
        if object.type == Type.REFLECTOR:
            self.bounce(rotate = True)
            self.team = object.team
        elif object.type == Type.SPACESHIP:
            self.alive = False
            explosion(self.next_pos()) 
        elif object.type != Type.POWERUP:
            self.health -= object.damage
            explosion(self.next_pos())
        
    
    # def copy(self):
    #     return OmniProjectile( image=self.image, pos=self.pos, speed=self.speed, health=self.health, direction=self.direction, spin=self.spin, angle=self.angle)