import pandas as pd


def RapportMenuDisplay():
    """
    view menu
    :return: response: int: witch correspond to the selected answer/button
    """
    print('bienvenue dans le menu des rapport')
    print('voulez-vous :')
    print("\t 1 - faire un rapport de tout les tournoi")
    print("\t 2 - faire un rapport de tout les joueurs par ordre alphabetique")
    print("\t 3 - faire un rapport de tout les joueurs par rangs")
    print('\t 4 - faire un rapport sur un tournoi')
    print('\t 0 - retour')
    response = int(input("=> "))
    return response


def RapportTournamentMenuDisplay():
    """
    view menu
    :return: response: int: witch correspond to the selected answer/button
    """
    print('bienvenue dans le menu des rapport de tournoi')
    print('voulez-vous :')
    print("\t 1 - faire un rapport de tout les joueurs par ordre alphabetique")
    print('\t 2 - faire un rapport de tout les joueurs par rangs')
    print('\t 3 - faire un rapport de tout les tours')
    print('\t 4 - faire un rapport de tout les match')
    print('\t 0 - retour')
    response = int(input("=> "))
    return response


def AllTurnRapport(turn_data):
    """
     display
    :param turn_data:
    :return:
    """
    turn_data_frame = pd.DataFrame.from_dict(turn_data)
    turn_data_frame = turn_data_frame[['name', 'is_over',
                                       'start_date', 'end_date']]
    print(turn_data_frame)


def AllMatchRapport(tournament):
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
    print('\n')


def AllTournamentRapport(tournament_list=None):
    """
    display
    :param tournament_list:
    :return:
    """
    tournament_data_frame = pd.DataFrame.from_dict(tournament_list)
    print(tournament_data_frame[
              ['name', 'location', 'number_of_player', 'start_day', 'end_day',
               'month', 'year',
               'description', 'time_mode']], "\n")


def AllPlayerRapport(players_list=None, order=0):
    """
    display
    :param order:
    :param players_list:
    :return:
    """
    players_data_frame = pd.DataFrame.from_dict(players_list)
    if order == 1:
        print(players_data_frame.sort_values(by='nom'), '\n')
    elif order == 2:
        print(players_data_frame.sort_values(by='rank'), '\n')
    elif order == 0:
        print(players_data_frame, '\n')
