from inspect import signature
from copy import deepcopy
from inspect import getdoc

from pgzero.clock import clock
from pgzero.keyboard import keyboard
from pgzero.loaders import sounds

from library.utils import Object, clamp_value
from library.globals import FPS, PLAYER_START_POS, ENEMY_START_POS, MIN_ABILITY_DURATION, MAX_ABILITY_DURATION, MIN_COOLDOWN, MAX_COOLDOWN, WIDTH, HEIGHT, Type, Team
from library.gui import Text
from library.weapon import Weapon
from library.reflector import Reflector

class Spaceship(Object):

    def __init__(self, image = 'spaceships/spaceship_orange1', health = 50, speed = 5, ability = None, ability_duration = 6, cooldown = 8, weapon: Weapon = None, source = None, control = keyboard, team = Team.PLAYER, dummy = False):
        if team == Team.ENEMY:
            pos = ENEMY_START_POS
            angle = 180
        else:
            pos = PLAYER_START_POS
            angle = 0
        super().__init__(image, pos, health=health, speed=speed, angle=angle, source=source, team=team, dummy = dummy)

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

        self.ability_message = getdoc(self._ability)

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
                         "actions"  :self._actions}
    @property
    def ability_message(self):
        return self._ability_message
    
    @ability_message.setter
    def ability_message(self, docstring: str):
        if docstring:
            ability_message = docstring.replace("\n"," ")
        else:
            ability_message = ""
        max_msg_len = 30
        if len(ability_message) > max_msg_len:
            ability_message = ability_message[:max_msg_len] + "..."
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
    def weapon(self, weapon: Weapon):
        if isinstance(weapon, Weapon):
            self._weapon = weapon.assemble(self) if weapon else Weapon(firerate=3, barrels=1, damage=5, mount=self)
        else:
            self._weapon = Weapon(firerate=3, barrels=1, damage=5, mount=self)

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
        value = clamp_value(value, MIN_ABILITY_DURATION, MAX_ABILITY_DURATION)
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
        if self.alive == False:
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
            if self.team == Team.PLAYER:
                Text(self._ability_message, (5,HEIGHT - 55), frames_duration=200, fontname='future_thin', fontsize=14, color=(255,255,255), fade = True)
            #After the duration reset the ability's effects
            clock.schedule_unique(self._reset, self.ability_duration)
        
        if self.control.space:
            self.weapon.shoot()
            # sounds.sfx_laser1.play()

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