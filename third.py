import random

health = 0
battles_fought = 0
battles_won = 0
battles_lost = 0
consecutive_battles_won = 0

def encounter_monster():
  global monster_strength
  monster_strength = random.randint(1, 5)
  print(f"Vous tombez face à face avec un adversaire de difficulté {monster_strength}.")
  
  action == int(input("""
  Que voulez-vous faire?
      1- Combattre cet adversaire
      2- Contourner cet adversaire et aller ouvrir une autre porte
      3- Afficher les règles du jeu
      4- Quitter la partie"""))


def fight_monster():
  global current_monster, monster_strength, health, battles_fought, battles_won, battles_lost, consecutive_battles_won
  
  player_roll = random.randint(1, 6)
  battles_fought += 1
  current_monster += 1
  
  print(f"""
  Adversaire: {current_monster}.
  Force de l'adversaire: {monster_strength}.
  Niveau de vie de l'usager: {health}.
  Combat {battles_fought}: {battles_won} victoires vs {battles_lost} défaites.
  
  Lancé du dé: {player_roll}.""")
  
  if player_roll > monster_strength:
    recent_battle_status = "Victoire"
  else:
    recent_battle_status = "Défaite"
  print(f"Dernier combat: {recent_battle_status}.")
  
    
