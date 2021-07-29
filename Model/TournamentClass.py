from tinydb import *
from tinydb.table import Document

from Model.TurnClass import Turn


class Tournament:
    def __init__(self, info_tournament):
        """
        store : name,location,start and end date,numbers of turns,each turns(winners & looser),time controller mod
                and description
        :param info_tournament:
        """
        self.turn_list = []
        self.info_tournament = info_tournament
        self.data_tournament = info_tournament
        self.name = self.info_tournament['name']
        self.location = self.info_tournament['location']
        self.start_day = self.info_tournament['start_day']
        self.end_day = self.info_tournament['end_day']
        self.month = self.info_tournament['month']
        self.year = self.info_tournament['year']
        self.active_turn = 0
        self.number_of_player = int(self.info_tournament['number_of_player']) or 8
        for i in range(int(self.number_of_player / 2)):
            self.turn_list.append(Turn('Turn #'+str(i), self.number_of_player))
        self.players_list = []
        self.players_data = []
        self.db_id = 1
        """self.serialized_turn_list = None"""

    def launch(self):
        self.active_turn = self.turn_list[0]
        self.active_turn.get_pairs_list(pairs_generator_for_turn_1(self.players_list))
        self.active_turn.generate_match()

    def nextTurn(self):
        self.active_turn = self.turn_list[self.turn_list.index(self.active_turn) + 1]
        self.active_turn.get_pairs_list(pairs_generator(self.players_list))
        self.active_turn.generate_match()

    def AddPlayer(self, temp_player):
        """
        a function to add a player to a tournament
        :param temp_player:
        :return: nothing
        """
        self.players_list.append(temp_player)
        self.players_data.append(temp_player.data_player)
        print(self.players_data)

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
        print('le joueurs a ete ajouter a la db ', self.db_id)
        tournament_data = self.SerializeDataTournament()
        tournament_table.update({'player_list': self.players_data}, doc_ids=[self.db_id])

    def SerializeDataTournament(self):
        """
        serialize the data so it can be stored
        :return: self.data tournament:la data serialiser pour la db
        """
        self.data_tournament = {
            'name': self.name,
            'location': self.location,
            'number_of_player': self.number_of_player,
            'start_day': str(self.start_day),
            'end_day': str(self.end_day),
            'month': str(self.month),
            'year': str(self.year),
            'player_list': self.players_data,
            'turn_list': self.serialized_turn
        }
        return dict(self.data_tournament)

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


def pairs_generator_for_turn_1(players_list):
    """
    generateur de pair se basant sur le rank des joueurs
    :param players_list:
    :return: pairs_list
    """

    def getRank(player):
        return int(player.rank)

    ranked_players = []
    pairs_list = []
    number_of_pairs = int(len(players_list) / 2)
    ranked_players = sorted(players_list,key=getRank)
    print(ranked_players)

    print('nombre de pairs a genéré est de ' + str(number_of_pairs))

    for i in range(number_of_pairs):
        pairs = [ranked_players[i], ranked_players[i + number_of_pairs]]
        pairs_list.append(pairs)
    return pairs_list


def pairs_generator(players_list):
    """
    generateur de pair se basant sur le score du joueurs
    :param players_list:
    :return: pairs_list
    """

    def get_score(player):
        return int(player.score_in_game)
    pairs_list = []
    number_of_pairs = int(len(players_list) / 2)
    ordered_players_by_score = sorted(players_list, key=get_score)
    print(ordered_players_by_score)

    print('nombre de pairs a genéré est de ' + str(number_of_pairs))

    for i in range(number_of_pairs):
        pair = [ordered_players_by_score[i], ordered_players_by_score[i + number_of_pairs]]
        pairs_list.append(pair)
    return pairs_list
