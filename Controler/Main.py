from Controler import Player
from Controler import Tournament
from Controler import Rapport
from View import MainDisplay


def MainMenu():
    """
    use the response from the main view
    and make make a decision
    :return: nothing
    """
    is_open = True
    while is_open:
        response = MainDisplay.Menu_Principal()
        if response == str(1):
            Player.PlayerMenu()
        elif response == str(2):
            Tournament.TournamentMenu()
        elif response == str(3):
            Rapport.RapportMenu()
        elif response == str(0):
            print("vous avez quitter")
            is_open = False
