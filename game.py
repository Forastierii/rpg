import os
import sys

class Player:
    def __init__(self,  name):
        self.name = name
        self.maxhealth = 100
        self.health = 100
        self.attack = 10
        self.defense = 50

def main():
    print("""
    Welcome to the amazing world of Generic Adventure!
    Type the desired option:
    1) Start the game.
    2) Load the game.
    3) Exit the game.
    """)
    
    option = input("-> ")
    
    if option == 1:
        start()
    
    elif option == 2:
        load()

    elif option == 3:
        sys.exit()
    
    else:
        main()

def start():
    print("""
    Let's start the game defining your name. What is your name?
    """)
    name = input("->")
    
    playerIG = Player(name)

    print("""
    Perfect, your name is {name}!
    """)

    sys.exit()

main()