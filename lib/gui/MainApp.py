import os
import sys
import random
import time
from tkinter import *

from PIL import Image, ImageTk

from lib.gui.Candy import Candy
from lib.manager import MANAGER, DEFAULT_IMG_DIR


class Game(Tk):
    def __init__(self, x, y, rule):
        """Initialisation de la fenêtre"""
        super().__init__()

        # quitter par la croix
        self.protocol("WM_DELETE_WINDOW", sys.exit)

        self.title("Candy Crush")
        # Créer la fenêtre principale
        self.title("CandyCrush")

        # appliquation du theme
        self.theme = "LIGTH"
        theme_path = DEFAULT_IMG_DIR.parent / "engine" 
        self.tk.call("source", theme_path / "theme.tcl")
        self.tk.call("set_theme", self.theme.lower())

        # Règle du jeu à utiliser
        self.rule = rule

        # autoriser les interactions avec la fenêtre
        self.enabled = False # désactivé par défaut

        # Créer la grille de boutons, avec une couleur d'arrière-plan
        self.grid = Frame(self)
        self.grid.pack(padx=10, pady=10)
        self.grid.configure(bg=MANAGER.get("BG_COLOR"))
        self.configure(bg=MANAGER.get("BG_COLOR"))

        # Créer un dictionnaire pour stocker les boutons
        self.candies = {}

        # Créer une liste pour stocker les bonbons à supprimer
        self.matches = []


        # initialiser le score
        self.score = 0

        # initialiser la taille de la grille
        self.x = x
        self.y = y

        # récupérer le meilleur score
        self.best = MANAGER.get("BEST_SCORE")

        # gestion du bonbon sélectionné
        self.selected = False # aucun bonbon sélectionné

        # Créer un bonbon dans chaque case de la grille
        for i in range(x):
            for j in range(y):
                self.spawn_candy(i, j)



        # Créer les labels pour le score et le meilleur score
        self.score_label = Label(self, text=f"Score: {self.score}", font=("Helvetica", 16), background=MANAGER.get("BG_COLOR"))
        self.score_label.pack(side=LEFT, padx=20)

        self.best_label = Label(self, text=f"Meilleur score: {self.best}", font=("Helvetica", 16), background=MANAGER.get("BG_COLOR"))
        self.best_label.pack(side=LEFT, padx=10)
        

        # Créer le bouton pour quitter
        self.quit_button = Button(self, text=" X ", command=self.destroy)
        self.quit_button.pack(side=RIGHT, padx=20)

        # calculer la taille de la fenêtre
        btn_size = MANAGER.get("BUTTON_SIZE")
        self.geometry(f"{max((x + 1) * btn_size  + 50, 400)}x{(y + 1) * btn_size + 40}")


        # Mettre à jour la fenêtre
        self.update()

        # petit délai pour que l'utilisateur puisse voir les bonbons
        time.sleep(1)

        # Vérifier si il y a des combinaisons
        self.run()

        # Activer les interactions avec la fenêtre
        self.enabled = True

    def spawn_candy(self, x, y):
        """Créer un bonbon dans la case (x, y)"""

        # Choisir un type de bonbon aléatoire
        type = random.randint(1, 5)

        # Charger l'image pour le bouton
        image = Image.open(os.path.join(MANAGER.get('IMG_DIR'), f"Candy{type}.png"))
        btn_size = MANAGER.get("BUTTON_SIZE")
        image = image.resize((btn_size, btn_size))  # Ajuster la taille de l'image si nécessaire
        photo = ImageTk.PhotoImage(image)

        # Créer le bouton et ajouter l'image
        self.candies[(x, y)] = Candy(self, self.grid, x, y, type, image=photo, bd=2, relief="groove")
        self.candies[(x, y)].image = photo

        # Définir la couleur d'arrière-plan 
        self.candies[(x, y)].change_color(MANAGER.get("CANDY_BG"))

        # Ajouter le bouton à la grille
        self.candies[(x, y)].grid(row=y, column=x)

    def play(self):
        """Jouer une partie"""
        self.mainloop()
        return self.score

    def swap(self, candy1, candy2):
        # Echanger les positions des deux bonbons
        candy1.grid(row=candy2.y, column=candy2.x)
        candy2.grid(row=candy1.y, column=candy1.x)

        # mettre à jour les positions des bonbons dans le dictionnaire
        self.candies[(candy1.x, candy1.y)] = candy2
        self.candies[(candy2.x, candy2.y)] = candy1

        # mettre à jour les coordonnées x et y des bonbons
        candy1.x, candy1.y, candy2.x, candy2.y = candy2.x, candy2.y, candy1.x, candy1.y

    def check_matches(self):
        """Vérifier si il y a des combinaisons de bonbons"""
        self.matches = self.rule(self.candies)

    def delete_matches(self):
        """Supprimer les bonbons qui sont dans la liste self.matches"""

        for c in self.matches:
            self.candies[c].destroy()
            del self.candies[c]
        
        self.score += len(self.matches)

        self.score_label.configure(text=f"Score: {self.score}")

        if self.score > self.best:
            self.best = self.score
            self.best_label.configure(text=f"Meilleur score: {self.best}")
            MANAGER.set("BEST_SCORE", self.best)

        self.update()

    def fall(self):
        """
        Remonte la grille de bonbons de haut en bas (de la première ligne vers l'avant-dernière)
        Pour chaque bonbon, si il y a un bonbon vide en dessous, descendre le bonbon
        
        Répéter jusqu'à ce que tous les bonbons soient descendus
        CAD: tant qu'il y a un bonbon qui a été déplacé
        
        """
        moved = True
        while moved:
            moved = True
            rows = list(range(0, self.y-1))
            rows = rows[::-1]
            while moved:
                moved = False
                for j in rows:
                    for i in range(self.x):
                        if (i, j) in self.candies and (i, j + 1) not in self.candies:
                            self.candies[(i, j + 1)] = self.candies[(i, j)]
                            self.candies[(i, j + 1)].y += 1
                            self.candies[(i, j + 1)].grid(row=j + 1, column=i)
                            del self.candies[(i, j)]
                            moved = True
                    self.update()
                    time.sleep(0.01)

    def fill(self):
        """Remplir les cases vides avec des bonbons"""
        for i in range(self.x):
            for j in range(self.y):
                if (i, j) not in self.candies:
                    self.spawn_candy(i, j)

    def can_move(self):
        """Vérifie si il existe un bonbon qui peut être déplacé"""
        # obtenir la liste des déplacements qui forment un match
        moves = []
        for c in self.candies:
            # obtenir les voisins du bonbon
            i, j = c
            neiboors = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]

            # vérifier si les voisins sont dans la grille
            neiboors = [n for n in neiboors if n[0] >= 0 and n[0] < self.x and n[1] >= 0 and n[1] < self.y]

            for n in neiboors:
                tmp = self.candies.copy()
                # swap les bonbons
                tmp[c], tmp[n] = tmp[n], tmp[c]
                moves += self.rule(tmp)

        # si il existe un déplacement qui forme un match, on peut déplacer un bonbon
        if len(moves) > 0:
            game_over = False

        # si il n'existe aucun déplacement qui forme un match, on ne peut pas déplacer un bonbon
        else:
            game_over = True

        if game_over:
            # laisser le joueur voir la grille puis fermer la fenêtre
            self.update()
            time.sleep(1.5)
            self.destroy()

    def click_handler(self, candy: Candy):
        # import des couleurs
        SELECTED_COLOR = MANAGER.get("CANDY_SELECTED")
        CANDY_BG = MANAGER.get("CANDY_BG")

        # Si aucun bonbon n'est sélectionné, sélectionner ce bonbon
        if self.selected is False:
            candy.selected = True
            self.selected = candy
            candy.change_color(SELECTED_COLOR)
            return True
        
        # Si un bonbon est déjà sélectionné
        else:
            # Si le bonbon sélectionné est le même que celui sur lequel on a cliqué, déselectionner le bonbon
            if self.selected == candy:
                candy.selected = False
                self.selected = False
                return False
                
            
            # Si le bonbon sélectionné est différent de celui sur lequel on a cliqué
            else:
                # si le bonbon sélectionné est à côté du bonbon sur lequel on a cliqué
                neiboors = [(candy.x, candy.y - 1), (candy.x, candy.y + 1), (candy.x - 1, candy.y), (candy.x + 1, candy.y)]
                neiboors = [n for n in neiboors if n[0] >= 0 and n[0] < self.x and n[1] >= 0 and n[1] < self.y]


                if (self.selected.x, self.selected.y) in neiboors:
                    try:
                        self.selected.change_color(CANDY_BG)
                    except:
                        pass

                    # créée une copie des coordonnées de la liste des coordonnées avec les futures coordonnées du bonbon sélectionné
                    new_coords = self.candies.copy()
                    new_coords[(self.selected.x, self.selected.y)], new_coords[(candy.x, candy.y)] = candy, self.selected

                    
                    # teste si il y a des bonbons à supprimer
                    res = self.rule(new_coords)

                    del new_coords

                    if res == []:
                        # si il n'y a pas de bonbons à supprimer, ne rien faire et déselectionner les bonbons
                        try:
                            self.selected.change_color(CANDY_BG)
                        except:
                            pass
                        self.selected = False
                        return False
                        
                    else:
                        # si il y a des bonbons à supprimer, les supprimer et déselectionner les bonbons (gestion des erreurs pour éviter les bugs)
                        self.swap(self.selected, candy)
                        self.run()
                        self.update()
                        try:
                            self.selected.change_color(CANDY_BG)
                        except:
                            pass
                        try :
                            candy.change_color(CANDY_BG)
                        except:
                            pass
                        self.selected = False
                        return False


                # si le bonbon sélectionné n'est pas à côté du bonbon sur lequel on a cliqué, sélectionner le bonbon sur lequel on a cliqué
                else:
                    try:
                        self.selected.change_color(CANDY_BG)
                    except:
                        pass
                    self.selected = candy
                    candy.selected = True
                    return True

    def run(self):
        """Supprime les combinaisons, puis remplis la grille"""

        # désactive les interactions avec la grille pour limiter les erreurs
        self.enabled = False

        run = True
        while run:
            self.check_matches()

            self.delete_matches()
            self.update()
            time.sleep(0.5)

            self.fall()
            self.update()
            time.sleep(0.5)

            self.fill()
            self.update()

            if self.matches == []:
                run = False

                # appliquer à tous les bonbons la couleur par défaut
                for c in self.candies.keys():
                    self.candies[c].change_color(MANAGER.get("CANDY_BG"))
            
        self.can_move()

        # réactive les interactions avec la grille
        self.enabled = True

