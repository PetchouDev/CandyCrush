import os
import json
import pathlib

# gestion des valeurs par défaut
BASE_DIR = pathlib.Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "assets" / "data"
DEFAULT_IMG_DIR = pathlib.Path(__file__).parent.parent / "assets" / "graphics"

# clé de chiffrement/déchiffrement
KEY = "CandyCrush"

# obtenir le système d'exploitation
system = None
if os.name == "nt":
    system = "windows"
elif os.name == "posix":
    system = "linux"

# obtenir le chemin de sauvegarde
if system == "windows":
    SAVE_PATH = pathlib.Path(os.getenv("APPDATA")) / "3Mousquetaires" / "CandyCrush"

elif system == "linux":
    SAVE_PATH = pathlib.Path(os.getenv("HOME")) / "3Mousquetaires" / "CandyCrush"

# créer le dossier de sauvegarde s'il n'existe pas
if not os.path.exists(SAVE_PATH):
    os.makedirs(SAVE_PATH, exist_ok=True)



# charger les données depuis le fichier
def get_data_from_file() -> bytes:
    """
    Charge les données d'un fichier
    """
    with open(SAVE_PATH / "settings.psw", "rb") as file: # Ouverture du fichier en mode binaire
        data = file.read() # Lecture des données

    return data

# chiffre/déchiffre les données
def xor_data(data: bytes) -> bytes:
    """
    Chiffre ou déchiffre les données
    """
    data = bytearray(data) # Conversion des données en tableau d'octets
    for index, value in enumerate(data):
        data[index] = value ^ ord(KEY[index % len(KEY)])

    return bytes(data)

# charge les données
def get_data() -> dict:
    """
    Charge les données
    """
    data = get_data_from_file()  # Récupération des données
    data = xor_data(data).decode()        # Décryptage des données
    data = json.loads(data)      # Conversion des données en dictionnaire

    return data

# exporte  les données
def write_data(data: dict) -> None:
    """
    Enregistre les données
    """
    with open(SAVE_PATH / "settings.psw", "wb") as file:
        file.write(data)       # Ecriture des données

# enregistre les données
def save_data(data: dict) -> None:
    """
    Enregistre les données
    """
    # créé le dossier s'il n'existe pas
    if not os.path.exists(SAVE_PATH):
        os.makedirs(SAVE_PATH, exist_ok=True)
    
    # créée le fichier s'il n'existe pas
    if not os.path.exists(SAVE_PATH / "settings.psw"):
        with open(SAVE_PATH / "settings.psw", "w") as file:
            pass
        
    data = json.dumps(data)     # Conversion des données en chaîne de caractères
    data = xor_data(data.encode()) # Cryptage des données
    write_data(data)            # Enregistrement des données



def load_manager():
    """
    Charge les paramètres
    """
    try:
        return Manager(), "Success"
    
    except Exception as e:
        return 0, e
    
class Manager:
    def __init__(self):
        if not self.check_existance():
            self.init()
        self.data = get_data()

        if self.data["IMG_DIR"] == "default":
            self.data["IMG_DIR"] = str(DEFAULT_IMG_DIR)

        
    def save(self):
        tmp = self.data.copy()
        if self.data["IMG_DIR"] == str(DEFAULT_IMG_DIR):
            tmp["IMG_DIR"] = "default"
        save_data(tmp)

    def get(self, key):
        return self.data.get(key)
    
    def set(self, key, value):
        self.data[key] = value
        self.save()
    
    def init(self):
        # initialisation des données
        self.data = {
            "IMG_DIR": str(DEFAULT_IMG_DIR),
            "MAX_WIDTH": 8,
            "MAX_HEIGTH": 8,
            "BEST_SCORE": 0,
            "BUTTON_SIZE": 100,
            "BG_COLOR": "#D778E3",
            "SELECTED_COLOR": "#f4fc77",
            "CANDY_BG": "#b1f6fc",
            "LAST_PLAYED": [6, 6, 1],
            "THEME": "Dark",
        }

        self.save()
    
    def check_existance(self):
        if not os.path.exists(SAVE_PATH / "settings.psw"):
            return False
        return True


MANAGER = Manager()



if __name__ == "__main__":
    manager = Manager()
    manager.init()

    # vérifier que les données sont bien enregistrées
    print(manager.data)

    test = manager.data.copy()

    # charger les données
    manager.__init__()

    print(manager.data)

    # vérifier que les données sont bien chargées
    print(manager.data == test)


