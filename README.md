# CandyCrush
 
[**Sujet du TD**](https://moodle.insa-lyon.fr/pluginfile.php/359009/mod_resource/content/2/Mini_projet_ISN2_v3.pdf)

## Fonctions imposées


Détection des bonbons formant une combinaison avec un bonbon donné


```python	
def detecte_coordonnees_combinaison(grille, i, j):
    """
    Renvoie une liste contenant les coordonnées de tous les bonbons
    appartenant à la combinaison du bonbon (i, j).
    """
```

Affichage de la grille

```python
def affichage_grille(grille, nb_type_bonbons):
    """
    Affiche la grille de jeu "grille" contenant au
    maximum "nb_type_bonbons" couleurs de bonbons différentes.
    """
    plt.imshow(grille, vmin=0, vmax=nb_type_bonbons−1, cmap=’jet’)
    plt.pause(0.1)
    plt.draw()
    plt.pause(0.1)
```

Test de la fonction detecte_coordonnees_combinaison (jeu de test à fournir)

```python
def test_detecte_coordonnees_combinaison():
    """
    Test la fonction detecte_coordonnees_combinaison(grille, i, j).
    Pour chaque cas de test, affiche True si le test passe,
    False sinon
    """
```

## Découpage fonctionnel

### Déroulement de la partie
1. Initialisation de la partie
    - Génération d'une grille de la taille souhaitée
    - Remplissage de la grille avec des bonbons aléatoires
    - Affichage de la grille
    - Demande du nombre maximal de coups et du score à atteindre

2. Boucle de jeu
    - Demande les coordonnées d'un bonbon
    - l'affiche en surbrillance
    - Demande les coordonnées d'un second bonbon
    - Si le second est adjacent au premier, les échange, sinon, le second mis en surbrillance, et le premier revient à sa couleur d'origine. Si le second est le même que le premier, on revient à l'étape 2.

    Après un échange:
    - Si une combinaison est formée, on supprime les bonbons de la combinaison
    - On applique la gravité
    - On remplit la grille avec des bonbons aléatoires
    - On affiche la grille
    - On décrémente le nombre de coups restants

3. Fin de la partie
    - Si le nombre de coups est épuisé, on affiche un message de défaite
    - Si le score est atteint, on affiche un message de victoire



