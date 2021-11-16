from Model import PlayerClass
from View import PlayerDisplay


def new_player():
    """
    get info from PlayerDisplay.new_player()
    witch return a dict with all the info linked to their key
    and create an instance of the PlayerClass
    :return: nothing #but why not return the instance
    """
    temp_player = PlayerDisplay.new_player()
    temp_player = PlayerClass.Player(temp_player)
    temp_player.save()


def print_all_player(players_list):
    """
    :param players_list:
    send it to the Playerdisplay
    """
    i = 0
    for player in players_list:
        name = player.name
        first_name = player.first_name
        i = i + 1
        PlayerDisplay.view_info_player(name, first_name, i)


def player_menu():
    """just as same as all the menu
    get a number from a display"""
    is_open = True
    while is_open:
        response = PlayerDisplay.menu_player()
        if response == 1:
            players_list = PlayerClass.Player.all()
            print_all_player(players_list)
        elif response == 2:
            new_player()
        elif response == 3:
            PlayerClass.Player.reset()
        elif response == 0:
            is_open = False
