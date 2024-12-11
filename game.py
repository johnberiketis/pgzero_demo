import random
import sys

parent_module = sys.modules["__main__"]
sys.modules["__main__"] = sys.modules[__name__]
import pgzrun
from pgzero.keyboard import keyboard

from library.spaceship import Spaceship
from library.laboratory import enemy_blueprint, player_blueprint, enemy_blueprint2
from library.agent import Agent
from library.asteroid import generate_random_asteroid
from library.powerups import generate_random_powerup
from library.gui import Text, enemybar, healthbar, abilitybar, cooldownbar 
from library.utils import CollisionInformation, background, world
from library.globals import WIDTH, HEIGHT, FPS, ASTEROIDS_PER_SECOND, POWERUPS_PER_SECOND, OBJECTS_LIMIT, WIN_GRAPHIC, LOSE_GRAPHIC, TUTORIAL, TUTORIAL_MESSAGE

world.enemy = Spaceship(enemy_blueprint)
agent= Agent("Enemy1")
agent2= Agent("Enemy2")

agent.take_control(world.enemy)
agent2.take_control(Spaceship(enemy_blueprint2))
world.player = Spaceship(player_blueprint)

if TUTORIAL:
    Text(TUTORIAL_MESSAGE, (WIDTH-300, HEIGHT-110), frames_duration=1200, typing=True, fontsize=14, fontname='future_thin')

def update_enviroment():

    if random.random() < (ASTEROIDS_PER_SECOND/FPS):
        generate_random_asteroid()

    if random.random() < (POWERUPS_PER_SECOND/FPS):
        generate_random_powerup()

def update_objects():

    world.objects = world.objects[:OBJECTS_LIMIT]
    for obj in world.objects:
        
        if obj.collidable:
            collided_objects = [o for o in world.objects if o.team != obj.team and o.collidable and obj.colliderect(o)] #Exclude same team objects (self is same team) and objects with no collision
            for collided_object in collided_objects:  
                obj.collide( CollisionInformation(collided_object) )

    for obj in world.objects:
        obj.update() 

    for obj in world.objects:
        if obj.alive == False:
            if obj == world.player and world.end_game == 0:
                #LOSS
                world.end_game = -1
            elif obj == world.enemy and world.end_game == 0:
                #VICTORY
                world.end_game = 1
            world.remove_object(obj)

def update_gui():

    for gui in world.guis:
        gui.update()

def update_effects():

    for e in world.effects:
        e.update()

def draw_enviroment():

    background.draw()

def draw_objects():

    for obj in world.objects:
        obj.draw()

def draw_gui():

    for gui in world.guis:
        gui.draw()

def draw_effects():

    for e in world.effects:
        e.draw()

##### GAME LOOP #####
def update():

    if keyboard.escape:
        sys.exit(0)

    agent.think([world.player])
    agent2.think([world.player])

    update_enviroment()
    update_objects()
    update_gui()
    update_effects()

##### DRAW LOOP #####
def draw():

    draw_enviroment()
    draw_objects()
    draw_gui()
    draw_effects()

    if world.end_game == 1:
        WIN_GRAPHIC.draw()
    elif world.end_game == -1:
        LOSE_GRAPHIC.draw()

def play():

    # world.player = SpaceshipMod(
    #     image               = parent_module.image if hasattr(parent_module, "image") else 'spaceships/spaceship_orange1',
    #     health              = parent_module.health if hasattr(parent_module, "health") else 1,
    #     speed               = parent_module.speed if hasattr(parent_module, "speed") else 0,
    #     move_function       = parent_module.move if hasattr(parent_module, "move") else None,
    #     shoot_function      = parent_module.shoot if hasattr(parent_module, "shoot") else None,
    #     ability             = parent_module.ability if hasattr(parent_module, "ability") else None,
    #     ability_duration    = parent_module.ability_duration if hasattr(parent_module, "ability_duration") else 1,  
    #     cooldown            = parent_module.cooldown if hasattr(parent_module, "cooldown") else 10,
    #     weapon              = parent_module.weapon if hasattr(parent_module, "weapon") else None,
    # )

    enemybar.source = world.enemy
    enemybar.value_attr = "health"
    enemybar.max_value_attr = "max_health"

    healthbar.source = world.player
    healthbar.value_attr = "health"
    healthbar.max_value_attr = "max_health"

    abilitybar.source = world.player
    abilitybar.value_attr = "_ability_timer_frames"
    abilitybar.max_value_attr = "_ability_duration_frames"

    cooldownbar.source = world.player
    cooldownbar.value_attr = "_cooldown_timer_frames"
    cooldownbar.max_value_attr = "_cooldown_frames"

    pgzrun.go()
