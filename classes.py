from pgzero.actor import Actor
from pgzero.clock import clock

class Projectile(Actor):

    def __init__(self, image, pos, speed = 8, direction = -1, timespan = 10, bounds = (1000, 800)):
        super().__init__(image, pos)
        self.speed = speed
        self.direction = direction
        self.timespan = timespan
        self.bounds = bounds
        self.alive = True
        clock.schedule_unique(self.kill, self.timespan)

    def update(self):
        self.y += self.speed*self.direction
        if self.y <= 0 or self.y >= self.bounds[1]:
            self.kill()

    def kill(self):
        self.alive = False