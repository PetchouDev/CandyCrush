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

2. Boucle de jeu
    - Tant qu'il y a des combinaisons possibles :
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

### Fonctions annexes

Génération de la grille

```python
def generer_grille(x, y):
    """
    Génère une grille de dimensions x*y, puis la remplie avec des bonbons aléatoires
    """
```

Remplissage de la grille avec des bonbons aléatoires

```python
def remplir_grille(grille):
    """
    Rempli la grille avec des bonbons aléatoires
    """
```

Affichage de la grille

```python
def affichage_grille(grille, nb_type_bonbons):  # voir les fonctions imposées
    """
    Affiche la grille de jeu "grille" contenant au
    maximum "nb_type_bonbons" couleurs de bonbons différentes.
    """
```

Demande du nombre maximal de coups et du score à atteindre

```python
def demander_parametres():
    """
    Demande le nombre maximal de coups et le score à atteindre
    """
```

Coup du joueur

```python
def coup_joueur(grille):
    """
    Demande les coordonnées d'un bonbon
    l'affiche en surbrillance
    Demande les coordonnées d'un second bonbon
    Si le second est adjacent au premier, les échange, sinon, le second mis en surbrillance, et le premier revient à sa couleur d'origine. Si le second est le même que le premier, on revient à l'étape 2.

    En cas déchange:
    Si une combinaison est formée, on supprime les bonbons de la combinaison

    Tant que des combinaisons sont formées:
        On applique la gravité
        On remplit la grille avec des bonbons aléatoires
    """
```

Echange de deux bonbons

```python
def echange_bonbons(grille, i1, j1, i2, j2):
    """
    Echange les bonbons aux coordonnées (i1, j1) et (i2, j2)
    """
```

mise en surbrillance d'un bonbon

```python
def surbrillance_bonbon(grille, i, j):
    """
    Met en surbrillance le bonbon aux coordonnées (i, j)
    """
```

Suppression des bonbons d'une combinaison

```python
def supprimer_bonbons(grille, combinaison):
    """
    Supprime les bonbons de la combinaison
    """
```

Application de la gravité

```python
def appliquer_gravite(grille):
    """
    Applique la gravité à la grille
    """
```

Verification de la fin de la partie

```python
def fin_partie(grille, nb_coups, score):
    """
    Vérifie si la partie est finie
    """
```




