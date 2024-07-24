import pgzrun
import spaceship, spaceship2
import random

WIDTH = 512
HEIGHT = 512

SPEED = 5

background = Actor('background')

characters_pool = [spaceship.CustomActor(), spaceship2.CustomActor()]

character = random.choice(characters_pool)

def update():
    character.logic(keyboard, SPEED)

def draw():
    background.draw()
    character.draw()

pgzrun.go()