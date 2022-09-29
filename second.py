import random

def default_stats():
    global player_health, monster_number, number_of_wins, consecutive_wins, number_of_losses, number_of_battles, recent_battle_status
    
    player_health = 20
    monster_number = 0
    number_of_wins = 0
    consecutive_wins = 0
    number_of_losses = 0
    number_of_battles = 0
    recent_battle_status = "N/A"

while True:
    current_monster_strength = random.randint(1, 5)
    
    print(f"Vous tombez face à face avec un adversaire de difficulté: {current_monster_strength}.")
    answer = int(input("Que voulez vous faire?"
                       "    1. Combattre cet adversaire."
                       "    2. Contourner cet adversaire et aller ouvrir une autre porte."
                       "    3. Afficher les règles du jeu."
                       "    4. Quitter la partie.")
                 
    if answer == 1:
          player_roll = random.randint(1, 6)
          monster_number += 1
          number_of_battles += 1
          
          print(f"Adversaire: {monster_number}."
                f"Force de l'adversaire: {current_monster_strength}."
                f"Niveau de vie de l'usager: {player_health}."
                f"Combat {number_of_battles}: {number_of_wins} victories vs {number_of_losses} defeats."
                f"Lancé du dé: {player_roll}."
                f"Dernier combat: {recent_battle_status}.")
                
          if player_roll > current_monster_strength:
                 health = health + current_monster_strength
                 number_of_wins += 1
                 consecutive_wins += 1
                 recent_battle_status = "Victory"
                 print(f"Niveau de vie: {health}."
                       f"Nombre de victoires consecutives: {consecutive_wins}.")
          else:
                 health = health - current_monster_strength
                 number_of_losses += 1
                 consecutive_wins = 0
                 recent_battle_status = "Defeat"
                 print(f"Niveau de vie: {health}."
                       if health <= 0
                           print(f"La partie est terminée, vous avez vaincu {number_of_wins} monstre(s)."
                           default_stats()
                       else:
                           continue
              
          
