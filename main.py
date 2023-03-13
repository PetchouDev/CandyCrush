import random

from lib.core import Color


def generate_grid(size):
    colors = Color.all()
    grid = []
    for i in range(size):
        l = []
        for j in range(size):
            l.append(random.choice(colors))
        grid.append(l)
    return grid

def ask_coordinates():
    x, y = input("Coordonnée X :"), input("Coordonnées Y :")
    return x, y

def swap():
    