from pgzero.clock import clock
from pgzero.keyboard import keyboard
from utils import Object, clamp_value
from globals import WIDTH, HEIGHT, FPS, PLAYER_START_POS, ENEMY_START_POS, ASTEROIDS_DAMAGE, ABILITY_DURATION_LIMIT, MIN_COOLDOWN, MAX_COOLDOWN, Type, Team
from . import weapon as weaponModule
from . import reflector as reflectorModule
from inspect import signature
from copy import deepcopy

class Spaceship(Object):

    def __init__(self, image, health = 10, speed = 5, ability = None, ability_duration = 6, cooldown = 8, weapon: weaponModule.Weapon = None, bounds = (WIDTH, HEIGHT), source = None, control = keyboard, team = Team.PLAYER, direction = -1):
        if team == Team.ENEMY:
            pos = ENEMY_START_POS
        else:
            pos = PLAYER_START_POS
        super().__init__(image, pos, health=health, speed=speed, bounds=bounds, source=source, team=team, direction=direction)
        if direction == 1:
            self.angle = 180
        else:
            self.angle = 0
        self.weapon = weapon
        self.control = control

        # Every action point can activate one ability
        self._actions = 1

        # After an ability there is a cooldown that will reset the action points
        self.ability = ability
        self.ability_duration = ability_duration
        self.cooldown = cooldown

        # Timers to countdown the cooldown and ability duration
        self._cooldown_timer_frames = 0
        self._ability_timer_frames = 0

        # The self._default represents the spaceship without any effects applied 
        # This dictionary is used to reset the state of the spaceship after an ability/effect ends
        self._default = {"image"    :image,
                         "max_health":self.max_health,
                         "speed"    :speed,
                         "ability"  :ability,
                         "ability_duration":ability_duration,
                         "cooldown" :cooldown,
                         "collidable":True,
                         "childs"   :deepcopy(self.childs),
                         "weapon"   :self.weapon.assemble(self),
                         "direction":direction,
                         "actions"  :self._actions}

    @property
    def cooldown(self):
        return self._cooldown_frames/FPS
    
    @cooldown.setter
    def cooldown(self, value):
        value = clamp_value(value, MIN_COOLDOWN, MAX_COOLDOWN)
        self._cooldown_frames = value*FPS

    @property
    def weapon(self):
        return self._weapon
    
    @weapon.setter
    def weapon(self, weapon: weaponModule.Weapon):
        if isinstance(weapon, weaponModule.Weapon):
            self._weapon = weapon.assemble(self) if weapon else weaponModule.Weapon(firerate=3, barrels=1, damage=5, mount=self)
        else:
            self._weapon = weaponModule.Weapon(firerate=3, barrels=1, damage=5, mount=self)

    @property
    def ability(self):
        return self._ability

    @ability.setter
    def ability(self, method):
        if not callable(method):
            method = lambda a: a
        else:
            sig = signature(method)
            if len(sig.parameters) != 1:
                method = lambda a: a
        self._ability = method

    @property
    def collidable(self):
        return self._collidable

    @collidable.setter
    def collidable(self, value: bool):
        if value:
            self._set_image(self._default["image"])
        else:
            self._set_image('spaceships/transparent')
        self._collidable = value
    
    @property
    def ability_duration(self):
        return self._ability_duration_frames/FPS

    @ability_duration.setter
    def ability_duration(self, value):
        value = clamp_value(value, 1, ABILITY_DURATION_LIMIT)
        self._ability_duration_frames = value*FPS

    def _reset(self):
        # Reset the character to its original state
        self.image = self._default["image"]
        self.max_health = self._default["max_health"]
        self.speed = self._default["speed"]
        self.ability = self._default["ability"]
        self.ability_duration = self._default["ability_duration"]
        self.cooldown = self._default["cooldown"]
        self.collidable = self._default["collidable"]
        self.childs = self._default["childs"]
        self.direction = self._default["direction"]

        self.weapon.firerate = self._default["weapon"].firerate
        self.weapon.barrels = self._default["weapon"].barrels
        self.weapon.damage = self._default["weapon"].damage
        self.weapon.speed = self._default["weapon"].speed

        #After the cooldown reset the action points
        self._cooldown_timer_frames = self._cooldown_frames
        clock.schedule_unique(self._reset_actions, self.cooldown)

    def _reset_actions(self):
        # Reset the character's action points
        self._actions = self._default["actions"]

    def _set_image(self, image):
        temp_angle = self.angle
        self.angle = 0 
        self.image = image
        self.angle = temp_angle

    def update(self):
        super().update()

        if self.health <= 0:
            self.alive = False
            return
        
        if self._cooldown_timer_frames > 0:
            self._cooldown_timer_frames -= 1 # pgzero runs at 60FPS by default

        if self._ability_timer_frames > 0:
            self._ability_timer_frames -= 1 # pgzero runs at 60FPS by default

        if self.control.left:
            self.move(-self.speed, 0)
            self.clamp()
        elif self.control.right:
            self.move(+self.speed, 0)
            self.clamp()

        # If left shift key is pressed and you have at least 1 action available
        # then activate the characters ability 
        if self.control.lshift and self._actions == 1:
            self._ability(self)
            self._ability_timer_frames = self._ability_duration_frames
            self._actions = 0
            #After the duration reset the ability's effects
            clock.schedule_unique(self._reset, self.ability_duration)
        
        if self.control.space:
            self.weapon.shoot()

    def _damage(self, damage):
        super()._damage( damage )

    def collide(self, object):
        super().collide(object)
        if object.type == Type.ASTEROID:
            self._damage(object.damage)
        elif object.type == Type.PROJECTILE:
            self._damage(object.damage)
        elif object.type == Type.POWERUP and self.team != Team.ENEMY:
            object.effect(self)
    
    def deploy_reflector(self):
        reflector = reflectorModule.Reflector(image = 'others/metal_wall', pos = (self.x, self.y + 60*self.direction), timespan = self.ability_duration, team=self.team)
        self.add_child( reflector )