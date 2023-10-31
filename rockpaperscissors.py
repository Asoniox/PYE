import random

def getChoices():
    player_choice = input("Pick one: (rock, paper, scissors): ")
    options = [
        'rock',
        'paper',
        'scissors'
    ]
    computer_choice = random.choice(options)

    choices = {
        "player": player_choice,
        "computer": computer_choice
    }

    return choices

def checkWin(player, computer):
    return [player, computer]