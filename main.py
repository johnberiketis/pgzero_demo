import pgzrun
import random
from pgzero.actor import Actor
from laboratory import *
from classes import Projectile

# The game window size
WIDTH = 1000
HEIGHT = 800

asteroids = []
characters = []
projectiles = []

background = Actor('background2')

# character = random.choice(characters_pool)

# Use the below line to avoid a random character selection
character = characters_pool[3]

characters.append(character)

asteroid_images = ['asteroid1',
                  'asteroid2',
                  'asteroid3',
                  'asteroid4',
                  'asteroid5',
                  'asteroid6',
                  'asteroid7']

def update():
    if random.randint(0, 150)  == 1:

        asteroid = Projectile(image = random.choice(asteroid_images), 
                              pos = (random.randint(-80,WIDTH), 0), 
                              speed = 3, 
                              direction = 1, 
                              timespan = 30, 
                              rotation = random.randint(-20,20)/100, 
                              angle = random.randint(1,360)
                              )
        
        asteroids.append(asteroid)

    for asteroid in asteroids:
        if asteroid.alive == False:
            asteroids.remove(asteroid)
        else:
            asteroid.update()
            proj_index = asteroid.collidelist(projectiles)
            if proj_index >= 0:
                asteroid.alive = False
                projectiles[proj_index].alive = False

    for character in characters:
        if character.alive == False:
            characters.remove(character)
        else:
            new_projectiles = character.update()
            if new_projectiles:
                for projectile in new_projectiles:
                    projectiles.append(projectile)
            asteroid_index = character.collidelist(asteroids)
            if asteroid_index >= 0:
                asteroids[asteroid_index].alive = False
                asteroids.remove(asteroids[asteroid_index])
                character.damage(1)

    for projectile in projectiles:
        if projectile.alive == False:
            projectiles.remove(projectile)
        else:
            projectile.update()

def draw():
    background.draw()
    for asteroid in asteroids:
        asteroid.draw()

    for character in characters:
        character.draw()
    
    for projectile in projectiles:
        projectile.draw()

pgzrun.go()