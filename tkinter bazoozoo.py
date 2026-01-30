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

def afficher_main(nom, main, cacher=False):
    if cacher:
        print(f"{nom}: [??] " + " ".join(main[1:]))  # Affiche toute la main sauf la première
    else:
        print(f"{nom}: {' '.join(main)}  (Total: {valeur_main(main)})")   # Affiche toute la main




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
    jeu_label['text'] = "Vous avez choisi de rester"

tk.Button(
    joueur_frame,
    text="Tirer",
    command=lambda: (changeValue(), tirer_carte()),
    **btn_style
).grid(row=1, column=0, padx=10, pady=10)


tk.Button(
    joueur_frame,
    text="Rester",
    command=lambda: bouton_clique("Rester"),
    **btn_style
).grid(row=1, column=1, padx=10, pady=10)
    
#afficher une image 
image = Image.open("U:/NSI/Bazooka21/dos de carte.png")
image = image.resize((200, 300))

photo = ImageTk.PhotoImage(image)
label = tk.Label(table_frame, image=photo)
label.image = photo 
label.pack()    
     
# Jeu
def jouer_blackjack():

    # Distribution des cartes
    joueur_main = [tirer_carte(), tirer_carte()]
    croupier_main = [tirer_carte(), tirer_carte()]

    afficher_main("Croupier", croupier_main, cacher=True)
    afficher_main("Vous", joueur_main)

    # Tour du joueur 
    while True:
        jeu_label['text'] = 'Que voulez vous faire ?'
        
        if buttonClicked == True:
            jeu_label['text'] = "Vous avez tiré"
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

# Lancement
root.mainloop()


