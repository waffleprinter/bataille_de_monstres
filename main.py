import random

i = 0
monster_list = []

class Player:
    health = 20
    strength = random.randint(1, 6)
    fights_won = 0
    fight_lost = 0


class Monster:
    def __init__(self, strength=None):
        self.strength = strength if strength else random.randint(1, 6)


def create_monster():
    global i
    i += 1
    monster_list.append(Monster(f"m{i}"))


def list_choices():
    create_monster()
    print(f"Vous tombez en face avec un adversaire de difficulté: {}")

list_choices()
