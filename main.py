import pgzrun
import random
from laboratory import player, enemy, agent
from classes.asteroid import Asteroid
from classes.spaceship import Spaceship
from gui import Bar
from pygame import Color
from utils import Background, CollisionInformation
from globals import WIDTH, HEIGHT, ASTEROIDS_SPEED, ASTEROIDS_PER_SECOND, asteroid_images, Team, OBJECTS_LIMIT
from world import world

background = Background('background2')

enemybar = Bar((5, 5), (WIDTH - 10,10), Color(64, 0, 0), Color(50, 50, 50))
healthbar = Bar((5,HEIGHT - 20), (180,10), Color(128, 0, 0), Color(50, 50, 50))
abilitybar = Bar((5,HEIGHT - 35), (180,10), Color(0, 200, 0), Color(50, 50, 50))
cooldownbar = Bar((5,HEIGHT - 35), (180,10), Color(0, 150, 0), Color(50, 50, 50), reversed = True)

def update_enviroment():

    if random.random() < (ASTEROIDS_PER_SECOND/60):
        Asteroid(image = random.choice(asteroid_images), 
                            pos = (random.randint(-80,WIDTH), -30),
                            angle = random.randint(1,360),
                            speed=ASTEROIDS_SPEED,
                            team = Team.TEAM2
                           )

def update_objects():
    
    # print(len(world.objects))
    world.objects = world.objects[:OBJECTS_LIMIT]
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
            if obj == player:
                #GAME OVER
                print("GAME OVER")
            elif obj == enemy:
                #VICTORY
                print("YOU WON")
            world.remove_object(obj)
            del obj

def update_gui():

    enemybar.update(enemy.health, enemy.max_health)
    healthbar.update(player.health, player.max_health)
    if player.ability_timer > 0:
        abilitybar.update(player.ability_timer, player.ability_duration*60)
    if player.cooldown_timer > 0:
        cooldownbar.update(player.cooldown_timer, player.cooldown*60)

##### GAME LOOP #####
def update():

    agent.think([player])
    update_enviroment()
    update_objects()
    update_gui()

##### MAIN DRAW #####
def draw():
    background.draw()
    for obj in world.objects:
        obj.draw()

    enemybar.draw()
    healthbar.draw()
    cooldownbar.draw()
    if player.ability_timer > 0:
        abilitybar.draw()
    
pgzrun.go()