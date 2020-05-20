import random
class card:
    def __init__(self, value, suit):
        self.value=value
        self.suit=suit

    def ShowCard(self):
        if self.value==1:
            rank="Ace"
        elif self.value==11:
            rank="Jack"
        elif self.value==12:
            rank="Queen"
        elif self.value==13:
            rank="King"
        else:
            rank=str(self.value)
        return "{} of {} ".format(rank, self.suit)


suits=["Heart","Diamond","Spade","Club"]

deck =[card(i,y).ShowCard() for i in range(1,14) for y in suits]


def Hand(deck,number):
     # draw = random.randrange(1, 54)
     hand=[deck[random.randint(1,52)] for i in range(1, number+1)]
     print (hand)



Hand(deck,5)

