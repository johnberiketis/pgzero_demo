import env_setup
import pgzrun
import random
from pgzero.keyboard import keyboard
from pgzero.actor import Actor
from laboratory import *

# The game window size
WIDTH = 1000
HEIGHT = 800

objects = []

background = Actor('background2')

# character = random.choice(characters_pool)

# Use the below line to avoid a random character selection
character = characters_pool[3]

objects.append(character)

def update():
    for obj in objects:
        if obj.alive == False:
            objects.remove(obj)
        new_object = obj.update()
        if new_object:
            objects.append(new_object)

def draw():
    background.draw()
    for obj in objects:
        obj.draw()

pgzrun.go()