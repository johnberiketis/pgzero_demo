from pygame import draw, Surface, Rect, Color
from pgzero import game
from globals import WIDTH, HEIGHT

class Bar():

    def generate_surface(self, size: tuple, color_front: Color) -> Surface:
        surface = Surface(size=size)
        rect_front = Rect(0, 0, size[0], size[1])
        draw.rect(surface, color_front, rect_front, border_radius = 4)
        return surface

    def __init__(self, pos, size, color_front, color_back, max_value = 1, visible = True, reversed = False):
        self.visible = visible
        self.pos = pos
        self.size = size
        self.surface = self.generate_surface(size, color_front)
        self.color_front = Color(color_front)
        self.color_back = Color(color_back)
        self.value = max_value
        self.max_value = max_value
        self.reversed = reversed

    def update_surface(self) -> Surface:
        if self.reversed:
            width_front = (1 - (self.value/self.max_value))*self.size[0]
        else:
            width_front = (self.value/self.max_value)*self.size[0]
        rect_back= Rect(0, 0, self.size[0], self.size[1])
        rect_front = Rect(0, 0, width_front, self.size[1])
        draw.rect(self.surface, self.color_back, rect_back, border_radius = 4)
        draw.rect(self.surface, self.color_front, rect_front, border_radius = 4)

    def update(self, value = None, max_value = None):
        if value:
            self.value = value
        if max_value:
            self.max_value = max_value
        self.update_surface()

    def draw(self):
        if self.visible:
            game.screen.blit(self.surface, self.pos)
    
enemybar        = Bar((5, 5),           (WIDTH - 10,10),    (64, 0, 0),     (50, 50, 50))
healthbar       = Bar((5,HEIGHT - 20),  (180,10),           (128, 0, 0),    (50, 50, 50))
abilitybar      = Bar((5,HEIGHT - 35),  (180,10),           (0, 200, 0),    (50, 50, 50))
cooldownbar     = Bar((5,HEIGHT - 35),  (180,10),           (0, 150, 0),    (50, 50, 50), reversed = True)