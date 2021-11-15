from tinydb import TinyDB
from Controler.Tournament import init_tournament
from View.RapportDisplay import *


def rapport_menu():
    """
    controller
    :return:
    """
    db = TinyDB("db.json")

    is_open = True
    while is_open:
        response = RapportMenuDisplay()
        if response == 1:
            tournament_table = db.table("Tournament")
            AllTournamentRapport(tournament_table.all())
        elif response == 2:
            players_table = db.table("players")
            AllPlayerRapport(players_table.all(), 1)
        elif response == 3:
            players_table = db.table("players")
            AllPlayerRapport(players_table.all(), 2)
        elif response == 4:
            tournament = init_tournament()
            rapport_tournament_menu(tournament)
        elif response == 0:
            is_open = False


def rapport_tournament_menu(tournament):
    """
    controller
    :param tournament:
    :return:
    """
    is_open = True
    while is_open:
        response = RapportTournamentMenuDisplay()
        if response == 1:
            AllPlayerRapport(tournament.data_tournament["player_list"], 1)
        elif response == 2:
            AllPlayerRapport(tournament.data_tournament["player_list"], 2)
        elif response == 3:
            AllTurnRapport(tournament.data_tournament["turn_list"])
        elif response == 4:
            AllMatchRapport(tournament)
        elif response == 0:
            is_open = False
