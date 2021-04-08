from tinydb import TinyDB

class Player:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.Save()

    def Get_info(self):
        print("\t Player \t")
        print("name : " + self.name)
        print("age : " + str(self.age))

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

    def Reset(self):
        db = TinyDB('db.json')
        players_table = db.table('players')
        players_table.truncate()