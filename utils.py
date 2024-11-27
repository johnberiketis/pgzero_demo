from pgzero.clock import clock
from pgzero.actor import Actor
from globals import WIDTH, HEIGHT, Team, Type
   
class Object(Actor):
        
    def __init__(self, image, pos, speed = 0, health = 1, direction = 0, timespan = -1, spin = 0, angle = 0, bounds = (WIDTH, HEIGHT), alive = True, collidable = True, source = None, team = Team.NEUTRAL):
        super().__init__(image, pos)
        self.speed = speed
        self.health = health
        self.max_health = health
        self.direction = direction
        self.timespan = timespan
        self.bounds = bounds
        self.alive = alive
        self._collidable = collidable
        self.spin = spin
        self.team = team
        self.source = source
        self.parent = None
        self.childs = []
        world.add_object(self)
        if direction == 1:
            self.angle = 180
        else:
            self.angle = 0
        
        if self.timespan > 0:
            clock.schedule_unique(self.kill, self.timespan)

    @property
    def collidable(self):
        return self._collidable

    @collidable.setter
    def collidable(self, value: bool):
        self._collidable = value

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

class Background(Actor):

    def __init__(self, image):
        super().__init__(image)

class World():

    def __init__(self):
        self.objects = []
        self.end_game = 0 

    def add_object(self, object):
        self.objects.append(object)

    def remove_object(self, object):
        self.objects.remove(object)
        del object

    def extend_objects(self, object_list):
        self.objects.extend(object_list)

class CollisionInformation():

    def __init__(self, object):
        self.type = Type[object.__class__.__name__.upper()]
        self.team = object.team if object.team else Team.NEUTRAL
        self.damage = object.damage if object.damage else 0
        
background = Background('background2')
world = World()


