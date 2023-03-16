def rule1(candies):
    """Vérifie si il y des combinaison de 3 bonbons MAXIMUM de la même couleur dans la grille.
    Prend en charge les combinaisons horizontales et verticales.
    Retourne une liste de tuples (x, y) des bonbons à supprimer.

    Args:
        candies (dict): Dictionnaire des bonbons de la grille. {(x, y): Candy}
    
    """
    matches = []
    for c in candies.keys():
        candy = candies[c]
        x, y = c
        
        # Vérifier si le bonbon est dans une combinaison de 3
        
        # HORIZONTAL
        # si le bonbon est à gauche des deux autres
        if (x + 2, y) in candies and candy.type == candies[(x + 1, y)].type == candies[(x + 2, y)].type and ((x + 1, y), (x + 2, y)) not in matches:
            matches.append((x, y))
            matches.append((x + 1, y))
            matches.append((x + 2, y))

        # si le bonbon est au milieu des deux autres
        elif (x - 1, y) in candies and (x + 1, y) in candies and candy.type == candies[(x - 1, y)].type == candies[(x + 1, y)].type and ((x - 1, y), (x + 1, y)) not in matches:
            matches.append((x, y))
            matches.append((x - 1, y))
            matches.append((x + 1, y))

        # si le bonbon est à droite des deux autres
        elif (x - 2, y) in candies and candy.type == candies[(x - 1, y)].type == candies[(x - 2, y)].type and ((x - 1, y), (x - 2, y)) not in matches:
            matches.append((x, y))
            matches.append((x - 1, y))
            matches.append((x - 2, y))

        # VERTICAL
        # si le bonbon est en haut des deux autres
        elif (x, y - 2) in candies and candy.type == candies[(x, y - 1)].type == candies[(x, y - 2)].type and ((x, y - 1), (x, y - 2)) not in matches:
            matches.append((x, y))
            matches.append((x, y - 1))
            matches.append((x, y - 2))

        # si le bonbon est au milieu des deux autres
        elif (x, y - 1) in candies and (x, y + 1) in candies and candy.type == candies[(x, y - 1)].type == candies[(x, y + 1)].type and ((x, y - 1), (x, y + 1)) not in matches:
            matches.append((x, y))
            matches.append((x, y - 1))
            matches.append((x, y + 1))

        # si le bonbon est en bas des deux autres
        elif (x, y + 2) in candies and candy.type == candies[(x, y + 1)].type == candies[(x, y + 2)].type and ((x, y + 1), (x, y + 2)) not in matches:
            matches.append((x, y))
            matches.append((x, y + 1))
            matches.append((x, y + 2))

    # suppression des doublons
    res = []
    for m in matches:
        if m not in res:
            res.append(m)

    # supprime les coordonnées qui n'existent pas dans le dictionnaire
    res = [r for r in res if r in candies.keys()]
        
    return res
    
def rule2(candies):
    ...


def rule3(candies):
    ...
class testCandy:
    def __init__(self, type):
        self.type = type

# Règles du jeu
RULES = {"1": rule1, "2": rule2, "3": rule3}

# test
if __name__ == "__main__":
    candies = {
        (0, 0): testCandy("red"),
        (1, 0): testCandy("blue"),
        (2, 0): testCandy("red"),
        (0, 1): testCandy("red"),
        (1, 1): testCandy("blue"),
        (2, 1): testCandy("blue"),
        (0, 2): testCandy("red"),
        (1, 2): testCandy("blue"),
        (2, 2): testCandy("red"),
    }

    print(candies[(0, 0)].type== candies[(0, 1)].type == candies[(0, 2)].type)

    test = rule1(candies)
    print(test)