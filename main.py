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


def swap(grid):
    candy_1 = ask_coordinates()
    candy_2 = ask_coordinates
    grid[candy_1[0]][candy_1[1]], grid[candy_2[0]][candy_2[1]] = grid[candy_2[0]][candy_2[1]], grid[candy_1[0]][candy_1[1]]


def gravite(grille):
    for i in range(len(grille)-1):
        for j in range(len(grille[i])):
            if grille[i+1][j]==0:
                grille[i+1][j]=grille[i][j]
                grille[i][j]=0
    return grille