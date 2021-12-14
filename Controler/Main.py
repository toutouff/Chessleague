from Controler import Player
from Controler import Tournament
from Controler import Rapport
from View import MainDisplay


def main_menu():
    """
    use the response from the main view
    and make make a decision
    :return: nothing
    """
    is_open = True
    while is_open:
        response = MainDisplay.menu_principal()
        if response == str(1):
            Player.player_menu()
        elif response == str(2):
            Tournament.tournament_menu()
        elif response == str(3):
            Rapport.rapport_menu()
        elif response == str(0):
            print("vous avez quitter")
            is_open = False