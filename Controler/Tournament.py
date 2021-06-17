from Model import PlayerClass
from View import PlayerDisplay
from Controler import Player
from tinydb import *
from Model import TournamentClass
from View import TournamentDisplay


class TournamentController:

    @classmethod
    def TournamentMenu(cls):
        tournament = None
        is_open = True
        tournament_exist = False
        while is_open:
            if tournament_exist:
                response = TournamentDisplay.View.MenuTournamentInitialized(tournament)
                if response == 1:
                    tournament = cls.NewTournament()
                    tournament_exist = True
                elif response == 2:
                    cls.ActiveTournamentMenu(tournament)
                elif response == 0:
                    is_open = False
            else:
                response = TournamentDisplay.View.MenuTournament()
                if response == 1:
                    tournament = cls.NewTournament()
                    tournament_exist = True
                elif response == 2:
                    tournament_list = TournamentClass.Tournament.All()
                    cls.PrintAllTournament(tournament_list)
                elif response == 3:
                    tournament = cls.InitTournament()
                    tournament_exist = True
                elif response == 0:
                    is_open = False

    @classmethod
    def ActiveTournamentMenu(cls, tournament):
        tournament = tournament
        is_open = True
        while is_open:
            response = TournamentDisplay.View.MenuActiveTournament(tournament)
            if response == 1:
                Player.PlayerController.PrintAllPlayer(tournament.players_list)
            elif response == 2:
                temp_player = cls.NewPlayer()
                tournament.AddPlayer(temp_player)
                tournament.save()
            elif response == 3:
                print("\t soon \n")
                print("tu sais ce qui te reste a faire")
                print("\t soon \n")
            elif response == 4:
                init_player = cls.InitPlayerByName()
                tournament.AddPlayer(init_player)
                tournament.Save()
            elif response == 0:
                is_open = False

    @classmethod
    def NewTournament(cls):
        tournament = TournamentClass.Tournament(TournamentDisplay.View.NewTournament())
        tournament.Save()
        return tournament

    @classmethod
    def NewPlayer(cls):
        info_player = PlayerDisplay.View.new_player()
        temp_player = PlayerClass.Player(info_player)
        temp_player.Save()
        return temp_player

    @classmethod
    def InitPlayerByName(cls):
        Player.PlayerController.PrintAllPlayer(PlayerClass.Player.All())
        player = Query()
        player_name = input("=>")
        db = TinyDB('db.json')
        table = db.table('players')
        result = table.search(player.nom == player_name)
        result = result[0]
        temp_player = PlayerClass.Player(result)
        return temp_player

    @staticmethod
    def PrintAllTournament(tournament_list):
        i = 0
        for tournament in tournament_list:
            i = i + 1
            TournamentDisplay.View.ViewInfoTournament(i, tournament)

    @classmethod
    def InitTournament(cls):
        i = 0
        tournament_list = TournamentClass.Tournament.All()
        cls.PrintAllTournament(tournament_list)
        tournament = Query()
        db = TinyDB('db.json')
        table = db.table('Tournament')
        result_list = table.search(tournament.location == input('indiquer la location du tournoie :\n=>'))
        for result in result_list:
            i = i + 1
            print('#' + str(i), result)
        print('veuillez indiquer le numero du tournoi : ')
        chosen_result_id = input('=>')
        result = result_list[(int(chosen_result_id))-1]
        tournament = TournamentClass.Tournament(result)
        return tournament
