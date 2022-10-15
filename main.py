import random


class Player:
    def __init__(self, health=20, strength=random.randint(1, 6), victories=0, defeats=0, consecutive_victories=0,
                 battles_fought=0, battle_status=None):
        self.health = health
        self.strength = strength
        self.victories = victories
        self.defeats = defeats
        self.consecutive_victories = consecutive_victories
        self.battles_fought = battles_fought
        self.battle_status = battle_status

    def roll(self):
        self.strength = random.randint(1, 6)

    def reset(self):
        self.__init__()


class Monster:
    def __init__(self, strength=random.randint(1, 5)):
        self.strength = strength

    def roll(self):
        self.strength = random.randint(1, 5)


def fight_monster():
    player.battles_fought += 1
    a = 1

    print(f"Numéro adversaire: {a}.\n"
          f"Force de l'adversaire: {monster.strength}.\n"
          f"Niveau de vie de l'usager: {player.health}.\n"
          f"Combat {player.battles_fought}: {player.victories} victoires vs {player.defeats} défaites.\n\n"
          f"Lancé du dé: {player.strength}.\n")

    if player.strength > monster.strength:
        player.health += monster.strength
        player.victories += 1
        player.consecutive_victories += 1
        player.battle_status = "Victoire"

    else:
        player.health -= monster.strength
        player.defeats += 1
        player.consecutive_victories = 0
        player.battle_status = "Défaite"

    print(f"Dernier combat: {player.battle_status}.\n"
          f"Niveau de vie: {player.health}.\n"
          f"Nombre de victoires consécutives: {player.consecutive_victories}.\n")

    if player.health < 1:
        reset_game()

    player.roll()
    monster.roll()


def run_away():
    player.health -= 1

    if player.health < 1:
        reset_game()
    else:
        print(f"Niveau de vie: {player.health}")
        monster.roll()


def display_rules():
    print("Pour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l’adversaire.\n"
          "Dans ce cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire.\n"
          "Une défaite a lieu lorsque la valeur du dé lancé par l’usager est "
          "inférieure ou égale à la force de l’adversaire.\n"
          "Dans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire.\n"
          ""
          "La partie se termine lorsque les points de vie de l’usager tombent sous 0.\n"
          ""
          "L’usager peut combattre ou éviter chaque adversaire, dans le cas de "
          "l’évitement, il y a une pénalité de 1 point de vie.\n")


def quit_game():
    print("Merci et au revoir...")


def reset_game():
    print(f"La partie est terminée, vous avez vaincu {player.victories} monstre(s).")
    player.reset()
    monster.roll()


player = Player()
monster = Monster()
play_game = True

while play_game:
    boss_fight = player.victories % 3 == 0 and player.victories != 0

    if boss_fight:
        print("Vous tombez face à face avec un BOSS!\n")
    else:
        print(f"Vous tombez face à face avec un monstre de difficulté {monster.strength}")

    action = int(input("Que voulez vous faire?\n"
                       "  1. Combattre cet adversaire.\n"
                       "  2. Contourner cet adversaire et aller ouvrir une autre porte.\n"
                       "  3. Afficher les règles du jeu.\n"
                       "  4. Quitter la partie.\n"))
    if action == 1:
        if boss_fight:
            print("You fight the boss!")
        else:
            fight_monster()
    elif action == 2:
        run_away()
    elif action == 3:
        display_rules()
    else:
        quit_game()
        play_game = False
