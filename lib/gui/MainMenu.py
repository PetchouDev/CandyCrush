import sys
import ctypes
from tkinter import *
from tkinter.ttk import Combobox

from PIL import Image, ImageTk

from lib.gui.Settings import open_settings
from lib.manager import MANAGER, DEFAULT_IMG_DIR



# Demander à l'utilisateur de choisir la taille de la grille, avec des menus déroulants de 4 à 10
class MainMenu(Tk):
    def __init__(self, last_options):
        """Initialisation de la fenêtre"""
        super().__init__()
        self.title("Candy Crush")
        self.resizable(False, False)

        # appliquation du theme
        self.theme = MANAGER.get("THEME")
        theme_path = DEFAULT_IMG_DIR.parent / "engine" 
        self.tk.call("source", theme_path / "theme.tcl")
        self.tk.call("set_theme", self.theme.lower())

        # récupérer les dernières options de jeu en tant que valeurs par défaut
        self.last_x = last_options[0]
        self.last_y = last_options[1]
        self.last_rule = last_options[2]

        # ajouter l'icon
        self.wm_iconphoto(False, ImageTk.PhotoImage(Image.open(DEFAULT_IMG_DIR / "SuperCandy.png")))

        # titre
        self.label = Label(self, text="options de jeu", font=("Arial", 20, "bold", "underline"))
        self.label.pack(pady=10)

        # grille de positionnement
        self.frame = Frame(self)
        self.frame.pack()

        # initialiser les menus déroulants
        self.x = IntVar()
        self.y = IntVar()

        self.x.set(self.last_x)
        self.y.set(self.last_y)

        # création des menus déroulants
        self.x_label = Label(self.frame, text="Largeur", font=("Arial", 15))
        self.y_label = Label(self.frame, text="Hauteur", font=("Arial", 15))
        

        self.x_menu = Combobox(self.frame, textvariable=self.x, values=[i for i in range(4, MANAGER.get("MAX_WIDTH") + 1)])
        self.y_menu = Combobox(self.frame, textvariable=self.y, values=[i for i in range(4, MANAGER.get("MAX_HEIGTH") + 1)])

        self.x_label.grid(row=0, column=0, padx=10, pady=10)
        self.y_label.grid(row=1, column=0, padx=10, pady=10)

        self.x_menu.grid(row=0, column=1, padx=10, pady=10)
        self.y_menu.grid(row=1, column=1, padx=10, pady=10)

        # règle du jeu à utiliser
        self.rule = IntVar()
        self.rule.set(self.last_rule)
        self.rule_menu = Combobox(self.frame, textvariable=self.rule, values=[i for i in range(1, 4)])
        self.rule_label = Label(self.frame, text="Règle du jeu", font=("Arial", 15))
        self.rule_label.grid(row=2, column=0, padx=10, pady=10) 
        self.rule_menu.grid(row=2, column=1, padx=10, pady=10)

        # afficher une icone d'info pour expliquer les règles à coté du menu déroulant
        self.info_img = ImageTk.PhotoImage(Image.open(DEFAULT_IMG_DIR / "infos.png").resize((20, 20)))
        color = "#ffffff" if MANAGER.get("THEME") == "Light" else "#333333"
        print(color)
        self.info_button = Button(self.frame, image=self.info_img, command=self.show_rules, highlightthickness=0, bd=0, bg=color)
        self.info_button.grid(row=2, column=2, padx=10, pady=10)

        # bouton paramètres
        self.settings_button = Button(self, text="Paramètres", command=open_settings, font=("Arial", 12, "bold"))
        self.settings_button.pack(pady=12, padx=0)

        self.button = Button(self, text="Jouer", command=self.check_options, font=("Arial", 12, "bold"))
        self.button.pack(pady=8, fill=X, padx=30)

        # quitter par la croix
        self.protocol("WM_DELETE_WINDOW", sys.exit)

    def get_game_settings(self):
        """Afficher la fenêtre et récupérer les options de jeu"""
        self.mainloop()
        return self.options
        
    def check_options(self):
        """Vérifier que les options de jeu sont valides"""
        try:
            # vérifier que les options de jeu sont valides (type de valeur, et si la valeur est autorisée)
            self.options = max(min(self.x.get(), MANAGER.get("MAX_HEIGTH")), 4), max(min(self.y.get(), MANAGER.get("MAX_WIDTH")), 4), min(max(self.rule.get(), 1), 3)
            self.destroy()
        except:
            # affiche le message d'erreur puis lance la partie avec la dernière taille valide
            text = "La taille de la grille est invalide, utilisation de la dernière taille valide."
            error_message = Toplevel()
            error_message.title("Erreur")
            error_message.resizable(False, False)
            Label(error_message, text=text).pack(pady=10)
            Button(error_message, text="Fermer", command=self.destroy).pack(pady=10)
            self.options = self.last_x, self.last_y, self.last_rule

            error_message.mainloop()
            self.destroy()



    def show_rules(self):
        # afficher les règles du jeu
        rules = Toplevel()
        rules.title("Règles du jeu")
        Label(rules, text="Règles du jeu :", font=("Arial", 20, "bold", "underline")).pack(pady=10)
        Label(rules, text="1. Alignement de 3 bonbons supprime ces bonbons").pack(pady=10)
        Label(rules, text="2. Alignement de 3 bonbons ou plus supprime ces bonbons").pack(pady=10)
        Label(rules, text="3. Alignement de 3 bonbons ou plus supprime ces bonbons, et tous ceux adjacent de la même couleur").pack(pady=10)
        Button(rules, text="Fermer", command=rules.destroy).pack(pady=10)


        rules.mainloop()
