from pgzero.actor import Actor
from pgzero.clock import clock

class CustomActor(Actor):

    def __init__(self, image, pos=(256, 460), health = 100, speed = 5, ability = None, dummy = False, **kwargs):
        super().__init__(image, pos)
        # Initialize additional variables
        self.health = health
        self.speed = speed
        self.ability = ability

        self.actions = 1
        self.cooldown = 8

        if not dummy:
            self.default = CustomActor(image, pos, health, speed, ability, dummy = True)
        else:
            self.default = None

    def reset(self):
        self.speed = self.default.speed
        self.cooldown = self.default.cooldown
        self.image = self.default.image
        self.y = self.default.y
        self._surf = self.default._surf

    def reset_actions(self):
        self.actions = self.default.actions

    def logic(self, keyboard):
        if keyboard.left:
            self.x -= self.speed
            if (self.x < 0): self.x = 0
        elif keyboard.right:
            self.x += self.speed
            if (self.x > 512): self.x = 512

        if keyboard.space and self.actions == 1:
            duration = self.ability(self)
            self.actions = 0
            if not duration:
                duration = 1
            clock.schedule_unique(self.reset, duration)
            clock.schedule_unique(self.reset_actions, self.cooldown)

    
