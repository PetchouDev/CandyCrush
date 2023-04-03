def rule1(candies):
    """

    Vérifie si il y des combinaison de 3 bonbons MAXIMUM de la même couleur dans la grille.
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
        if (x + 2, y) in candies and candy.type == candies[(x + 1, y)].type == candies[(x + 2, y)].type and (x + 1, y) not in matches and (x + 2, y) not in matches:
            matches.append((x, y))
            matches.append((x + 1, y))
            matches.append((x + 2, y))

        # si le bonbon est au milieu des deux autres
        elif (x - 1, y) in candies and (x + 1, y) in candies and candy.type == candies[(x - 1, y)].type == candies[(x + 1, y)].type and (x - 1, y) not in matches and (x + 1, y) not in matches:
            matches.append((x, y))
            matches.append((x - 1, y))
            matches.append((x + 1, y))

        # si le bonbon est à droite des deux autres
        elif (x - 2, y) in candies and candy.type == candies[(x - 1, y)].type == candies[(x - 2, y)].type and (x - 1, y) not in matches and (x - 2, y) not in matches:
            matches.append((x, y))
            matches.append((x - 1, y))
            matches.append((x - 2, y))

        # VERTICAL
        # si le bonbon est en haut des deux autres
        elif (x, y - 2) in candies and candy.type == candies[(x, y - 1)].type == candies[(x, y - 2)].type and (x, y - 1) not in matches and (x, y - 2) not in matches:
            matches.append((x, y - 1))
            matches.append((x, y - 2))
            matches.append((x, y))

        # si le bonbon est au milieu des deux autres
        elif (x, y - 1) in candies and (x, y + 1) in candies and candy.type == candies[(x, y - 1)].type == candies[(x, y + 1)].type and (x, y - 1) not in matches and (x, y + 1) not in matches:
            matches.append((x, y))
            matches.append((x, y - 1))
            matches.append((x, y + 1))

        # si le bonbon est en bas des deux autres
        elif (x, y + 2) in candies and candy.type == candies[(x, y + 1)].type == candies[(x, y + 2)].type and (x, y + 1) not in matches and (x, y + 2) not in matches:
            matches.append((x, y))
            matches.append((x, y + 1))
            matches.append((x, y + 2))
        
    return matches

def rule2(candies):
    """
    
    Vérifie si il y des combinaison de 3 bonbons ou plus de la même couleur dans la grille.
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
    

def rule3(candies):
    """

    Vérifie si il y des combinaison de 3 bonbons ou plus de la même couleur dans la grille.
    Prend en charge les combinaisons horizontales et verticales.
    propage sur tous les bonbons adjacents de la même couleur.
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
        if (x + 2, y) in candies and candy.type == candies[(x + 1, y)].type == candies[(x + 2, y)].type and (x + 1, y) not in matches and (x + 2, y) not in matches:
            matches.append((x, y))
            matches.append((x + 1, y))
            matches.append((x + 2, y))

        # si le bonbon est au milieu des deux autres
        elif (x - 1, y) in candies and (x + 1, y) in candies and candy.type == candies[(x - 1, y)].type == candies[(x + 1, y)].type and (x - 1, y) not in matches and (x + 1, y) not in matches:
            matches.append((x, y))
            matches.append((x - 1, y))
            matches.append((x + 1, y))

        # si le bonbon est à droite des deux autres
        elif (x - 2, y) in candies and candy.type == candies[(x - 1, y)].type == candies[(x - 2, y)].type and (x - 1, y) not in matches and (x - 2, y) not in matches:
            matches.append((x, y))
            matches.append((x - 1, y))
            matches.append((x - 2, y))

        # VERTICAL
        # si le bonbon est en haut des deux autres
        elif (x, y - 2) in candies and candy.type == candies[(x, y - 1)].type == candies[(x, y - 2)].type and (x, y - 1) not in matches and (x, y - 2) not in matches:
            matches.append((x, y - 1))
            matches.append((x, y - 2))

        # si le bonbon est au milieu des deux autres
        elif (x, y - 1) in candies and (x, y + 1) in candies and candy.type == candies[(x, y - 1)].type == candies[(x, y + 1)].type and (x, y - 1) not in matches and (x, y + 1) not in matches:
            matches.append((x, y))
            matches.append((x, y - 1))
            matches.append((x, y + 1))

        # si le bonbon est en bas des deux autres
        elif (x, y + 2) in candies and candy.type == candies[(x, y + 1)].type == candies[(x, y + 2)].type and (x, y + 1) not in matches and (x, y + 2) not in matches:
            matches.append((x, y))
            matches.append((x, y + 1))
            matches.append((x, y + 2))

    # propagation des combinaisons
    print('propagating matches...')
    for m in matches:
        # obtenir les voisins du bonbon
        neighboors = []
        for n in [(m[0] - 1, m[1]), (m[0] + 1, m[1]), (m[0], m[1] - 1), (m[0], m[1] + 1)]:
            if n in candies.keys():
                neighboors.append(candies[n])

        print('neighboors of', m, 'are', neighboors)
        # ajouter les voisins de la même couleur à la liste des combinaisons
        for n in neighboors:
            neighboor_coords = (n.x, n.y)
            if n and n.type == candies[m].type and neighboor_coords not in matches:
                matches.append((n.x, n.y))
                
    print(matches)

    # suppression des doublons
    res = []
    for m in matches:
        if m not in res:
            res.append(m)

    # supprime les coordonnées qui n'existent pas dans le dictionnaire
    res = [r for r in res if r in candies.keys()]
        
    return res

def detecte_coordonnees_combinaison(candies, rule):
    return rule(candies)


# Règles du jeu
RULES = {"1": rule1, "2": rule2, "3": rule3}

