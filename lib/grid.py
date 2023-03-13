from random import choice

from lib.candy import Candy
from lib.core import Color, colored

COLORS = Color().all()

class Grid:
    def __init__(self, size_x, size_y):
        self.size_x = size_x
        self.size_y = size_y

        self.score = 0

        # Créée une grille sous forme d'une liste de listes
        self.grid = [[0 for x in range(size_x)] for y in range(size_y)]

    def fill(self):
        """
        Remplis la grille de bonbons aléatoirement
        """
        for x in range(self.size_x):
            for y in range(self.size_y):
                self.grid[x][y] = Candy(choice(COLORS))

    
    def candy_exists(self, x, y):
        """
        Vérifie si un bonbon existe à la position x, y
        """
        res =  0 <= x < self.size_x and 0 <= y < self.size_y

        return res
    

    def hightlight(self, x, y):
        """
        Met en évidence un bonbon
        """
        self.grid[x][y].selected = True


    def swap(self, x1, y1, x2, y2):
        """
        Echange deux bonbons
        """
        self.grid[x1][y1], self.grid[x2][y2] = self.grid[x2][y2], self.grid[x1][y1]

    def __str__(self):
        """
        Affiche la grille
        Format :
        C | C | C | C | C
        --+---+---+---+--
        C | C | C | C | C
        --+---+---+---+--
        C | C | C | C | C
        """
        grid = ""
        for y in range(self.size_y):
            for x in range(self.size_x):
                grid += f"{self.grid[x][y]} " + ("| " if x < self.size_x - 1 else "")
            grid += "\n"
            grid += ("--+-" * (self.size_x - 1) + "-\n") if y < self.size_y - 1 else colored(f"Score: {self.score}", "yellow")

        return grid
        
            




