from inspect import signature
from copy import deepcopy
from inspect import getdoc

from pgzero.clock import clock
from pgzero.keyboard import keyboard

from library.utils import Object, clamp_value
from library.globals import FPS, PLAYER_START_POS, ENEMY_START_POS, MAX_ABILITY_MSG_LENGTH, MIN_ABILITY_DURATION, MAX_ABILITY_DURATION, MIN_COOLDOWN, MAX_COOLDOWN, WIDTH, HEIGHT, Type, Team
from library.gui import Text
from library.weapon import Weapon
from library.reflector import Reflector
from library.blueprints import SpaceshipBlueprint, WeaponBlueprint

class Spaceship(Object):

    def __init__(self, blueprint: SpaceshipBlueprint):
        if blueprint.team == Team.ENEMY:
            pos = ENEMY_START_POS
            angle = 180
        else:
            pos = PLAYER_START_POS
            angle = 0
        super().__init__(blueprint.image, pos=pos, angle=angle, health=blueprint.health, speed=blueprint.speed, team=blueprint.team)

        self.weapon = blueprint.weapon
        self.control = keyboard
        self.ability = blueprint.ability_function # After an ability there is a cooldown that will reset the action points
        self.ability_duration = blueprint.ability_duration
        self.ability_message = getdoc(self._ability)
        self.cooldown = blueprint.cooldown_duration
        self.move_function = blueprint.move_function
        self.shoot_function = blueprint.shoot_function

        self._actions = 1 # Every action point can activate one ability
        self._cooldown_timer_frames = 0 # Timer to countdown the cooldown duration
        self._ability_timer_frames = 0 # Timer to countdown the ability duration
        self._blueprint = blueprint

    def _fix_callable(self, method):
        if not callable(method):
            method = lambda a: a
        else:
            sig = signature(method)
            if len(sig.parameters) != 1:
                method = lambda a: a
        return method

    @property
    def move_function(self):
        return self._move_function

    @move_function.setter
    def move_function(self, method):
        self._move_function = self._fix_callable(method)

    @property
    def shoot_function(self):
        return self._shoot_function

    @shoot_function.setter
    def shoot_function(self, method):
        self._shoot_function = self._fix_callable(method)

    @property
    def ability_message(self):
        return self._ability_message
    
    @ability_message.setter
    def ability_message(self, docstring: str):
        if docstring:
            ability_message = docstring.replace("\n"," ")
        else:
            ability_message = ""
        if len(ability_message) > MAX_ABILITY_MSG_LENGTH:
            ability_message = ability_message[:MAX_ABILITY_MSG_LENGTH] + "..."
        self._ability_message = ability_message if self._ability else "" 

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
    def weapon(self, weapon_blueprint: WeaponBlueprint):
        if weapon_blueprint and isinstance(weapon_blueprint, WeaponBlueprint):
            self._weapon = Weapon(weapon_blueprint)
            self._weapon._mount = self
        else:
            self._weapon = None

    @property
    def ability(self):
        return self._ability

    @ability.setter
    def ability(self, method):
        self._ability = self._fix_callable(method)

    @property
    def collidable(self):
        return self._collidable

    @collidable.setter
    def collidable(self, value: bool):
        if value:
            self._set_image(self._blueprint.image)
        else:
            self._set_image('spaceships/transparent')
        self._collidable = value
    
    @property
    def ability_duration(self):
        return self._ability_duration_frames/FPS

    @ability_duration.setter
    def ability_duration(self, value):
        value = clamp_value(value, MIN_ABILITY_DURATION, MAX_ABILITY_DURATION)
        self._ability_duration_frames = value*FPS

    def _reset(self):
        # Reset the character to its original state
        self.image = self._blueprint.image
        self.max_health = self._blueprint.health
        self.speed = self._blueprint.speed
        self.ability = self._blueprint.ability_function
        self.ability_duration = self._blueprint.ability_duration
        self.cooldown = self._blueprint.cooldown_duration
        self.collidable = True
        self.weapon = self._blueprint.weapon

        #After the cooldown reset the action points
        self._cooldown_timer_frames = self._cooldown_frames
        clock.schedule_unique(self._reset_actions, self.cooldown)

    def _reset_actions(self):
        # Reset the character's action points
        self._actions = 1

    def _set_image(self, image):
        temp_angle = self.angle
        self.angle = 0 
        self.image = image
        self.angle = temp_angle

    def update(self):
        super().update()
        if self.alive == False:
            return
        
        if self._cooldown_timer_frames > 0:
            self._cooldown_timer_frames -= 1 # pgzero runs at 60FPS by default

        if self._ability_timer_frames > 0:
            self._ability_timer_frames -= 1 # pgzero runs at 60FPS by default

        # Movement
        # self.move_function(self) if self.move_function else None
        # self.clamp()

        if self.control.left:
            self.move(-self.speed, 0)
            self.clamp()
        elif self.control.right:
            self.move(+self.speed, 0)
            self.clamp()

        # Ability
        if self.control.lshift and self._actions == 1:
            self.ability(self)
            self._ability_timer_frames = self._ability_duration_frames
            self._actions = 0
            if self.team == Team.PLAYER:
                Text(self._ability_message, (5,HEIGHT - 55), frames_duration=200, fontname='future_thin', fontsize=14, color=(255,255,255), fade = True)
            #After the duration reset the ability's effects
            clock.schedule_unique(self._reset, self.ability_duration)
        
        if self.control.space:
            self.weapon.shoot()
        # Shooting
        # if self.weapon:
        #     self.shoot_function(self) if self.shoot_function else None

    def _damage(self, damage):
        super()._damage( damage )

    def collide(self, object):
        super().collide(object)
        if object.type == Type.ASTEROID:
            self._damage(object.damage)
        elif object.type == Type.PROJECTILE:
            self._damage(object.damage)
        elif object.type == Type.POWERUP and self.team != Team.ENEMY:
            message = getdoc(object.effect)
            if message:
                message = message.replace("\n"," ")
                Text(message[:30], (5,HEIGHT - 55), frames_duration=200, fontname='future_thin', fontsize=14, color=(255,255,255), fade = True)
            object.effect(self)
    
    def deploy_reflector(self):
        reflector = Reflector(image = 'others/metal_wall', pos = (self.x, self.y - 60*self.team.value), timespan = self.ability_duration, team=self.team)
        self.add_child( reflector )