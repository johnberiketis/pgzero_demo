from utils import Object
from globals import Team
from pgzero.loaders import sounds

class Reflector(Object):
    def __init__(self, image = 'others/metal_wall', pos = (0,0), health = 20, timespan = 5, team = Team.NEUTRAL):
        super().__init__(image, pos, health=health, timespan=timespan, team=team)
        # sounds.sfx_shield_up.play()

    def kill(self):
        self.alive = False
        # sounds.sfx_shield_down.play()