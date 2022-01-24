from datetime import datetime
from operator import attrgetter

from tinydb import TinyDB
from Model.TurnClass import Turn



class Tournament:
    def __init__(self, info_tournament):
        """
        store : name,location,start and end date,numbers of turns,each turns
        (winners & looser),time controller mod
                and description
        :param info_tournament:
        """
        self.description = info_tournament["description"]
        self.time_mode = info_tournament["time_mode"]
        self.turn_list = []
        self.info_tournament = info_tournament
        self.data_tournament = info_tournament
        self.name = self.info_tournament["name"]
        self.location = self.info_tournament["location"]
        self.start_day = self.info_tournament["start_day"]
        self.end_day = self.info_tournament["end_day"]
        self.month = self.info_tournament["month"]
        self.year = self.info_tournament["year"]
        self.active_turn = 0
        self.number_of_player = int(
            self.info_tournament['number_of_player']) or 8
        for i in range(int(self.number_of_player / 2)):
            self.turn_list.append(Turn('Turn #' + str(i),
                                       self.number_of_player))
        self.players_list = []
        self.players_data = []
        self.db_id = 1
        self.turns_data = []

    def launch(self):
        self.active_turn = self.turn_list[0]
        self.active_turn.get_pairs_list(
            pairs_generator_for_turn_1(self.players_list))
        self.active_turn.generate_match()
        self.active_turn.is_exist = True
        self.active_turn.start_date = datetime.now()

    def next_turn(self):
        self.active_turn.end_date = datetime.now()
        if self.turn_list.index(self.active_turn) == int(
                len(self.turn_list) - 1):
            print("le tournoie est fini")
        else:
            self.active_turn = self.turn_list[
                self.turn_list.index(self.active_turn) + 1]
            self.active_turn.get_pairs_list(pairs_generator(self.players_list))
            self.active_turn.generate_match()
            self.active_turn.is_exist = True
            self.active_turn.start_date = datetime.now()

    def add_player(self, temp_player):
        """
        a function to add a player to a tournament
        :param temp_player:
        :return: nothing
        """
        self.players_list.append(temp_player)
        self.players_data.append(temp_player.data_player)

    def save(self):
        """
        should create the save of the instance into the database
        :return: nothing
        """
        self.serialize_data_tournament()
        db = TinyDB("db.json")
        tournament_table = db.table("Tournament")
        self.db_id = tournament_table.insert(self.data_tournament)

    def update_players_list(self):
        """
        should update the actual instance into the database
        :return: nothing
        """
        db = TinyDB('db.json')
        tournament_table = db.table('Tournament')
        print('le joueurs a ete ajouter a la db ', self.db_id)
        tournament_table.update({'player_list': self.players_data},
                                doc_ids=[self.db_id])

    def update_turn_list(self):
        self.serialize_data_turn()
        db = TinyDB('db.json')
        tournament_table = db.table('Tournament')
        tournament_table.update({'turn_list': self.turns_data},
                                doc_ids=[self.db_id])

    def serialize_data_tournament(self):
        """
        serialize the data so it can be stored
        :return: self.data tournament:la data serialiser pour la db
        """
        self.data_tournament = {
            "name": self.name,
            "location": self.location,
            "number_of_player": self.number_of_player,
            "start_day": str(self.start_day),
            "end_day": str(self.end_day),
            "month": str(self.month),
            "year": str(self.year),
            "player_list": self.players_data,
            "turn_list": self.turns_data,
            "time_mode": self.time_mode,
            "description": self.description,
        }
        return dict(self.data_tournament)

    def serialize_data_turn(self):
        self.turns_data = []
        for turn in self.turn_list:
            if turn.is_exist:
                turn_data = turn.serialize()
                self.turns_data.append(turn_data)
        return self.turns_data

    @staticmethod
    def all():
        """
        create a list that contains evry tournament in the db
        :return:the famous list
        """
        tournament_list = []
        db = TinyDB("db.json")
        tournament_table = db.table("Tournament")
        for tournament in tournament_table:
            tournament_list.append(Tournament(tournament))
        return tournament_list

    def add_fought_player(self, pair):
        player_index = self.players_list.index(pair[0])
        oppo_index = self.players_list.index(pair[1])
        self.players_list[player_index].fought_player_index.append(
            oppo_index)
        self.players_list[oppo_index].fought_player_index.append(
            player_index)


def pairs_generator_for_turn_1(players_list):
    """
    generateur de pair se basant sur le rank des joueurs
    :param players_list:
    :return: pairs_list
    """


    pairs_list = []
    number_of_pairs = int(len(players_list) / 2)
    ranked_players = sorted(players_list, key=attrgetter('rank'))

    print("nombre de pairs a genéré est de " + str(number_of_pairs))

    for i in range(number_of_pairs):
        pairs = [ranked_players[i], ranked_players[i + number_of_pairs]]
        pairs_list.append(pairs)
    return pairs_list


def pairs_generator(players_list):
    def pair_tester(pair):
        fpi_list_size = int((pair[0].fought_player_index))
        if players_list[pair[0].fought_player_index[fpi_list_size - 1]] == pair[
            1] or players_list[
            pair[1].fought_player_index[fpi_list_size - 1]] == pair[0]:
            return True

    alone_player = False
    pairs_list = []
    scored_players = sorted(players_list, key=attrgetter('score_in_game', 'rank'),
                            reverse=True)
    for i in range(0, len(players_list), 2):
        if alone_player and i < len(scored_players)-2:
            pair = [scored_players[i], scored_players[i + 2]]
            i += 1
        else:
            pair = [scored_players[i], scored_players[i + 1]]
        if pair_tester(pair) and i < len(scored_players)-2:
            print(str(pair[0]) + "+" + str(pair[1]))
            pair = [scored_players[i], scored_players[i + 2]]
            i -= 1
            alone_player = True
        pairs_list.append(pair)
    return pairs_list


