from utils import Object

class Reflector(Object):
    def __init__(self, image = 'metal_wall', pos = (0,0), health = 20, timespan = 5):
        super().__init__(image, pos, health=health, timespan=timespan)
