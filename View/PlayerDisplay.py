# coding=utf-8
from Controler.InputChecker import *


def menu_player():
    """
    first menu for managing the player
    :return: response: int: witch correspond to the selected answer/button
    """
    print("Bienvenue dans le menu des Joueurs \n")
    print("Voulez-vous : ")
    print("\t 1 - Afficher la liste des joueurs ")
    print("\t 2 - Créer un nouveau joueur ")
    print("\t 0 - Menu principal")
    return Checkinput.int("=> ")


def new_player():
    """
    ask info with input for creating a new player
    :return: info_player: dict: contains all the info for a new player
    """
    print("création d'un nouveau joueur")
    info_player = {
        "nom": Checkinput.str("nom : "),
        "prenom": Checkinput.str("prenom :"),
        "date de naissance": Checkinput.int("année de naissance :"),
        "genre": Checkinput.str("genre :"),
        "rank": Checkinput.int("classement :"),
        "score in game": 0
    }
    return info_player


def view_info_player(name, first_name, i=1):
    """
    print the basic info of a player
    ideal to print a enumeration of player
    :param i: the index of the player (default = 1)
    :param name: name of the player
    :param first_name: first name of the player
    :return: nothing
    """
    print("\tjoueur #" + str(i))
    print("nom : " + name)
    print("prénom : " + first_name + "\n")
