from lib.rules import RULES, detecte_coordonnees_combinaison
from lib.gui.Candy import Candy

def test_candy(x, y, type):
    return Candy(parent=None, holder=None, x=x, y=y, type=type, mode="test")

def test_detecte_coordonnees_combinaison():
    
    # paramètres de test
    X = 4
    Y = 4
    RULE = 3
    
    # pattern de la grille de test
    TYPES = [
        1, 1, 1, 3, 
        1, 4, 2, 1,
        3, 3, 3, 3,
        4, 2, 1, 3,
    ]
    
    # génération de la grille de test
    candies = {(x, y): test_candy(x, y, TYPES[y * 4 + x]) for x in range(X) for y in range(Y)}
    
    # résultat attendu
    expected = {(0, 0), (1, 0), (2, 0), (0, 1), (0, 2), (1, 2), (2, 2), (3, 2), (3, 3)}

    # affichage du résultat attendu
    print(expected)

    # lancement du test
    result = set(detecte_coordonnees_combinaison(candies, RULES[f"{RULE}"]))
    
    # affichage du résultat
    print(result)

    # vérification du résultat
    try:
        assert result == expected
        print("Test réussi")
    except AssertionError as e:
        print("Test échoué")
        print(e)


if __name__ == "__main__":
    test_detecte_coordonnees_combinaison()