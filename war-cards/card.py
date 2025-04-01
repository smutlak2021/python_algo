class card:
    def __init__(self, suit, _card):
        self.suit = suit
        self._card = _card


    def __str__(self):
        return str(self.suit) + " " + str(self._card)

    def __gt__(self, other):  # Greater than
        if isinstance(other, card):
            if self.suit.value > other.suit.value:
                if self._card.value > other._card.value:
                        return True
        else:
            return NotImplemented
        
        return False
        