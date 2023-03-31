import random
import numpy as np
import camera_rps as cam

def get_computer_choice():
    options = ["Rock","Paper","Scissors"]
    return random.choice(options)

def get_user_choice():
    return input("Rock, Paper or Scissors?")

def get_winner(computer_choice,user_choice):
    if(computer_choice == user_choice):
      print("It is a tie!")
      return [0,0]
    if(computer_choice == "Rock"):
      if(user_choice == "Paper"):
        print("You won!")
        return [0,1]
      else:
        print("You lost")
        return [1,0]
    elif(computer_choice == "Paper"):
      if(user_choice == "Rock"):
        print("You lost")
        return [1,0]
      else:
        print("You won!")
        return [0,1]
    elif(computer_choice == "Scissors"):
      if(user_choice == "Rock"):
        print("You won!")
        return [0,1]
      else:
        print("You lost")
        return [1,0]

def play():
  rounds = 5
  current_round = 0
  computer_wins = 0
  user_wins = 0

  while(current_round < rounds and computer_wins < 3 and user_wins < 3):    
    user_choice = cam.get_prediction()
    computer_choice = get_computer_choice()
    winner = get_winner(computer_choice, user_choice)
    if(np.argmax(winner) == 0):
      computer_wins += 1
    elif(np.argmax(winner) == 1):
      user_wins += 1
    current_round += 1
    print("Computer: ", computer_wins, " User:", user_wins)  
