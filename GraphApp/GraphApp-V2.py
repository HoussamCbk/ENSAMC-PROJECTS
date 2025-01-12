import numpy as np
import matplotlib.pyplot as plt
from tkinter import Tk, Label, Button, StringVar, OptionMenu, Entry, Text, END
from tkinter.filedialog import asksaveasfilename
from matplotlib import rcParams

# Configure global font style
rcParams['font.family'] = 'Times New Roman'

# Global variable to hold the figure
figure = None

# Function to parse user input into numpy arrays
def parse_input(input_text):
    try:
        # Convert the input string to a numpy array
        data = [float(x) for x in input_text.split(",")]
        return np.array(data)
    except ValueError:
        print("Erreur: Veuillez entrer des nombres valides séparés par des virgules.")
        return None

# Function to plot the graph
def tracer_graphique():
    global figure
    # Get user inputs for X and Y data
    x_text = x_entry.get("1.0", END).strip()
    y_text = y_entry.get("1.0", END).strip()

    # Parse the inputs
    x = parse_input(x_text)
    y = parse_input(y_text)

    # Ensure inputs are valid and of the same length
    if x is None or y is None or len(x) != len(y):
        print("Erreur: Assurez-vous que les deux listes sont de longueur égale et valides.")
        return

    # Perform linear regression
    coeff_main = np.polyfit(x, y, 1)
    x_range = np.linspace(min(x), max(x), 100)
    line_main = coeff_main[0] * x_range + coeff_main[1]

    # Plot the graph
    figure, ax = plt.subplots(figsize=(10, 6))
    ax.plot(x, y, linestyle='-', marker='o', color=color_var.get(), label='Courbe réelle')
    ax.plot(x_range, line_main, linestyle='--', color="red",
            label=f'Régression linéaire: y = {coeff_main[0]:.3f}x + {coeff_main[1]:.3f}')

    # Annotate points
    for i in range(len(x)):
        ax.annotate(f"({x[i]:.3f}, {y[i]:.3f})", (x[i], y[i]), textcoords="offset points",
                    xytext=(10, -10), ha='center', fontsize=10)

    # Set title and labels with user customization
    ax.set_title(title_var.get(), color=title_color_var.get())
    ax.set_xlabel(x_label_var.get(), color=axes_color_var.get())
    ax.set_ylabel(y_label_var.get(), color=axes_color_var.get())

    # Add legend and grid
    ax.legend()
    ax.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

    # Display the plot
    plt.show()

# Function to save the graph
def sauvegarder_graphique():
    global figure
    if figure is not None:
        file_path = asksaveasfilename(defaultextension=".png",
                                      filetypes=[("PNG files", "*.png"), ("All files", "*.*")],
                                      title="Enregistrer le graphique sous")
        if file_path:
            figure.savefig(file_path)
            print(f"Graphique sauvegardé sous: {file_path}")
    else:
        print("Veuillez d'abord tracer un graphique.")

# Tkinter GUI setup
root = Tk()
root.title("Personnalisation du graphique")

# Variables for options
color_var = StringVar(value="blue")
title_var = StringVar(value="Graphique personnalisé")
title_color_var = StringVar(value="black")
axes_color_var = StringVar(value="black")
x_label_var = StringVar(value="Axe X")
y_label_var = StringVar(value="Axe Y")

# Interface components
Label(root, text="Entrez les valeurs pour l'axe X séparées par des virgules:").pack(pady=5)
x_entry = Text(root, height=3, width=40)
x_entry.pack(pady=5)

Label(root, text="Entrez les valeurs pour l'axe Y séparées par des virgules:").pack(pady=5)
y_entry = Text(root, height=3, width=40)
y_entry.pack(pady=5)

Label(root, text="Choisissez une couleur pour la courbe réelle:").pack(pady=5)
colors = ["blue", "red", "green", "orange", "purple", "black", "cyan"]
OptionMenu(root, color_var, *colors).pack(pady=5)

Label(root, text="Entrez le titre du graphique:").pack(pady=5)
Entry(root, textvariable=title_var).pack(pady=5)

Label(root, text="Entrez le nom de l'axe X:").pack(pady=5)
Entry(root, textvariable=x_label_var).pack(pady=5)

Label(root, text="Entrez le nom de l'axe Y:").pack(pady=5)
Entry(root, textvariable=y_label_var).pack(pady=5)

Label(root, text="Choisissez une couleur pour le titre:").pack(pady=5)
OptionMenu(root, title_color_var, *colors).pack(pady=5)

Label(root, text="Choisissez une couleur pour les axes:").pack(pady=5)
OptionMenu(root, axes_color_var, *colors).pack(pady=5)

# Buttons
Button(root, text="Tracer le graphique", command=tracer_graphique).pack(pady=10)
Button(root, text="Télécharger le graphique", command=sauvegarder_graphique).pack(pady=10)

# Run the Tkinter application
root.mainloop()
