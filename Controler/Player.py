import Model.Player
import View.Player


class PlayerController:
    @staticmethod
    def NewPlayer():
        temp_player = View.Player.View.new_player()
        temp_player = Model.Player.Player(temp_player)
        temp_player.Save()

    @staticmethod
    def PrintAllPlayer():
        print(Model.Player.Player.All())

    @staticmethod
    def PlayerMenu():
        is_open = True
        while is_open:
            response = View.Player.View.MenuPlayer()
            if response == 1:
                PlayerController.PrintAllPlayer()
            elif response == 2:
                PlayerController.NewPlayer()
            elif response == 3:
                Model.Player.Player.Reset()
            elif response == 0:
                is_open = False
