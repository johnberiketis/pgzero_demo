import random

from library.globals import WIDTH, HEIGHT

class Agent():

    def __init__(self, name, puppet = None):
        self.name = name
        self.puppet = puppet
        
        self.right = False
        self.left = False
        self.lshift = False
        self.space = True

    def take_control(self, puppet):
        self.puppet = puppet
        puppet.control = self

    def think(self, surroundings):
        if surroundings[0]:
            player = surroundings[0] #0 index is the player

        if player.alive:
            if self.lshift:
                self.lshift = False

            if random.random() < 0.02:
                self.left = not self.left
                self.right = not self.right

            if self.puppet:
                if self.puppet.x <= 10:
                    self.left = False
                    self.right = True
                elif self.puppet.x >= WIDTH-10:
                    self.left = True
                    self.right = False
        else:
            self.right = False
            self.left = False
            self.lshift = False
            self.space = False 

        if random.random() < 0.02:
            self.lshift = True