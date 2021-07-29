from Model.MatchClass import Match


class Turn:
    def __init__(self,name, number_of_player=8):
        self.name = name
        self.pairs_list = []
        self.is_over = False
        self.match_list = []
        for i in range(int(number_of_player/2)):
            self.match_list.append(Match())

    def get_pairs_list(self, pairs_list):
        self.pairs_list = pairs_list

    def generate_match(self):
        for i in range(len(self.pairs_list)):
            print(i, self.pairs_list[i])
            print(self.match_list[i])
            self.match_list[i].generate(self.pairs_list[i])
            print(self.match_list[i].player1)
