import tkinter as tk

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
croupier_frame = tk.Frame(root, bg="#222")
croupier_frame.grid(row=0, column=0, sticky="nsew")

croupier_label = tk.Label(
    croupier_frame,
    text="DEALER",
    font=("Arial",24, "bold"),
    fg="white",
    bg="#222"
                          )

croupier_label.pack(pady=20)

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
def bouton_clique(action):
    joueur_info.config(text=f"Joueur 1   💰 1000 — {action}")

# Boutons
btn_style = {
    "font": ("Arial", 20, "bold"),
    "fg": "white",
    "bg": "black",
    "width": 10,
    "height": 2
}

tk.Button(joueur_frame, text="Tirer",
          command=lambda: bouton_clique("Tirer"),
          **btn_style).grid(row=1, column=0, padx=10, pady=10)

tk.Button(joueur_frame, text="Rester",
          command=lambda: bouton_clique("Rester"),
          **btn_style).grid(row=1, column=1, padx=10, pady=10)

tk.Button(joueur_frame, text="Doubler",
          command=lambda: bouton_clique("Doubler"),
          **btn_style).grid(row=2, column=0, padx=10, pady=10)

tk.Button(joueur_frame, text="Split",
          command=lambda: bouton_clique("Split"),
          **btn_style).grid(row=2, column=1, padx=10, pady=10)

# Lancement
root.mainloop()
