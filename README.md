# Quick Start

Make a new python file in the same directory as **game.py** . For example **myname.py**
Put inside the following two lines:

```python
import game
game.play()
```

You can now run your file and the game will start. Your code must go between those two lines.

# The Game

The bottom spaceship is you and the top is your enemy. 
Your goal is to destroy the enemy spaceship/s. 

## UI

The green bar on top of the enemy is his health points. Your health bar is at 
the bottom left corner. The bright yellow bars indicate an
active ability and also keep the time that the ability will be active.
The dark yellow bar that increases after your ability is finished is
the cooldown period until your ability is ready again.

## Controls

The controls depend on your code but the default keys are the left and right arrows, spacebar and left shift. What those keys will do is up to you but the most common use is arrows to move, space to shoot and left shift to activate your ability. Esc button will close the game (or ctrl + Q ).

## Enviroment

Except from the spaceships there are two more elements. 

#### Asteroids

Asteroids can be destroyed with your weapon. If an asteroid crashes on you then you lose some health points depending on the asteroid size. Asteroids depending on their size have a small chance to drop a powerup when destroyed. 

#### Powerups

Powerups upgrade the spaceship when picked up. The current powerups are health points, extra weapon and bullets upgrade. Except from those you can create your own powerups.

## The spaceship

You will notice the first time that your spaceship does not move or shoot. 
Thats because you have to write the `update` method for the spaceship

The name of the function must be "update" and take 1 argument that represents the spaceship.

This method will run in every frame of the game. The game supports keyboard
input and the spaceship requires 4 keys to control. The default keys are:
LEFT and RIGHT arrow, SPACE and LEFT SHIFT. When you press those keys your spaceship
will read the keyboad and will store a boolean value in the property control.*keyname*
For example if you press the left arrow the property spaceship.control.left will have
the value True.

*All your code should be between* `import game` *and* `game.play()`

The spaceship has the following properties that you can initialize in your file:

| Property | Description |
| ------ | ----------- |
| `speed` | The speed in which the spaceship moves |
| `health` | The starting health of the spaceship |
| `cooldown` | The time in seconds until the ability is ready to be used again |
| `ability_duration` | The duration of the ability |
| `image` | The image used for the spaceship. The images can be found under images directory in the same directory as your python file. |
| `weapon` | The spaceship's weapon |

Those are the main properties you can set in your python file to control the
spaceship. You can create and set those variables in your file.
(The names have to be the same as above and also the currect type. For example weapon
must be of type `WeaponBlueprint`). 

Except from those properties and the update function the spaceship can have 
an ability function. This ability can upgrade your spaceship when activated
but will return to its original state once the ability ends. An ability for
example can incease the spaceship speed or the weapon's damage. This function
should take exactly one argument that represents the spaceship object/instance. 

The ability can also affect other properties of the spaceship that are not
mentioned above and cannot be set at your file as variables. Those are accessed using the ability's
argument. For example spaceship.x (If you have named the argument 'spaceship')

| Property | Description |
| ------ | ----------- |
| `x` | The horizontal position of the spaceship |
| `y` | The vertical position of the spaceship |
| `collidable` | If True the spaceship collides with objects normaly. If False the spaceship does not collide with anything. (Including powerups!) |
| `angle` | The rotation angle of the spaceship in degrees |
| `health` | This is different from the health mentioned above. This property is the spaceship's health when the ability gets activated not the starting health |

## The weapon

The weapon has these properties: 

| Property | Description |
| ------ | ----------- |
| `firerate` | The maximum number of bullets/projectiles the weapon can shoot per second |
| `damage` | The amount of damage the projectile will inflict to the enemy |
| `barrels` | The number of projectiles that the weapon shoots each time it fires. (max 4) |
| `speed` | The speed in which the projectiles travel when shot |
| `spread_angle` | The angle that the bullets will spread when shooting with a weapon with more than one barrels |
| `randomness` | Adds a random angle to the bullets. In other words it makes the weapon inaccurate. It is mostly used for the enemy weapon |

## Game Rules and Constraints

For the game to be challenging but also fun there are some rules and constraints. Some are strict and some are loose but all of them can be bypassed (not recommended).

#### Constraint 1
You cannot use properties that have the "\_" character in front of their name. Those are private variables and functions only used for game internal
functionality. If a keyword starting with "\_" is found the game will warn you and will automatically close. This applies for the following constraints.

#### Constraint 2
Your spaceship cannot be overpowered. The game will calculate a value (points) that the generated spaceship is worth and if this value is
above a threshold it will warn you and won't allow you to play. The points are calculated with the following formulas:

**weapon points** : (firerate\*barrels\*damage)+(bullet speed)

**spaceship points** :

The spaceship points is the sum of the properties below. The weight is multiplied with the property's value before addition.

| Property | Weight |
| ------ | ----------- |
| max_health | 0.25 |
| health | 0.25 |
| speed | 2 |
| ability_duration| 2|
| cooldown | 2 |
| number of child objects | 20 |
| 1 if collidable=False or -1 if collidable=True | 10 |

*child objects are object attached on the spaceship (for example a reflecting shield or a turret)*

#### Constraint 3
The update function cannot alter the spaceship capabilities/points. (No you cannot increase your health when you shoot)

The constraints mentioned above cannot be bypassed by default. If you like a good challenge try bypassing them while they're active but if you don't like to challenge yourself at all you can deactivate all by changing the constant `USE_INSPECTOR` inside library.globals, its up to you.

#### Constraint 4
The spaceship's properties can take values only between a minimum and a maximum. For example firerate's value cannot be above 12 per second. The main reason for those boundaries is game perfomance but also to not allow the spaceship become overpowered. Don't worry though most of the maximum values are still high enough for fun. If you set a value outside the range it will automatically change to the closests legal value inside the range.

| Property | min | max |
| ------ | ----------- | ----------- |
| `cooldown` | 1 | 30 |
| `ability_duration` | 1 | 20 |
| weapon `firerate` | 1 | 12 |
| weapon `barrels` | 1 | 4 |
| weapon `damage` | 1 | 10 |
| weapon `speed` | 1 | 25 |
| weapon `spread_angle` | 0 | 120 |
| weapon `randomness` | 0 | 30 |

#### Rule 1
If you work in a coolaborative enviroment with multiple persons and multiple branches one obvious rule applies which is that you cannot edit the game files except from yours. 

## Making your own images

In the directory images/templates there are some templates that you can copy and then edit to create your own spaceship image and powerup image. Do not edit the original images but rather create a copy of them to a different directory. Also keep the dimensions the same. After you have created your images put the in the corresponding folder and then reference their name in your code for example `image = 'spaceships/myspaceship'`.