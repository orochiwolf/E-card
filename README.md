# 🎴 E-Card Game (Kaiji) — Python Console Version

Une implémentation du jeu **E-Card** inspiré de l’anime *Kaiji*, écrite en **Python** et jouable directement dans la console.

## 📖 Règles du jeu

- Deux joueurs s’affrontent :
  - **Player 1** : possède la carte *Emperor* et des *Citizens*.
  - **Player 2** : possède la carte *Slave* et des *Citizens*.
- Chaque joueur choisit une carte à chaque manche.
- Les cartes sont comparées selon ces règles :
  - **Emperor bat Citizen** (+1 point pour Player 1)  
  - **Citizen bat Slave** (+1 point pour Player 1)  
  - **Slave bat Emperor** (+1 point pour Player 1)  
  - **Emperor perd contre Slave** (+5 points pour Player 2)  
  - **Citizen perd contre Emperor** (+5 points pour Player 2)  
  - **Slave perd contre Citizen** (+5 points pour Player 2)  
  - **Même carte** → Match nul (pas de points)

## 🕹️ Fonctionnement

- Le jeu se joue sur **12 manches maximum**.
- Après chaque victoire, les mains sont réinitialisées.
- Le score est affiché après chaque manche.
- À la fin, le programme affiche le gagnant.

## 🚀 Lancer le jeu

1. Assurez-vous d’avoir **Python 3** installé sur votre machine.
2. Clonez ce repository :
   ```bash
   git clone https://github.com/ton-compte/ecard-kaiji.git
   cd ecard-kaiji```
3. Exécutez le script :
    ``` python E-card.py```

