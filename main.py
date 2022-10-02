import random


class Player:
    health = 20
    strength = random.randint(1, 6)
    battles_fought = 0
    battles_won = 0
    battles_lost = 0
    consecutive_wins = 0
    recent_battle_status = None

    def reroll(self):
        self.strength = random.randint(1, 6)

    def die(self):
        print(f"La partie est terminée, vous avez vaincu {player.battles_won} monstres.\n")
        monster.reroll()
        player.reset()

    def reset(self):
        self.health = 20
        self.strength = random.randint(1, 6)
        self.battles_fought = 0
        self.battles_won = 0
        self.battles_lost = 0
        self.consecutive_wins = 0
        self.recent_battle_status = None


class Monster:
    def __init__(self):
        self.strength = random.randint(1, 5)

    def reroll(self):
        self.strength = random.randint(1, 5)


def encounter_monster():
    print(f"Vous tombez face à face avec un monstre de difficulté {monster.strength}.")

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

    print(f"Numéro adversaire: {player.battles_fought}.\n"
          f"Force de l'adversaire: {monster.strength}.\n"
          f"Niveau de vie de l'usager: {player.health}.\n"
          f"Combat {player.battles_fought}: {player.battles_won} victoires vs {player.battles_lost} défaites.\n\n"
          f"Lancé du dé: {player.strength}.")

    if player.strength <= monster.strength:
        player.health -= monster.strength
        player.battles_lost += 1
        player.consecutive_wins = 0
        print("Dernier combat: Défaite.\n"
              f"Niveau de vie: {player.health}.\n")
        if player.health < 1:
            player.die()
    else:
        player.health += monster.strength
        player.battles_won += 1
        player.consecutive_wins += 1
        print("Dernier combat: Victoire.\n"
              f"Niveau de vie: {player.health}.\n"
              f"Nombre de victoires consécutives: {player.consecutive_wins}.\n")

    player.reroll()
    monster.reroll()


def run_away():
    player.health -= 1

    if player.health < 1:
        player.die()
    else:
        print(f"Niveau de vie: {player.health}")
        monster.reroll()


def list_rules():
    print("Pour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l’adversaire.\n"
          "Dans ce cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire.\n"
          "Une défaite a lieu lorsque la valeur du dé lancé par l’usager est "
          "inférieure ou égale à la force de l’adversaire.\n"
          "Dans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire.\n\n"
          "La partie se termine lorsque les points de vie de l’usager tombent sous 0.\n\n"
          "L’usager peut combattre ou éviter chaque adversaire, dans le cas de "
          "l’évitement, il y a une pénalité de 1 point de vie.\n")


def quit_game():
    print("Merci et au revoir...")


player = Player()
monster = Monster()

encounter_monster()
