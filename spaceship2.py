# import pgzrun
from pgzero.actor import Actor
import pygame

class CustomActor(Actor):
    RESIZE_WIDTH = 50
    RESIZE_HEIGHT = 100
    def __init__(self, image='spaceship2', pos=(456, 760), **kwargs):
        super().__init__(image, pos)
        self.original_image = self._surf  # Store the original image for future resizing
        self.resize_image(self.RESIZE_WIDTH, self.RESIZE_HEIGHT)          
        # Initialize additional variables
        # self.health = kwargs.get('health', 100)
        # self.speed = kwargs.get('speed', 5)
        # self.score = kwargs.get('score', 0)    
    def logic(self, keyboard, SPEED):
        if keyboard.left:
            self.x -= SPEED
            if (self.x < 0): self.x = 0
        elif keyboard.right:
            self.x += SPEED
            if (self.x > 512): self.x = 512
    def resize_image(self, width, height):
        self._surf = pygame.transform.scale(self.original_image, (width, height))
        self.width, self.height = self._surf.get_size()



