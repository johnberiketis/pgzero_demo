import math

from pgzero.actor import Actor
from pgzero import game, ptext, game

from library.utils import world, clamp_value
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
        super().__init__("effects/explosion1",  pos) #TODO change the default value
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

class Text():

    def __init__(self, text, pos, frames_duration = FPS, fontname='future', fontsize = 32, speed=0, direction=0, color = (255,255,255), alpha = 1.0, fade = False, typing= False):
        self._frames_counter = 0
        self._end_frame = frames_duration - 1
        self.pos = pos
        self.fontname = fontname
        self.speed = speed
        self.direction = direction
        self.content = text
        self._initial_content = text
        self.fontsize = fontsize
        self.color = color
        self.alpha = alpha
        self.fade = fade
        self.typing = typing
        self._fade_step = alpha/frames_duration
        self._typing_letter_frames = 4
        world.add_effect(self)

    @property
    def pos(self):
        return (self.x, self.y)
    
    @pos.setter
    def pos(self, pos: tuple):
        self.x = pos[0]
        self.y = pos[1]

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
        if self.fade:
            self.alpha = self.alpha - self._fade_step
        if self.typing:
            text_length = self._frames_counter//self._typing_letter_frames
            text_length = clamp_value(text_length, 0, len(self._initial_content))
            self.content = self._initial_content[0:text_length]
        self._frames_counter += 1

    def draw(self):
        ptext.draw( surf=game.screen, text=self.content, pos=self.pos, fontname=self.fontname, fontsize=self.fontsize, color=self.color, alpha = self.alpha)

def explosion(pos):
    duration = 15

    Effect(frames=EXPLOSION_FRAMES, pos=pos, frames_duration=duration)