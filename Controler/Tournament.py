from tinydb import *

from Controler import Player
from Model import PlayerClass
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
            response = TournamentDisplay.MenuTournamentInitialized(tournament)
            if response == 1:
                tournament = NewTournament()
                tournament_exist = True
            elif response == 2:
                cls.ActiveTournamentMenu(tournament)
            elif response == 0:
                is_open = False
        else:
            response = TournamentDisplay.MenuTournament()
            if response == 1:
                tournament = NewTournament()
                tournament_exist = True
            elif response == 2:
                tournament_list = TournamentClass.Tournament.All()
                PrintAllTournament(tournament_list)
            elif response == 3:
                tournament = InitTournament()
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
            tournament.save()
        elif response == 3:
            print("\t soon \n")
            print("tu sais ce qui te reste a faire")
            print("\t soon \n")
        elif response == 4:
            init_player = InitPlayerByName()
            tournament.AddPlayer(init_player)
            tournament.Save()
        elif response == 0:
            is_open = False


def NewTournament():
    """
    create a new tournament(so get info from display and send it to the model)
    :return: the instance of the Tournament class created
    """
    tournament = TournamentClass.Tournament(TournamentDisplay.NewTournament())
    tournament.Save()
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
    Player.PrintAllPlayer(PlayerClass.Player.All())
    player = Query()
    player_name = input("=>")
    db = TinyDB('db.json')
    table = db.table('players')
    result = table.search(player.nom == player_name)
    result = result[0]
    temp_player = PlayerClass.Player(result)
    return temp_player


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


def InitTournament():
    i = 0
    tournament_list = TournamentClass.Tournament.All()
    cls.PrintAllTournament(tournament_list)
    tournament = Query()
    db = TinyDB('db.json')
    table = db.table('Tournament')
    result_list = table.search(tournament.location == input('indiquer la location du tournoie :\n=>'))
    for result in result_list:
        i = i + 1
        print('#' + str(i), result)
    print('veuillez indiquer le numero du tournoi : ')
    chosen_result_id = input('=>')
    result = result_list[(int(chosen_result_id)) - 1]
    tournament = TournamentClass.Tournament(result)
    return tournament
