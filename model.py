from tinydb import TinyDB


class Player:
    def __init__(self, info_player):
        self.data_player = info_player
        self.name = self.data_player['nom']
        self.first_name = self.data_player['prenom']
        self.rank = self.data_player['rank']
        self.Save()

    def Save(self):
        db = TinyDB('db.json')
        players_table = db.table('players')
        players_table.insert(self.data_player)

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


class Tournament:
    def __init__(self, info_tournament):
        self.info_tournament = info_tournament
        self.name = None
        self.location = None
        self.day = None
        self.month = None
        self.year = None

# Nom
# Lieu :
# Date
# Jusqu'à présent, tous nos tournois sont des événements d'un jour, mais nous pourrions en organiser de plusieurs jours à l'avenir, ce qui devrait donc permettre de varier les dates.
# Nombre de tours
# Réglez la valeur par défaut sur 4.
# Tournées
# La liste des instances rondes.
# Joueurs
# Liste des indices correspondant aux instances du joueur stockées en mémoire.
# Contrôle du temps
# C'est toujours un bullet, un blitz ou un coup rapide.
# Description
# Les remarques générales du directeur du tournoi vont ici

#  1. Créer un nouveau tournoi.
#  2. Ajouter huit joueurs.
#  3. L'ordinateur génère des paires de joueurs pour le premier tour.
#  4. Lorsque le tour est terminé, entrez les résultats.
#  5. Répétez les étapes 3 et 4 pour les tours suivants jusqu'à ce que tous les tours soient joués, et que le tournoi soit terminé.


# instancier mes joueurs