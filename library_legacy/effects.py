import math

from pgzero.actor import Actor

from library.utils import world
from library.globals import EXPLOSION_FRAMES, FPS

class Effect(Actor):

    def __init__(self, pos, frames_duration = FPS, frames = None, speed=0, direction=0):
        self._frames_counter = 0
        self._index_counter = 1
        self._end_frame = frames_duration - 1
        self.speed = speed
        self.direction = direction
        self.frames = frames
        self.current_frame = frames[0]
        if len(frames) > 1:
            self.next_frame = frames[1]
        else:
            self.next_frame = None
        super().__init__("effects/explosion1",  pos)
        world.add_effect(self)

    @property
    def direction(self):
        return self._direction
    
    @direction.setter
    def direction(self, value):
        self._direction = value - 90
    
    def next_pos(self):
        x = self.x + self.speed*math.cos(math.radians(self.direction))
        y = self.y + self.speed*math.sin(math.radians(self.direction))
        return (x, y)
    
    def move_to(self, x, y):
        self.x = x
        self.y = y

    def update(self):
        
        self.move_to(*self.next_pos())
        if self._frames_counter == self._end_frame:
            world.remove_effect(self)
        elif self.next_frame:
            if self._frames_counter == self.next_frame["frame_number"]:
                self._index_counter += 1
                self.current_frame = self.next_frame

                self._orig_surf = self._surf = self.current_frame["image"]
                self._update_pos()

                if self._index_counter < len(self.frames):
                    self.next_frame = self.frames[self._index_counter]
                else:
                    self.next_frame = None

        self._frames_counter += 1

def explosion(pos):
    duration = 15

    Effect(frames=EXPLOSION_FRAMES, pos=pos, frames_duration=duration)