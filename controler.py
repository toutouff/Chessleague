from model import Player
from view import *


class PlayerController:
    @staticmethod
    def NewPlayer():
        Player(ViewPlayer.view_newPlayer())

    @staticmethod
    def PrintAllPlayer():
        print(Player.All())

    @staticmethod
    def PlayerMenu():
        is_open = True
        while is_open:
            response = ViewPlayer.MenuPlayer()
            if response == 1:
                PlayerController.PrintAllPlayer()
            elif response == 2:
                PlayerController.NewPlayer()
            elif response == 3:
                Player.Reset()
            elif response == 0:
                is_open = False


class MainController:
    @staticmethod
    def MainMenu():
        is_open = True
        while is_open:
            response = ViewMain.Menu_Principal()
            if response == 1:
                PlayerController.PlayerMenu()
            elif response == 2:
                TournamentController.TournamentMenu()
            elif response == 0:
                print("vous avez quitter")
                is_open = False


class TournamentController:
    @staticmethod
    def TournamentMenu():
        is_open = True
        while is_open:
            response = ViewTournament.MenuTournament()
            if response == 1:
                TournamentController.NewTournament()
            elif response == 0:
                is_open = False
    @staticmethod
    def NewTournament():
        print(ViewTournament.NewTournament())
