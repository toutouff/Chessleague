from tinydb import *


class Tournament:
    def __init__(self, info_tournament):
        self.data_tournament = info_tournament
        self.name = self.data_tournament['name']
        self.location = self.data_tournament['location']
        self.start_day = self.data_tournament['start_day']
        self.end_day = self.data_tournament['end_day']
        self.month = self.data_tournament['month']
        self.year = self.data_tournament['year']
        self.turn = 0
        self.number_of_player = 0
        self.players_list = []
        self.players_data = []

    def AddPlayer(self, temp_player):
        self.players_list.append(temp_player)
        self.players_data.append(temp_player.data_player)
        self.number_of_player = self.number_of_player + 1

    def Save(self):
        self.Serialize()
        db = TinyDB('db.json')
        tournament_table = db.table('Tournament')
        tournament_table.insert(self.data_tournament)

    def Serialize(self):
        self.data_tournament = {
            'name': self.name,
            'location': self.location,
            'start date': str(self.start_day + '/' + self.month + '/' + self.year),
            'end date': str(self.end_day + '/' + self.month + '/' + self.year),
            'player list': self.players_data
        }
