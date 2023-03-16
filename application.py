import os

from lib.manager import load_manager, MANAGER
from lib.core import handle_error
from lib.rules import *
from lib.gui.MainMenu import MainMenu
from lib.gui.EndScreen import EndScreen
from lib.gui.MainApp import Game






def play():
    """Lance le jeu"""
    # régler le chemin par défaut vers les images
    replay = True
    while replay:
        replay = False

        if MANAGER.get("IMG_DIR") == "default":
            MANAGER.data["IMG_DIR"] = os.path.join(os.path.dirname(__file__), "assets", "graphics")

        # obtenir les règles
        main = MainMenu(MANAGER.get("LAST_PLAYED"))
        x, y = main.ask_size()
        r = 1

        # sauvegarder les dimensions
        MANAGER.data["LAST_PLAYED"] = (x, y)
        MANAGER.save()

        game = Game(x, y, RULES[str(r)])
        score = game.play()

        if score > MANAGER.get("BEST_SCORE"):
            MANAGER.data["BEST_SCORE"] = score
            MANAGER.save()

        replay = EndScreen(score).show_result()

if __name__ == '__main__':
    play()
