import pgzrun
import spaceship

WIDTH = 512
HEIGHT = 512

SPEED = 5

background = Actor('background')

# spaceship = Actor('spaceship')
# spaceship.pos = (256, 460)

# character = spaceship.CustomActor('spaceship')
character = spaceship.CustomActor()
# character.pos = (256, 460)

def update():
    # if keyboard.left:
    #     spaceship.x -= SPEED
    #     if (spaceship.x < 0): spaceship.x = 0
    # elif keyboard.right:
    #     spaceship.x += SPEED
    #     if (spaceship.x > 512): spaceship.x = 512
    character.logic(keyboard, SPEED)

def draw():
    background.draw()
    character.draw()

pgzrun.go()