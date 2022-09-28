import random


class Player:
    health = 20
    strength = random.randint(1, 6)
    fights_won = 0 
    fight_lost = 0


class Monster:
    def __init__(self, strength):
        self.strength = random.randint(1, 5)




