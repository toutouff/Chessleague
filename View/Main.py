class ViewMain:
    @staticmethod
    def Menu_Principal():
        print("bienvenue dans chessLeague ")
        print("voulez-vous :")
        print("\t 1 - menu des joueurs ")
        print("\t 2 - menu des championat")
        print("\t 0 - quitter")
        response = int(input("=> "))
        return response
