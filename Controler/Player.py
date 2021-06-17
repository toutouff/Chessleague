from Model import PlayerClass
from View import PlayerDisplay


class PlayerController:
    @staticmethod
    def NewPlayer():
        temp_player = PlayerDisplay.View.new_player()
        temp_player = PlayerClass.Player(temp_player)
        temp_player.Save()

    @staticmethod
    def PrintAllPlayer(players_list):
        i = 0
        for player in players_list:
            name = player.name
            first_name = player.first_name
            i = i + 1
            PlayerDisplay.View.view_Info_Player(i, name, first_name)


    @staticmethod
    def PlayerMenu():
        is_open = True
        while is_open:
            response = PlayerDisplay.View.MenuPlayer()
            if response == 1:
                players_list = PlayerClass.Player.All()
                PlayerController.PrintAllPlayer(players_list)
            elif response == 2:
                PlayerController.NewPlayer()
            elif response == 3:
                PlayerClass.Player.Reset()
            elif response == 0:
                is_open = False
