from utils import Object
from globals import WIDTH, HEIGHT, IMAGES_POWERUPS, Type, Team
from .spaceship import Spaceship 
import random

class Powerup(Object):

    def __init__(self, image, pos, effect = None, speed = 3, direction = -1):
        super().__init__(image=image, pos=pos, speed=speed, direction=direction)
        self.effect = effect

    def update(self):
        self.angle = self.angle + self.spin
        self.y += self.speed*-self.direction
        if self.y <= -50 or self.y >= self.bounds[1] + 50 or self.health <= 0:
            self.kill()

    def collide(self, object):
        super().collide(object)
        if object.type != Type.PROJECTILE and object.team != Team.ENEMY:
            self.alive = False

def repair(spaceship: Spaceship):
    spaceship.health += 20

def weapon_plus(spaceship: Spaceship):
    spaceship.weapon.barrels += 1
    spaceship._default["weapon"].barrels += 1

def projectile_upgrade(spaceship: Spaceship):
    spaceship.weapon.damage += 1
    spaceship._default["weapon"].damage += 1

def generate_random_powerup(position = None):
    random_number = random.random()
    if random_number < 0.33:
        name = "repair"
        effect = repair
    elif random_number < 0.66:
        name = "weapon_plus"
        effect = weapon_plus
    else:
        name = "projectile_upgrade"
        effect = projectile_upgrade
    Powerup( image = IMAGES_POWERUPS[name], 
             pos = position if position else (random.randint(-80,WIDTH), -30),
            effect= effect)
