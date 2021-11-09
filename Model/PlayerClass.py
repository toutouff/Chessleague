from tinydb import *


class Player:
    def __init__(self, info_player):
        """
        store : name,first,birthdate,rank
        :param info_player: dict containing all necessary info from player
        """
        self.data_player = info_player
        self.name = self.data_player["nom"]
        self.first_name = self.data_player["prenom"]
        self.rank = self.data_player["rank"]
        self.score_in_game = 0

    def Save(self):
        """
        to save the player in the db
        :return: nothing
        """
        db = TinyDB("db.json")
        players_table = db.table("players")
        players_table.insert(self.data_player)

    @staticmethod
    def Reset():
        """
        reset the player table
        :return:
        """
        db = TinyDB("db.json")
        players_table = db.table("players")
        players_table.truncate()

    @staticmethod
    def All():
        """
        create a list with all the player inside the db
        :return: players_list
        """
        players_list = []
        db = TinyDB("db.json")
        players_table = db.table("players")
        for player in players_table:
            players_list.append(Player(player))
        return players_list
