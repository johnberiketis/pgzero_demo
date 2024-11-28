from utils import Object
from globals import WIDTH, HEIGHT, ASTEROIDS_SPEED, IMAGES_ASTEROIDS, Type, Team
import random

class Asteroid(Object):

    def __init__(self, image, pos, speed = ASTEROIDS_SPEED, health = 10, direction = 1, timespan = 30, spin = 0, angle = 0, bounds = (WIDTH, HEIGHT), source = None, team = Team.ENEMY):
        super().__init__(image, pos, speed=speed, health=health, direction=direction, timespan=timespan, spin=spin, angle=angle, bounds=bounds, source=source, team=team)

    def update(self):
        self.angle = self.angle + self.spin
        self.y += self.speed*self.direction
        if self.y <= -50 or self.y >= self.bounds[1] + 50 or self.health <= 0:
            self.kill()

    def collide(self, object):
        super().collide(object)
        if object.type == Type.SPACESHIP:
            self.alive = False
        elif object.type == Type.REFLECTOR:
            self.direction = -self.direction
            self.team = object.team
        elif object.type == Type.PROJECTILE:
            self._damage( object.damage )

def generate_random_asteroid():
    Asteroid( image = random.choice(IMAGES_ASTEROIDS), 
              pos = (random.randint(-80,WIDTH), -30),
              angle = random.randint(1,360) )