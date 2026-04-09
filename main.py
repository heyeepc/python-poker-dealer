class Card():

    RANKS = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]

    SUITS = ["梅","方","红","黑"]

    def __init__(self, rank, suit,face_up=True):
        self.rank = rank
        self.suit = suit
        self.is_face_up = face_up

    def __str__(self):
        if self.is_face_up:
            rep = self.suit+self.rank
        else:
            rep = "XX"
        return rep

    def pic_order(self):
        if self.rank == "A":
            FaceNum = 1
        elif self.rank == "j":
            FaceNum = 11
        elif self.rank == "Q":
            FaceNum = 12
        elif self.rank == "K":
            FaceNum = 13
        else:
            FaceNum = int(self.rank)
        if self.suit == "梅":
            suit=1
        elif self.suit == "方":
            suit=2
        elif self.suit == "红":
            suit=3
        else:
            suit=4
        return (suit-1)*13+FaceNum

    def flip(self):
        self.is_face_up = not self.is_face_up
class Hand():
    def __init__(self, suit):
        self.cards = []
    def __str__(self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep = rep + str(card) + "\t"
                
            else:
                rep = "无牌"
            return rep
    def clear(self):
        self.cards = []
    def add(self,card):
        self.cards.append(card)
    def give(self,card,other_hand):
        self.cards.remove(card)
        other_hand.add(card)

        
