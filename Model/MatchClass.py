class Match:
    def __init__(self):
        self.pair = []
        self.player1 = []
        self.player2 = []
        self.results = ()
        self.is_over = False

    def generate(self, pair):
        self.player1 = pair[0]
        self.player2 = pair[1]

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