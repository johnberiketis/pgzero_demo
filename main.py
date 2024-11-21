import pgzrun
import random
from laboratory import character
from classes.asteroid import Asteroid
from classes.reflector import Reflector
from gui import Bar
from pygame import Color
import sys
from utils import asteroid_images, Background
from globals import *

background = Background('background2')

objects = [character]
healthbar = Bar((5,HEIGHT - 20), (180,10), Color(128, 0, 0), Color(50, 50, 50), 10)
abilitybar = Bar((5,HEIGHT - 35), (180,10), Color(0, 200, 0), Color(50, 50, 50), 10)
cooldownbar = Bar((5,HEIGHT - 35), (180,10), Color(0, 150, 0), Color(50, 50, 50), 10, reversed = True)

def update_enviroment():

    if random.randint(0, 100) < (ASTEROIDS_PER_SECOND/60)*100:
        asteroid = Asteroid(image = random.choice(asteroid_images), 
                            pos = (random.randint(-80,WIDTH), -30),
                            angle = random.randint(1,360),
                            speed=ASTEROIDS_SPEED
                           )
        
        objects.append(asteroid)

def update_objects():

    new_objects = []

    for obj in objects:
        
        obj.handle_collitions(objects)

        created_objects = obj.update()
        if created_objects:
            new_objects.extend(created_objects)

    for obj in objects:
        if obj.alive == False:
            if obj == character:
                #GAME OVER
                print("GAME OVER")
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