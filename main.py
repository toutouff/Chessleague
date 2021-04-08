from Player import Player

def newPlayer():
    print("creation d'un nouveau joueurs")
    nom = input("nom : ")
    age = input("age : ")
    return Player(nom, age)

newPlayer()
