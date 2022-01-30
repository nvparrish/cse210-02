"""THIS IS WHERE THE "DEALER" WILL ASK QUESTIONS AND WILL REVEAL
THE CARDS TO THE PLAYER"""

from game.card import Deck

class Players:
    def __init__(self):
        self.first = Deck()
        self.is_playing = True
        self.score = 300

    def begin(self):
        while self.is_playing:
            pass

    def player_input(self):
        cardnumber=self.first.value
        print("The card is: %d" %cardnumber)

    dealer = ""
    while dealer != "h" or dealer != "l":
        dealer = input("Higher or Lower? [h/l]: ")
        previous_card = self.first
        new_card = Deck()
        if(dealer == "h"):
            self.high(previous_card,new_card)
            break
        elif(dealer == "l"):
            self.low(previous_card,new_card)
            break
        else:
            print("Choose h or l only.")