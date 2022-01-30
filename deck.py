import random

class Deck:
    """thirteen (13) cards with values ranging from 1 to 13.
    The responsibility of the deck is to keep track of the cards that are drawn and 
    calculate the points earned or lost
    
    Attributes:
    value (int) : the number on the card
    """
    def __init__(self):
        """makes a new instance of deck
        Arguments: 
        self (deck): an instance of the deck
        """
        self.value = 0
        self.points = 0

    def chosecard(self):
        """generates a random value for the card and calculates the points given on
        each guess
        """
        self.value = random.randint(1, 14)
        self.points = 100 if self.value == 'h' else -75 if self.value == 'l' else  0 