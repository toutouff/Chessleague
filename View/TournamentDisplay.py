from Controler.InputChecker import Checkinput

def menu_tournament():
    """
    first menu for managing tournament
    :return: response: int: witch correspond to the selected answer/button
    """
    print("Bienvenu Dans le menu des tournois")
    print("Voulez-vous : ")
    print("\t 1 - Créer un nouveau tournoi")
    print("\t 2 - Afficher tout les tournois ")
    print("\t 3 - Initialiser un tournoi")
    print("\t 0 - Retour")
    return Checkinput.int("=> ")


def new_tournament():
    """
    ask info with input for creating a new tournament
    :return: info_tournament: dict: contains all the info for a new tournament
    """
    print("Bienvenue sur la page de création de tournoi")
    print("création d'un nouveau tournoi")
    info_tournament = {
        "name": Checkinput.str("nom du tournois: "),
        "location": Checkinput.str("location du tournoi: "),
        "number_of_player": Checkinput.pair("nombre de joueurs: "),
        "start_day": Checkinput.int("jour de début: "),
        "end_day": Checkinput.int("jour de fin: "),
        "month": Checkinput.int("mois: "),
        "year": Checkinput.int("année: "),
        "time_mode": Checkinput.str(
            "mode de jeux(un bullet, un blitz ou un coup rapide): "),
        "description": Checkinput.str("description: ")

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
        "un tournoi est actuellement initialisé \n"
        "\tNom du tournoi : " + tournament.name + "\n"
        "\tVille du tournoi : " + tournament.location
    )
    print("voulez-vous : ")
    print("\t 1 - créer un nouveau tournoi")
    print("\t 2 - accéder au tournoi initialisé")
    print("\t 0 - retour")
    return Checkinput.int("=> ")


def menu_active_tournament(tournament):
    """
    third menu to manage evrything inside the tournament like player assiged
    turn and all that shit
    :param tournament: instance of Tournament class
    :return: response: int: witch correspond to the selected answer/button
    """
    print("Bienvenu dans le menu du " + tournament.name)
    print("\tde la ville de " + tournament.location)
    print("\tle tournoi compte " + str(
        len(tournament.players_list)) + "/" + str(
        tournament.number_of_player) + "inscrit")

    print()
    print("voulez vous : ")
    print("\t 1 - Afficher la liste des joueurs ")
    print("\t 2 - Créer un nouveau joueur ")
    print("\t 3 - Initaliser un joueur depuis la base de données")
    print("\t 4 - Générer le premier tour")
    print("\t 5 - Lancer le tournoi")
    print("\t 0 - Retour")
    return Checkinput.int("=>")


def view_info_tournament(i, tournament):
    """
    print the basic info of a tournament
    ideal to print a enumeration of tournament
    :param i: index of the tournament
    :param tournament: instance of Tournament class
    :return: nothing
    """
    print("\tTournoi #" + str(i))
    print("nom : " + tournament.name)
    print("location : " + tournament.location + "\n")


def view_info_match(match, i=1):
    print(f'match #{i}:\t {match.player1.name} {match.player1.score_in_game}'
          f' {match.player2.name} {match.player2.score_in_game}')


def menu_active_turn(tournament):
    if tournament.turn_list.index(tournament.active_turn) == 0:
        print("Bienvenu dans le premier tour\n")
    else:
        print("Bienvenu dans le " + str(tournament.turn_list.index(
            tournament.active_turn) + 1) + "eme tour\n")
    print("Voulez vous: ")
    print("\t 1 - Afficher la liste des match")
    print("\t 2 - Entrez un resultat")
    print("\t 3 - Générer le prochain tour ")
    print("\t 0 - Retour")
    return Checkinput.int("=>")


def tournament_is_full(tournament):
    print(
        "Le nombre defini de "
        + str(tournament.number_of_player)
        + " joueurs est atteint\n")
