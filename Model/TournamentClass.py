from tinydb import *


class Tournament:
    def __init__(self, info_tournament):
        """
        store : name,location,start and end date,numbers of turns,each turns(winners & looser),time controller mod
                and description
        :param info_tournament:
        """
        self.info_tournament = info_tournament
        self.data_tournament = info_tournament
        self.name = self.info_tournament['name']
        self.location = self.info_tournament['location']
        self.start_day = self.info_tournament['start_day']
        self.end_day = self.info_tournament['end_day']
        self.month = self.info_tournament['month']
        self.year = self.info_tournament['year']
        self.turn = 0
        self.number_of_player = 0
        self.players_list = []
        self.players_data = self.data_tournament['player_list']
        self.db_id = [1]

    def AddPlayer(self, temp_player):
        """
        a function to add a player to a tournament
        :param temp_player:
        :return: nothing
        """
        self.players_list.append(temp_player)
        self.players_data.append(temp_player.data_player)
        self.number_of_player = self.number_of_player + 1
        self.UpdatePlayersList()

    def Save(self):
        """
        should create the save of the instance into the database
        :return: nothing
        """
        self.SerializeDataTournament()
        db = TinyDB('db.json')
        tournament_table = db.table('Tournament')
        self.db_id = tournament_table.insert(self.data_tournament)

    def UpdatePlayersList(self):
        """
        should update the actual instance into the database
        :return: nothing
        """
        db = TinyDB('db.json')
        tournament_table = db.table('Tournament')
        tournament_table.update(fields=self.SerializeDataTournament(), doc_ids=self.db_id)

    def SerializeDataTournament(self):
        """
        serialize the data so it can be stored
        :return: self.data tournament:la data serialiser pour la db
        """
        self.data_tournament = {
            'name': self.name,
            'location': self.location,
            'start_day': str(self.start_day),
            'end_day': str(self.end_day),
            'month': str(self.month),
            'year': str(self.year),
            'player_list': self.players_data
        }
        return self.data_tournament

    @staticmethod
    def All():
        """
        create a list that contains evry tournament in the db
        :return:the famous list
        """
        tournament_list = []
        db = TinyDB('db.json')
        tournament_table = db.table('Tournament')
        for tournament in tournament_table:
            tournament_list.append(Tournament(tournament))
        return tournament_list
