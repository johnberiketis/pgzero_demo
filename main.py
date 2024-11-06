import pgzrun
import random
from pgzero.actor import Actor
from laboratory import *
from classes import Asteroid, Background
from copy import deepcopy

# The game window size
WIDTH = 1000
HEIGHT = 800
background = Background('background2')

objects = [character]
    
def update_enviroment():

    asteroid_images = ['asteroid1',
                       'asteroid2',
                       'asteroid3',
                       'asteroid4',
                       'asteroid5',
                       'asteroid6',
                       'asteroid7']

    if random.randint(0, 150)  == 1:
        asteroid = Asteroid(image = random.choice(asteroid_images), 
                            pos = (random.randint(-80,WIDTH), 0), 
                            speed = 3,
                            health = 4, 
                            direction = 1, 
                            timespan = 30, 
                            spin = random.randint(-20,20)/100, 
                            rotation = random.randint(1,360)
                           )
        
        objects.append(asteroid)

def update_objects():

    for obj in objects:

        coll_index = obj.collidelist(objects)
        if coll_index >= 0 and objects[coll_index] is not obj:
            obj.collide( objects[coll_index] )

        new_objects = obj.update()

        if new_objects:
            objects.extend(new_objects)

        if obj.alive == False:
            objects.remove(obj)

def update():

    update_enviroment()
    update_objects()

def draw():
    background.draw()
    for obj in objects:
        obj.draw()

pgzrun.go()