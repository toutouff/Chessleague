from Controler import Player
from Controler import Tournament
from View import MainDisplay


def MainMenu():
    """
    use the response from the main view
    and make make a decision
    :return: nothing
    """
    is_open = True
    while is_open:
        response = MainDisplay.ViewMain.Menu_Principal()
        if response == 1:
            Player.PlayerController.PlayerMenu()
        elif response == 2:
            Tournament.TournamentController.TournamentMenu()
        elif response == 0:
            print("vous avez quitter")
            is_open = False
