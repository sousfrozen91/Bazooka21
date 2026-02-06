import tkinter as tk
from random import *
from PIL import Image, ImageTk


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


# Pas utiliser pour le moment, plus tard pour ajouter mises 
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

#-----------TKINTER-----------------------

# Fenêtre principale
root = tk.Tk()
root.title("Bazooka21")
root.geometry("1200x800")
root.state("zoomed")  # plein écran 
root.configure(bg="#0b5d1e")

# Permet d'occuper tout l'espace
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=3)
root.rowconfigure(2, weight=2)
root.columnconfigure(0, weight=1)

# ---------------- CROUPIER ----------------
croupier_frame = tk.Frame(root, bg="#0b5d1e")
croupier_frame.grid(row=0, column=0, sticky="nsew")

croupier_label = tk.Label(
    croupier_frame,
    text="DEALER",
    font=("Arial",24, "bold"),
    fg="white",
    bg="#222"
                          )

jeu_label = tk.Label(
    croupier_frame,
    text='Que voulez-vous faire ?',
    font=("Arial",24, "bold"),
    fg="white",
    bg="#222"
    )

croupier_label.pack(pady=20)
jeu_label.pack(pady=60)

# ---------------- TABLE ----------------
table_frame = tk.Frame(root, bg="#0b5d1e")
table_frame.grid(row=1, column=0, sticky="nsew")

# ---------------- JOUEUR ----------------
joueur_frame = tk.Frame(root, bg="#111")
joueur_frame.grid(row=2, column=0, sticky="nsew")
joueur_frame.columnconfigure((0, 1), weight=1)

joueur_info = tk.Label(
    joueur_frame,
    text="Joueur 1   💰 1000",
    font=("Arial", 20),
    fg="gold",
    bg="#111"
)
joueur_info.grid(row=0, column=0, columnspan=2, pady=10)

# Action quand bouton cliqué
'''def bouton_clique(action):
    joueur_info.config(text=f"Joueur 1   💰 1000 — {action}")''' 

# Boutons
btn_style = {
    "font": ("Arial", 20, "bold"),
    "fg": "white",
    "bg": "black",
    "width": 100,
    "height": 2
}


buttonClicked = False

def changeValue():
    global buttonClicked
    buttonClicked = not buttonClicked
    jeu_label['text'] = "Vous avez tiré"

def bouton_clique(action):
    global etat
    etat = "croupier"

    while valeur_main(croupier_main) < 17:
        croupier_main.append(tirer_carte())

    maj_affichage()

    if valeur_main(croupier_main) > 21 or valeur_main(joueur_main) > valeur_main(croupier_main):
        fin_partie("Gagné ")
    elif valeur_main(joueur_main) < valeur_main(croupier_main):
        fin_partie("Perdu ")
    else:
        fin_partie("Égalité ")

  
#afficher une image 
image = Image.open("U:/NSI/Bazooka21/dos de carte.png")
image = image.resize((200, 300))

photo = ImageTk.PhotoImage(image)
label = tk.Label(table_frame, image=photo)
label.image = photo 
label.pack()    
 
 
#----------------JOUER--------------------- 
 
etat = "joueur"
joueur_main = []
croupier_main = []

def action_tirer():
    if etat != "joueur":
        return
    joueur_main.append(tirer_carte())
    maj_affichage()
    if valeur_main(joueur_main) > 21:
        fin_partie("Perdu !")

tk.Button(
    joueur_frame,
    text="Tirer",
    command=action_tirer,   # important
    **btn_style
).grid(row=1, column=0, padx=10, pady=10)

tk.Button(
    joueur_frame,
    text="Rester",
    command=lambda: bouton_clique("Rester"),
    **btn_style
).grid(row=1, column=1, padx=10, pady=10)


def nouvelle_partie():
    global joueur_main, croupier_main, etat

    # Sécurité : reshuffle si le paquet est presque vide
    if jeu.longueur() < 20:
        jeu.vider()
        cartes = [i + j for i in ['2','3','4','5','6','7','8','9','10','V','D','R','A']
                  for j in ["♠","♥","♦","♣"]] * 8
        shuffle(cartes)
        jeu.valeurs = cartes

    joueur_main = [tirer_carte(), tirer_carte()]
    croupier_main = [tirer_carte(), tirer_carte()]
    etat = "joueur"

    maj_affichage()

tk.Button(
    joueur_frame,
    text="Rejouer",
    font=("Arial", 16),
    command=nouvelle_partie,
    bg="#444",
    fg="white"
).grid(row=2, column=0, columnspan=2, pady=15)


def maj_affichage():
    jeu_label.config(
        text=f"Vous : {valeur_main(joueur_main)} | "f"Croupier : {valeur_main(croupier_main) if etat=='fin' else '?? + ' + str(valeur_carte(croupier_main[0])) }")

def fin_partie(message):
    global etat
    etat = "fin"
    jeu_label.config(text=message)

# Lancement
nouvelle_partie()
root.mainloop()

