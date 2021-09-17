import pandas as pd
from tinydb import *
from Controler.Tournament import *

tournament = init_tournament()


for turn in tournament.turn_list:
    table = []
    if turn.is_exist:
        for match in turn.match_list:
            row = {'Player_1': match.player1.first_name[0] + '.' + match.player1.name, 'Result': match.results,
                   'Player_2': match.player2.first_name[0] + '.' + match.player2.name}
            table.append(row)
        print(turn.name)
        print(pd.DataFrame(table))
