class Pokemon:
    def __init__(self, name, level, type, max_health, current_health, knocked_out):
        self.name = name
        self.level = level
        self.type = type
        self.max_health = max_health
        self.current_health = current_health
        self.knocked_out = knocked_out

    def lose_health(self, health_loss):
        print(self.name + " losing health!!")
        self.current_health -= health_loss
        print(self.name + " now has " + str(self.current_health) + " health!!")
        if self.current_health <= 0:
            self.current_health = 0
            Pokemon.knockout_pokemon(self)

    def gain_health(self, health_gain):
        print(self.name + " regaining health!!")
        self.current_health += health_gain
        if self.current_health > self.max_health:
            self.current_health = self.max_health
        print(self.name + " now has " + str(self.current_health) + " health!!")

    def knockout_pokemon(self):
        self.knocked_out = "Yes"
        print(self.name + " knocked out!!")

    def revive_pokemon(self):
        self.current_health += 50
        self.knocked_out = "No"
        print(self.name + " revived!!")
        print(self.name + " has " + str(self.current_health) + " health!!")

    def attack(self, other_pokemon):
        damage = 20
        if self.type == "Fire" and other_pokemon.type == "Grass":
            other_pokemon.lose_health(2 * damage)

        elif self.type == "Water" and other_pokemon.type == "Grass":
            other_pokemon.lose_health(0.5 * damage)

        elif self.type == "Fire" and other_pokemon.type == "Water":
            other_pokemon.lose_health(0.5 * damage)

        elif self.type == "Grass" and other_pokemon.type == "Fire":
            other_pokemon.lose_health(0.5 * damage)

        elif self.type == "Grass" and other_pokemon.type == "Water":
            other_pokemon.lose_health(2 * damage)

        elif self.type == "Water" and other_pokemon.type == "Fire":
            other_pokemon.lose_health(0.5 * damage)

        elif self.type == other_pokemon.type:
            other_pokemon.lose_health(0.5 * damage)


class Trainer:
    def __init__(self, pokemon, name, potion_num, active_pokemon_no):
        self.pokemon = pokemon
        self.name = name
        self.potion_num = potion_num
        self.active_pokemon_no = active_pokemon_no

        if len(self.pokemon) > 6:
            raise Exception("Max 6 Pokemon allowed!!")

    def use_potion(self):
        if self.potion_num <= 0:
            raise Exception("No potions left!!")
        self.potion_num -= 1
        gain = 20
        Pokemon.gain_health(self.pokemon[self.active_pokemon_no - 1], gain)
        print(self.pokemon[self.active_pokemon_no - 1].name + " has gained " + str(gain) + " health!!")

    def attack_another_trainer(self, other_trainer):
        if self.pokemon[self.active_pokemon_no - 1].knocked_out == "Yes":
            raise Exception("Cannot attack as this Pokemon is knocked out, must swap!!")
        other_pokemon = other_trainer.pokemon[self.active_pokemon_no - 1]
        print("Other trainer's pokemon is " + other_pokemon.name)
        self.pokemon[self.active_pokemon_no - 1].attack(other_pokemon)

    def switch_active_pokemon(self, active_pokemon_no):
        self.active_pokemon_no = active_pokemon_no
        if self.pokemon[self.active_pokemon_no - 1].knocked_out == "Yes":
            raise Exception("Cannot swap to this pokemon as knocked out!!")
        print("Active pokemon for " + self.name + " is now " + self.pokemon[self.active_pokemon_no - 1].name)


# Creating pokemon
charmender = Pokemon("Charmender", 15, "Fire", 100, 100, "No")
charizard = Pokemon("Charizard", 15, "Fire", 100, 100, "No")
bulbasaur = Pokemon("Bulbasaur", 10, "Grass", 100, 100, "No")
venasaur = Pokemon("Venasaur", 10, "Grass", 100, 100, "No")
squirtle = Pokemon("Squirtle", 10, "Water", 100, 100, "No")
blastoise = Pokemon("Blastoise", 10, "Water", 100, 100, "No")


# Creating trainers
ash = Trainer([charizard, bulbasaur, charmender, venasaur, squirtle, blastoise], "Ash", 3, 1)
ketch = Trainer([bulbasaur, charizard, squirtle, blastoise, venasaur], "Ketch", 3, 1)

while bulbasaur.current_health > 0:
    charmender.attack(bulbasaur)

bulbasaur.revive_pokemon()


ash.attack_another_trainer(ketch)
ash.switch_active_pokemon(4)
ketch.switch_active_pokemon(2)
ketch.switch_active_pokemon(4)

ketch.attack_another_trainer(ash)
ash.attack_another_trainer(ketch)

ash.use_potion()
ketch.use_potion()
ash.attack_another_trainer(ketch)
ash.attack_another_trainer(ketch)
ketch.switch_active_pokemon(2)



