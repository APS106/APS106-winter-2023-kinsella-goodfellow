import random

def continue_walking(turtle):
    """
    (turtle) --> bool
    Will determine if the turtle has hit the left wall or if it is ok to continue walking.

    Example:
        at_wall(turtle)
        >> True
    """
    if turtle.get_state()['points'][-1]['x'] == 380:
        return False
    else:
        return True


def rpsls_winner(input1, input2):
    """
    (str, str) -> int
    Determine winner of a two person rock-paper-scissors-lizard-Spock game from two user inputs
        rock beats scissors and lizard
        scissors beats paper and lizard
        paper beats rock and Spock
        lizard beats paper and Spock
        Spock beats scissors and rock
    If input1 wins, return -1
    If input2 wins, return 1
    """
    return_value = 0
    if input1 != input2:
        # not a tie
        return_value = 1  # assume player2 wins

        # determine if player1 actually wins
        if ((input1 == 'rock') and (input2 == 'scissors' or input2 == 'lizard')) or \
                ((input1 == 'scissors') and (input2 == 'paper' or input2 == 'lizard')) or \
                ((input1 == 'paper') and (input2 == 'rock' or input2 == 'spock')) or \
                ((input1 == 'lizard') and (input2 == 'paper' or input2 == 'spock')) or \
                ((input1 == 'spock') and (input2 == 'scissors' or input2 == 'rock')):
            return_value = -1

    return return_value


def generate_guess():
    """
    Converts int number to a string name (choice in RPLS)
    () -> string
    """
    guess_number = random.randrange(0, 5)
    guess_str = ""

    if guess_number == 0:
        guess_str = "rock"
    elif guess_number == 1:
        guess_str = "spock"
    elif guess_number == 2:
        guess_str = "paper"
    elif guess_number == 3:
        guess_str = "lizard"
    elif guess_number == 4:
        guess_str = "scissors"

    return guess_str


def play_rpsls():
    """
    () -> int
    Prompt the user to enter "rock", "paper", "scissors", "lizard", or "spock".
    """

    user_input = input('Enter "rock", "paper", "scissors", "lizard", or "spock"? ').lower()

    while (user_input != "rock" and user_input != "paper" and user_input != "scissors" and
           user_input != "lizard" and user_input != "spock"):
        print('Incorrect input! Try again.')
        user_input = input('Enter "rock", "paper", "scissors", "lizard", or "spock"? ').lower()

    computer_guess = generate_guess()

    result = rpsls_winner(user_input, computer_guess)

    print("Your Choice:", user_input)
    print("Computer Choice:", computer_guess)
    if result == -1:
        print('Outcome: You Win (-1)\n')
    elif result == 0:
        print('Outcome: Tie (0)\n')
    else:
        print('Outcome: Computer Wins (1)\n')

    return result
