from re import A


class Dice:
    def __init__(self):
        self.face1   = 0
        self.face2   = 0
        self.face3   = 0
        self.face4   = 0
        self.face5   = 0
        self.face6   = 0

Dice1   = Dice()

N   = [int(n) for n in input().split()]
Order   = [str(s) for s in input().split()]
