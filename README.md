#  Pokemon Master

For this concept which is a Codeacademy project, a game system similar to a popular game series Pokemon will be implemented.  For those unfamilliar with Pokemon, it is a game where creatures (Pokemon) battle against each other.  Each Pokemon has statistics associated with it like health, level, type and a name.  

The steps taken to implement this project is as follows:
- A Pokemon class was created that keeps track of Pokemon's name, level, type (such as "Fire" and "Water"), maximum health, current health and whether or not Pokemon was knocked out.  
- With this class, inlcuded methods to decrease the Pokemon's health, regaining health and "knock out" a Pokemon (when health is 0), revive a knocked out Pokemon. 
- Attack is another method in this class where takes another Pokemon as argument and deals damage to that Pokemon.  Amount of damage dealt to that Pokemon depends on type of attacking Pokemon and Pokemon being attacked.  If attcking Pokemon has advantage over other Pokemon (such as "Fire" Pokemon attacking a "Grass" pokemon), dealt damage equal to twice the normal damage (this was set manually).  If the attacking Pokemon has disadvantage over other Pokemon(such as "Fire" Pokemon attacking a "Water" pokemon), dealt damage equal to half the normal damage(this was set manually).  Currently just coded for Fire, Water and Grass.
- A trainer class was created that can have up to 6 Pokemon, a name, and a number of Pokemon that can use to heal their Pokemon as well as a "currently active Pokemon", represented as number.
- For this class, trainer can use potion and attack another trainer.  For use potion scenario, it heals the trainer's currently active Pokemon.  Likewise, when a trainer attacks another trainer, the currently active Pokemon deals damage to other trainer's current Pokemon.  In addition, the trainer can switch Pokemon which is currently active.
- Some Pokemon and Trainers were created and tested to see if functionality works such as creating trainers that have multiple Pokemon and switch between them.
- Resumed to methods and added some logic for dealing with edge cases including:
  - A potion should not be able to heal a Pokémon past its maximum health.
  - A Pokémon that is knocked out should not be able to attack another Pokémon.
  - A trainer should not be able to switch their active Pokémon to one that is knocked out.
  
This is just basic version, I am looking to expand this further with adding additional functionality as follows:
- Give Pokémon experience for battling other Pokémon. A Pokémon’s level should increase once it gets enough experience points.
- Create specific Classes that inherit from the general Pokémon class. For example, could you create a Charmander class that has all of the functionality of a Pokémon plus some extra features?
- Let your Pokémon evolve once they hit a certain level.
- Have more stats associated with a Pokémon. In the real game, every Pokémon has stats like Speed, Attack, Defense. All of those stats effect the way Pokemon battle with each other. For example, the Pokémon with the larger Speed stat will go first in the battle.
