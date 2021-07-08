from Model import PlayerClass
from View import PlayerDisplay


def NewPlayer():
    """
    get info from PlayerDisplay.newPlayer()
    witch return a dict with all the info linked to their key
    and create an instance of the PlayerClass
    :return: nothing #but why not return the instance
    """
    temp_player = PlayerDisplay.newPlayer()
    temp_player = PlayerClass.Player(temp_player)
    temp_player.Save()


def PrintAllPlayer(players_list):
    """
    :param players_list:
    send it to the Playerdisplay
    """
    i = 0
    for player in players_list:
        name = player.name
        first_name = player.first_name
        i = i + 1
        PlayerDisplay.ViewInfoPlayer(name, first_name, i)


def PlayerMenu():
    """just as same as all the menu
    get a number from a display """
    is_open = True
    while is_open:
        response = PlayerDisplay.MenuPlayer()
        if response == 1:
            players_list = PlayerClass.Player.All()
            PrintAllPlayer(players_list)
        elif response == 2:
            NewPlayer()
        elif response == 3:
            PlayerClass.Player.Reset()
        elif response == 0:
            is_open = False
