from Model.MatchClass import Match
import datetime


class Turn:
    def __init__(self, name, number_of_player=8):
        self.name = name
        self.pairs_list = []
        self.is_over = False
        self.is_exist = False
        self.match_list = []
        self.match_data = []
        self.data_turn = {}
        for i in range(int(number_of_player / 2)):
            self.match_list.append(Match())
        self.start_date = datetime.datetime(2000, 1, 1, 0, 0, 0, 0)
        self.end_date = datetime.datetime(2000, 1, 1, 0, 0, 0, 0)

    def get_pairs_list(self, pairs_list):
        self.pairs_list = pairs_list

    def generate_match(self):
        for i in range(len(self.pairs_list)):
            print(i, self.pairs_list[i])
            print(self.match_list[i])
            self.match_list[i].generate(self.pairs_list[i])
            print(self.match_list[i].player1)

    def serialize(self):
        self.match_data = []
        self.data_turn = {
            'name': self.name,
            'is_over': self.is_over,
            'is_exist': self.is_exist,
            'start_date': date_serialliser(self.start_date),
            'end_date': date_serialliser(self.end_date)
        }
        for match in self.match_list:
            self.match_data.append(match.serialize())
        self.data_turn['match_list'] = self.match_data
        return self.data_turn

    def deserialize(self, turn_data):
        self.name = turn_data['name']
        self.is_over = bool(turn_data['is_over'])
        self.is_exist = bool(turn_data['is_exist'])
        self.start_date = datetime.datetime.fromisoformat(turn_data['start_date'])
        self.end_date = datetime.datetime.fromisoformat(turn_data['end_date'])
        for y, match_data in enumerate(turn_data['match_list']):
            match = self.match_list[y]
            match.de_serialize(match_data)


def date_serialliser(date=datetime.datetime.now()):
    date = date
    serialized_date = date.isoformat()
    return serialized_date
