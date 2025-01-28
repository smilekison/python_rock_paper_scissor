import random

def get_choices():
    human_choice = input("Enter a choice (rock, paper, scissors):::    ")
       
    available_choices = ['rock','paper','scissors']
    computer_choice = random.choice(available_choices)

    choices = {"player": human_choice, "computer": computer_choice}

    return check_win(choices["player"], choices["computer"])


def check_win(player,computer):
    print (f"You choose {player} Computer choose {computer}")
    if player == computer:
        return "It's a tie"
    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes scissors! You win"
        else:
            return "Paper covers rock. Computer wins"
    elif player == "paper":
        if computer == "rock":
            return "Paper covers rock. You wins"
        else:
            return "Scissors cuts paper! Computer win"
    elif player == "scissors":
        if computer == "paper":
            return "scissor cuts paper! You win"
        else:
            return "Rock covers rock. Computer wins"


print(get_choices())