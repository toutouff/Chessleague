from model import *
from view import *



class PlayerController:
    @staticmethod
    def NewPlayer():
        temp_player = ViewPlayer.new_player()
        temp_player = Player(temp_player)
        temp_player.Save()

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
    @classmethod
    def TournamentMenu(cls):
        tournament = None
        is_open = True
        tournament_exist = False
        while is_open:
            if tournament_exist:
                response = ViewTournament.MenuTournamentInitialized(tournament)
                if response == 1:
                    tournament = TournamentController.NewTournament()
                    tournament_exist = True
                elif response == 2:
                    TournamentController.ActiveTournamentMenu()
                elif response == 0:
                    is_open = False
            else:
                response = ViewTournament.MenuTournament()
                if response == 1:
                    tournament = TournamentController.NewTournament()
                    tournament_exist = True
                elif response == 0:
                    is_open = False

    @classmethod
    def ActiveTournamentMenu(cls,):
        is_open = True
        while is_open:
            response = ViewTournament.MenuActiveTournament(tournament)
            if response == 1:
                print(tournament.players_data)
            elif response == 2:
                temp_player = cls.NewPlayer()
                tournament.AddPlayer(temp_player)
                tournament.Save()
            elif response == 3:
                print("\t soon \n")
                print("tu sais ce qui te reste a faire")
                print("\t soon \n")
            elif response == 4:
                init_player = TournamentController.InitPlayerByName()
                tournament.AddPlayer(init_player)
                tournament.Save()
            elif response == 0:
                is_open = False

    @classmethod
    def NewTournament(cls):
        tournament = Tournament(ViewTournament.NewTournament())
        tournament.Save()
        return tournament

    @classmethod
    def NewPlayer(cls):
        info_player = ViewPlayer.new_player()
        temp_player = Player(info_player)
        return temp_player

    @classmethod
    def InitPlayerByName(cls):
        player = Query()
        player_name = input("=>")
        db = TinyDB('db.json')
        table = db.table('players')
        result = table.search(player.nom == player_name)
        result = result[0]
        temp_player = Player(result)
        return temp_player


#temp_player = TournamentController.NewPlayer()
#