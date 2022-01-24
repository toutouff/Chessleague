import pandas as pd

from Controler.InputChecker import Checkinput


def rapport_menu_display():
    """
    view menu
    :return: response: int: witch correspond to the selected answer/button
    """
    print("Bienvenue dans le menu des rapports")
    print("Voulez-vous :")
    print("\t 1 - Faire un rapport de tout les tournois")
    print("\t 2 - Faire un rapport de tout les joueurs par ordre alphabetique")
    print("\t 3 - Faire un rapport de tout les joueurs par rang")
    print("\t 4 - Faire un rapport sur un tournoi")
    print("\t 0 - Retour")
    return Checkinput.int("=> ", 4)


def rapport_tournament_menu_display():
    """
    view menu
    :return: response: int: witch correspond to the selected answer/button
    """
    print("Bienvenue dans le menu des rapports de tournoi")
    print("Voulez-vous :")
    print("\t 1 - Faire un rapport de tout les joueurs par ordre alphabetique")
    print("\t 2 - Faire un rapport de tout les joueurs par classement")
    print("\t 3 - Faire un rapport de tout les tours")
    print("\t 4 - Faire un rapport de tout les matchs")
    print("\t 0 - Retour")
    return Checkinput.int("=>", 4)


def all_turn_rapport(turn_data):
    """
     display
    :param turn_data:
    :return:
    """
    turn_data_frame = pd.DataFrame.from_dict(turn_data)
    turn_data_frame = turn_data_frame[['name', 'is_over',
                                       'start_date', 'end_date']]
    print(turn_data_frame)


def all_match_rapport(tournament):
    """
    display
    :param tournament:Model.TournamentClass.Tournament
    :return:
    """
    for turn in tournament.turn_list:
        table = []
        if turn.is_exist:
            for match in turn.match_list:
                row = {'Player_1': match.player1.first_name[
                                       0] + '.' + match.player1.name,
                       'Result': match.results,
                       'Player_2': match.player2.first_name[
                                       0] + '.' + match.player2.name}
                table.append(row)
            print(turn.name)
            print(pd.DataFrame(table))
    print("\n")


def all_tournament_rapport(tournament_list=None):
    """
    display
    :param tournament_list:
    :return:
    """
    tournament_data_frame = pd.DataFrame.from_dict(tournament_list)
    print(
        tournament_data_frame[
            [
                "name",
                "location",
                "number_of_player",
                "start_day",
                "end_day",
                "month",
                "year",
                "description",
                "time_mode",
            ]
        ],
        "\n",
    )


def all_player_rapport(players_list=None, order=0):
    """
    display
    :param order:
    :param players_list:
    :return:
    """
    players_data_frame = pd.DataFrame.from_dict(players_list)
    if order == 1:
        print(players_data_frame.sort_values(by="nom"), "\n")
    elif order == 2:
        print(players_data_frame.sort_values(by="score in game",
                                             ascending=False), "\n")
    elif order == 3:
        print(players_data_frame.sort_values(by="rank"), "\n")
    elif order == 0:
        print(players_data_frame, "\n")
