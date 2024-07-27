from pgzero.actor import Actor
from pgzero.clock import clock
from pgzero.keyboard import keyboard
from classes import Projectile

class CustomActor(Actor):

    def __init__(self, image, pos=(500, 750), health = 100, speed = 5, ability = None, dummy = False, bounds = (1000, 800), **kwargs):
        super().__init__(image, pos)
        # Initialize additional variables
        self.health = health
        self.speed = speed
        self.ability = ability
        self.bounds = bounds
        self.alive = True
        self.firerate = 3 #shots per second
        self.gun_ready = True

        # Every action point can activate one ability
        self.actions = 1

        # After an ability there is a cooldown that will reset the action points
        self.cooldown = 8

        # The self.default is the original object without any effects applied 
        # This object is used to reset the state of the character
        # The dummy parameter is used to avoid exceeding recursion depth
        if not dummy:
            self.default = CustomActor(image, pos, health, speed, ability, dummy = True)
        else:
            self.default = None

    def reset(self):
        # Reset the character to its original state
        self.speed = self.default.speed
        self.cooldown = self.default.cooldown
        self.image = self.default.image
        self.y = self.default.y
        self._surf = self.default._surf
        self.firerate = self.default.firerate

    def reset_actions(self):
        # Reset the character's action points
        self.actions = self.default.actions

    def update(self):
        if keyboard.left:
            self.x -= self.speed
            if (self.x < 0): self.x = 0
        elif keyboard.right:
            self.x += self.speed
            if (self.x > self.bounds[0]): self.x = self.bounds[0]

        # If space key is pressed and you have at least 1 action available
        # then activate the characters ability 
        if keyboard.lshift and self.actions == 1:
            duration = self.ability(self)
            self.actions = 0
            if not duration:
                duration = 1
            #After the duration reset the ability's effects
            clock.schedule_unique(self.reset, duration)
            #After the cooldown reset the action points
            clock.schedule_unique(self.reset_actions, self.cooldown)

        if keyboard.space:
            if self.gun_ready:
                return self.shoot()

    def kill(self):
        self.alive = False

    def shoot(self):
        projectile = Projectile('projectile', self.pos)
        self.gun_ready = False
        clock.schedule_unique(self.reload, 1/self.firerate)
        return projectile

    def reload(self):
        self.gun_ready = True
    
