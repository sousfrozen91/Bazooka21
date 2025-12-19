import tkinter as tk

# Créer la fenêtre principale
root = tk.Tk()
root.title("Interface avec Boutons")

# Fonction qui est appelée lorsqu'un bouton est cliqué
def bouton_clique(nom_bouton):
    label.config(text=f"Vous avez cliqué sur : {nom_bouton}")

# Créer un label pour afficher quel bouton a été cliqué
label = tk.Label(root, text="Que voulez-vous faire ?", font=("Arial", 14))
label.grid(row=0, column=0, columnspan=4, pady=20)

# Créer plusieurs boutons et lier chaque bouton à la fonction bouton_clique
button1 = tk.Button(root, text="Tirer", font=("Arial", 50), fg="lightblue", bg="blue", command=lambda: bouton_clique("Tirer"))
button1.grid(row=1, column=0, padx=10, pady=10)

button2 = tk.Button(root, text="Rester", font=("Arial", 50), fg="lightblue", bg="blue", command=lambda: bouton_clique("Rester"))
button2.grid(row=1, column=1, padx=10, pady=10)

button3 = tk.Button(root, text="Doubler", font=("Arial", 50), fg="lightblue", bg="blue", command=lambda: bouton_clique("Doubler"))
button3.grid(row=2, column=0, padx=10, pady=10)

button4 = tk.Button(root, text="Split", font=("Arial", 50), fg="lightblue", bg="blue", command=lambda: bouton_clique("Split"))
button4.grid(row=2, column=1, padx=10, pady=10)

# Liste des joueurs avec un nom et une somme d'argent initiale
joueurs = [
    {"nom": "j1", "jetons": 500},
    {"nom": "j2", "jetons": 500},
    {"nom": "j3", "jetons": 500},
    {"nom": "j4", "jetons": 500},
]

# Créer un Frame pour les joueurs en bas de la fenêtre
frame_joueurs = tk.Frame(root)
frame_joueurs.grid(row=3, column=0, columnspan=4, pady=20, sticky="s")

# Créer une liste pour stocker les labels des joueurs
labels_joueurs = []

# Créer des labels pour chaque joueur et les placer dans le Frame
for i, joueur in enumerate(joueurs):
    label = tk.Label(frame_joueurs, text=f"{joueur['nom']} : jetons = {joueur['jetons']}", font=("Arial", 16))
    label.grid(row=0, column=i, padx=20, pady=10)  # Placer les labels des joueurs sur une même ligne
    labels_joueurs.append(label)

# Lancer la boucle principale
root.mainloop()
