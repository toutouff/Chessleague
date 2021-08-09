from tinydb import TinyDB
from Controler.Tournament import init_tournament
from View.RapportDisplay import *


def RapportMenu():
    """
    controller
    :return:
    """
    db = TinyDB('db.json')

    is_open = True
    while is_open:
        response = RapportMenuDisplay()
        if response == 1:
            tournament_table = db.table('Tournament')
            AllTournamentRapport(tournament_table.all())
        elif response == 2:
            players_table = db.table('players')
            AllPlayerRapport(players_table.all())
        elif response == 3:
            tournament = init_tournament()
            RapportTournamentMenu(tournament)


def RapportTournamentMenu(tournament):
    """
    controller
    :param tournament:
    :return:
    """
    is_open = True
    while is_open:
        response = RapportTournamentMenuDisplay()
        if response == 1:
            AllPlayerRapport(tournament.players_data)
        elif response == 2:
            AllTurnRapport(tournament.data_tournament['turn_list'])
        elif response == 3:
            AllMatchRapport(tournament.data_tournament['turn_list'])
        elif response == 0:
            is_open = False
