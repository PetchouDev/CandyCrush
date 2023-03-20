import sys
from tkinter import *
from tkinter.ttk import Combobox

from ..PIL import Image, ImageTk

from lib.gui.Settings import open_settings
from lib.manager import MANAGER, DEFAULT_IMG_DIR



# Demander à l'utilisateur de choisir la taille de la grille, avec des menus déroulants de 4 à 10
class MainMenu(Tk):
    def __init__(self, last_dimensions):
        super().__init__()
        self.title("Candy Crush")
        self.geometry("300x250")
        self.resizable(False, False)

        
        self.last_x = last_dimensions[0]
        self.last_y = last_dimensions[1]

        # ajouter l'icon
        self.wm_iconphoto(False, ImageTk.PhotoImage(Image.open(DEFAULT_IMG_DIR / "SuperCandy.png")))

        self.label = Label(self, text="Choisissez la taille de la grille")
        self.label.pack(pady=10)

        self.frame = Frame(self)
        self.frame.pack()

        self.x = IntVar()
        self.y = IntVar()

        self.x.set(self.last_x)
        self.y.set(self.last_y)

        self.x_label = Label(self.frame, text="Largeur")
        self.y_label = Label(self.frame, text="Hauteur")

        self.x_menu = Combobox(self.frame, textvariable=self.x, values=[i for i in range(4, MANAGER.get("MAX_WIDTH") + 1)])
        self.y_menu = Combobox(self.frame, textvariable=self.y, values=[i for i in range(4, MANAGER.get("MAX_HEIGTH") + 1)])

        self.x_label.grid(row=0, column=0, padx=10, pady=10)
        self.y_label.grid(row=1, column=0, padx=10, pady=10)

        self.x_menu.grid(row=0, column=1, padx=10, pady=10)
        self.y_menu.grid(row=1, column=1, padx=10, pady=10)

        # bouton paramètres
        self.settings_button = Button(self, text="Paramètres", command=open_settings)
        self.settings_button.pack(pady=10, padx=30, fill=X)

        self.button = Button(self, text="Jouer", command=self.check_size)
        self.button.pack(pady=10, fill=X, padx=30)

        # quitter par la croix
        self.protocol("WM_DELETE_WINDOW", sys.exit)

    def ask_size(self):
        self.mainloop()
        return self.size
        
    def check_size(self):
        try:
            self.size = min(self.x.get(), MANAGER.get("MAX_HEIGTH")), min(self.y.get(), MANAGER.get("MAX_WIDTH"))
            self.destroy()
        except:
            # affiche le message d'erreur puis lance la partie avec la dernière taille valide
            text = "La taille de la grille est invalide, utilisation de la dernière taille valide."
            error_message = Toplevel()
            error_message.title("Erreur")
            error_message.resizable(False, False)
            Label(error_message, text=text).pack(pady=10)
            Button(error_message, text="Fermer", command=self.destroy).pack(pady=10)
            self.size = self.last_x, self.last_y

            error_message.mainloop()
            self.destroy()



        finally:
            print("ready to start")
