from tinydb import *

from Controler import Player
from Model import PlayerClass, TurnClass
from Model import TournamentClass
from View import PlayerDisplay
from View import TournamentDisplay


def TournamentMenu():
    """just a same as all the menu"""
    tournament = None
    is_open = True
    tournament_exist = False
    while is_open:
        if tournament_exist:
            tournament_exist = ActiveTournamentMenu(tournament)
        else:
            response = TournamentDisplay.MenuTournament()
            if response == 1:
                tournament = NewTournament()
                tournament.Save()
                tournament_exist = True
            elif response == 2:
                tournament_list = TournamentClass.Tournament.All()
                PrintAllTournament(tournament_list)
            elif response == 3:
                tournament = init_tournament()
                tournament_exist = True
            elif response == 0:
                is_open = False


def ActiveTournamentMenu(tournament):
    """
    same as the other menu but this time your interacting inside an instance of the Tournament classe
    :param tournament: the instance in question
    :return: nothing
    """
    tournament = tournament
    is_open = True
    while is_open:
        response = TournamentDisplay.MenuActiveTournament(tournament)
        if response == 1:
            Player.PrintAllPlayer(tournament.players_list)
        elif response == 2:
            temp_player = NewPlayer()
            tournament.AddPlayer(temp_player)
        elif response == 3:
            tournament.AddPlayer(InitPlayerByName())
            tournament.UpdatePlayersList()
        elif response == 4:
            tournament.launch()
        elif response == 5:
            launch_tournament(tournament)
        elif response == 0:
            is_open = False
            return False


def NewTournament():
    """
    create a new tournament(so get info from display and send it to the model)
    :return: the instance of the Tournament class created
    """
    tournament = TournamentClass.Tournament(TournamentDisplay.NewTournament())
    return tournament


def NewPlayer():
    """
    get info from PlayerDisplay.newPlayer()
    witch return a dict with all the info linked to their key
    and create an instance of the PlayerClass
    :return: the instance
    """
    info_player = PlayerDisplay.newPlayer()
    temp_player = PlayerClass.Player(info_player)
    temp_player.Save()
    return temp_player


def InitPlayerByName():
    """i have to"""
    i = 1
    db = TinyDB('db.json')
    players_table = db.table('players')
    players_list = players_table.all()
    for player in players_list:
        player = PlayerClass.Player(player)
        PlayerDisplay.ViewInfoPlayer(str(player.name), str(player.first_name), i)
        i += 1
    print('veuillez indiquer le numero du joueur : ')
    result_id = int(input('=>'))
    player_data = players_table.get(doc_id=result_id)
    player = PlayerClass.Player(dict(player_data))
    return player


def PrintAllTournament(tournament_list):
    """
    iter in the param and send it individualy to the display
    :param tournament_list:
    :return:
    """
    i = 0
    for tournament in tournament_list:
        i = i + 1
        TournamentDisplay.ViewInfoTournament(i, tournament)


def init_tournament():
    db = TinyDB('db.json')
    tournament_table = db.table('Tournament')
    tournament_list = tournament_table.all()
    for i, tournament_data in enumerate(tournament_list):  #
        tournament = TournamentClass.Tournament(tournament_data)
        TournamentDisplay.ViewInfoTournament(i + 1, tournament)  #
    print('veuillez indiquer le numero du tournoi : ')
    result_id = int(input('=>'))
    tournament_data = tournament_table.get(doc_id=result_id)
    tournament = TournamentClass.Tournament(dict(tournament_data))
    tournament_players_list = tournament.data_tournament['player_list']
    for player in tournament_players_list:
        player = PlayerClass.Player(player)
        tournament.AddPlayer(player)
    tournament_turns_data = tournament.data_tournament['turn_list']
    for turn_data in tournament_turns_data:
        tournament.active_turn = TurnClass.Turn(turn_data['name'], tournament.number_of_player)
        tournament.turn_list[int(tournament.active_turn.name[6])] = tournament.active_turn
        for i, match_data in enumerate(turn_data['match_list']):
            match = tournament.active_turn.match_list[i]
            match.de_serialize(match_data)
    return tournament


def end_a_match(tournament):
    turn = tournament.active_turn
    for i in range(len(turn.match_list)):
        print(i, turn.match_list[i])
        TournamentDisplay.ViewInfoMatch(turn.match_list[i].player1, turn.match_list[i].player2, i)
    response = input('quelle match est fini ?\n=> ')
    match = turn.match_list[int(response) - 1]
    if not match.is_over:
        match.get_result()
    else:
        print('un score est deja enregitré pour ce match')
    print(match.player1.score_in_game)
    print(match.player2.score_in_game)


def launch_tournament(tournament):
    is_active = True
    while is_active:
        response = TournamentDisplay.MenuActiveTurn(tournament)
        if response == 1:
            for i, match in enumerate(tournament.active_turn.match_list):
                TournamentDisplay.ViewInfoMatch(match.player1, match.player2, i)
        if response == 2:
            end_a_match(tournament)
        if response == 3:
            tournament.nextTurn()
        if response == 0:
            is_active = False
