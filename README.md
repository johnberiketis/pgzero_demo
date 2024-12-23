# Quick Start

Make a new python file in the same directory as **game.py** . For example **"myname.py"**
Put inside the following two lines:

```python
import game
game.play()
```

You can now run your file and the game will start.
The bottom spaceship is you and the top is your enemy. 
Your goal is to destroy the enemy spaceship. The green bar
on top of the enemy is his health points. Your health bar is at 
the bottom left corner. The bright yellow bars indicate an
active ability and keep the time that the ability will be active.
The dark yellow bar that increases after your ability is finished is
the cooldown period until your ability is ready again.

## The spaceship

You will notice the first time that your spaceship does not move or shoot. 
Thats because you have to write an `update` method for the spaceship. 
This method will run in every frame of the game. The game supports keyboard
input and the spaceship requires 4 keys to control. The default keys are:
LEFT and RIGHT arrow, SPACE and LEFT SHIFT. When you press those keys your spaceship
will read the keyboad and will store a boolean value in the property control.*keyname*
For example if you press the left arrow the variable spaceship.control.left will have
the value True.

*All your code should be between* `import game` *and* `game.play()`

The spaceship has the following properties:

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

## Game Rules

For the game to be challenging but also fun there are some rules. Some are strict and some are loose but all of them can be bypassed if you really want to. (not recomended)
One rule is that you are not allowed to use properties that have the "_" character in front of their name. Those are private variables only used for game internal
functionality. If a keyword starting with "_" is found the game will warn you and will automatically close. This applies for the following rules also.
Another rule is that your spaceship cannot be overpowered. The game will calculate a value (points) that the generated spaceship is worth and if this value is
above a threshold it will warn you and won't allow you to play. The points are calcualated with the following formulas:

weapon points = (weapon.firerate\*weapon.barrels\*weapon.damage)+weapon.speed

spaceship points = max_health\*0.25+health\*0.25+speed\*2+ability_duration\*2-cooldown\*2+(number of child objects)\*10 plus 10 if collidable=False or -10 if collidable=True

*child objects are object attached on the spaceship (for example a reflecting shield or a turret)*

The final rule is that the update function cannot alter the spaceship capabilities/points. (No unfortunatelly you cannot increase your health when you shoot)

Those rules as bentioned above cannot be bypasses easily by default. If you like a good challenge try bypassing the rules or if you don't like to challenge yourself at all you can deactivate all the rules by changing the constant `USE_INSPECTOR` inside library.globals, its up to you.

