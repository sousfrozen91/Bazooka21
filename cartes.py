class Pile:
    #1.
    def __init__(self):
        self.valeurs = []
        
    def affiche(self):
        '''Affiche le contenu de la pile'''
        n = len(self.valeurs)
        if n == 0:
            print('| |')
        else:
            for i in range(n):
                print('|'+ str(self.valeurs[n-1-i]) + '|')
        print('‾‾‾')
            
    
    #2.
    def est_vide(self):
        '''renvoie True si la pile est vide,
        False sinon'''
        n=len(self.valeurs)
        if n == 0 :
            return True
        else :
            return False
        
        
        pass
    
    #3.
    def empiler(self,a):
        '''Place l'élément a au sommet de la pile'''
        self.valeurs.append(a)
        
        
        pass
    
    #4.
    def depiler(self):
        '''Supprime l'élément placé au sommet de la pile
        A condition qu'elle soit non vide.
        Renvoie l'élément supprimé.'''
        assert len(self.valeurs) != 0,'La liste est vide'
        return self.valeurs.pop()
        
        
        
        pass
    
    #5.
    def sommet(self):
        '''Renvoie la valeur du sommet de la pile
        si elle est n'est pas vide
        (sans la retirer)'''
        assert len(self.valeurs) != 0,'La liste est vide'
        return self.valeurs[-1]
        
        
        
        pass
    
    #6.
    def longueur(self):
        '''Renvoie le nombre d'élément dans la pile'''
        return len(self.valeurs)
        
        
        pass
    
    #7.
    def vider(self):
        '''Vide la pile'''
        self.valeurs = []
        
        
        pass


class Joueur :
    def __init__(self,nom,argent,position):
        self.nom = nom
        self.argent = argent
        self.position = position

    def deck():
        deck = []
        
        


from random import *


cartes = [i + j for i in ['2','3','4','5','6','7','8','9','10','V','D','R','A'] for j in ["♠","♥","♦","♣"]]
cartes = cartes*8
shuffle(cartes)


jeu=Pile()
jeu.valeurs=cartes






