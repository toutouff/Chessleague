import Controler.Player
import Controler.Tournament
import View.Main



class MainController:
    @staticmethod
    def MainMenu():
        is_open = True
        while is_open:
            response = View.Main.ViewMain.Menu_Principal()
            if response == 1:
                Controler.Player.PlayerController.PlayerMenu()
            elif response == 2:
                Controler.Tournament.TournamentController.TournamentMenu()
            elif response == 0:
                print("vous avez quitter")
                is_open = False
