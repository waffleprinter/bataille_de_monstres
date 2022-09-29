import random

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
  global current_monster, monster_strength, health, battles_fought, battles_won, battles_lost
  
  print(f"""
  Adversaire: {current_monster}.
  Force de l'adversaire: {monster_strength}.
  Niveau de vie de l'usager: {health}.
  Combat {battles_fought}: {battles_won} victoires vs {battles_lost} défaites.""")
  
  player_roll = random.randint(1, 6)
  
  print(f"Lancé du dé: {player_roll}.")
  
