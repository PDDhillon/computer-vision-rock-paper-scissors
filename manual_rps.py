import random

options = ["Rock","Paper","Scissors"]

def get_computer_choice():
    return random.choice(options)

def get_user_choice():
    return input("Rock, Paper or Scissors?")