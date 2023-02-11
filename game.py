import os
import sys
import random

class Player:
    
    def __init__(self,  name, race, job):
        
        self.name = name
        self.race = race
        self.job = job
        self.health = 100
        self.attack = 30
        self.defense = 70
        self.gp = 0

class Goblin:
    
    def __init__(self):
        
        self.name = "goblin"
        self.health = 100
        self.attack = 10
        self.defense = 10
        self.gold = 10

GoblinIG = Goblin()

class Zombie:
    
    def __init__(self):
        
        self.name = "zombie"
        self.health = 100
        self.attack = 20
        self.defense = 20
        self.gold = 20

ZombieIG = Zombie()
        
def main():
    print("""
    Welcome to the amazing world of Generic Adventure!
    Type the desired option:
    1) Start the game.
    2) Load the game.
    3) Exit the game.
    """)
    
    option = input("-> ")
    
    if option == "1":
        setup_new_game()
    
    elif option == "2":
        load_a_game()

    elif option == "3":
        sys.exit()
    
    else:
        main()

def setup_new_game():
    print("""
    Let's start the game defining your name. What is your name?
    """)
    name = input("->")
    
    print("""
    What is your race?
    """)
    race = input("->")
    
    print("""
    What is your class?
    """)
    job = input("->")

    playerIG = Player(name, race, job)

    print("Perfect, your name is", playerIG.name, ".")
    print("You are a", playerIG.race, ".")
    print("You are a", playerIG.job, ".")
    print("You have", playerIG.gp, "gold coins.")
    print("Your stats are:")
    print("Health:", playerIG.health)
    print("Attack:", playerIG.attack)
    print("Defense:", playerIG.defense)
    
    return playerIG

def enemy_choice():
    enemy_number = random.randint(1, 2)
    
    try:
        if enemy_number == 1:
            enemy = GlobinIG
        elif enemy_number == 2:
            enemy = ZombieIG
        else:
            enemy_choice()
    
    except:
        raise Exception("Error handling enemy_choice")
    
    return enemy

def pre_fight():
    enemy = enemy_choice()
    print("A", enemy.name, "is attacking you!")
    return enemy

def damage(playerIG):
    damage = playerIG.attack - enemy.defense
    enemy.health -= damage
    print("The enemy took", damage, "damage.")
    print("It has", enemy.health, "points of life.")

def attack():
    print("You attack with all your might!")
    damage(playerIG)
    
def defend():
    print("You embrace yourself and avoid any damage that would be done to you.")

def run():
    print("You run away.")
    game()

def fight(playerIG):
    
    while playerIG.health >0 and enemy.health >0:
    
        print("It is your turn.")
        print("Your stats are:")
        print("Health:", playerIG.health)
        print("Attack:", playerIG.attack)
        print("Defense:", playerIG.defense)
        print("You have", playerIG.gp, "gold coins.")
        
        print("""
        What would like to do?
        1. Attack.
        2. Defend.
        3. Run.
        """)
        
        option = input("-> ")
        
        if option == "1":
            attack()
            
        elif option == "2":
            defend()
        
        elif option == "3":
            run()
        
        else:
            print("You have to choose among the options below.")
            fight()
            
    if playerIG.health <= 0:
        print("You lose!")
        sys.exit()
    
    elif enemy.health <= 0:
        print("You win!")
    
def travel():
    print("Under construction.")
    sys.exit()

def game():
    print("Your stats are:")
    print("Health:", playerIG.health)
    print("You have", playerIG.gp, "gold coins.")
    
    print("""
    What would you like doing?
    1) Explore a dungeon.
    2) Go to the town center.
    3) Leave the game.
    """)

    option = input("-> ")
    
    if option == "1":
        enemy_choice()
        pre_fight()
        fight()
    
    elif option == "2":
        travel()

    elif option == "3":
        print("Thank you for playing!")
        sys.exit()
    
    else:
        print("Choose an option below.")
        game()


def world(): #This function establishes the primary order of the game
    main()
    game()

world()