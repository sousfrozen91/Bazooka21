import tkinter as tk

# Fonction qui est appelée lorsqu'un bouton est cliqué
def bouton_clique(nom_bouton):
    label.config(text=f"Vous avez cliqué sur : {nom_bouton}")

# Créer la fenêtre principale
root = tk.Tk()
root.title("Interface avec Boutons")

# Créer un label pour afficher quel bouton a été cliqué
label = tk.Label(root, text="Que voulez-vous faire ?", font=("Arial", 14))
label.pack(pady=20)


# Créer un Frame pour contenir les boutons
frame = tk.Frame(root)
frame.pack(pady=10)


# Créer plusieurs boutons et lier chaque bouton à la fonction bouton_clique
button1 = tk.Button(frame, text="Tirer", font=("Arial", 50), command=lambda: bouton_clique("Tirer"))
button1.pack(side=tk.LEFT, padx=10)

button2 = tk.Button(frame, text="Rester", font=("Arial", 50), command=lambda: bouton_clique("Rester"))
button2.pack(side=tk.LEFT, padx=10)

button3 = tk.Button(frame, text="Doubler", font=("Arial", 50), command=lambda: bouton_clique("Doubler"))
button3.pack(side=tk.LEFT, padx=10)

button4 = tk.Button(frame, text="Split", font=("Arial", 50), command=lambda: bouton_clique("Split"))
button4.pack(side=tk.LEFT, padx=10)

# Lancer la boucle principale
root.mainloop()
