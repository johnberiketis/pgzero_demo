from pgzero.clock import clock
from pgzero.keyboard import keyboard
from utils import Object, team
from globals import WIDTH, HEIGHT
from . import weapon as weaponModule
from . import asteroid as asteroidModule
from . import projectile as projectileModule

class Spaceship(Object):

    def __init__(self, image, pos=(500, 750), health = 10, speed = 5, ability = None, ability_duration = 5, weapon: weaponModule.Weapon = None, dummy = False, bounds = (WIDTH, HEIGHT), source = None, control = keyboard, team = team.TEAM1):
        super().__init__(image, pos, health=health, speed=speed, bounds=bounds, source=source, team=team)
        # Initialize additional variables
        self.ability = ability
        self.ability_duration = ability_duration if ability_duration > 0 else 5
        self.weapon = weapon.copy() if weapon else weaponModule.Weapon(firerate=3, barrels=1, damage=5)
        self.weapon.set_mount(self)
        self.control = control

        # Every action point can activate one ability
        self.actions = 1

        # After an ability there is a cooldown that will reset the action points
        self.cooldown = 8
        self.cooldown_timer = 0

        # The self.default is the original object without any effects applied 
        # This object is used to reset the state of the character
        # The dummy parameter is used to avoid exceeding recursion depth
        if not dummy:
            self.default = Spaceship(image, pos, health, speed, ability, dummy = True, weapon=self.weapon)
        else:
            self.default = None

        self.has_active_ability = False
        self.ability_timer = 0

    def reset(self):
        # Reset the character to its original state
        self.has_active_ability = False
        self.speed = self.default.speed
        self.cooldown = self.default.cooldown
        self.image = self.default.image
        self.collidable = True
        self.childs = self.default.childs

        self.weapon.firerate = self.default.weapon.firerate
        self.weapon.barrels = self.default.weapon.barrels
        self.weapon.calc_muzzles_pos()
        self.weapon.set_mount(self)

        #After the cooldown reset the action points
        self.cooldown_timer = self.cooldown*60
        clock.schedule_unique(self.reset_actions, self.cooldown)

    def reset_actions(self):
        # Reset the character's action points
        self.actions = self.default.actions

    def update(self):
        new_objects = []

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
        ability_output = []
        if self.control.lshift and self.actions == 1:
            ability_output = self.ability(self)
            if ability_output and not isinstance(ability_output, list):
                ability_output = [ability_output]
            self.has_active_ability = True
            self.ability_timer = self.ability_duration*60
            self.actions = 0
            #After the duration reset the ability's effects
            clock.schedule_unique(self.reset, self.ability_duration)
        
        projectiles = []
        if self.control.space:
            projectiles = self.weapon.shoot()
            if not projectiles:
                projectiles = [] 
        
        if ability_output:
            new_objects.extend(ability_output)
        new_objects.extend(projectiles)
        return new_objects

    def damage(self, damage):
        super().damage( damage )

    def collide(self, object):
        #TODO don't forget to use the new attribute "team" in Object
        super().collide(object)
        if isinstance(object, asteroidModule.Asteroid):
            self.damage(1)
        elif isinstance(object, projectileModule.Projectile):
            if object.source != self:
                self.damage(object.damage)
        elif isinstance(object, Spaceship):
            self.damage(1)
