from random import *

class Pile:
    def __init__(self):
        self.valeurs = []
        
    def affiche(self):
        # Affiche le contenu de la pile
        n = len(self.valeurs)
        if n == 0:
            print('| |')
        else:
            for i in range(n):
                print('|'+ str(self.valeurs[n-1-i]) + '|')
        print('‾‾‾')
            
    
    
    def est_vide(self):
        # Renvoie True si la pile est vide, False sinon
        n=len(self.valeurs)
        if n == 0 :
            return True
        else :
            return False

        pass
    
    
    def empiler(self,a):
        # Place l'élément a au sommet de la pile 
        self.valeurs.append(a)
        
        pass
    
    
    def depiler(self):
        # Supprime l'élément placé au sommet de la pile A condition qu'elle soit non vide. Renvoie l'élément supprimé.
        assert len(self.valeurs) != 0,'La liste est vide'
        return self.valeurs.pop()
        
        pass
    
    def sommet(self):
        # Renvoie la valeur du sommet de la pile si elle est n'est pas vide (sans la retirer)
        assert len(self.valeurs) != 0,'La liste est vide'
        return self.valeurs[-1]
            
        pass
    
    
    def longueur(self):
        # Renvoie le nombre d'élément dans la pile
        return len(self.valeurs)
        
        pass
    
    
    def vider(self):
        # Vide la pile
        self.valeurs = []
        
        pass

#------------------------------------------------------------------------------
 
# Création du jeu de carte
cartes = [i + j for i in ['2','3','4','5','6','7','8','9','10','V','D','R','A'] for j in ["♠","♥","♦","♣"]]
cartes = cartes*8    # 8 jeux
shuffle(cartes)

class Joueur :
    def __init__(self,nom,argent,position):
        self.nom = nom
        self.argent = argent
        self.position = position

    def deck():
        deck1 = cartes.depiler*2
        deck2 = cartes.depiler*2
        deck3 = cartes.depiler*2
        deck4 = cartes.depiler*2


jeu=Pile()
jeu.valeurs=cartes


# Fonctions
def valeur_carte(c):
    v = c[0]     # Valeur sans symbole
    if v in ["V", "D", "R"]:
        return 10
    if v == "A":
        return 11
    return int(v)
    
def valeur_main(main):
    total = 0
    as_count = 0

    for carte in main:
        v = valeur_carte(carte)
        total += v
        if v[0] == "A":       
            as_count += 1    #Compteur As

    # Ajustement pour les As (11 ou 1)
    while total > 21 and as_count > 0:
        total -= 10
        as_count -= 1
        
    return total    
    
def tirer_carte():
    return jeu.depiler()

def afficher_main(nom, main, cacher=False):
    if cacher:
        print(f"{nom}: [??] " + " ".join(main[1:]))
    else:
        print(f"{nom}: {' '.join(main)}  (Total: {valeur_main(main)})")



# Jeu

def jouer_blackjack():
    print("\n=== DÉBUT DU BLACKJACK ===")

    # Distribution
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
                print("Vous dépassez 21 ! Perdu.")
                return
        else:
            break

    # --- Tour du croupier ---
    print("\n--- Tour du croupier ---")
    afficher_main("Croupier", croupier_main)

    while valeur_main(croupier_main) < 17:
        croupier_main.append(tirer_carte())
        afficher_main("Croupier", croupier_main)

    # --- Résultat ---
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



