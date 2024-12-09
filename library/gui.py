import math

from pygame import draw, Surface, Rect, Color
from pgzero import game, ptext

from library.globals import WIDTH, HEIGHT, FPS
from library.utils import world, clamp_value

class Bar():

    def generate_surface(self, size: tuple, color_front: Color) -> Surface:
        surface = Surface(size=size)
        rect_front = Rect(0, 0, size[0], size[1])
        draw.rect(surface, color_front, rect_front, border_radius = 4)
        return surface

    def __init__(self, pos, size, color_front, color_back, max_value = 1, visible = True, reversed = False, source = None, attached = False, value_attr = None, max_value_attr = None):
        self.visible = visible
        self.pos = pos
        self.size = size
        self.surface = self.generate_surface(size, color_front)
        self.color_front = Color(color_front)
        self.color_back = Color(color_back)
        self._value = 1
        self._max_value = 1
        self.value = max_value
        self.max_value = max_value
        self.source = source
        self.value_attr: str = value_attr
        self.max_value_attr: str = max_value_attr
        self.attached = attached
        self.reversed = reversed
        world.add_gui(self)

    def update_surface(self) -> Surface:
        self.surface = Surface(self.size)
        if self.reversed:
            width_front = (1 - (self._percentage))*self.size[0]
        else:
            width_front = (self._percentage)*self.size[0]
        rect_back= Rect(0, 0, self.size[0], self.size[1])
        rect_front = Rect(0, 0, width_front, self.size[1])
        draw.rect(self.surface, self.color_back, rect_back, border_radius = 4)
        draw.rect(self.surface, self.color_front, rect_front, border_radius = 4)

    def update(self, value = None, max_value = None):
        if self._percentage > 0:
            self.visible = True
        else:
            self.visible = False

        if self.source:
            self.value = getattr(self.source, self.value_attr)
            self.max_value = getattr(self.source, self.max_value_attr)
        elif value or max_value:
            if value:
                self.value = value
            if max_value:
                self.max_value = max_value

        if self.attached and self.source:
            self.pos = ((self.source.pos[0] - self.size[0]//2), (self.source.pos[1] - self.size[1]//2))
         
        self.update_surface()

    def draw(self):
        if self.visible:
            game.screen.blit(self.surface, self.pos)

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, val):
        self._value = val
        if self._max_value == 0:
            self._percentage = 0
        else:
            self._percentage = self._value/self._max_value

    @property
    def max_value(self):
        return self._max_value
    
    @max_value.setter
    def max_value(self, val):
        self._max_value = val
        if self._max_value == 0:
            self._percentage = 0
        else:
            self._percentage = self._value/self._max_value

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
        world.add_gui(self)

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
            world.remove_gui(self)
        if self.fade:
            self.alpha = self.alpha - self._fade_step
        if self.typing:
            text_length = self._frames_counter//self._typing_letter_frames
            text_length = clamp_value(text_length, 0, len(self._initial_content))
            self.content = self._initial_content[0:text_length]
        self._frames_counter += 1

    def draw(self):
        ptext.draw( surf=game.screen, text=self.content, pos=self.pos, fontname=self.fontname, fontsize=self.fontsize, color=self.color, alpha = self.alpha)
    
enemybar        = Bar((5, 5),           (WIDTH - 10,10),    (93, 152, 37),  (50, 50, 50))
healthbar       = Bar((5,HEIGHT - 20),  (180,10),           (113, 172, 57), (50, 50, 50))
cooldownbar     = Bar((5,HEIGHT - 35),  (180,10),           (99, 88, 26),   (50, 50, 50), reversed = True)
abilitybar      = Bar((5,HEIGHT - 35),  (180,10),           (200, 178, 52), (50, 50, 50))