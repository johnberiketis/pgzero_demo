import pygame as pg
from pgzero.actor import Actor

class Projectile(Actor):
    """a bullet the Player sprite fires."""

    def __init__(self, image, pos):
        super().__init__(image, pos)
        self.speed = 5
        self.direction = 1

    def update(self):
        self.y += self.speed
        if self.y <= 0 or self.y >= 0:
            self.kill()
