class deck:
    def __init__(self, cards):
        self.cards = cards

    def face_up(self):
        #c = self.cards[0]
        if(len(self.cards)>0):
            return self.cards.pop(0)
        else:
            return None


    def face_down(self):
        if(len(self.cards)>0):
            return self.cards.pop(0)
        else:
            return None

    def __str__(self):
       
        scards = ""
        for index, c in enumerate(self.cards):
            scards += str(index) + "=" + str(c) +"\n"

        return "DECK count="+ str(len(self.cards)) + "\n" +scards
        

        
        