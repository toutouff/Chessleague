from tinydb import *


class Player:
    def __init__(self, info_player):
        self.data_player = info_player
        self.name = self.data_player['nom']
        self.first_name = self.data_player['prenom']
        self.rank = self.data_player['rank']

    def Save(self):
        db = TinyDB('db.json')
        players_table = db.table('players')
        players_table.insert(self.data_player)

    @staticmethod
    def Reset():
        db = TinyDB('db.json')
        players_table = db.table('players')
        players_table.truncate()

    @staticmethod
    def All():
        players_list = []
        db = TinyDB('db.json')
        players_table = db.table('players')
        for player in players_table:
            players_list.append(Player(player))
        return players_list

