import pgzrun
import random
from pgzero.keyboard import keyboard
from pgzero.actor import Actor
from laboratory import *

# The game window size
WIDTH = 1000
HEIGHT = 800

background = Actor('background2')

# character = random.choice(characters_pool)

# Use the below line to avoid a random character selection
character = characters_pool[0]

def update():
    character.update(keyboard)

def draw():

    background.draw()
    character.draw()

pgzrun.go()