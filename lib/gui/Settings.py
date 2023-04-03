import os
from tkinter import *
from tkinter.ttk import *

from ..manager import MANAGER, DEFAULT_IMG_DIR
from ..core import handle_error

# fenêtre de paramètres
class Settings(Tk):
    def __init__(self):

        # initialisation de la fenêtre
        super().__init__()
        self.title("Candy Crush - settings")

        self.label = Label(self, text="Paramètres")

        self.label.grid(row=0, column=0, columnspan=2, pady=10)
        

        # mettre le titre de la fenêtre en gras
        self.label.config(font=("Arial", 20, "bold"))

        # appliquation du theme
        self.theme = MANAGER.get("THEME")
        theme_path = DEFAULT_IMG_DIR.parent / "engine" 
        self.tk.call("source", theme_path / "theme.tcl")
        self.tk.call("set_theme", self.theme.lower())

        # entrée nombre pour la dimension maximale de la grille
        self.max_width = Entry(self)
        self.max_width.insert(0, MANAGER.get("MAX_WIDTH"))

        self.max_heigth = Entry(self)
        self.max_heigth.insert(0, MANAGER.get("MAX_HEIGTH"))

        self.max_width_label = Label(self, text="Largeur maximale")
        self.max_heigth_label = Label(self, text="Hauteur maximale")


        # changer la taille des boutons
        self.button_size = Entry(self)
        self.button_size.insert(0, MANAGER.get("BUTTON_SIZE"))

        self.button_size_label = Label(self, text="Taille des boutons")

        # changer les couleurs de fond, de sélection et des boutons
        self.bg_color = Entry(self)
        self.bg_color.insert(0, MANAGER.get("BG_COLOR"))

        self.selected_color = Entry(self)
        self.selected_color.insert(0, MANAGER.get("SELECTED_COLOR"))

        self.candy_bg = Entry(self)
        self.candy_bg.insert(0, MANAGER.get("CANDY_BG"))

        self.bg_color_label = Label(self, text="Couleur de fond")
        self.selected_color_label = Label(self, text="Couleur de sélection")
        self.candy_bg_label = Label(self, text="Couleur des boutons")


        # changer les ressources graphiques
        self.resources = Entry(self)
        self.resources.insert(0, MANAGER.get("IMG_DIR"))

        self.resources_label = Label(self, text="Chemin des ressources")


        # affichage des options (placement dans la fenetre)
        self.max_width_label.grid(row=1, column=0, padx=10, pady=10)
        self.max_width.grid(row=1, column=1, padx=10, pady=10)

        self.max_heigth_label.grid(row=2, column=0, padx=10, pady=10)
        self.max_heigth.grid(row=2, column=1, padx=10, pady=10)

        self.button_size_label.grid(row=3, column=0, padx=10, pady=10)
        self.button_size.grid(row=3, column=1, padx=10, pady=10)

        self.bg_color_label.grid(row=4, column=0, padx=10, pady=10)
        self.bg_color.grid(row=4, column=1, padx=10, pady=10)

        self.selected_color_label.grid(row=5, column=0, padx=10, pady=10)
        self.selected_color.grid(row=5, column=1, padx=10, pady=10)

        self.candy_bg_label.grid(row=6, column=0, padx=10, pady=10)
        self.candy_bg.grid(row=6, column=1, padx=10, pady=10)

        self.resources_label.grid(row=7, column=0, padx=10, pady=10)
        self.resources.grid(row=7, column=1, padx=10, pady=10)

        # theme settings
        self.theme = StringVar(self)
        self.theme.set(MANAGER.get("THEME"))
        self.theme_label = Label(self, text="Thème")

        self.theme_label.grid(row=8, column=0, padx=10, pady=10)
        self.theme_menu = Combobox(self, textvariable=self.theme, values=["Dark", "Light"])
        self.theme_menu.grid(row=8, column=1, padx=10, pady=10)


        # bouton pour appliquer les changements
        self.button = Button(self, text="Appliquer", command=self.apply)
        self.button.grid(row=9, column=0, columnspan=2, pady=10)


    def apply(self):
        """Appliquer les changements"""
        try:
            # récupérer les valeurs des entrées
            tmp_max_width = int(self.max_width.get())
            tmp_max_height = int(self.max_heigth.get())

            tmp_button_size = int(self.button_size.get())

            tmp_bg_color = self.bg_color.get()
            tmp_selected_color = self.selected_color.get()
            tmp_candy_bg = self.candy_bg.get()

            tmp_ressources_path = self.resources.get()
            tmp_theme = self.theme.get()

            # vérifer si le chemin des ressources est valide et si il contient Candy[1-5]
            if os.path.exists(tmp_ressources_path):
                if os.walk(tmp_ressources_path):
                    content = os.listdir(tmp_ressources_path)
                    print([f"Candy{i}" for i in range(1, 6)])
                    print(content)
                    if not all([f"Candy{i}.png" in content for i in range(1, 6)]):
                        raise ValueError("Le dossier ne contient pas les ressources nécessaires.")
                    
                    else :
                        # sauvegarder les changements
                        MANAGER.data["IMG_DIR"] = tmp_ressources_path
                        MANAGER.data["MAX_WIDTH"] = tmp_max_width
                        MANAGER.data["MAX_HEIGTH"] = tmp_max_height
                        MANAGER.data["BUTTON_SIZE"] = tmp_button_size
                        MANAGER.data["BG_COLOR"] = tmp_bg_color
                        MANAGER.data["SELECTED_COLOR"] = tmp_selected_color
                        MANAGER.data["CANDY_BG"] = tmp_candy_bg
                        MANAGER.data["THEME"] = 'Light' if tmp_theme == "Light" else "Dark"

                        MANAGER.save()
                    
                else:
                    raise ValueError("Le chemin spécifié n'est pas un dossier.")


        except Exception as e:
            # si une erreur est survenue, afficher un message d'erreur et restaurer les valeurs par défaut
            class error_details:
                def __init__(self, error, message):
                    self.error = error
                    self.message = message

                    self.__name__ =type(error).__name__

                def __str__(self):
                    return self.message + "\n" + str(self.error)
                
                def __type__(self):
                    return type(self.error)
                
            handle_error(error_details(e, "Une erreur est survenue lors de l'application des changements."))

        self.destroy()

    def update_settings(self):
        self.mainloop()


def open_settings():
    """Ouvre la fenêtre de paramètres"""
    s = Settings()
    s.update_settings()

