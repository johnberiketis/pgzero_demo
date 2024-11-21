from utils import Object

class Enemy(Object):

    def __init__(self, image, pos, health, speed):
        super().__init__(image, pos, health=health, speed=speed)

