from tinydb import TinyDB

from Controler.Tournament import init_tournament
from View.RapportDisplay import rapport_menu_display, all_tournament_rapport, \
    all_player_rapport, rapport_tournament_menu_display, all_turn_rapport, \
    all_match_rapport


def rapport_menu():
    """
    controller
    :return:
    """
    db = TinyDB("db.json")

    is_open = True
    while is_open:
        response = int(rapport_menu_display())
        if response == 1:
            tournament_table = db.table("Tournament")
            all_tournament_rapport(tournament_table.all())
        elif response == 2:
            players_table = db.table("players")
            all_player_rapport(players_table.all(), 1)
        elif response == 3:
            players_table = db.table("players")
            all_player_rapport(players_table.all(), 3)
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
        response = rapport_tournament_menu_display()
        if response == 1:
            all_player_rapport(tournament.data_tournament["player_list"], 1)
        elif response == 2:
            all_player_rapport(tournament.data_tournament["player_list"], 2)
        elif response == 3:
            all_turn_rapport(tournament.data_tournament["turn_list"])
        elif response == 4:
            all_match_rapport(tournament)
        elif response == 0:
            is_open = False
