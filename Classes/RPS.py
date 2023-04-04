"""RPS Module

This module was created to model the various actors that are required to play a game of rock, paper, scissors.

Classes
- Player (Abstract class)
- GetChoiceMixin (Interface equivalent)
- User (Child of Player, implements GetChoiceMixin)
- Computer (Child of Player, implements GetChoiceMixin)"""

from dataclasses import dataclass
import random

class GetChoiceMixin:
    '''A mixin to force children to implement a get_choice method.
            
    Methods
    ----------
    get_choice
        Returns not implemented. A way to force functionality that is specific to players.
    '''

    def get_choice(self):
        ''' Returns not implemented. A way to force functionality that is specific to players.

            Returns:
                NotImplementedError
        '''
        raise NotImplementedError

@dataclass(order=True)
class Player(GetChoiceMixin):
    '''A class to represent an abstract player of the game.
    
    Attributes
    ----------
    _wins : int
            How many times a player has won the game.
    _current_choice : int
            The players current choice in the game.
            
    Methods
    ----------
    Getter and Setter methods for above attributes.
    GetChoiceMixin forces all concrete classes to implement their own get choice methods.
    '''
    _wins: int 
    _current_choice: str

    @property
    def wins(self) -> int:
        return self._wins

    @wins.setter
    def wins(self, v: int) -> None:
        self._wins = v
    
    @property
    def current_choice(self) -> str:
        return self._current_choice

    @current_choice.setter
    def wins(self, v: str) -> None:
        self._current_choice = v

class User(Player):
    '''A class to represent the user who is playing the game. Inherits the class Player.
    
    Methods
    ----------
    get_choice
        Gets the current choice for the user. The setter methods inherted also perform the same functionality.
        However, this allows for the get_choice method to be expanded on in the future for speciality functionality.
    '''
    def get_choice(self):
        print(self.current_choice) 
        
class Computer(Player):
    '''A class to represent the computer who the user plays. Inherits the class Player.
    
    Methods
    ----------
    get_choice
        Gets a random option and sets it as the current choice for the computer.
    '''
    def get_choice(self):
        options = ["Rock","Paper","Scissors"]
        self._current_choice = random.choice(options)
        return self._current_choice

@dataclass(order=True)
class Game:
    '''A class to represent the game.
    
    Attributes
    ----------
    _rounds : int
            How many rounds can be played in one game.
    _win_threshold : int
            How many times a player can win the game before it ends.
    _played_rounds : int
            The current count of how many games have been played.
            
    Methods
    ----------
    get_winner(user_choice="", computer_choice="")
        Returns whether win conditions have been met.
    is_game_over(usr_wins=0, cpu_wins=0)
        Determines whether the win conditions have been met to end the whole game.
    '''
    _rounds:int
    _win_threshold: int
    _played_rounds:int = 0

    def get_winner(self, user_choice ,computer_choice):    
        ''' Returns whether win conditions have been met.

                Parameters:
                    user_choice (str) : The users current choice
                    computer_choice (str) : The computers current choice
                
                Returns:
                    [0,0,0] : An array which represents the 3 possible end results. User win, CPU win or draw. When a value is = 1, it represents that specific condition.
        '''    
        if(computer_choice == user_choice or user_choice == 'Nothing'):
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
        ''' Determines whether the win conditions have been met to end the whole game.

                Parameters:
                    usr_wins (int) : The users amount of wins
                    cpu_wins (int) : The computers amount of wins
                
                Returns:
                    boolean : True or False as to whether the game has finished.
        '''    
        if self._played_rounds == self._rounds or usr_wins == self._win_threshold or cpu_wins == self._win_threshold:
            return True
        else:
            return False