# Pouilleux / Old Maid — Python CLI

![Python](https://img.shields.io/badge/Python-3.10%2B-informational)
![Type](https://img.shields.io/badge/Type-CLI-blue)
![Lang FR](https://img.shields.io/badge/Lang-FR%20(prompts)-blue)
![Status](https://img.shields.io/badge/Status-Prototype-yellow)

> 🇫🇷 **Code et interactions (prompts) en français.**  
> 🇬🇧 **Codebase & UI messages are in French.**

---

## Français

**Pouilleux (Old Maid)** en ligne de commande, version simplifiée à **2 joueurs** (Humain vs Robot).  
Le paquet contient **51 cartes** (valet de trèfle retiré). Les **paires** (même **valeur**, couleur ignorée) sont défaussées.  
Le joueur qui termine avec la dernière carte (le **pouilleux**) **perd**.

### Règles (résumé)
- Mélange du paquet.
- Distribution alternée : l’Humain reçoit la 1ʳᵉ carte, le Robot la 2ᵉ (→ avec 51 cartes : **Humain 26**, **Robot 25**).
- À chaque tour :
  - **Humain** choisit une **position** parmi les cartes du Robot (valeurs cachées).
  - **Robot** choisit **au hasard** une carte parmi celles de l’Humain.
  - Après chaque prise, on **défausse les paires par valeur** (couleur ignorée) et on **mélange** la main.
- Fin : quand un des joueurs n’a plus de cartes. L’autre perd s’il reste avec le pouilleux.

### Extrait d’exécution
Bonjour. Je m'appelle Robot et je distribue les cartes.
Votre main de cartes est:
7♣ 9♠ 10♦ 9♣ 8♦ A♠
Ne vous inquiétez pas, je ne peux pas voir vos cartes ni leur ordre.
Maintenant défaussez toutes les paires de votre main. Je vais le faire moi aussi.
Appuyez Enter pour continuer.


### Prérequis
- Python **3.10+** (testé avec 3.12)

### Installation (optionnelle : environnement virtuel)
```bash
python -m venv .venv
# Windows PowerShell
.venv\Scripts\Activate.ps1
# macOS / Linux
source .venv/bin/activate


### Lancez le jeu
python pouilleux.py

---


### English

Command-line Old Maid in Python, simplified to 2 players (Human vs Robot).
Deck has 51 cards (club jack removed). Pairs (same rank, suit ignored) are discarded.
The player who ends with the last card (the old maid) loses.

### Rules (summary)

Shuffle the deck.

Alternate dealing: Human gets the 1st card, Robot the 2nd (→ with 51 cards: Human 26, Robot 25).

Each turn:

Human picks a position among Robot’s face-down cards.

Robot randomly picks one from Human’s hand.

After each pick, discard pairs by rank (suit ignored) and shuffle the hand.

End: when one player has no cards left; the other loses if holding the old maid.

### Run
python pouilleux.py
