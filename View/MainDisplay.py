from Controler.InputChecker import Checkinput

def menu_principal():
    """
    first menu to chose between all menu
    :return:
    """
    print("Bienvenue dans ChessLeague ")
    print("Voulez-vous :")
    print("\t 1 - Menu des Joueurs ")
    print("\t 2 - Menu des tournoi")
    print("\t 3 - Menu des Rapport")
    print("\t 0 - Quitter")
    return Checkinput.int("=>")
