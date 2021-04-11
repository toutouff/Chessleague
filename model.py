from tinydb import TinyDB


class Player:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.Save()

    def serialize(self):
        serialized_player = {
            "name": self.name,
            "age": self.age
        }
        return serialized_player

    def Save(self):
        db = TinyDB('db.json')
        players_table = db.table('players')
        players_table.insert(self.serialize())

    @staticmethod
    def Reset():
        db = TinyDB('db.json')
        players_table = db.table('players')
        players_table.truncate()

    @staticmethod
    def All():
        db = TinyDB('db.json')
        players_table = db.table('players')
        return players_table.all()