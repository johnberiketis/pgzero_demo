import pgzrun
import random
from laboratory import player, enemy, agent
from classes.asteroid import generate_random_asteroid
from gui import enemybar, healthbar, abilitybar, cooldownbar 
from utils import CollisionInformation
from globals import WIDTH, HEIGHT, ASTEROIDS_PER_SECOND, OBJECTS_LIMIT, WIN_GRAPHIC, LOSE_GRAPHIC
from utils import background, world

def update_enviroment():

    if random.random() < (ASTEROIDS_PER_SECOND/60):
        generate_random_asteroid()

def update_objects():

    world.objects = world.objects[:OBJECTS_LIMIT]
    for obj in world.objects:
        
        #TODO collitions should be handled by event (enter, exit) 
        if obj.collidable:
            collided_objects = [o for o in world.objects if o != obj and o.collidable and obj.colliderect(o)] #Exclude self and objects with no collision
            for collided_object in collided_objects:
                obj.collide( CollisionInformation(collided_object) )

    for obj in world.objects:
        obj.update()

    for obj in world.objects:
        if obj.alive == False:
            if obj == player:
                #LOSS
                world.end_game = -1
                enemy.collidable = False
            elif obj == enemy:
                #VICTORY
                world.end_game = 1
                player.collidable = False
            world.remove_object(obj)
            del obj

def update_gui():

    enemybar.update(enemy.health, enemy.max_health)
    healthbar.update(player.health, player.max_health)
    if player.ability_timer > 0:
        abilitybar.update(player.ability_timer, player.ability_duration*60)
    if player.cooldown_timer > 0:
        cooldownbar.update(player.cooldown_timer, player.cooldown*60)

def draw_enviroment():

    background.draw()

def draw_objects():

    for obj in world.objects:
        obj.draw()

def draw_gui():

    enemybar.draw()
    healthbar.draw()
    cooldownbar.draw()
    if player.ability_timer > 0:
        abilitybar.draw()
    
##### GAME LOOP #####
def update():

    agent.think([player])

    update_enviroment()
    update_objects()
    update_gui()

##### DRAW LOOP #####
def draw():

    draw_enviroment()
    draw_objects()
    draw_gui()

    if world.end_game == 1:
        WIN_GRAPHIC.draw()
    elif world.end_game == -1:
        LOSE_GRAPHIC.draw()
    
pgzrun.go()