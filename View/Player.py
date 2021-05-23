class View:
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
    def view_Info_Player(i, name, first_name):
        print('\tjoueurs #' + str(i))
        print('name : ' + name)
        print('age : ' + first_name + '\n')