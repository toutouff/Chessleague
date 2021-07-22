from Controler import Tournament
from Model import TournamentClass

tournament = Tournament.init_tournament()
for i in range(int(tournament.number_of_player / 2)):
    if i == 0:
        turn = TournamentClass.Turn(TournamentClass.pairs_generator_for_turn_1(tournament.players_list))
        turn.generate_match()
        tournament.turn_list.append(turn)
        tournament.active_turn = turn
        print("le premier tour a ete genéré")
    else:
        turn = TournamentClass.Turn(TournamentClass.pairs_generator(tournament.players_list))
        turn.generate_match()
        tournament.turn_list.append(turn)
        print('le ' + str(i) + 'ème tour a été genéré')
