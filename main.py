import pgzrun
import random
from laboratory import character
from classes import Asteroid, Background
from gui import Bar
from pygame import Color
import sys

# The game window size
WIDTH = 1000
HEIGHT = 800
background = Background('background2')

objects = [character]
healthbar = Bar((5,HEIGHT - 20), (180,10), Color(128, 0, 0), Color(50, 50, 50), 10)
abilitybar = Bar((5,HEIGHT - 35), (180,10), Color(0, 200, 0), Color(50, 50, 50), 10)
cooldownbar = Bar((5,HEIGHT - 35), (180,10), Color(0, 150, 0), Color(50, 50, 50), 10, reversed = True)
    
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

    new_objects = []

    for obj in objects:
        
        if obj.collidable:
            filtered_objects_list = [o for o in objects if o != obj and o.collidable] #Exclude self and objects with no collision
            coll_index = obj.collidelist(filtered_objects_list)
            if coll_index >= 0:
                obj.collide( filtered_objects_list[coll_index] )

        created_objects = obj.update()
        if created_objects:
            new_objects.extend(created_objects)

    for obj in objects:
        if obj.alive == False:
            if obj == character:
                #GAME OVER
                sys.exit(0)
            objects.remove(obj)
            del obj

    objects.extend(new_objects)

def update_gui():

    healthbar.update(character.health, character.max_health)
    if character.ability_timer > 0:
        abilitybar.update(character.ability_timer, character.ability_duration*60)
    if character.cooldown_timer > 0:
        cooldownbar.update(character.cooldown_timer, character.cooldown*60)

##### GAME LOOP #####
def update():

    update_enviroment()
    update_objects()
    update_gui()

##### MAIN DRAW #####
def draw():
    background.draw()
    for obj in objects:
        obj.draw()

    healthbar.draw()
    cooldownbar.draw()
    if character.ability_timer > 0:
        abilitybar.draw()
    
pgzrun.go()