"""THIS IS WHERE WE CAN CREATE THE DECK OF RANDOM CARDS FOR THE GAME"""
import random

class Deck:
    def __init__(self):
        self.numbers = random.randint(1,13)

    def getnumbers(self):
        return self.numbers