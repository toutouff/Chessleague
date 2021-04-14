from model import Player
from view import *


def newPlayer():
    info_Player = view_newPlayer()
    Player(info_Player['nom'], info_Player['age'])


def Print_Player_All():
    allPlayerList = Player.All()
    i = 1
    for player in allPlayerList:
        name = player['name']
        age = player['age']
        view_Info_Player(i, name, age)
        i += 1


response_Principal = Menu_Principal()

while response_Principal !=0:
    if response_Principal == 1:
        response_Player = Menu_Player()
        if response_Player == 1:
            Print_Player_All()
        if response_Player == 2:
            newPlayer()