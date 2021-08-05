import values as values


def MenuTournament():
    """
    first menu for managing tournament
    :return: response: int: witch correspond to the selected answer/button
    """
    print("bienvenu dans le menu des tournois")
    print("voulez-vous : ")
    print("\t 1 - creer un nouveau tournois")
    print("\t 2 - afficher tout les tournois ")  # this line bealong to the rapport menu
    print("\t 3 - initialiser un tournoi")  # does it's still work well ?
    print("\t 0 - menu principal")
    response = int(input("=> "))
    return response


def NewTournament():
    """
    ask info with input for creating a new tournament
    :return: info_tournament: dict: contains all the info for a new tournament
    """
    print("bienvenue sur la page de creation de tournoi")
    print("creation d'un nouveau tournois")
    info_tournament = {
        "name": input("nom du tournois: "),
        "location": input("location du tournoi: "),
        "number_of_player": input("nombres de joueurs: "),
        "start_day": input("jour de debut: "),
        "end_day": input("jour de fin: "),
        "month": input("mois: "),
        "year": input("année: ")
    }
    return info_tournament


def MenuTournamentInitialized(tournament):
    """
    second menu when you initialized a tournament
    :param tournament: instance of Tournament class
    :return: response: int: witch correspond to the selected answer/button
    """
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


def MenuActiveTournament(tournament):
    """
    third menu to manage evrything inside the tournament like player assiged turn and all that shit
    :param tournament: instance of Tournament class
    :return: response: int: witch correspond to the selected answer/button
    """
    print("bienvenu dans le menu du " + tournament.name)
    print("\tde la ville de " + tournament.location)
    print("\tle tournois compte " + str(len(tournament.players_list)) + "/" + str(
        tournament.number_of_player) + "inscrit")
    print()
    print("voulez vous : ")
    print("\t 1 - afficher la liste des joueurs ")
    print("\t 2 - creer un nouveau joueur ")
    print("\t 3 - Initaliser un joueur depuis la base de donné")
    print("\t 4 - generer le premier tour")
    print("\t 5 - lancer le tournoi")
    print("\t 0 - menu principal")
    response = int(input("=> "))
    return response


def ViewInfoTournament(i, tournament):
    """
    print the basic info of a tournament
    ideal to print a enumeration of tournament
    :param i: index of the tournament
    :param tournament: instance of Tournament class
    :return: nothing
    """
    print('\tTournoi #' + str(i))
    print('name : ' + tournament.name)
    print('location : ' + tournament.location + '\n')


def ViewInfoMatch(player1, player2, i=1):
    print(f'match #{i}:\t {player1.name} / {player2.name}')


def MenuActiveTurn(tournament):
    if tournament.turn_list.index(tournament.active_turn) == 0:
        print('bienvenu dans le premier tour\n')
    else:
        print('bienvenu dans le ' + str(tournament.turn_list.index(tournament.active_turn) + 1) + 'eme tour\n')
    print('voulez vous: ')
    print("\t 1 - afficher la liste des match")
    print("\t 2 - entrez un resultat")
    print("\t 3 - generer le prochain tour ")
    print("\t 0 - menu principal")
    response = int(input("=> "))
    return response
