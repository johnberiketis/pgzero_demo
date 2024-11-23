from utils import Object
from globals import Team

class Reflector(Object):
    def __init__(self, image = 'metal_wall', pos = (0,0), health = 20, timespan = 5, team = Team.NEUTRAL):
        super().__init__(image, pos, health=health, timespan=timespan, team=team)
