from string import Template

from Model import PlayerClass, TournamentClass


def RapportMenuDisplay():
    """
    view menu
    :return: response: int: witch correspond to the selected answer/button
    """
    print('bienvenue dans le menu des rapport')
    print('voulez-vous :')
    print("\t 1 - faire un rapport de tous les tournoi")
    print("\t 2 - faire un rapport de tous les joueurs")
    print('\t 3 - faire un rapport sur un tournoi')
    response = int(input("=> "))
    return response


def RapportTournamentMenuDisplay():
    """
    view menu
    :return: response: int: witch correspond to the selected answer/button
    """
    print('bienvenue dans le menu des rapport de tournoi')
    print('voulez-vous :')
    print("\t 1 - faire un rapport de tout les joueurs")
    print('\t 2 - faire un rapport de tout les tours')
    print('\t 3 - faire un rapport de tout les match')
    response = int(input("=> "))
    return response


def AllTurnRapport(turn_data):
    """
    display
    :param turn_data:
    :return:
    """
    turn_template_raw = '| $name | $is_over | $date | $number_of_match |'
    print(Template(turn_template_raw).substitute(name='nom', is_over='est-il-fini', date='date',
                                                 number_of_match='nombre de match'))
    for turn in turn_data:
        print(Template(turn_template_raw).substitute(name=turn['name'], is_over=turn['is_over'], date='',
                                                     number_of_match=len(turn['match_list'])))


def AllMatchRapport(turn_data):
    """
    display
    :param turn_data:
    :return:
    """
    turn_template_raw = '| $name | $is_over | $date | $number_of_match |'
    print(Template(turn_template_raw).substitute(name='nom', is_over='est-il-fini', date='date',
                                                 number_of_match='nombre de match'))
    for turn in turn_data:
        print(Template(turn_template_raw).substitute(name=turn['name'], is_over=turn['is_over'], date='',
                                                     number_of_match=len(turn['match_list'])))
        match_template = '| $player1name | $rank1 | VS | $player2name | $rank2 || $result'
        for match in turn['match_list']:
            player1 = PlayerClass.Player(match['player1'])
            player2 = PlayerClass.Player(match['player2'])
            if hasattr(match, 'result'):
                result = match['result']
                print(Template(match_template).substitute(player1name=player1.first_name[0] + '.' + player1.name,
                                                          rank1=player1.rank,
                                                          player2name=player2.first_name[0] + '.' + player2.name,
                                                          rank2=player2.rank, result=result))
            else:
                print(Template(match_template).substitute(player1name=player1.first_name[0] + '.' + player1.name,
                                                          rank1=player1.rank,
                                                          player2name=player2.first_name[0] + '.' + player2.name,
                                                          rank2=player2.rank, result=match['is_over']))


def AllTournamentRapport(tournament_list=None):
    """
    display
    :param tournament_list:
    :return:
    """
    tournament_template_row = '| $name | $location | $date | $number_of_turn | $time_control | ' \
                              '$description |'
    print(Template(tournament_template_row).substitute(name='nom', location='location', date='date',
                                                       number_of_turn='manches',
                                                       time_control='mode de jeu', description='description'))
    for tournament_data in tournament_list:
        tournament = TournamentClass.Tournament(tournament_data)
        print(Template(tournament_template_row).substitute(name=tournament.name, location=tournament.location,
                                                           date=tournament.start_day + '/' + tournament.month + '/' +
                                                           tournament.year,
                                                           number_of_turn=str(int(tournament.number_of_player / 2)),
                                                           time_control='standard', description='description'))


def AllPlayerRapport(players_list=None):
    """
    display
    :param players_list:
    :return:
    """
    player_template_row = '| $first_name | $name | $birthyear | $sexe | $rank |'
    print(Template(player_template_row).substitute(first_name='prenom', name='nom', birthyear='anne de naiscance',
                                                   sexe='genre', rank='classement'))
    for player_data in players_list:
        player = PlayerClass.Player(player_data)
        print(Template(player_template_row).substitute(first_name=player.first_name, name=player.name,
                                                       birthyear=player.data_player['date de naiscance'],
                                                       sexe=player.data_player['genre'], rank=player.rank))
