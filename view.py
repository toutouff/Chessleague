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
    def new_player():
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
    @classmethod
    def MenuTournament(cls):
        print("bienvenu dans le menu des tournois")
        print("voulez-vous : ")
        print("\t 1 - creer un nouveau tournois")
        print("\t 0 - menu principal")
        response = int(input("=> "))
        return response

    @classmethod
    def NewTournament(cls):
        print("bienvenue sur la page de creation de tournoi")
        print("creation d'un nouveau tournois")
        info_tournois = {
            "name": input("nom du tournois: "),
            "location": input("location du tournoi: "),
            "start_day": input("jour de debut: "),
            "end_day": input("jour de fin: "),
            "month": input("mois: "),
            "year": input("année: ")
        }
        return info_tournois

    @classmethod
    def MenuTournamentInitialized(cls, tournament):
        print("bienvenu dans le menu des tournois ")
        print("un tournoi est actuellement initialiser \n"
              "\tNom du tournoi : " + tournament.name + "\n"
              "\tVille du tournoi : " + tournament.location)
        print("voulez-vous : ")
        print("\t 1 - creer un nouveau tournois")
        print("\t 2 - acceder au tournoi initialisé")
        print("\t 0 - menu principal")
        response = int(input("=> "))
        return response

    @classmethod
    def MenuActiveTournament(cls, tournament):
        print("bienvenu dans le menu du " + tournament.name)
        print("\tde la ville de " + tournament.location)
        print("\tle tournois compte " + str(tournament.number_of_player) + " inscrit.")
        print("voulez vous : ")
        print("\t 1 - afficher la liste des joueurs ")
        print("\t 2 - creer un nouveau joueur ")
        print("\t 3 - creer un nouveau tour")
        print("\t 4 - Initaliser un joueur depuis la base de donné")
        print("\t 0 - menu principal")
        response = int(input("=> "))
        return response
