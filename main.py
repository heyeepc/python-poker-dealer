import random


class Card():
    RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    SUITS = ["梅", "方", "红", "黑"]

    def __init__(self, rank, suit, face_up=True):
        self.rank = rank
        self.suit = suit
        self.is_face_up = face_up

    def __str__(self):
        if self.is_face_up:
            rep = self.suit + self.rank
        else:
            rep = "XX"
        return rep

    def flip(self):
        self.is_face_up = not self.is_face_up


class Hand():
    def __init__(self):  # 移除了多余的 suit 参数
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

    def add(self, card):
        self.cards.append(card)

    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)


class Poke(Hand):  # 建议类名首字母大写
    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank, suit))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, hands, per_hand=13):  # 修正了缩进和拼写
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards.pop(0)  # pop 使用圆括号，且会自动删除该元素
                    hand.add(top_card)
                else:
                    print("不能继续发牌，牌已经发完")
                    return  # 牌完即止


if __name__ == "__main__":
    print("--- 扑克牌分发系统 ---")

    # 1. 创建4个玩家实例
    players = [Hand(), Hand(), Hand(), Hand()]

    # 2. 创建一叠牌并初始化
    poke1 = Poke()
    poke1.populate()
    poke1.shuffle()

    # 3. 发牌
    poke1.deal(players, 13)

    # 4. 显示结果
    n = 1
    for hand in players:
        print(f"牌手 {n}: {hand}")
        n += 1

    input("\n按回车键退出")


        
