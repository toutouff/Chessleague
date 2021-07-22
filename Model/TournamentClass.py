import depending as depending
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
        self.active_turn = 0
        self.number_of_player = int(self.info_tournament['number_of_player']) or 8
        self.turn_list = [Turn] * 8
        self.players_list = []
        self.players_data = []
        self.db_id = []  # trouver solution pour pu avoir list

    def launch(self):
        turn = Turn()
        turn.get_pairs_list()
        self.turn_list.append(turn)
        turn.generate_match()
        self.active_turn = self.turn_list[0]

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

    """ask if it needs to go to another file or in a main file"""


class Turn:
    def __init__(self):
        self.pairs_list = []
        self.is_over = False
        self.match_list = []

    def get_pairs_list(self, pairs_list):
        self.pairs_list = pairs_list

    def generate_match(self):
        for pair in self.pairs_list:
            match = Match()
            self.match_list.append(match)


class Match:
    def __init__(self, ):
        self.pair = []
        self.player1 = None
        self.player2 = None
        self.results = ()
        self.is_over = False

    def generate_(self, pair):
        self.pair = pair
        self.player1 = pair[0][1]
        self.player2 = pair[1][1]

    def get_result(self):
        self.results = input("result(if player1 win write 10 but if it's player2 write 01)\n=>")
        if self.results == '10':
            self.player1.score_in_game += 1
            self.player2.score_in_game += 0
            self.is_over = True
        elif self.results == '01':
            self.player1.score_in_game += 0
            self.player2.score_in_game += 1
            self.is_over = True
        elif self.results == '00' or self.results == '11':
            self.player1.score_in_game += 0.5
            self.player2.score_in_game += 0.5
            self.is_over = True
        else:
            print('veuillez entré un resultat valide')
            self.is_over = False


def pairs_generator_for_turn_1(players_list):
    ranked_players = []
    pairs_list = []
    number_of_pairs = int(len(players_list) / 2)

    for player in players_list:
        row = [int(player.rank), player]
        ranked_players.append(row)
        ranked_players = sorted(ranked_players)
    print(ranked_players)

    print('nombre de pairs a genéré est de ' + str(number_of_pairs))

    for i in range(number_of_pairs):
        pairs = [ranked_players[i], ranked_players[i + number_of_pairs]]
        pairs_list.append(pairs)
    return pairs_list


def pairs_generator(players_list):
    ordered_players_by_score = []
    pairs_list = []
    number_of_pairs = int(len(players_list)/2)

    for player in players_list:
        row = [int(player.score_in_game), player]
        ordered_players_by_score.append(row)
        ordered_players_by_score.sort()
    print(ordered_players_by_score)

    print('nombre de pairs a genéré est de ' + str(number_of_pairs))

    for i in range(number_of_pairs):
        pair = [ordered_players_by_score[i], ordered_players_by_score[i + number_of_pairs]]
        pairs_list.append(pair)
    return pairs_list
