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


class ViewPlayer:
    @staticmethod
    def MenuPlayer():
        print("bienvenue dans le menu des joueurs \n")
        print("voulez-vous : ")
        print("\t 1 - afficher la liste des joueurs ")
        print("\t 2 - creer un nouveau joueur ")
        print("\t 3 - reset la database")
        print("\t 0 - menu principal")
        response = int(input("=> "))
        return response

    @staticmethod
    def view_newPlayer():
        print("creation d'un nouveau joueurs")
        info_player = {
            "nom": input("nom : "),
            "prenom": input("prenom :"),
            "date de naiscance": input("année de naiscance :"),
            "genre": input("genre :"),
            "rank": input("classement :")
        }
        return info_player

    @staticmethod
    def view_Info_Player(i, name, age):
        print('\tjoueurs #' + str(i))
        print('name : ' + name)
        print('age : ' + age + '\n')


class ViewTournament:
    @staticmethod
    def MenuTournament():
        print("bienvenu dans le menu du tournois")
        print("voulez-vous : ")
        print("\t 1 - creer un nouveau tournois")
        print("\t 0 - menu principal")
        response = int(input("=> "))
        return response
    @staticmethod
    def NewTournament():
        print("creation d'un nouveau tournois")
        info_tournois = {
            "nom": input("nom tournois: ")
        }
        return info_tournois