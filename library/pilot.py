import random

from pgzero.keyboard import keyboard

from library.globals import WIDTH, HEIGHT

class Pilot():

    def __init__(self, name, puppet = None):
        self.name = name
        self.puppet = puppet
        
        self.right = False
        self.left = False
        self.ability_key = False
        self.shooting_key = True

    def take_control(self, puppet):
        self.puppet = puppet
        puppet._control = self

    def think(self, surroundings):
        if surroundings[0]:
            player = surroundings[0] #0 index is the player

        if player.alive:
            if self.ability_key:
                self.ability_key = False

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
            self.ability_key = False
            self.shooting_key = False 

        if random.random() < 0.02:
            self.ability_key = True

class Player1():
     
    def __init__(self, name, puppet = None):
        self.name = name
        self.puppet = puppet

        self.right = False
        self.left = False
        self.ability_key = False
        self.shooting_key = True       

    def take_control(self, puppet):
        self.puppet = puppet
        puppet._control = self

    def read_keyboard(self):
        self.left = bool(keyboard.left)
        self.right = bool(keyboard.right)
        self.ability_key = bool(keyboard.lshift)
        self.shooting_key = bool(keyboard.space)

class Player2():
     
    def __init__(self, name, puppet = None):
        self.name = name
        self.puppet = puppet

        self.right = False
        self.left = False
        self.ability_key = False
        self.shooting_key = True       

    def take_control(self, puppet):
        self.puppet = puppet
        puppet._control = self

    def read_keyboard(self):
        self.left = bool(keyboard.kp4)
        self.right = bool(keyboard.kp6)
        self.ability_key = bool(keyboard.KP_ENTER)
        self.shooting_key = bool(keyboard.kp0)

