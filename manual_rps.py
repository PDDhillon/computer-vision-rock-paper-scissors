import random

def get_computer_choice():
    options = ["Rock","Paper","Scissors"]
    return random.choice(options)

def get_user_choice():
    return input("Rock, Paper or Scissors?")

def computer_wins():
    print("You lost")

def user_wins():
    print("You won!")

def get_winner(computer_choice,user_choice):
    if(computer_choice == user_choice):
      print("It is a tie!")
    if(computer_choice == "Rock"):
      if(user_choice == "Paper"):
        user_wins()
      else:
        computer_wins()
    elif(computer_choice == "Paper"):
      if(user_choice == "Rock"):
        computer_wins()
      else:
        user_wins()
    elif(computer_choice == "Scissors"):
      if(user_choice == "Rock"):
        user_wins()
      else:
        computer_wins()