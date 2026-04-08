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
