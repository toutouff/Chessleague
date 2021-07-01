def MenuPlayer():
    """
    first menu for managing the player
    :return: response: int: witch correspond to the selected answer/button
    """
    print("bienvenue dans le menu des joueurs \n")
    print("voulez-vous : ")
    print("\t 1 - afficher la liste des joueurs ")
    print("\t 2 - creer un nouveau joueur ")
    print("\t 3 - reset la database")
    print("\t 0 - menu principal")
    response = int(input("=> "))
    return response


def newPlayer():
    """
    ask info with input for creating a new player
    :return: info_player: dict: contains all the info for a new player
    """
    print("creation d'un nouveau joueurs")
    info_player = {
        "nom": input("nom : "),
        "prenom": input("prenom :"),
        "date de naiscance": input("année de naiscance :"),
        "genre": input("genre :"),
        "rank": input("classement :")
    }
    return info_player


def ViewInfoPlayer(name, first_name, i=1):
    """
    print the basic info of a player
    ideal to print a enumeration of player
    :param i: the index of the player (default = 1)
    :param name: name of the player
    :param first_name: first name of the player
    :return: nothing
    """
    print('\tjoueurs #' + str(i))
    print('name : ' + name)
    print('prenom : ' + first_name + '\n')
