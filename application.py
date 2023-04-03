from lib.manager import MANAGER
from lib.rules import RULES
from lib.gui.MainMenu import MainMenu
from lib.gui.EndScreen import EndScreen
from lib.gui.MainApp import Game

# fonctionnement du jeu
def play():
    """Lance le jeu"""
    # boucle de jeu (relance une partie tant que le jeu n'est pas quitté)
    replay = True
    while replay:
        replay = False # quitter par défault à la fermeture si "rejouer" n'est pas cliqué

        # obtenir les règles
        main = MainMenu(MANAGER.get("LAST_PLAYED"))
        x, y, rule= main.get_game_settings()

        # sauvegarder les règles utilisées
        MANAGER.set("LAST_PLAYED", [x, y, rule])
        MANAGER.save()

        # lancer le jeu avec les règles choisies
        game = Game(x, y, RULES[str(rule)])
        score = game.play()

        # sauvegarder le nouveau meilleur score si il est supérieur au précédent
        if score > MANAGER.get("BEST_SCORE"):
            MANAGER.data["BEST_SCORE"] = score
            MANAGER.save()


        # afficher l'écran de fin de partie et obtenir le choix de l'utilisateur
        replay = EndScreen(score).show_result()


# appel de la fonction si le fichier est exécuté
if __name__ == '__main__':
    play()
