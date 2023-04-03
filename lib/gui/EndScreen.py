import sys
from tkinter import *

from lib.gui.Settings import open_settings
from lib.manager import MANAGER, DEFAULT_IMG_DIR

# écran de fin de partie
class EndScreen(Tk):
    def __init__(self, score):
        """Initialisation de l'écran de fin de partie"""
        super().__init__()

        # appliquation du theme
        self.theme = MANAGER.get("THEME")
        theme_path = DEFAULT_IMG_DIR.parent / "engine" 
        self.tk.call("source", theme_path / "theme.tcl")
        self.tk.call("set_theme", self.theme.lower())

        # quitter par la croix
        self.protocol("WM_DELETE_WINDOW", sys.exit)

        # titre
        self.title("Candy Crush")

        # récupérer le score
        self.score = score

        # initialiser les widgets (avec une méthode différente, pour mes tests perso ;)   )
        self.create_widgets()

        

        self.exit_mode = 0

    def create_widgets(self):
        """Création des widgets"""

        # titre
        self.label = Label(self, text="Game Over !", font=("Arial", 30))
        self.label.pack(pady=10)

        # si le score est le meilleur score, afficher un message de félicitations²
        if self.score >= MANAGER.get("BEST_SCORE"):
            self.congtrats_label = Label(self, text="Nouveau meilleur score !", font=("Arial", 20))
            self.congtrats_label.pack(pady=10)

        # afficher le score
        self.score_label = Label(self, text="Score : " + str(self.score), font=("Arial", 20))
        self.score_label.pack(pady=10)


        # boutons
        # bouton pour rejouer
        self.button = Button(self, text="Rejouer", font=("Arial", 20), command=self.replay)
        self.button.pack(pady=10)

        # bouton pour ouvrir les paramètres
        self.settingButton = Button(self, text="Paramètres", font=("Arial", 20), command=open_settings)
        self.settingButton.pack(pady=10)

        # bouton pour quitter
        self.quitButton = Button(self, text="Quitter", font=("Arial", 20), command=self.exit_game)
        self.quitButton.pack(pady=10)

        # ajouter des marges
        self.minsize(350, 300)

        # taille de la fenêtre
        self.resizable(False, False)


    def replay(self):
        """Rejouer"""
        self.destroy()
        self.exit_mode = 1

    def exit_game(self):
        """Quitter"""
        self.destroy()
        self.exit_mode = 0

    def show_result(self):
        """Afficher l'écran de fin de partie"""
        self.mainloop()
        return self.exit_mode
