from Model.MatchClass import Match


class Turn:
    def __init__(self, name, number_of_player=8):
        self.name = name
        self.pairs_list = []
        self.is_over = False
        self.match_list = []
        self.match_data = []
        self.data_turn = {}
        for i in range(int(number_of_player / 2)):
            self.match_list.append(Match())

    def get_pairs_list(self, pairs_list):
        self.pairs_list = pairs_list

    def generate_match(self):
        for i in range(len(self.pairs_list)):
            print(i, self.pairs_list[i])
            print(self.match_list[i])
            self.match_list[i].generate(self.pairs_list[i])
            print(self.match_list[i].player1)

    def serialize(self):
        for match in self.match_list:
            self.match_data.append(match.serialize())
        self.data_turn = {
            'name': self.name,
            'is_over': str(self.is_over),
            'match_list': self.match_data
        }
        return self.data_turn

    def deserialize(self, turn_data):
        self.name = turn_data['name']
        self.is_over = bool(turn_data['is_over'])
        for y, match_data in enumerate(turn_data['match_list']):
            match = self.match_list[y]
            match.de_serialize(match_data)
