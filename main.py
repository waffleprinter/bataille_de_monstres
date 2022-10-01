import random


class Player:
    health = 20
    battles_won = 0
    battles_lost = 0
    battles_fought = 0
    consecutive_wins = 0
    strength = None
    last_combat_status = None

    def reset(self):
        self.health = 20
        self.battles_won = 0
        self.battles_lost = 0
        self.battles_fought = 0
        self.consecutive_wins = 0
        self.strength = None
        self.last_combat_status = None


class Monster:
    def __init__(self, strength=None, number=None):
        self.strength = strength if strength else random.randint(1, 5)
        self.number = number if number else 0

    def reset(self, strength=None, number=None):
        self.strength = strength if strength else random.randint(1, 5)
        self.number = number if number else 0


def encounter_monster():
    print(f"Vous tombez face à face avec un adversaire de difficulté {monster.strength}")
    action = int(input("Que voulez vous faire?:\n"
                       "  1. Combattre cet adversaire.\n"
                       "  2. Contourner cet adversaire et aller ouvrir une autre porte.\n"
                       "  3. Afficher les règles du jeu.\n"
                       "  4. Quitter la partie.\n"))

    if action == 1:
        fight_monster()
        encounter_monster()
    elif action == 2:
        run_away()
        encounter_monster()
    elif action == 3:
        list_rules()
        encounter_monster()
    else:
        quit_game()


def fight_monster():
    player.battles_fought += 1
    player.strength = random.randint(1, 6)
    monster.number += 1

    print(f"Adversaire: {monster.number}\n"
          f"Force de l'adversaire: {monster.strength}\n"
          f"Niveau de vie de l'usager: {player.health}\n"
          f"Combat {player.battles_fought}: {player.battles_won} victoires vs {player.battles_lost} défaites.\n\n"
          f"Lancé du dé: {player.strength}\n")

    if player.strength > monster.strength:
        player.last_combat_status = "Victoire"
        player.health = player.health + monster.strength
        player.battles_won += 1
        player.consecutive_wins += 1
    else:
        player.last_combat_status = "Défaite"
        player.health = player.health - monster.strength
        player.battles_lost += 1
        player.consecutive_wins = 0

    print(f"Dernier combat: {player.last_combat_status}\n"
          f"Niveau de vie: {player.health}\n"
          f"Nombre de victoires consecutives: {player.consecutive_wins}\n")
    if player.health < 1:
        reset_game()
    else:
        monster.reset()


def run_away():
    player.health -= 1
    if player.health < 1:
        reset_game()
    else:
        monster.reset()
        print(f"Niveau de vie: {player.health}\n")


def list_rules():
    print("Pour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l’adversaire.\n"
          "Dans ce cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire.\n"
          "Une défaite a lieu lorsque la valeur du dé lancé par l’usager"
          "est inférieure ou égale à la force de l’adversaire.\n"
          "Dans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire.\n\n"
          "La partie se termine lorsque les points de vie de l’usager tombent sous 0.\n\n"
          "L’usager peut combattre ou éviter chaque adversaire, dans le "
          "cas de l’évitement, il y a une pénalité de 1 point de vie.\n")


def quit_game():
    print("Merci et au revoir...")


def reset_game():
    print(f"La partie est terminée, vous avez vaincu {player.battles_won} monstres.")
    player.reset()
    monster.reset()


player = Player()
monster = Monster()

encounter_monster()
