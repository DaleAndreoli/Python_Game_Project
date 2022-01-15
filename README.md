## Dale Andreoli
and17081@byui.edu

# Python Game Project
This project uses the Python library, Asciimatics, to handle the input and output for a 2D game. The player selects their ship and tries to destroy enemy ships while avoiding damage. The game ends when the player is destroyed or all enemies are defeated.

<img src="Resources/Clip.gif" alt="gameplay" width="1500"/>
<img src="Resources/Hangar.png" alt="gameplay" width="1500"/>

Many of the classes in this project are based off a theater analogy in which a cast of actors that follow a script of actions to accomplish the main game loop.

This project aims to demonstrate the following principles of Object Oriented Programming:

* Abstraction
* Encapsulation
* Inheritance
* Polymorphism

Some examples:

Abstraction is used when a class handles things under the hood that we don't need to worry about from other files. 

Encapsulation is used by the classes that have attributes that cannot be changed from other files unless the proper method is called.

Inheritance is used by the "actors". Anything that is drawn on the screen inherits from Actor. It is also used by the events of the game loop, which all inherit from Action.

Polymorphism is used by the events that make up the game loop. They each implement different versions of the same .execute() method.

# Installation
This project uses the [Asciimatics](https://asciimatics.readthedocs.io/en/stable/intro.html) library to handle input and output. 

Asciimatics supports Python versions 2 and 3.

To install Asciimatics, simply install with pip. If necessary, see the [Asciimatics Installation Page](https://asciimatics.readthedocs.io/en/stable/intro.html#installation) for further instructions.

```
$ pip install asciimatics
```

# Configure Your Output Terminal

This project uses the output terminal to display a screen 260 characters wide and 80 characters tall. This can exceed default terminal settings and prevent the game from rendering properly.

To make the game more visible, you will likely need to resize your terminal to take up as much of the screen as possible.

In VS Code, you can adjust your output terminal font size in your settings.json file. To find your settings file, in VS Code:
1. Open the Command Pallette ( Windows: Ctrl + Shift + P, MacOS: Command + Shift + P )
2. Search for "Open Settings (JSON)" and hit enter to open the settings file.
3. Add the following line to set your output terminal font to size 12. Be sure to add a comma after the line that was previously the bottom setting.
```
"terminal.integrated.fontSize": 12 // Default 14
```
You may want to set your font size smaller or larger depending on your screen resolution and size.