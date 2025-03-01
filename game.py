import random
import sys
import inspect
# parent_module = sys.modules["__main__"]
# parent_source = inspect.getsource(parent_module)
# sys.modules["__main__"] = sys.modules[__name__]
import pgzrun
from pgzero.keyboard import keyboard
from pgzero.clock import clock
# from library.game_setup_default import enemies, pilots, player1, player2
from library.spaceship import Spaceship, default_update
from library.asteroid import generate_random_asteroid
from library.powerups import generate_random_powerup
from library.gui import Text, Bar
from library.utils import CollisionInformation
from library.globals import Team, WIDTH, HEIGHT, FPS, ASTEROIDS_PER_SECOND, POWERUPS_PER_SECOND, OBJECTS_LIMIT, WIN_GRAPHIC, LOSE_GRAPHIC, TUTORIAL, USE_INSPECTOR
from library.utils import Background, World
from library.spaceship import Spaceship, default_update
from library.projectile import Projectile
from library.pilot import Pilot, Player1, Player2
from library.utils import Team
from library.globals import IMAGES_SPACESHIPS, NUMBER_OF_PLAYERS, NUMBER_OF_ENEMIES
from library.weapon import Weapon

background = Background('others/background')
world = World()

######################################
######### ABILITIES LAB ##############
######################################

def super_speed(spaceship : Spaceship):
    ''' Super speed!!! '''
    spaceship.speed = 13

def invisibility(spaceship : Spaceship):
    '''Invisibility!!!'''
    spaceship.collidable = False

def too_many_guns(spaceship : Spaceship):
    '''Quad fire!!!'''
    spaceship.weapon.barrels = 4

def machine_gun(spaceship: Spaceship):
    '''Fire barraze!!!'''
    spaceship.weapon.firerate = spaceship.weapon.firerate + 5

def reflection(spaceship: Spaceship):
    '''Reflector deployed!!!'''
    spaceship.deploy_reflector()

def buff_up(spaceship: Spaceship):
    '''Damage bonus!!!'''
    spaceship.weapon.damage = spaceship.weapon.damage + 2/spaceship.weapon.barrels

def hypervelocity(spaceship: Spaceship):
    '''Bullets super speed!!!'''
    spaceship.weapon.speed = 20

def fanfire(spaceship: Spaceship):
    '''Mines deployed!!!'''
    n = 10
    spread = 100
    for i in range(0,n+1):
        Projectile(image = 'others/bomb', pos = spaceship.pos, speed=2, damage = 12, health = 12, source=spaceship, team=spaceship.team, direction= -spread/2 + (i*spread/n) )

abilities = [
    super_speed,
    invisibility,
    too_many_guns,
    machine_gun,
    reflection,
    buff_up,
    hypervelocity,
    fanfire
    ]

######################################
############ WEAPON LAB ##############
######################################

# weapon points = (damage * barrels * firerate) + speed
cannon      = Weapon(firerate = 2, barrels = 1, damage = 8, speed = 6)  # 22
super_auto  = Weapon(firerate = 8, barrels = 1, damage = 1.5, speed = 13) # 25
automatic   = Weapon(firerate = 4, barrels = 1, damage = 4, speed = 12) # 28
dual        = Weapon(firerate = 2, barrels = 2, damage = 3, speed = 9)  # 21
dual_plasma = Weapon(firerate = 1, barrels = 2, damage = 5, speed = 8)  # 18

gatling_gun = Weapon(firerate = 12, barrels = 1, damage = 1, speed = 18, randomness=3 )
trident     = Weapon(firerate = 2, barrels = 3, damage = 2, speed = 9,  spread_angle=45)
shotgun     = Weapon(firerate = 1, barrels = 4, damage = 4, speed = 25, spread_angle=5, randomness=2 )

#Weapon for fun
malfunction = Weapon(firerate = 12, barrels = 1, damage = 5, speed = 18, randomness=45 )
default = Weapon(firerate = 1, barrels = 1, damage = 1, speed = 6)

weapons = [
    cannon,
    super_auto,
    automatic,
    dual,
    dual_plasma,
    gatling_gun,
    trident,
    shotgun
]

######################################
######### CHARACTERS LAB #############
######################################


############# ENEMIES ################
# enemy_blueprints = []
enemies = []
pilots = []  
for e in range(0,NUMBER_OF_ENEMIES):
    enemies.append( Spaceship(image = random.choice(IMAGES_SPACESHIPS), 
                                                health = 50, 
                                                speed = 4, 
                                                ability_function = random.choice(abilities),
                                                ability_duration = 6, 
                                                cooldown_duration = 6, 
                                                weapon = random.choice(weapons), 
                                                team=Team.ENEMY) )

  
for enemy in enemies:
    pilot = Pilot("Enemy")
    # enemy_spaceship = Spaceship( spaceship_b )
    pilot.take_control( enemy )
    # enemies.append( enemy_spaceship )
    pilots.append( pilot )
    world.add_object(enemy)

############# FRIENDS ################
# friends_blueprints = []
# friends = []
# f_agents = []  
# for f in range(0,2):
#     friends_blueprints.append( SpaceshipBlueprint(image = random.choice(IMAGES_SPACESHIPS), 
#                                                 health = 200, 
#                                                 speed = 4, 
#                                                 ability_function = random.choice(abilities), 
#                                                 ability_duration = 6, 
#                                                 cooldown_duration = 8, 
#                                                 weapon = random.choice(weapons), 
#                                                 team=Team.PLAYER) )

  
# for f_spaceship_b in friends_blueprints:
#     f_agent = Pilot("Enemy")
#     f_spaceship = Spaceship( f_spaceship_b )
#     f_agent.take_control( f_spaceship )
#     friends.append( f_spaceship )
#     f_agents.append( f_agent )

# ############# PLAYERS ################
# player1 = Spaceship(image = random.choice(IMAGES_SPACESHIPS), 
#                                       health = 500, 
#                                       speed = random.choice([7,8,9]), 
#                                       ability_function = random.choice(abilities), 
#                                       ability_duration = 10, 
#                                       cooldown_duration = 2, 
#                                       weapon = random.choice(weapons),
#                                       team=Team.PLAYER)

# player1 = Player1("Player1")

# player2 = None
# # world.player2 = None
# if NUMBER_OF_PLAYERS == 2:
#     player2 = Spaceship(image = random.choice(IMAGES_SPACESHIPS), 
#                                         health = 500, 
#                                         speed = random.choice([7,8,9]), 
#                                         ability_function = random.choice(abilities),
#                                         ability_duration = 10, 
#                                         cooldown_duration = 2,
#                                         update_function = default_update, 
#                                         weapon = random.choice(weapons),
#                                         team = Team.PLAYER)

#     player2 = Player2("Player2")
#     # world.player2 = Spaceship(player2)
#     # player2.take_control( world.player2 )




# if TUTORIAL:
#     from library.globals import TUTORIAL_MESSAGE, TUTORIAL_MESSAGE_P2
#     Text(TUTORIAL_MESSAGE, (10, HEIGHT-150), frames_duration=1200, typing=True, fontsize=14, fontname='future_thin')
#     if player2:
#         Text(TUTORIAL_MESSAGE_P2, (WIDTH-300, HEIGHT-160), frames_duration=1200, typing=True, fontsize=14, fontname='future_thin')

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
            if sum([e.health for e in enemies]) <= 0 and world.end_game == 0:
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
    # if player2:
    #     player2.read_keyboard() 

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

# def play():

# if hasattr(parent_module, "spaceship"):
#     player1spaceship = parent_module.spaceship
#     if hasattr(parent_module, "update"):
#         player1spaceship.update_function = parent_module.update
#     else:
#         player1spaceship.update_function = default_update
# else:
#     player1spaceship = Spaceship(
#         image               = parent_module.image if hasattr(parent_module, "image") else 'spaceships/spaceship_orange1',
#         health              = parent_module.health if hasattr(parent_module, "health") else 1,
#         speed               = parent_module.speed if hasattr(parent_module, "speed") else 0,
#         update_function     = parent_module.update if hasattr(parent_module, "update") else lambda a:a,  
#         ability_function    = parent_module.ability if hasattr(parent_module, "ability") else None,
#         ability_duration    = parent_module.ability_duration if hasattr(parent_module, "ability_duration") else 1,  
#         cooldown_duration   = parent_module.cooldown if hasattr(parent_module, "cooldown") else 10,
#         weapon              = parent_module.weapon if hasattr(parent_module, "weapon") else None,
#         team                = Team.PLAYER
#     )

############# PLAYERS ################
player1_spaceship = Spaceship(image = random.choice(IMAGES_SPACESHIPS), 
                                    health = 500, 
                                    speed = random.choice([7,8,9]), 
                                    ability_function = random.choice(abilities), 
                                    ability_duration = 10, 
                                    cooldown_duration = 2, 
                                    weapon = random.choice(weapons),
                                    team=Team.PLAYER)

world.add_object(player1_spaceship)

player1 = Player1("Player1")

# player2 = None
# world.player2 = None
if NUMBER_OF_PLAYERS == 2:
    player2 = Spaceship(image = random.choice(IMAGES_SPACESHIPS), 
                                        health = 500, 
                                        speed = random.choice([7,8,9]), 
                                        ability_function = random.choice(abilities),
                                        ability_duration = 10, 
                                        cooldown_duration = 2,
                                        update_function = default_update, 
                                        weapon = random.choice(weapons),
                                        team = Team.PLAYER)

    player2 = Player2("Player2")
    # world.player2 = Spaceship(player2)
    # player2.take_control( world.player2 )


world.player1 = player1_spaceship

player1.take_control(world.player1)

#Enemy UI bars init
for e in enemies:
    Bar((0, -50), (180,10), (93, 152, 37), (50, 50, 50), source = e, attached = True, value_attr = "health", max_value_attr = "max_health")
    Bar((0, -35), (180,10), (200, 178, 52), (50, 50, 50), source = e, attached = True, value_attr = "_ability_timer_frames", max_value_attr = "_ability_duration_frames")

#Player 1 UI bars init
Bar((5,HEIGHT - 20),  (180,10),  (113, 172, 57), (50, 50, 50), source=world.player1, value_attr = "health", max_value_attr = "max_health")
Bar((5,HEIGHT - 35),  (180,10),  (99, 88, 26),   (50, 50, 50), reversed = True, source=world.player1, value_attr = "_cooldown_timer_frames", max_value_attr = "_cooldown_frames")
Bar((5,HEIGHT - 35),  (180,10),  (200, 178, 52), (50, 50, 50), source = world.player1, value_attr = "_ability_timer_frames", max_value_attr = "_ability_duration_frames")

    #Player 2 UI bars init
    # if player2:
    #     Bar((WIDTH-185, HEIGHT - 20),  (180,10),  (113, 172, 57), (50, 50, 50), source=world.player2, value_attr = "health", max_value_attr = "max_health")
    #     Bar((WIDTH-185, HEIGHT - 35),  (180,10),  (99, 88, 26),   (50, 50, 50), reversed = True, source=world.player2, value_attr = "_cooldown_timer_frames", max_value_attr = "_cooldown_frames")
    #     Bar((WIDTH-185, HEIGHT - 35),  (180,10),  (200, 178, 52), (50, 50, 50), source = world.player2, value_attr = "_ability_timer_frames", max_value_attr = "_ability_duration_frames")

    #Run inspection
    # if USE_INSPECTOR:
    #     illegal_code = run_source_code_inspection(str(parent_source))
    #     inspection_message = ""
    #     if len(illegal_code) > 0:
    #         illegal_code = [f"\"{code}\"" for code in illegal_code]
    #         inspection_message = "Illegal source code: " + str.join(', ', illegal_code)
    #     inspection_message += run_inspection(player1spaceship)
    #     if len(inspection_message)>0:
    #         print(inspection_message)
    #         world.objects = []
    #         world.guis = []
    #         Text("WARNING:\n" + inspection_message, (50, HEIGHT//2 - 100), 1200, fontsize=30, color=(200, 50, 50))
    #         clock.schedule_unique(sys.exit, 20)



print("#######World###########")
print(pilots)
print(world.objects)
        
pgzrun.go()

