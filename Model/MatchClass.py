from Model.PlayerClass import Player


class Match:
    def __init__(self):
        self.pair = []
        self.player1 = []
        self.player2 = []
        self.results = ()
        self.is_over = False

        self.data = {}

    def generate(self, pair):
        self.pair = pair
        self.player1 = pair[0]
        self.player2 = pair[1]

    def get_result(self):
        print(self.is_over)
        self.results = input(
            "result(if player1 win write 10,if it's player2 write 01,if it's a draw write 00 or 11)\n=>"
        )
        # creer un display et s'assurer du bon placement de cette fonction(condition dans le controlleur)
        if self.results == "10":
            self.player1.score_in_game += 1
            self.player2.score_in_game += 0
            self.is_over = True
        elif self.results == "01":
            self.player1.score_in_game += 0
            self.player2.score_in_game += 1
            self.is_over = True
        elif self.results == "00" or self.results == "11":
            self.player1.score_in_game += 0.5
            self.player2.score_in_game += 0.5
            self.is_over = True
        else:
            print("veuillez entré un resultat valide")
            self.is_over = False

    def serialize(self):
        if self.is_over:
            self.data = {
                "player1": self.player1.data_player,
                "player2": self.player2.data_player,
                "is_over": self.is_over,
                "results": self.results,
            }
            return self.data
        else:
            self.data = {
                "player1": self.player1.data_player,
                "player2": self.player2.data_player,
                "is_over": self.is_over,
            }
            return self.data

    def de_serialize(self, match_data):
        self.player1 = Player(match_data["player1"])
        self.player2 = Player(match_data["player2"])
        if not match_data["is_over"]:
            self.is_over = False
        elif match_data["is_over"]:
            self.is_over = True
            self.results = match_data["results"]
