def menu_tournament():
    """
    first menu for managing tournament
    :return: response: int: witch correspond to the selected answer/button
    """
    print("bienvenu dans le menu des tournois")
    print("voulez-vous : ")
    print("\t 1 - creer un nouveau tournois")
    print("\t 2 - afficher tout les tournois ")
    print("\t 3 - initialiser un tournoi")
    print("\t 0 - retour")
    response = input("=> ")
    return response


def new_tournament():
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
        "year": input("année: "),
        "time_mode": input(
            "mode de jeux(un bullet, un blitz ou un coup rapide): "),
        "description": input("description: ")

    }
    return info_tournament


def menu_tournament_initialized(tournament):
    """
    second menu when you initialized a tournament
    :param tournament: instance of Tournament class
    :return: response: int: witch correspond to the selected answer/button
    """
    print("bienvenu dans le menu des tournois ")
    print(
        "un tournoi est actuellement initialiser \n"
        "\tNom du tournoi : " + tournament.name + "\n"
        "\tVille du tournoi : " + tournament.location
    )
    print("voulez-vous : ")
    print("\t 1 - creer un nouveau tournois")
    print("\t 2 - acceder au tournoi initialisé")
    print("\t 0 - retour")
    response = int(input("=> "))
    return response


def menu_active_tournament(tournament):
    """
    third menu to manage evrything inside the tournament like player assiged
    turn and all that shit
    :param tournament: instance of Tournament class
    :return: response: int: witch correspond to the selected answer/button
    """
    print("bienvenu dans le menu du " + tournament.name)
    print("\tde la ville de " + tournament.location)
    print("\tle tournois compte " + str(
        len(tournament.players_list)) + "/" + str(
        tournament.number_of_player) + "inscrit")

    print()
    print("voulez vous : ")
    print("\t 1 - afficher la liste des joueurs ")
    print("\t 2 - creer un nouveau joueur ")
    print("\t 3 - Initaliser un joueur depuis la base de donné")
    print("\t 4 - generer le premier tour")
    print("\t 5 - lancer le tournoi")
    print("\t 0 - retour")
    response = input("=> ")
    return response


def view_info_tournament(i, tournament):
    """
    print the basic info of a tournament
    ideal to print a enumeration of tournament
    :param i: index of the tournament
    :param tournament: instance of Tournament class
    :return: nothing
    """
    print("\tTournoi #" + str(i))
    print("name : " + tournament.name)
    print("location : " + tournament.location + "\n")


def view_info_match(match, i=1):
    print(f'match #{i}:\t {match.player1.name}{match.player1.score_in_game}'
          f'{match.player2.name}{match.player2.score_in_game}')


def menu_active_turn(tournament):
    if tournament.turn_list.index(tournament.active_turn) == 0:
        print("bienvenu dans le premier tour\n")
    else:
        print('bienvenu dans le ' + str(tournament.turn_list.index(
            tournament.active_turn) + 1) + 'eme tour\n')
    print('voulez vous: ')
    print("\t 1 - afficher la liste des match")
    print("\t 2 - entrez un resultat")
    print("\t 3 - generer le prochain tour ")
    print("\t 0 - retour")
    response = int(input("=> "))
    return response


def tournament_is_full(tournament):
    print(
        "le nombre defini de "
        + str(tournament.number_of_player)
        + " joueur est atteint\n")
