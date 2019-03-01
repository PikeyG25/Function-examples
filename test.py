class Card(object):

                """a playing card"""

                RANKS = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]

                SUITS = ["C","D","H","S"]

                def __init__(self,rank,suit):

                                self.rank=rank

                                self.suit=suit

#main

card1 = Card(rank = "A",suit="C")

print(card1)
