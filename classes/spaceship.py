from pgzero.clock import clock
from pgzero.keyboard import keyboard
from utils import Object
from globals import WIDTH, HEIGHT, PLAYER_START_POS, ENEMY_START_POS, ASTEROIDS_DAMAGE, ABILITY_DURATION_LIMIT, Type, Team
from . import weapon as weaponModule

class Spaceship(Object):

    def __init__(self, image, health = 10, speed = 5, ability = None, ability_duration = 6, weapon: weaponModule.Weapon = None, bounds = (WIDTH, HEIGHT), source = None, control = keyboard, team = Team.PLAYER, direction = -1):
        if team == Team.ENEMY:
            pos = ENEMY_START_POS
        else:
            pos = PLAYER_START_POS
        super().__init__(image, pos, health=health, speed=speed, bounds=bounds, source=source, team=team, direction=direction)
        self.ability = ability

        if ability_duration > ABILITY_DURATION_LIMIT:
            ability_duration = ABILITY_DURATION_LIMIT
        elif ability_duration <= 0:
            ability_duration = 1

        self.ability_duration = ability_duration
        self.weapon = weapon.assemble(self) if weapon else weaponModule.Weapon(firerate=3, barrels=1, damage=5, mount=self)
        # self.weapon.set_mount(self)
        self.control = control

        # Every action point can activate one ability
        self.actions = 1

        # After an ability there is a cooldown that will reset the action points
        self.cooldown = 8
        self.cooldown_timer = 0

        self.ability_timer = 0

        # The self.default is the original object without any effects applied 
        # This object is used to reset the state of the character after an ability ends
        self.default = SpaceshipClone(image, pos, health, speed, ability, weapon=self.weapon, direction=self.direction, angle=self.angle)

    def reset(self):
        # Reset the character to its original state
        self.speed = self.default.speed
        self.cooldown = self.default.cooldown
        self.image = self.default.image
        self.collidable = True
        self.childs = self.default.childs
        self.angle = self.default.angle
        self.direction = self.default.direction

        self.weapon.firerate = self.default.weapon.firerate
        self.weapon.barrels = self.default.weapon.barrels
        self.weapon.damage = self.default.weapon.damage
        self.weapon.calc_muzzles_pos()

        #After the cooldown reset the action points
        self.cooldown_timer = self.cooldown*60
        clock.schedule_unique(self.reset_actions, self.cooldown)

    def reset_actions(self):
        # Reset the character's action points
        self.actions = self.default.actions

    @property
    def collidable(self):
        return self._collidable

    @collidable.setter
    def collidable(self, value: bool):
        if value:
            self.set_image(self.default.image)
        else:
            self.set_image('spaceship_transparent')
        self._collidable = value

    def set_image(self, image):
        temp_angle = self.angle
        self.angle = 0 
        self.image = image
        self.angle = temp_angle

    def update(self):
        super().update()

        if self.health <= 0:
            self.alive = False
            return
        
        if self.cooldown_timer > 0:
            self.cooldown_timer -= 1 # pgzero runs at 60FPS

        if self.ability_timer > 0:
            self.ability_timer -= 1 # pgzero runs at 60FPS

        if self.control.left:
            self.move(-self.speed, 0)
            self.clamp()
        elif self.control.right:
            self.move(+self.speed, 0)
            self.clamp()

        # If left shift key is pressed and you have at least 1 action available
        # then activate the characters ability 
        if self.control.lshift and self.actions == 1:
            self.ability(self)
            self.ability_timer = self.ability_duration*60
            self.actions = 0
            #After the duration reset the ability's effects
            clock.schedule_unique(self.reset, self.ability_duration)
        
        if self.control.space:
            self.weapon.shoot()

    def damage(self, damage):
        super().damage( damage )

    def collide(self, object):
        super().collide(object)
        if object.team != self.team:
            if object.type == Type.ASTEROID:
                self.damage(ASTEROIDS_DAMAGE)
            elif object.type == Type.PROJECTILE:
                self.damage(object.damage)

class SpaceshipClone():

    def __init__(self, image, pos=(500, 750), health = 10, speed = 5, ability = None, ability_duration = 5, weapon: weaponModule.Weapon = None, bounds = (WIDTH, HEIGHT), source = None, control = keyboard, team = Team.PLAYER, angle = 0,  direction = -1):
        self.image = image
        self.pos = pos
        self.angle = angle
        self.direction = direction
        self.speed = speed
        self.health = health
        self.bounds = bounds
        self.source = source
        self.team = team
        self.ability = ability
        self.ability_duration = ability_duration if ability_duration > 0 else 5
        self.weapon = weapon.assemble(self) if weapon else weaponModule.Weapon(firerate=3, barrels=1, damage=5, mount=self)
        self.control = control
        self.actions = 1
        self.cooldown = 8
        self.cooldown_timer = 0
        self.ability_timer = 0
        self.childs = []