# program - game war
#A standard deck of playing cards contains 52 cards.   
"""
These 52 cards are divided into four suits: hearts, diamonds, clubs, and spades.
Each suit has 13 cards: Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, and King.   
Sources and related content
"""

import kit
import suit
import _card_
import deck



if __name__ == '__main__':
    k = kit.kit()
    d1 = deck.deck(k.cards[0:26])
    d2 = deck.deck(k.cards[26:52])
    print(k)
    print(d1)
    print(d2)
    index = 0
    while True:
        print("*********** " + str(index))
        index += 1
        c1 = d1.face_up()
        if c1 is None:
            break
        print(c1)
        c2 = d2.face_up()
        if c2 is None:
            break
        print(c2)
        if(c1 > c2):
            print ("c1 is higher than c2")
        else:
            print ("c2 is higher than c1")



