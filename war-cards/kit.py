#kit class
import suit
import _card_
import card
import random

class kit:
    def __init__(self):
        self.cards = []
        for s in suit.SUIT:
            for c in _card_._CARD_:
                self.cards.append(card.card(s, c))

        random.shuffle(self.cards)
        #random.shuffle(self.cards)
        #self.cards.pop(0)
        #self.cards.count()


    def __str__(self):
        scards = ""
        for index, c in enumerate(self.cards):
            scards += str(index) + "=" + str(c) +"\n"

        return "Kit count="+ str(len(self.cards)) + "\n" +scards

if __name__ == '__main__':
    k = kit()
    print(k)

