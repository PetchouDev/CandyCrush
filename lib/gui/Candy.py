from tkinter import Button

from ..manager import MANAGER


# classe Candy, objet représentant un bonbon dans la grille
class Candy(Button):
    def __init__(self, parent, holder, x, y, type, mode="production", **kwargs):
        """Initialisation d'un bonbon"""

        # initialisation des variables
        self.x = x
        self.y = y
        self.type = type
        
        # statut de sélection (gère la couleur d'arrière plan de la case)
        self.selected = False

        # mode de création (production ou test)
        if mode == "production":
            # mode production (affichage graphique dans la grille)
            self.holder = holder
            self.parent = parent

            Button.__init__(self, holder, **kwargs)
            
            self.configure(image=MANAGER.get(f"CANDY_{self.type}")) # image du bonbon
            self.bind(f"<Button-1>", lambda event: self.clicked())  # gestion du clic
            self.change_color(MANAGER.get("CANDY_BG"))              # couleur d'arrière plan

        

    def change_color(self, color):
        """Change la couleur d'arrière plan du bonbon"""
        self.configure(bg=color, highlightcolor=color, activebackground=color, activeforeground=color)


    def clicked(self):
        """Gestion du clic sur le bonbon"""
        # vérifier si la grille autorise les clics
        if self.parent.enabled:
            selected = self.parent.click_handler(self)
            try:
                if selected:
                    self.change_color(MANAGER.get("SELECTED_COLOR"))
                else:
                    self.change_color(MANAGER.get("CANDY_BG"))
            except:
                pass
        else:
            # sinon, ne rien faire
            pass

