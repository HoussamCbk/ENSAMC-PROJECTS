import numpy as np
import matplotlib.pyplot as plt
from tkinter import Tk, Label, Button, StringVar, OptionMenu, Entry
from tkinter.filedialog import asksaveasfilename
from matplotlib import rcParams

#NB! ce script a été rédigé par CHOUBIK Houssam pour tracer les graphiques demandés 

# Configuration globale pour le style de police
rcParams['font.family'] = 'Times New Roman'

# Variables globales pour sauvegarder le graphique
figure = None

# Fonction pour calculer et afficher les intersections avec les noms
def tracer_graphique():
    global figure  # Pour sauvegarder la figure
    # Données d'exemple
    m = np.array([1.548,2.332,3.900])  # Force totale du poids (N)
    a = np.array([0.390, 0.580, 0.780])  # Force de glissement (N)

    # Ajustement linéaire
    coeff_main = np.polyfit(m, a, 1)  # Linear fit
    m_range = np.linspace(min(m), max(m), 100)  # Generate smooth range of x-values
    line_main = coeff_main[0] * m_range + coeff_main[1]  # Regression line equation

    # Tracé
    figure, ax = plt.subplots(figsize=(10, 6))

    # Tracer la courbe réelle
    ax.plot(m, a, linestyle='-', marker='o', color=color_var.get(), label='Courbe réelle')

    # Tracer la ligne de régression
    ax.plot(m_range, line_main, linestyle='--', color="red", label=f'Régression linéaire: y = {coeff_main[0]:.3f}m + {coeff_main[1]:.3f}')

    # Annoter chaque point avec son nom et ses coordonnées exactes
    labels = ['A', 'B', 'C']  # Noms des points
    for i in range(len(m)):
        ax.annotate(
            f"{labels[i]} ({m[i]:.3f}, {a[i]:.3f})",  # Texte annoté avec le nom et les coordonnées
            (m[i], a[i]),  # Position du point
            textcoords="offset points",
            xytext=(10, -10),  # Décalage pour éviter le chevauchement
            ha='center',
            fontsize=10
        )

    # Ajouter le titre et personnaliser les couleurs
    ax.set_title(title_var.get(), color=title_color_var.get())
    ax.set_xlabel('Force totale du poids (N)', color=axes_color_var.get())
    ax.set_ylabel('Force de glissement (N)', color=axes_color_var.get())

    # Légende et grille
    ax.legend()
    ax.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

    # Afficher le graphique
    plt.show()

# Fonction pour sauvegarder le graphique en PNG
def sauvegarder_graphique():
    global figure
    if figure is not None:
        # Ouvrir le sélecteur de fichiers pour choisir l'emplacement et le nom
        file_path = asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG files", "*.png"), ("All files", "*.*")],
            title="Enregistrer le graphique sous"
        )
        if file_path:  # Vérifier que l'utilisateur n'a pas annulé
            figure.savefig(file_path)
            print(f"Graphique sauvegardé sous: {file_path}")
    else:
        print("Veuillez d'abord tracer un graphique.")

# Création de la fenêtre Tkinter
root = Tk()
root.title("Personnalisation du graphique")

# Variables pour les options
color_var = StringVar(value="blue")  # Couleur de la courbe réelle
title_var = StringVar(value="Courbe Metal-Metal Force de glissement")  # Titre du graphique
title_color_var = StringVar(value="black")  # Couleur du titre
axes_color_var = StringVar(value="black")  # Couleur des axes

# Interface utilisateur
Label(root, text="Choisissez une couleur pour la courbe réelle:").pack(pady=5)
colors = ["blue", "red", "green", "orange", "purple", "black", "cyan"]
OptionMenu(root, color_var, *colors).pack(pady=5)

Label(root, text="Entrez le titre du graphique:").pack(pady=5)
Entry(root, textvariable=title_var).pack(pady=5)

Label(root, text="Choisissez une couleur pour le titre:").pack(pady=5)
OptionMenu(root, title_color_var, *colors).pack(pady=5)

Label(root, text="Choisissez une couleur pour les axes:").pack(pady=5)
OptionMenu(root, axes_color_var, *colors).pack(pady=5)

# Boutons pour tracer et sauvegarder le graphique
Button(root, text="Tracer le graphique", command=tracer_graphique).pack(pady=10)
Button(root, text="Télécharger le graphique", command=sauvegarder_graphique).pack(pady=10)

# Lancer l'application Tkinter
root.mainloop()
