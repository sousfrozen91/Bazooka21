from random import *

class Pile: 
    def __init__(self):
        self.valeurs = []
        
    def affiche(self):
        n = len(self.valeurs)
        if n == 0:
            print('| |')
        else:
            for i in range(n):
                print('|'+ str(self.valeurs[n-1-i]) + '|')
        print('‾‾‾')
            
    def est_vide(self):
        return len(self.valeurs) == 0
    
    def empiler(self, a):
        self.valeurs.append(a)
    
    def depiler(self):
        assert len(self.valeurs) != 0, 'La liste est vide'
        return self.valeurs.pop()
    
    def sommet(self):
        assert len(self.valeurs) != 0, 'La liste est vide'
        return self.valeurs[-1]
    
    def longueur(self):
        return len(self.valeurs)
    
    def vider(self):
        self.valeurs = []


# Pas utiliser pour le moment, plus tard pour ajouter mises et plusieurs joueurs
'''
class Joueur:
    def __init__(self, nom, argent, position):
        self.nom = nom
        self.argent = argent
        self.position = position
'''


# Création du jeux de cartes
cartes = [i + j for i in ['2','3','4','5','6','7','8','9','10','V','D','R','A']
          for j in ["♠","♥","♦","♣"]]

cartes = cartes * 8   # Créer 8 jeux
shuffle(cartes)      

jeu = Pile()
jeu.valeurs = cartes



# Fonctions du Blackjack

def valeur_carte(c):
    v = c[:-1]         # Valeur sans le symbole
    if v in ["V", "D", "R"]:
        return 10
    if v == "A":
        return 11
    return int(v)

def valeur_main(main):
    total = 0
    as_count = 0

    # Additionne les valeurs des cartes de la main
    for carte in main:          
        v = valeur_carte(carte)
        total += v
        if carte[:-1] == "A":
            as_count += 1

    # Ajuste la valeur des As
    while total > 21 and as_count > 0:
        total -= 10
        as_count -= 1
    
    return total

def tirer_carte():
    return jeu.depiler()

def afficher_main(nom, main, cacher=False):
    if cacher:
        print(f"{nom}: [??] " + " ".join(main[1:]))  # Affiche toute la main sauf la première
    else:
        print(f"{nom}: {' '.join(main)}  (Total: {valeur_main(main)})")   # Affiche toute la main



# Jeu
def jouer_blackjack():
    print("\n=== DÉBUT DU BLACKJACK ===")

    # Distribution des cartes
    joueur_main = [tirer_carte(), tirer_carte()]
    croupier_main = [tirer_carte(), tirer_carte()]

    afficher_main("Croupier", croupier_main, cacher=True)
    afficher_main("Vous", joueur_main)

    # Tour du joueur 
    while True:
        choix = input("Tirer une carte ? (o/n) : ").lower()   
        if choix == "o":
            joueur_main.append(tirer_carte())
            afficher_main("Vous", joueur_main)
            if valeur_main(joueur_main) > 21:
                print(" Vous dépassez 21 ! Perdu.")
                return
        else:
            break

    # Tour du croupier
    print("\n--- Tour du croupier ---")
    afficher_main("Croupier", croupier_main)

    while valeur_main(croupier_main) < 17:
        croupier_main.append(tirer_carte())
        afficher_main("Croupier", croupier_main)

    # Scores
    score_j = valeur_main(joueur_main)
    score_c = valeur_main(croupier_main)

    print("\n=== RÉSULTAT ===")
    if score_j > 21:
        print("Vous perdez.")
    elif score_c > 21 or score_j > score_c:
        print("Vous gagnez !")
    elif score_j == score_c:
        print("Égalité.")
    else:
        print("Croupier gagne.")


# Lancer le jeu
jouer_blackjack()

