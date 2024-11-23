from enum import Enum, IntEnum
from pgzero.clock import clock
from pgzero.actor import Actor
from globals import WIDTH, HEIGHT
from world import world

class team(IntEnum):
    ENEMY = -1
    NEUTRAL = 0
    TEAM1 = 1
    TEAM2 = 2
   

class Object(Actor):
        
    def __init__(self, image, pos, speed = 0, health = 1, direction = 0, timespan = -1, spin = 0, angle = 0, bounds = (WIDTH, HEIGHT), alive = True, collidable = True, source = None, team = team.NEUTRAL):
        super().__init__(image, pos)
        self.speed = speed
        self.health = health
        self.max_health = health
        self.direction = direction
        self.timespan = timespan
        self.bounds = bounds
        self.alive = alive
        self.collidable = collidable
        self.spin = spin
        self.angle = angle
        self.team = team
        self.source = source
        self.parent = None
        self.childs = []
        world.add_object(self)
        if self.timespan > 0:
            clock.schedule_unique(self.kill, self.timespan)

    def handle_collitions(self, objects):
        if self.collidable:
            collided_objects = [o for o in objects if o != self and o.collidable and self.colliderect(o)] #Exclude self and objects with no collision
            for collided_object in collided_objects:
                self.collide( collided_object )

    def update(self):
        pass

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        [child.sync_pos() for child in self.childs]

    def sync_pos(self):
        self.x = self.parent.x + self.dx
        self.y = self.parent.y + self.dy

    def move_to(self, x, y):
        self.x = x
        self.y = y

    def clamp(self):

        if (self.x < 0): self.x = 0
        if (self.x > self.bounds[0]): self.x = self.bounds[0]

        if (self.y < 0): self.y = 0
        if (self.y > self.bounds[1]): self.y = self.bounds[1]

    def add_child(self, obj):
        obj.set_parent(self)
        self.childs.append(obj)

    def set_parent(self, obj):
        self.parent = obj
        self.dx = self.x - obj.x
        self.dy = self.y - obj.y

    def damage(self, damage):
        self.health -= damage

    def collide(self, object):
        pass
        # print(f"{type(self).__name__} collided with", type(object).__name__)

    def kill(self):
        self.alive = False

class ProjectileImage(Enum):
    TYPE0 = 'projectile'
    TYPE1 = 'projectile_1'
    TYPE2 = 'projectile_2'
    TYPE3 = 'projectile_3'
    TYPE4 = 'projectile_4'
    TYPE5 = 'projectile_5'
    TYPE6 = 'projectile_bullet'
    TYPEBALL = 'projectile_ball'
 
asteroid_images = [
    'asteroid1',
    'asteroid2',
    'asteroid3',
    'asteroid4',
    'asteroid5',
    'asteroid6',
    'asteroid7'
]

class Background(Actor):

    def __init__(self, image):
        super().__init__(image)

# def global_pos(local_pos: tuple, reference_pos: tuple):
#     x = reference_pos[0] + local_pos[0]
#     y = reference_pos[1] + local_pos[1]
#     return (x,y)

# def local_pos(global_pos: tuple, reference_pos: tuple):
#     rx =  global_pos[0] - reference_pos[0]
#     ry =  global_pos[1] - reference_pos[1]
#     return (rx,ry)
    

