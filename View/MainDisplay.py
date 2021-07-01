def Menu_Principal():
    """
    first menu to chose between all menu
    :return:
    """
        print("bienvenue dans chessLeague ")
        print("voulez-vous :")
        print("\t 1 - menu des joueurs ")
        print("\t 2 - menu des championat")
        print("\t 0 - quitter")
        response = int(input("=> "))
        return response