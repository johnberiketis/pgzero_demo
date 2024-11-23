import pgzrun
import random
from laboratory import character, agent
from classes.asteroid import Asteroid
from classes.spaceship import Spaceship
from gui import Bar
from pygame import Color
import sys
from utils import Background, CollisionInformation
from globals import WIDTH, HEIGHT, ASTEROIDS_SPEED, ASTEROIDS_PER_SECOND, asteroid_images
from world import world

background = Background('background2')

healthbar = Bar((5,HEIGHT - 20), (180,10), Color(128, 0, 0), Color(50, 50, 50), 10)
abilitybar = Bar((5,HEIGHT - 35), (180,10), Color(0, 200, 0), Color(50, 50, 50), 10)
cooldownbar = Bar((5,HEIGHT - 35), (180,10), Color(0, 150, 0), Color(50, 50, 50), 10, reversed = True)

def update_enviroment():

    if random.random() < (ASTEROIDS_PER_SECOND/60):
        Asteroid(image = random.choice(asteroid_images), 
                            pos = (random.randint(-80,WIDTH), -30),
                            angle = random.randint(1,360),
                            speed=ASTEROIDS_SPEED
                           )

def update_objects():

    for obj in world.objects:
        
        #TODO collitions should be handled by event (enter, exit) 
        # and pass a "read only" or a Collition class object at the obj.collitions method
        # obj should only have a representaton of the collided object not the object itself
        if obj.collidable:
            collided_objects = [o for o in world.objects if o != obj and o.collidable and obj.colliderect(o)] #Exclude self and objects with no collision
            for collided_object in collided_objects:
                obj.collide( CollisionInformation(collided_object) )

    for obj in world.objects:
        obj.update()

    for obj in world.objects:
        if obj.alive == False:
            if obj == character:
                #GAME OVER
                print("GAME OVER")
                sys.exit(0)
            world.remove_object(obj)
            del obj

def update_gui():

    healthbar.update(character.health, character.max_health)
    if character.ability_timer > 0:
        abilitybar.update(character.ability_timer, character.ability_duration*60)
    if character.cooldown_timer > 0:
        cooldownbar.update(character.cooldown_timer, character.cooldown*60)

##### GAME LOOP #####
def update():

    agent.think(None)
    update_enviroment()
    update_objects()
    update_gui()

##### MAIN DRAW #####
def draw():
    background.draw()
    for obj in world.objects:
        obj.draw()

    healthbar.draw()
    cooldownbar.draw()
    if character.ability_timer > 0:
        abilitybar.draw()
    
pgzrun.go()