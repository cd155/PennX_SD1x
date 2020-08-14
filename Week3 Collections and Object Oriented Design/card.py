import random

class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

deck = []
suits = ['d', 's', 'c', 'h']
for i in range(13):
    for j in range(4):
        c = Card()
        c.suit = suits[j]
        c.rank = i
        deck.append(c)

random.shuffle(deck)

# pick the 10th card
tenth_card = deck[9]
print(str(tenth_card.rank) + " " + str(tenth_card.suit))