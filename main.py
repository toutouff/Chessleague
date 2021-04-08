class Player:
    def __init__(self, name, age):
        self.name = name
        self.age = age

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

P1 = Player("jean", 23)
seriaL_P1 = P1.serialize()
print(seriaL_P1)