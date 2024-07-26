import pgzrun
import random
from pgzero.keyboard import keyboard
from pgzero.actor import Actor
from laboratory import *

WIDTH = 512
HEIGHT = 512

background = Actor('background')

character = random.choice(characters_pool)
# character = characters_pool[2]

def update():
    character.logic(keyboard)

def draw():
    background.draw()
    character.draw()

pgzrun.go()