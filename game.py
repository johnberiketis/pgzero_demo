import random
import sys
import inspect

parent_module = sys.modules["__main__"]
parent_source = inspect.getsource(parent_module)
sys.modules["__main__"] = sys.modules[__name__]
import pgzrun
from pgzero.keyboard import keyboard
from pgzero.clock import clock

from library.laboratory import pilots, player2
from library.spaceship import Spaceship, default_update
from library.asteroid import generate_random_asteroid
from library.powerups import generate_random_powerup
from library.gui import Text, Bar
from library.utils import CollisionInformation, background, world
from library.pilot import Player1
# from library.inspector import run_inspection, run_source_code_inspection
from library.globals import Team, WIDTH, HEIGHT, FPS, ASTEROIDS_PER_SECOND, POWERUPS_PER_SECOND, OBJECTS_LIMIT, WIN_GRAPHIC, LOSE_GRAPHIC, TUTORIAL, USE_INSPECTOR

player1 = Player1("Player1")

if TUTORIAL:
    from library.globals import TUTORIAL_MESSAGE, TUTORIAL_MESSAGE_P2
    Text(TUTORIAL_MESSAGE, (10, HEIGHT-150), frames_duration=1200, typing=True, fontsize=14, fontname='future_thin')
    if player2:
        Text(TUTORIAL_MESSAGE_P2, (WIDTH-300, HEIGHT-160), frames_duration=1200, typing=True, fontsize=14, fontname='future_thin')

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
            if (obj == world.player1 or obj == world.player2) and world.end_game == 0:
                #LOSS
                world.end_game = -1
            if sum([e.health for e in world.enemy_spaceships]) <= 0 and world.end_game == 0:
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

    for pilot in pilots:
        pilot.think([world.player1])

    player1.read_keyboard()
    if player2:
        player2.read_keyboard() 

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
    if hasattr(parent_module, "spaceship"):
        player1spaceship = parent_module.spaceship
        if hasattr(parent_module, "update"):
            player1spaceship._update_function = parent_module.update
        else:
            player1spaceship._update_function = default_update
    else:
        player1spaceship = Spaceship(
            image               = parent_module.image if hasattr(parent_module, "image") else 'spaceships/spaceship_orange1',
            health              = parent_module.health if hasattr(parent_module, "health") else 1,
            speed               = parent_module.speed if hasattr(parent_module, "speed") else 0,
            update_function     = parent_module.update if hasattr(parent_module, "update") else lambda a:a,  
            ability_function    = parent_module.ability if hasattr(parent_module, "ability") else None,
            ability_duration    = parent_module.ability_duration if hasattr(parent_module, "ability_duration") else 1,  
            cooldown_duration   = parent_module.cooldown if hasattr(parent_module, "cooldown") else 10,
            weapon              = parent_module.weapon if hasattr(parent_module, "weapon") else None,
            team                = Team.PLAYER
        )

    world.player1 = player1spaceship

    player1.take_control(world.player1)

    if hasattr(parent_module, "enemy"):
        enemy_spaceship = parent_module.enemy
        world.objects.remove(world.enemy_spaceships[0])
        world.enemy_spaceships[0] = enemy_spaceship
        pilots[0].take_control(enemy_spaceship)

    #Enemy UI bars init
    for e in world.enemy_spaceships:
        Bar((0, -50), (180,10), (93, 152, 37), (50, 50, 50), source = e, attached = True, value_attr = "health", max_value_attr = "max_health")
        Bar((0, -35), (180,10), (200, 178, 52), (50, 50, 50), source = e, attached = True, value_attr = "_ability_timer_frames", max_value_attr = "_ability_duration_frames")

    #Player 1 UI bars init
    Bar((5,HEIGHT - 20),  (180,10),  (113, 172, 57), (50, 50, 50), source=world.player1, value_attr = "health", max_value_attr = "max_health")
    Bar((5,HEIGHT - 35),  (180,10),  (99, 88, 26),   (50, 50, 50), reversed = True, source=world.player1, value_attr = "_cooldown_timer_frames", max_value_attr = "_cooldown_frames")
    Bar((5,HEIGHT - 35),  (180,10),  (200, 178, 52), (50, 50, 50), source = world.player1, value_attr = "_ability_timer_frames", max_value_attr = "_ability_duration_frames")

    #Player 2 UI bars init
    if player2:
        Bar((WIDTH-185, HEIGHT - 20),  (180,10),  (113, 172, 57), (50, 50, 50), source=world.player2, value_attr = "health", max_value_attr = "max_health")
        Bar((WIDTH-185, HEIGHT - 35),  (180,10),  (99, 88, 26),   (50, 50, 50), reversed = True, source=world.player2, value_attr = "_cooldown_timer_frames", max_value_attr = "_cooldown_frames")
        Bar((WIDTH-185, HEIGHT - 35),  (180,10),  (200, 178, 52), (50, 50, 50), source = world.player2, value_attr = "_ability_timer_frames", max_value_attr = "_ability_duration_frames")

    #Run inspection
    # if USE_INSPECTOR:
    #     illegal_code = run_source_code_inspection(str(parent_source))
    #     inspection_message = ""
    #     if len(illegal_code) > 0:
    #         illegal_code = [f"\"{code}\"" for code in illegal_code]
    #         inspection_message = "Illegal source code: " + str.join(', ', illegal_code)
    #     inspection_message += run_inspection(player1spaceship_blueprint)
    #     if len(inspection_message)>0:
    #         print(inspection_message)
    #         world.objects = []
    #         world.guis = []
    #         Text("WARNING:\n" + inspection_message, (50, HEIGHT//2 - 100), 1200, fontsize=30, color=(200, 50, 50))
    #         clock.schedule_unique(sys.exit, 20)
        
    pgzrun.go()
