import random

from library.utils import Object
from library.powerups import generate_random_powerup
from library.globals import WIDTH, HEIGHT, ASTEROIDS_SPEED, IMAGES_ASTEROIDS, ASTEROIDS_DAMAGE, Type, Team

class Asteroid(Object):

    def __init__(self, image, pos, speed = ASTEROIDS_SPEED, health = 10, damage = 10, direction = 180, timespan = 30, spin = 0, angle = 0, drop_chance = 0, source = None, team = Team.ENEMY):
        super().__init__(image, pos, speed=speed, health=health, damage = damage, direction=direction, timespan=timespan, spin=spin, angle=angle, source=source, team=team)
        self.drop_chance = drop_chance
        
    def update(self):
        self.move_to(*self.next_pos())
        if self.y <= -50 or self.y >= self.bounds[1] + 50:
            self.kill()
        if self.health <= 0:
            self.kill()
            if random.random() < self.drop_chance:
                generate_random_powerup(self.pos)


    def collide(self, object):
        super().collide(object)
        if object.type == Type.SPACESHIP:
            self.alive = False
        elif object.type == Type.REFLECTOR:
            self.bounce()
            self.team = object.team
        elif object.type == Type.PROJECTILE:
            self._damage( object.damage )

def generate_random_asteroid():
    random_number = random.random()
    if random_number < 0.3:
        Asteroid( image = random.choice(IMAGES_ASTEROIDS[0:4]), 
              pos = (random.randint(-80,WIDTH), -30),
              health = 10, 
              drop_chance = 0.2,
              angle = random.randint(0,360),
              damage = ASTEROIDS_DAMAGE)
    elif random_number < 0.6:
        Asteroid( image = random.choice(IMAGES_ASTEROIDS[4:6]), 
              pos = (random.randint(-80,WIDTH), -30),
              health = 6,
              drop_chance = 0.1,
              angle = random.randint(0,360),
              damage = ASTEROIDS_DAMAGE - 4 )
    else:
        Asteroid( image = random.choice(IMAGES_ASTEROIDS[6:]), 
              pos = (random.randint(-80,WIDTH), -30),
              health = 4,
              drop_chance = 0.01,
              angle = random.randint(0,360),
              damage = ASTEROIDS_DAMAGE - 6 )