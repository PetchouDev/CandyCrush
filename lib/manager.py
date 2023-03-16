import os
import json
import pathlib

BASE_DIR = pathlib.Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "assets" / "data"
IMG_DIR = BASE_DIR / "assets" / "graphics"

KEY = "CandyCrush"





def get_data_from_file() -> bytes:
    """
    Charge les données d'un fichier
    """
    with open(DATA_DIR / "settings.psw", "rb") as file: # Ouverture du fichier en mode binaire
        data = file.read() # Lecture des données

    return data

def xor_data(data: bytes) -> bytes:
    """
    Chiffre ou déchiffre les données
    """
    data = bytearray(data) # Conversion des données en tableau d'octets
    for index, value in enumerate(data):
        data[index] = value ^ ord(KEY[index % len(KEY)])

    return bytes(data)

def get_data() -> dict:
    """
    Charge les données
    """
    data = get_data_from_file()  # Récupération des données
    data = xor_data(data).decode()        # Décryptage des données
    data = json.loads(data)      # Conversion des données en dictionnaire

    return data

def write_data(data: dict) -> None:
    """
    Enregistre les données
    """
    with open(DATA_DIR / "settings.psw", "wb") as file:
        file.write(data)       # Ecriture des données

def save_data(data: dict) -> None:
    """
    Enregistre les données
    """
    # créé le dossier s'il n'existe pas
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
    
    # créée le fichier s'il n'existe pas
    if not os.path.exists(DATA_DIR / "settings.psw"):
        with open(DATA_DIR / "settings.psw", "w") as file:
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
        self.data = get_data()
        
    def save(self):
        save_data(self.data)

    def get(self, key):
        return self.data.get(key)
    
MANAGER = Manager()

if __name__ == "__main__":
    # initialisation des données
    data = {
        "IMG_DIR": "default",
        "MAX_WIDTH": 10,
        "MAX_HEIGTH": 10,
        "BEST_SCORE": 0,
        "BUTTON_SIZE": 50,
        "BG_COLOR": "#CCCCCC",
        "SELECTED_COLOR": "#FFFFCC",
        "CANDY_BG": "#FFFFFF",
        "LAST_PLAYED": "6x6",
    }

    # Enregistrement des données
    save_data(data)

    # test de récupération des données
    data2 = get_data()

    print(data == data2) # True si le test passe
