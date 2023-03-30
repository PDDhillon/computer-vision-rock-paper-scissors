import random

def get_computer_choice():
    options = ["Rock","Paper","Scissors"]
    return random.choice(options)

def get_user_choice():
    return input("Rock, Paper or Scissors?")