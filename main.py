import random

from lib.core import Color
from lib.grid import Grid

# génération de la grille
def generate_grid(x, y):
    grid = Grid(x, y)
    grid.fill()

    print(grid)


generate_grid(10, 10)

