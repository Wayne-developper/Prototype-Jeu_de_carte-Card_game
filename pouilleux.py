# Jeu de cartes appelé "Pouilleux" 

# L'ordinateur est le donneur des cartes.

# Une carte est une chaine de 2 caractères. 
# Le premier caractère représente une valeur et le deuxième une couleur.
# Les valeurs sont des caractères comme '2','3','4','5','6','7','8','9','10','J','Q','K', et 'A'.
# Les couleurs sont des caractères comme : ♠, ♡, ♣, et ♢.
# On utilise 4 symboles Unicode pour représenter les 4 couleurs: pique, coeur, trèfle et carreau.
# Pour les cartes de 10 on utilise 3 caractères, parce que la valeur '10' utilise deux caractères.

import random

def attend_le_joueur():
    '''()->None
    Pause le programme jusqu'au l'usager appui Enter
    '''
    try:
         input("Appuyez Enter pour continuer. ")
    except SyntaxError:
         pass


def prepare_paquet():
    '''()->list of str
        Retourne une liste des chaines de caractères qui représente tous les cartes,
        sauf le valet noir.
    '''
    paquet=[]
    couleurs = ['\u2660', '\u2661', '\u2662', '\u2663']
    valeurs = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    for val in valeurs:
        for couleur in couleurs:
            paquet.append(val+couleur)
    paquet.remove('J\u2663') # élimine le valet noir (le valet de trèfle)
    return paquet

def melange_paquet(p):
    '''(list of str)->None
       Melange la liste des chaines des caractères qui représente le paquet des cartes    
    '''
    random.shuffle(p)

def donne_cartes(p):
     '''(list of str)-> tuple of (list of str,list of str)

     Retournes deux listes qui représentent les deux mains des cartes.  
     Le donneur donne une carte à l'autre joueur, une à lui-même,
     et ça continue jusqu'à la fin du paquet p.
     '''
     
     donneur=[]
     autre=[]


     # COMPLETEZ CETTE FONCTION EN CONFORMITE AVEC LA DESCRIPTION CI-DESSUS
     # AJOUTEZ VOTRE CODE ICI
     for i in range(0, len(p), 2):
         autre.append(p[i])
         if i + 1 < len(p):
             donneur.append(p[i+1])
     
     return (donneur, autre)


def elimine_paires(l):
    '''
     (list of str)->list of str

     Retourne une copy de la liste l avec tous les paires éliminées 
     et mélange les éléments qui restent.

     Test:
     (Notez que l'ordre des éléments dans le résultat pourrait être différent)
     
     >>> elimine_paires(['9♠', '5♠', 'K♢', 'A♣', 'K♣', 'K♡', '2♠', 'Q♠', 'K♠', 'Q♢', 'J♠', 'A♡', '4♣', '5♣', '7♡', 'A♠', '10♣', 'Q♡', '8♡', '9♢', '10♢', 'J♡', '10♡', 'J♣', '3♡'])
     ['10♣', '2♠', '3♡', '4♣', '7♡', '8♡', 'A♣', 'J♣', 'Q♢']
     >>> elimine_paires(['10♣', '2♣', '5♢', '6♣', '9♣', 'A♢', '10♢'])
     ['2♣', '5♢', '6♣', '9♣', 'A♢']
    '''

    resultat=[]


    # COMPLETEZ CETTE FONCTION EN CONFORMITE AVEC LA DESCRIPTION CI-DESSUS
    # AJOUTEZ VOTRE CODE ICI
     
    reste = {}
    for carte in l:
        v = carte[:-1]
        if v in reste:
            del reste[v]
        else:
            reste[v] = carte
            
    resultat = list(reste.values())

    random.shuffle(resultat)
    return resultat


def affiche_cartes(p):
    '''
    (list)-None
    Affiche les éléments de la liste p séparées par d'espaces
    '''


    # COMPLETEZ CETTE FONCTION EN CONFORMITE AVEC LA DESCRIPTION CI-DESSUS
    # AJOUTEZ VOTRE CODE ICI
    print(" ".join(p))

    

def entrez_position_valide(n):
     '''
     (int)->int
     Retourne un entier du clavier, de 1 à n (1 et n inclus).
     Continue à demander si l'usager entre un entier qui n'est pas dans l'intervalle [1,n]
     
     Précondition: n>=1
     '''

     # COMPLETEZ CETTE FONCTION EN CONFORMITE AVEC LA DESCRIPTION CI-DESSUS
     # AJOUTEZ VOTRE CODE ICI
     while True:
         s = input(f"SVP entrez un entier de 1 à {n}: ")
         try:
             pos = int(s)
             if 1 <= pos <= n:
                 return pos
             else:
                 print(f"Position invalide. SVP entrez un entier de 1 à {n}.")
         except ValueError:
             print(f"Position invalide. SVP entrez un entier de 1 à {n}.")
    
        
     

def joue():
     '''()->None
     Cette fonction joue le jeu'''
    
     p=prepare_paquet()
     melange_paquet(p)
     tmp=donne_cartes(p)
     donneur=tmp[0]
     humain=tmp[1]

     print("Bonjour. Je m'appelle Robot et je distribue les cartes.")
     print("Votre main est:")
     affiche_cartes(humain)
     print("Ne vous inquiétez pas, je ne peux pas voir vos cartes ni leur ordre.")
     print("Maintenant défaussez toutes les paires de votre main. Je vais le faire moi aussi.")
     attend_le_joueur()
     
     donneur=elimine_paires(donneur)
     humain=elimine_paires(humain)

     # COMPLETEZ CETTE FONCTION EN CONFORMITE AVEC LA DESCRIPTION CI-DESSUS
     # AJOUTEZ VOTRE CODE ICI
     tour = 1
     while True:
         if len(humain) == 0:
             print("J'ai terminé toutes les cartes.")
             print("Vous avez perdu! Moi, Robot, j'ai gagné.")
             break
         if len(donneur) == 0:
             print("J'ai terminé toutes les cartes.")
             print("Félicitation! Vous, Humain, vous avez gagné.")
             break
         if tour == 1:
             print("***********************************************************")
             print("Votre tour.")
             print("Votre main est:")
             affiche_cartes(humain)
             n = len(donneur)
             print(f"J'ai {n} cartes. Si 1 est la position de ma première carte et")
             print(f"{n} la position de ma dernière carte, laquelle de mes cartes voulez-vous?")
             pos = entrez_position_valide(n)      # 1..n
             carte_prise = donneur.pop(pos - 1)
             print(f"Vous avez demandé ma {pos}e carte.")
             print(f"La voilà. C'est un {carte_prise}")
             humain.append(carte_prise)

             print("Avec", carte_prise, "ajouté, votre main est:")
             affiche_cartes(humain)

             humain = elimine_paires(humain)
             print("Après avoir défaussé toutes les paires et mélangé les cartes, votre main est:")
             affiche_cartes(humain)
             attend_le_joueur()

             tour = 0
             
         else:
             print("***********************************************************")
             print("Mon tour.")
             k = random.randrange(1, len(humain) + 1)
             print(f"J'ai pris votre {k}ème carte.")
             carte_prise = humain.pop(k - 1)
             donneur.append(carte_prise)

             donneur = elimine_paires(donneur)
             attend_le_joueur()

             tour = 1
            
            
    

	 
# programme principale
joue()

