import sys
from tkinter import *

from lib.gui.Settings import open_settings
from lib.manager import MANAGER

class EndScreen(Tk):
    def __init__(self, score):
        super().__init__()

        # quitter par la croix
        self.protocol("WM_DELETE_WINDOW", sys.exit)

        self.title("Candy Crush")
        self.score = score

        self.create_widgets()

        self.geometry(f"{400}x{400}")
        self.resizable(False, False)

        self.exit_mode = 0

    def create_widgets(self):
        self.label = Label(self, text="Game Over !", font=("Arial", 30))
        self.label.pack(pady=10)

        if self.score > MANAGER.get("BEST_SCORE"):
            self.congtrats_label = Label(self, text="Nouveau meilleur score !", font=("Arial", 20))
            self.congtrats_label.pack(pady=10)

        self.score_label = Label(self, text="Score : " + str(self.score), font=("Arial", 20))
        self.score_label.pack(pady=10)

        self.button = Button(self, text="Rejouer", font=("Arial", 20), command=self.replay)
        self.button.pack(pady=10)
        self.settingButton = Button(self, text="Paramètres", font=("Arial", 20), command=open_settings)
        self.settingButton.pack(pady=10)
        self.quitButton = Button(self, text="Quitter", font=("Arial", 20), command=self.exit_game)
        self.quitButton.pack(pady=10)


    def replay(self):
        self.destroy()
        self.exit_mode = 1

    def exit_game(self):
        self.destroy()
        self.exit_mode = 0

    def show_result(self):
        self.mainloop()
        return self.exit_mode
