from tinydb import TinyDB


class Player:
    def __init__(self, info_player):
        """
        store : name,first,birthdate,rank
        :param info_player: dict containing all necessary info from player
        """
        self.data_player = info_player
        self.name = self.data_player["nom"]
        self.first_name = self.data_player["prenom"]
        self.rank = self.data_player["rank"]
        self.score_in_game = int(self.data_player["score in game"])
        self.fought_player_index = self.data_player['fought player']

    def __str__(self):
        str = self.name + " " + self.first_name
        return str

    def save(self):
        """
        to save the player in the db
        :return: nothing
        """
        db = TinyDB("db.json")
        players_table = db.table("players")
        players_table.insert(self.data_player)

    @staticmethod
    def all():
        """
        create a list with all the player inside the db
        :return: players_list
        """
        players_list = []
        db = TinyDB("db.json")
        players_table = db.table("players")
        for player in players_table:
            players_list.append(Player(player))
        return players_list

    def update_score(self):
        self.data_player['score in game'] = self.score_in_game
