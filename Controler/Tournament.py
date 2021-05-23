import Model.Tournament
import View.Tournament
import Model.Player
import View.Player
import Controler.Player
from tinydb import *


class TournamentController:

    @classmethod
    def TournamentMenu(cls):
        tournament = None
        is_open = True
        tournament_exist = False
        while is_open:
            if tournament_exist:
                response = View.Tournament.View.MenuTournamentInitialized(tournament)
                if response == 1:
                    tournament = cls.NewTournament()
                    tournament_exist = True
                elif response == 2:
                    cls.ActiveTournamentMenu(tournament)
                elif response == 0:
                    is_open = False
            else:
                response = View.Tournament.View.MenuTournament()
                if response == 1:
                    tournament = cls.NewTournament()
                    tournament_exist = True
                elif response == 0:
                    is_open = False

    @classmethod
    def ActiveTournamentMenu(cls, tournament):
        tournament = tournament
        is_open = True
        while is_open:
            response = View.Tournament.View.MenuActiveTournament(tournament)
            if response == 1:
                Controler.Player.PlayerController.PrintAllPlayer(tournament.players_list)
            elif response == 2:
                temp_player = cls.NewPlayer()
                tournament.AddPlayer(temp_player)
                tournament.Save()
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
        tournament = Model.Tournament.Tournament(View.Tournament.View.NewTournament())
        tournament.Save()
        return tournament

    @classmethod
    def NewPlayer(cls):
        info_player = View.Player.View.new_player()
        temp_player = Model.Player.Player(info_player)
        return temp_player

    @classmethod
    def InitPlayerByName(cls):
        Controler.Player.PlayerController.PrintAllPlayer(Model.Player.Player.All())
        player = Query()
        player_name = input("=>")
        db = TinyDB('db.json')
        table = db.table('players')
        result = table.search(player.nom == player_name)
        result = result[0]
        temp_player = Model.Player.Player(result)
        return temp_player
