from pgzero.actor import Actor
from pgzero.clock import clock
from pgzero.keyboard import keyboard

class Object(Actor):
        
    def __init__(self, image, pos, speed = 0, health = 1, direction = 0, timespan = -1, spin = 0, rotation = 0, bounds = (1000, 800), alive = True, collidable = True, parent = None):
        super().__init__(image, pos)
        self.speed = speed
        self.health = health
        self.direction = direction
        self.timespan = timespan
        self.bounds = bounds
        self.alive = alive
        self.collidable = collidable
        self.spin = spin
        self.rotation = rotation
        self.parent = parent

    def damage(self, damage):
        self.health -= damage

    def collide(self, object):
        pass

    def kill(self):
        self.alive = False

class Spaceship(Object):

    def __init__(self, image, pos=(500, 750), health = 2, speed = 5, ability = None, dummy = False, bounds = (1000, 800), parent = None):
        super().__init__(image, pos, health=health, speed=speed, bounds=bounds, parent=parent)
        # Initialize additional variables
        self.ability = ability
        self.gun = Gun(mount=self, firerate=3, barrels=1)

        # Every action point can activate one ability
        self.actions = 1

        # After an ability there is a cooldown that will reset the action points
        self.cooldown = 8

        # The self.default is the original object without any effects applied 
        # This object is used to reset the state of the character
        # The dummy parameter is used to avoid exceeding recursion depth
        if not dummy:
            self.default = Spaceship(image, pos, health, speed, ability, dummy = True)
        else:
            self.default = None

    def reset(self):
        # Reset the character to its original state
        self.speed = self.default.speed
        self.cooldown = self.default.cooldown
        self.image = self.default.image
        self.y = self.default.y

        self.gun.firerate = self.default.gun.firerate
        self.gun.barrels = self.default.gun.barrels
        self.gun.calc_muzzles_pos()
        self.gun.set_mount(self)

    def reset_actions(self):
        # Reset the character's action points
        self.actions = self.default.actions

    def update(self):
        if self.health <= 0:
            self.alive = False
            return

        if keyboard.left:
            self.x -= self.speed
            if (self.x < 0): self.x = 0
        elif keyboard.right:
            self.x += self.speed
            if (self.x > self.bounds[0]): self.x = self.bounds[0]

        # If left shift key is pressed and you have at least 1 action available
        # then activate the characters ability 
        if keyboard.lshift and self.actions == 1:
            duration = self.ability(self)
            self.actions = 0
            if not duration:
                duration = 1
            #After the duration reset the ability's effects
            clock.schedule_unique(self.reset, duration)
            #After the cooldown reset the action points
            clock.schedule_unique(self.reset_actions, self.cooldown)

        if keyboard.space:
            return self.gun.shoot()

    def damage(self, damage):
        super().damage( damage )
        print(self.health)

    def collide(self, object):
        if isinstance(object, Asteroid):
            print("Collided with Asteroid")
            self.damage(1)
        elif isinstance(object, Projectile):
            print("Collided with Projectile")
            self.damage(object.damage)
        elif isinstance(object, Spaceship):
            print("Collided with Spaceship")
            self.damage(1)
        else:
            print("Collided with Unkown")

class Asteroid(Object):

    def __init__(self, image, pos, speed = 8, health = 10, direction = -1, timespan = 10, spin = 0, rotation = 0, bounds = (1000, 800), parent = None):
        super().__init__(image, pos, speed=speed, health=health, direction=direction, timespan=timespan, spin=spin, rotation=rotation, bounds=bounds, parent=parent)

    def update(self):
        self.rotation = self.rotation + self.spin
        self.y += self.speed*self.direction
        if self.y <= -50 or self.y >= self.bounds[1] + 50 or self.health <= 0:
            self.kill()

    def damage(self, damage):
        self.health -= damage
        print("Asteroid:", self.health)

    def collide(self, object):
        if isinstance(object, Spaceship):
            self.alive = False
        elif isinstance(object, Projectile):
            self.damage( object.damage )


class Projectile(Object):

    def __init__(self, image, pos, speed = 8, health = 1, direction = -1, timespan = 10, spin = 0, rotation = 0, bounds = (1000, 800), damage = 1, parent = None):
        super().__init__(image, pos, speed=speed, health=health, direction=direction, timespan=timespan, spin=spin, rotation=rotation, bounds=bounds, parent=parent)
        self.damage: int = damage
        clock.schedule_unique(self.kill, self.timespan)

    def update(self):
        self.rotation = self.rotation + self.spin
        self.y += self.speed*self.direction
        if self.y <= -50 or self.y >= self.bounds[1] + 50:
            self.kill()

    def collide(self, object):
        if self.parent != object:
            self.alive = False

class Gun():

    def __init__(self, mount, firerate = 3, barrels = 1):
        self.mount = mount
        self.firerate = firerate
        barrels = 1 if barrels > 4 else barrels
        self.barrels = barrels
        self.muzzles_pos = []
        self.calc_muzzles_pos()
        self.gun_ready = True

    def shoot(self):
        if self.gun_ready:
            projectiles = []
            for i in range(self.barrels):
                projectiles.append(Projectile('projectile', tuple([sum(x) for x in zip(self.mount.pos, self.muzzles_pos[i])]), parent = self.mount))
            self.gun_ready = False
            clock.schedule_unique(self.reload, 1/self.firerate)
            return projectiles
    
    def reload(self):
        self.gun_ready = True
    
    def set_mount(self, obj):
        self.mount = obj

    def set_barrels(self, barrels):
        self.barrels = barrels
        self.calc_muzzles_pos()

    def calc_muzzles_pos(self):
        barrels = self.barrels
        if barrels == 2:
            self.muzzles_pos = [(-8,-50), (+8,-50)]
        elif barrels == 3:
            self.muzzles_pos = [(-20,0), (0,-50), (+20,0)]
        elif barrels == 4:
            self.muzzles_pos = [(-20,0), (-8,-50), (+8,-50), (+20,0)]
        else:
            self.muzzles_pos = [(0,-50)]

class Background(Actor):

    def __init__(self, image):
        super().__init__(image)