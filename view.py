def Menu_Principal():
    print("bienvenue dans chessLeague ")
    print("voulez-vous :\n \t 1 - menu des joueurs \n \t 0 - quitter")
    response = int(input("=>"))
    return response


def Menu_Player():
    print("bienvenue dans le menu des joueurs \n")
    print("voulez-vous : \n \t 1 - afficher la liste des joueurs \n \t 2 - creer un nouveau joueur \n \t 0 - quitter")
    response = int(input("=>"))
    return response


def view_newPlayer():
    print("creation d'un nouveau joueurs")
    info_player = {
        'nom': input("nom : "),
        'age': input("age : ")
    }
    return info_player


def view_Info_Player(i, name, age):
    print('\tjoueurs #' + str(i))
    print('name : ' + name)
    print('age : ' + age + '\n')
