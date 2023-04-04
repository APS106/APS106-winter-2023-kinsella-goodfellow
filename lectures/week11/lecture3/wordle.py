import random

def print_guess(guess, colours, incorrect_letters):
    """
    (str, list of strs, incorrect_letters) -> None
    This function will generate a very fancy printing of the user's guess and its correctness.
    """

    white = "\x1b[0m"
    grey = "\x1b[47m"

    for i in range(len(guess)):
        print(colours[i] + guess[i], end=" ")
       
    # print a white space
    print(white, end='\t')

    # print the incorrect letters
    print('Incorrect Letters: ', end=" ")
    for letter in sorted(incorrect_letters):
        print(grey + letter, end=" ")
    print(white) # add a newline

        
def get_solution(valid_words):
    """
    (list of strings) -> str
    Pick a random string from the list and return it
    """
    # use random to get a random index value
    rand_index = random.randint(0, len(valid_words)-1)
    
    return valid_words[rand_index]


def get_input_feedback(guess, valid_words):
    """
    (str, list of str) -> bool
    Check the string and provide feedback to the user.
    Returns true if the guess is valid, false otherwise.
    """
    valid = True
    
    if len(guess) > 5:
        print('Your word is too long!')
        valid = False
    elif len(guess) < 5:
        print('Your word is too short!')
        valid = False
    elif not guess.isalpha():
        print('Your word contains invalid characters!')
        valid = False
    elif guess not in valid_words:
        print("This isn't a real word!")
        valid = False
        
    return valid
        
def get_guess(valid_words):
    """
    (list of strings) -> str
    
    Ask the user to guess a 5 letter word and check if its valid.
    The first valid entry is returned.
    """
    guess = input('Please enter a guess: ')
    guess = guess.lower() # convert the guess to lower-case

    while not get_input_feedback(guess, valid_words):
        guess = input('Give me a new guess: ')
        guess = guess.lower()
        
    return guess


def check_letter(guess, solution, index):
    """
    (str,str,int) -> int, bool
    
    Checks if the letter at a specified index is correct
    or if the letter is contained within the solution.
    
    The first return value is a 1 if the letter is correct, otherwise 0 is returned.
    The second return value is True if the letter at the specified index is within
    the solution, false otherwise.
    """
    if guess[index] == solution[index]:
        return 1, True
    elif guess[index] in solution:
        return 0, True
    else:
        return 0, False

def check_guess(guess, solution):
    """
    (str, str) -> int, str, list of escape sequences
    
    Evaluates a guess against a solution and returns the 
    score of the guess, the incorrect letters contained within
    the guess, and a list of escape sequences defining the 
    background colours to be printed behind the letters.
    """
    
    green_background = "\x1b[42m"
    yellow_background = "\x1b[43m"
    grey_background = "\x1b[47m"
    
    word_score = 0
    incorrect_letters = ""
    print_colours = []
    
    for i in range(len(guess)):
        letter_score, in_solution = check_letter(guess, solution, i)
        
        if letter_score == 1:
            print_colours.append(green_background)
        elif in_solution:
            print_colours.append(yellow_background)
        else:
            print_colours.append(grey_background)
            
            if guess[i] not in incorrect_letters:
                incorrect_letters += guess[i]
        
        word_score += letter_score
        
    return word_score, incorrect_letters, print_colours
    
def load_valid_words():
    """
    (None) -> list of str
    
    Reads a list of valid wordle words from the file
    valid-wordle-words.txt and returns them within
    a list
    """
    valid_words = []

    # open the file for reading
    with open('valid-wordle-words.txt',  'r') as file:
        # each line in the file contains a word
        # loop over the lines and add each word to the list
        for word in file:
            valid_words.append(word.strip()) # the strip method removes the newline '\n' character

    return valid_words

def play_wordle():
    
    valid_words = load_valid_words()

    # Get the solution
    solution = get_solution(valid_words)

    # Initialize some variables
    remaining_attempts = 6
    incorrect_letters = ""
    score = 0

    while (remaining_attempts > 0 and score != 5):
        
        guess = get_guess(valid_words)
    
        score, attempt_incorrect_letters, print_colours = check_guess(guess, solution)
    
        for letter in attempt_incorrect_letters:
            if letter not in incorrect_letters:
                incorrect_letters += letter
        print_guess(guess, print_colours, incorrect_letters)
    
        remaining_attempts -= 1
    
    if (score == 5):
        print("Well done! You got the word " + solution)
    else:
        print("Better luck next time... the answer was: " + solution)