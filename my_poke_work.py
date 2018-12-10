import random

class Pokemon():
    # Contains the arguments used for the Pokemon
    def __init__(self, hp, tackle, quickattack, special, name):
        self.hp = hp
        self.tackle = tackle
        self.quickattack = quickattack
        self.special = special
        self.name = name

    def battle_initiate(self):
        print('I am the Pokemon', self.name)


pikachu = Pokemon(100, 25, 45, 49, "pikachu")
charmander = Pokemon(100, 20, 30, 49, "charmander")
squirtle = Pokemon(100, 23, 37, 51, "squirtle")
bulbasaur = Pokemon(110, 18, 15, 45, "bulbasaur")

def enemy_death_check(self, other):
    if other.hp <= 0:
        print(other.name,"fainted")
        quit()

def self_death_check(self, other):
    if self.hp <= 0:
        print(self.name,"fainted")
        quit()

def opponent_tackle(self, other):
    n = random.randint(1,25)
    if n > 20:
        print(self.name,"dodged")
    else:
        print(other.name,"used tackle")
        self.hp = self.hp - other.tackle
        print(self.name,"has",self.hp,'hp left')
        self_death_check(self, other)

def opponent_quickattack(self, other):
    n = random.randint(1,25)
    if n > 20:
        print(self.name,"dodged")
    else:
        print(other.name,"used quickattack")
        self.hp = self.hp - other.quickattack
        print(self.name,"has",self.hp,'hp left')
        self_death_check(self, other)

def opponent_special(self, other):
    n = random.randint(1,25)
    if n > 20:
        print(self.name,"dodged")
    else:
        print(other.name,"used their special move")
        self.hp = self.hp - other.special
        print(self.name,"has",self.hp,"hp left")
        self_death_check(self, other)

def opponent_turn(self, other):
    n = random.randint(1,15)
    if n > 10:
        opponent_tackle(self, other)
    if 6 <= n <= 10:
        opponent_quickattack(self, other)
    if 1 <= n <= 5:
        opponent_special(self, other)

def self_tackle(self, other):
    n = random.randint(1,25)
    if n > 20:
        print(other.name,"dodged")
    else:
        print(self.name,"used tackle")
        other.hp = other.hp - self.tackle
        print(other.name,"has",other.hp,"hp left")
        enemy_death_check(self, other)

def self_quickattack(self, other):
    n = random.randint(1,25)
    if n > 20:
        print(other.name,"dodged")
    else:
        print(self.name,"used quickattack")
        other.hp = other.hp - self.quickattack
        print(other.name,"has",other.hp,'hp left')
        enemy_death_check(self, other)

def self_special(self, other):
    n = random.randint(1,25)
    if n > 20:
        print(other.name,"dodged")
    else:
        print(self.name,"used thunderbolt")
        other.hp = other.hp - self.special
        print(other.name,"has",other.hp,"hp left")
        enemy_death_check(self, other)

def battle(self, other):
    print(self.name, 'and', other.name, 'are fighting')
    print(self.name,"has",self.hp,"hp","and",other.name,"has",other.hp,"hp")
    enemy_death_check(self, other)
    self_death_check(self, other)
    # Gives list of moves that your pokemon knows
    print("pikachu knows 3 attacks: tackle, quickattack, and thunderbolt")
    # Asks for a move
    move = input("what attack would you like to use?")
    if move == "tackle":
        self_tackle(self, other)
    elif move == "quickattack":
        self_quickattack(self, other)
    elif move == "thunderbolt":
        self_special(self, other)
    else:
        print("You did nothing!")
    opponent_turn(self, other)
    battle(self, other)


pikachu.battle_initiate()
print("a wild Pokemon is in front of you")
choice = input("Do you want to start a battle? ")
if choice == "no":
    print("you ran away")

else:
    n = input("Which battle do you want to do? 1 = Pikachu vs. Charmander, 2 = Pikachu vs. Squirtle, 3 = Pikachu vs. Bulbasaur ")
    if n == 1:
        battle(pikachu, charmander)
    elif n == 2:
        battle(pikachu, squirtle)
    else:
        battle(pikachu, bulbasaur)
