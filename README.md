# Comment executer et utiliser Chessleague

## Installation

pour l’installation il est recommandé de cloner le repository sur votre machine

```bash
git clone https://github.com/toutouff/Chessleague
```

## requirement

les bibliothèques pandas et tinydb sont requise

## execution

Démarrer ChessLeague il suffit de démarré [main.py](https://github.com/toutouff/Chessleague/blob/main/main.py) grâce a python3

## Utilisation

l'interface est très  simple les menu sont présenter  sous la forme suivante 

```bash
bienvenue dans chessLeague
voulez-vous :
	 1 - menu des joueurs
	 2 - menu des championat
	 3 - menu des Rapport
	 0 - quitter
=>
```

il suffit de répondre au niveau du '=>' avec le numéro correspondant a votre choix

## Documentation

l'arborescence des menu est fait de même :

### 1. menu des joueurs

1. afficher la liste des joueurs
	
affiche la liste de tout les joueurs dans la base de donné
	
2. creer un nouveau joueur
	
Créer un joueurs
	
3. retourner au menu principal 
	
### 2. menu des championnat
	
1. creer un nouveau tournoi

creer un nouveau tournoi et lance le menu de gestion du tournoi en question

2. afficher tout les tournois

affiche la liste de tout les tournois
	
3. initialiser un tournoi
	
affiche tout les tournoi et permet d'en charger un depuis la base de donné si il n'est pas fini

### 2.A Menu de gestion d'un championat avant lancement 
	
1. afficher la liste des joueurs

affiche la liste de tout les joueurs dans las base de donné

2. creer un nouveau joueurs

creer un nouveau joueurs et l'inscrit automatiquement
	
3. Initialiser un joueurs depuis la base de donné

initalise un joueurs depuis la base de donne et l'inscrit automatiquement

4. generer le premier tour

genere les paire et match du premier tour et lance le championat

5. lancer le premier tour 

lance le championat et indique si aucun tour na été genere

### 2.B Menu de gestion du Championat une fois lancé

1. afficher la liste des matches

affiche tout les match du tour en cours

2. entrez un resultat

affiche d'abord tout les match avec un numero associé 
ensuite entrez le numero du match dont vous voulez entrez le resultat
indiquer le resutat sous la forme

| entrée | joueurs 1 | joueurs 2 |
|--------|-----------|-----------|
| 00     | égalité   | égalité   |
| 11     | égalité   | égalité   |
| 10     | gagnant   | perdant   |
| 01     | perdant   | gagnant   |

3. generer le prochain tour

si et seulement si tout les match sont fini genere et lance le tour suivant en fonction des resultat actuel

### 3. menu des Rapport

1. faire un rapport de tout les tournois 
2. faire un rapport de tout les joueurs par ordre alphabetique
3. faire un rapport de tout les joueurs par rangs
4. faire un rapport sur un tournoi
	- faire un rapport de tout les joueurs par ordre alphabetique
	- faire un rapport de tout les joueurs rangs
	- faire un rapport de tout les tours 
	- faire un rqpport de tout les match

# generer un nouveau rapport flake8

simplement

```$ pip install flake8-html```

ensuite executer la comande flake8 avec l'option --format=html et un --htmldir:

```$ flake8 --format=html --htmldir=flake-report```




















