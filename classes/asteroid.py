from utils import Object
from globals import WIDTH, HEIGHT, Type, Team

class Asteroid(Object):

    def __init__(self, image, pos, speed = 1, health = 10, direction = 1, timespan = 30, spin = 0, angle = 0, bounds = (WIDTH, HEIGHT), source = None, team = Team.NEUTRAL):
        super().__init__(image, pos, speed=speed, health=health, direction=direction, timespan=timespan, spin=spin, angle=angle, bounds=bounds, source=source, team=team)

    def update(self):
        self.angle = self.angle + self.spin
        self.y += self.speed*self.direction
        if self.y <= -50 or self.y >= self.bounds[1] + 50 or self.health <= 0:
            self.kill()

    def collide(self, object):
        super().collide(object)
        if object.type == Type.SPACESHIP and object.team != self.team:
            self.alive = False
        elif object.type == Type.REFLECTOR and object.team != self.team:
            self.direction = -self.direction
            self.team = object.team
        elif object.type == Type.PROJECTILE and object.team != self.team:
            self.damage( object.damage )
