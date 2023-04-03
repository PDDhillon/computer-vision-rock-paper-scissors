from Classes.player import Player
import random
class Computer(Player):
    def get_choice(self):
        options = ["Rock","Paper","Scissors"]
        self._current_choice = random.choice(options)
        return self._current_choice