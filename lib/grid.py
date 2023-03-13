from lib.candy import Candy

class Grid:
    def __init__(self, size_x, size_y):
        self.size_x = size_x
        self.size_y = size_y

        # Créée une grille sous forme d'une liste de listes
        self.grid = [[0 for x in range(size_x)] for y in range(size_y)]

    def fill(self, candy):
        for x in range(self.size_x):
            for y in range(self.size_y):
                self.grid[x][y] = Candy(candy)




