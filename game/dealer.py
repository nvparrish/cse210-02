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
            self.player_input()
            self.player_output()

    def player_input(self):
        cardnumber=self.first.numbers
        print("Moo. The card is: %d" %cardnumber)

        dealer = ""
        while dealer != "h" or dealer != "l":
            dealer = input("Moo. Higher or Lower? [h/l]: ")
            previous_card = self.first
            new_card = Deck()
            if(dealer == "h"):
                self.high(previous_card,new_card)
                break
            elif(dealer == "l"):
                self.low(previous_card,new_card)
                break
            else:
                print("Moo. Choose h or l only.")

    def updates(self, guess, new_card):
        self.score += guess 
        if (self.score <= 0):
            self.is_playing = False
        self.first.numbers=new_card

    def player_output(self):
        print(f"Moo. Your score is: {self.score}")
        print(f"Moo. The next card was: {self.first.numbers}")

        if(self.score <=0):
            self.is_playing = False
            return

        abc=""
        while abc != "n" or "y":
            abc = input("Moo. Play again? [y/n]: ")
            if(abc == "n"):
                self.is_playing = False
                break
            elif(abc == "y"):
                print(" ")
                break
            else:
                print("Moo. Choose y or n only.")

    def high(self, card1, card2):
        if card2.numbers > card1.numbers:
            self.updates(100, card2.numbers)
        elif card2.numbers < card1.numbers:
            self.updates(-75,card2.numbers)

    def low(self, card1, card2):
        if card2.numbers < card1.numbers:
            self.updates(100,card2.numbers)
        elif card2.numbers > card1.numbers:
            self.updates(-75,card2.numbers)
        else:
            print("Moo.  ")
            return