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


class Joueur :
    def __init__(self,nom,argent,position):
        self.nom = nom
        self.argent = argent
        self.position = position

    def deck():
        deck = []
        
 

# Création du jeu de carte

cartes = [i + j for i in ['2','3','4','5','6','7','8','9','10','V','D','R','A'] for j in ["♠","♥","♦","♣"]]
cartes = cartes*8
shuffle(cartes)


jeu=Pile()
jeu.valeurs=cartes


#
def valeur_carte(c):
    v = c[:-1]     # Valeur sans symbole
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
        if carte[:-1] == "A":
            as_count += 1

    # Ajustement pour les As
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