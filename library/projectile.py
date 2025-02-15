from library.utils import Object, clamp_value
from library.globals import WIDTH, HEIGHT, MIN_PROJECTILE_DAMAGE, MAX_PROJECTILE_DAMAGE, MIN_PROJECTILE_SPEED, MAX_PROJECTILE_SPEED,Type, Team
from library.effects import explosion

class Projectile(Object):

    def __init__(self, image = 'projectiles/projectilemissile1', pos = (0,0), speed = 8, health = 1, spin = 0, damage = 1, source = None, team = Team.NEUTRAL, direction = 0, dummy = False):
        if team == Team.ENEMY:
            direction += 180
        
        super().__init__(image, pos, health=health, direction=direction, timespan=15, spin=spin, angle=-direction, source=source, team=team, dummy=dummy)
        self.damage: float = damage
        self.speed: int = speed

    @property
    def damage(self):
        return self._damage_value
    
    @damage.setter
    def damage(self, value):
        self._damage_value = clamp_value(value, MIN_PROJECTILE_DAMAGE, MAX_PROJECTILE_DAMAGE)

    @property
    def speed(self):
        return self._speed
    
    @speed.setter
    def speed(self, value):
        self._speed = clamp_value(value, MIN_PROJECTILE_SPEED, MAX_PROJECTILE_SPEED)

    def update(self):
        self.move_to_next_pos()
        if self.y <= -10 or self.y >= (HEIGHT + 10) or self.health <= 0:
            self.alive = False

    def collide(self, object):
        if object.type == Type.REFLECTOR:
            self.bounce(rotate = True)
            self.team = object.team
        elif object.type == Type.SPACESHIP:
            self.alive = False
            explosion(self.next_pos()) 
        elif object.type != Type.POWERUP:
            self.health -= object.damage
            explosion(self.next_pos())