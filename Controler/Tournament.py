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
            if response == str(1):
                tournament = NewTournament()
                tournament.Save()
                tournament_exist = True
            elif response == str(2):
                tournament_list = TournamentClass.Tournament.All()
                PrintAllTournament(tournament_list)
            elif response == str(3):
                tournament = init_tournament()
                tournament_exist = True
            elif response == str(0):
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
        if response == str(1):
            Player.PrintAllPlayer(tournament.players_list)
        elif response == str(2):
            if not tournament.number_of_player == len(tournament.players_list):
                temp_player = NewPlayer()
                tournament.AddPlayer(temp_player)
            else:
                TournamentDisplay.TournamentIsFull(tournament)
        elif response == str(3):
            if not tournament.number_of_player == len(tournament.players_list):
                tournament.AddPlayer(InitPlayerByName())
                tournament.UpdatePlayersList()
            else:
                TournamentDisplay.TournamentIsFull(tournament)
        elif response == str(4):
            tournament.launch()
        elif response == str(5):
            if tournament.active_turn == 0:
                tournament.launch()
                launch_tournament(tournament)
                update_turn_list(tournament)
            else:
                launch_tournament(tournament)
                update_turn_list(tournament)
        elif response == str(0):
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
    tournament = TournamentClass.Tournament(tournament_data)
    tournament.db_id = result_id
    tournament.players_list = []  # reset de la list de joueurs
    for player_data in tournament_data['player_list']:
        tournament.players_list.append(PlayerClass.Player(
            player_data))  # ajout des joueurs a partir du dict players_list contenu dans tournament_data

    for y, turn_data in enumerate(tournament_data['turn_list']):  # deserialisation des tours
        tournament.turn_list[y].deserialize(turn_data)

    for i, turn in enumerate(tournament.turn_list):
        if turn.is_exist:
            for y, match in enumerate(turn.match_list):
                player_id_1 = tournament.data_tournament['player_list'].index(tournament.data_tournament['turn_list'][i]
                                                                              ['match_list'][y]['player1'])
                player_id_2 = tournament.data_tournament['player_list'].index(tournament.data_tournament['turn_list'][i]
                                                                              ['match_list'][y]['player2'])
                match.player1 = tournament.players_list[player_id_1]
                match.player2 = tournament.players_list[player_id_2]
                if match.is_over:
                    if match.results == '10':
                        match.player1.score_in_game += 1
                        match.player2.score_in_game += 0
                    elif match.results == '01':
                        match.player1.score_in_game += 0
                        match.player2.score_in_game += 1
                    elif match.results == '00' or match.results == '11':
                        match.player1.score_in_game += 0.5
                        match.player2.score_in_game += 0.5
            tournament.active_turn = turn

    return tournament


def end_a_match(tournament):
    turn = tournament.active_turn
    match_over = 0
    for i in range(len(turn.match_list)):
        if not turn.match_list[i].is_over:
            TournamentDisplay.ViewInfoMatch(turn.match_list[i], i + 1)
        elif turn.match_list[i].is_over:
            match_over = match_over + 1
    if len(turn.match_list) == match_over:
        print('le tour est fini')
    else:
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
                TournamentDisplay.ViewInfoMatch(match, i + 1)
        if response == 2:
            end_a_match(tournament)
            update_turn_list(tournament)
        if response == 3:
            if OverTester(tournament.active_turn.match_list):
                tournament.active_turn.is_over = True
                tournament.nextTurn()
                update_turn_list(tournament)
            else:
                print("tout les match ne sont pas fini")
        if response == 0:
            is_active = False


def update_turn_list(tournament):
    tournament.turns_data = []
    for turn in tournament.turn_list:
        if turn.is_exist:
            tournament.turns_data.append(turn.serialize())
    db = TinyDB('db.json')
    tournament_table = db.table('Tournament')
    tournament_table.update({'turn_list': tournament.turns_data}, doc_ids=[tournament.db_id])


def OverTester(match_list):
    """
    test if all the match/turn of a list a ended or not
    :param match_list: series of match class or turn class
    :return: TRUE id
    """
    number_of_end_match = 0
    for match in match_list:
        if match.is_over:
            number_of_end_match = number_of_end_match + 1
    if number_of_end_match == len(match_list):
        return True
