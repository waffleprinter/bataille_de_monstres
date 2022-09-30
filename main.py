import random


class Player:
    health = 20
    battles_won = 0
    battles_lost = 0
    
    def reset(self):
        health = 20
        battles_won = 0
        battles_lost = 0

class Monster:
    def __init__(self, strength=None):
        self.strength = strength if strength else random.randint(1, 5)

    def reset(self, strength=None):
        self.strength = strength if strength else random.randint(1, 5)


def encounter_monster():
    print(f"Vous tombez face à face avec un adversaire de difficulté {monster.strength}")
    action = int(input("Que voulez vous faire?:\n"
                       "  1. Combattre cet adversaire.\n"
                       "  2. Contourner cet adversaire et aller ouvrir une autre porte.\n"
                       "  3. Afficher les règles du jeu.\n"
                       "  4. Quitter la partie.\n"))

    if action == 1:
        print("You fight the monster!")
        
    elif action == 2:
        run_away()
        encounter_monster()
        
    elif action == 3:
        list_rules()
        encounter_monster()
        
    else:
        quit_game()


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
