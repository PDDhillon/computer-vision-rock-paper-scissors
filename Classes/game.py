from Classes.user import User
from Classes.computer import Computer
from dataclasses import dataclass
from typing import List

@dataclass(order=True)
class Game:
    rounds:int
    win_threshold: int
    played_rounds:int = 0

    def get_winner(self, user_choice ,computer_choice):    
        '''Gets the winner of the game. The method returns an array where each position represents an end condition. 0th pos represents a USR win, 1st a CPU win and 2nd a draw. '''    
        if(computer_choice == user_choice or user_choice):
            return [0,0,1]
        if(computer_choice == "Rock"):
            if(user_choice == "Paper"):
                return [1,0,0]
            else:
                return [0,1,0]
        elif(computer_choice == "Paper"):
            if(user_choice == "Rock"):
                return [0,1,0]
            else:
                return [1,0,0]
        elif(computer_choice == "Scissors"):
            if(user_choice == "Rock"):
                return [1,0,0]
            else:
                return [0,1,0]
    
    def is_game_over(self,usr_wins, cpu_wins):
        if self.played_rounds == self.rounds or usr_wins == self.win_threshold or cpu_wins == self.win_threshold:
            return True
        else:
            return False

