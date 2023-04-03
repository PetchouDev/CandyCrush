import sys
from tkinter import *

# affichage des messages d'erreur
def handle_error(log: Exception):
    """Affiche le log d'erreur"""
    # crée la fenêtre    
    root = Tk()
    root.title("Candy Crush")

    # gestiion de la taille de la fenêtre
    x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
    y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
    root.geometry("+%d+%d" % (x, y))

    # afficher une erreur
    l1 = Label(root, text="Une erreur est survenue.").pack(pady=10)
    l2 = Label(root, text=log).pack(pady=10)

    # détails sous forme type ValueError: invalid literal for int() with base 10: 'a' et un boutton détails
    ErrorType = type(log).__name__
    ErrorDetails = str(log)

    # affichage des détails
    def show_details():
        details = Toplevel()
        details.title("Détails de l'erreur")
        details.resizable(False, False)
        Label(details, text=ErrorType).pack(pady=10)
        Label(details, text=ErrorDetails).pack(pady=10)
        Button(details, text="Fermer", command=details.destroy).pack(pady=10)
        try:
            details.geometry("{}x{}".format(l1.reqwidth() + l2.reqwidth() + 50, l1.reqheight() + l2.reqheight() + 50))
        except:
            details.geometry("500x200")


    # boutton détails
    b1 = Button(root, text="Détails", command=show_details).pack(pady=10)

    # boutton quitter
    b2 = Button(root, text="Quitter", command=root.destroy).pack(pady=10)


    # ajuster la taille de la fenêtre
    try:
        root.geometry("{}x{}".format(l1.reqwidth() + l2.reqwidth() + b1.reqwidth() + b2.reqwidth() + 50, l1.reqheight() + l2.reqheight() + b1.reqheight() + b2.reqheight() + 50))
    except:
        root.geometry("500x200")
    root.resizable(False, False)

    # afficher la fenêtre
    root.mainloop()

    # quitter le script
    if str(log) != "La taille de la grille est invalide, utilisation de la dernière taille valide.":
        sys.exit(1)


