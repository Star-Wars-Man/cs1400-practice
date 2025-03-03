def new_game():
    ''' 
    Parameters: none
    Return value: a list containing 3 items, 
     a list of guessed letters, the word, and 
     the number of misses.

    Example: 
    game = new_game()
    game[0] # list of guessed letters
    game[1] # the mystery word
    game[2] # the number of misses
    '''
    word = pick_word() 
    guessed_letters = []
    misses = 0
    game = [ guessed_letters, word, misses ]
    return game

def pick_word():
    '''
    Name: pick_word
    Parameters: none
    Return value: one string representing a word

    Example: 
    word = pick_word()
    '''
    import random
    import json
    with open('words.json', 'r') as file:
        words = json.load(file)
    num = random.randrange(len(words)) # choose a random index
    return words[num]

def guess_letter(game, letter):
    '''
    Name: guess_letter
    Parameters: the game list, and a single character string
    Return value: None
    '''
    game[0].append(letter)
    if not is_letter_in_word(game, letter):
       game[2]+=1

def is_letter_in_word(game, letter):
    '''
    Name: is_letter_in_word
    Parameters: the game list, and a single character string
    Return values: True if the letter is in the word, False otherwise
    '''
    word = game[1]
    for c in word:
        if c == letter:
            return True
    return False

def is_word_guessed(game):
    '''
    Name: is_word_guessed
    Parameters: the game list
    Return value: True is all letters in the word have been guessed, False otherwise    
    '''
    guessed_letters = game[0]
    word = game[1]
    for c in word:
        if not c in guessed_letters: # if one letter is found, it can't be True
            return False
    return True

def is_game_over(game):
    '''
    Name: is_game_over
    Parameters: the game list
    Return value: True if there are too many misses or the word is guessed, False otherwise
    '''
    misses = game[2]
    return misses >= 6 or is_word_guessed(game)

def display_status(game):
    '''
    Name: display_status
    Parameters: the game list
    Return value: None
    '''
    display_picture(game)
    display_word(game)
    display_guessed_letters(game)
    
def display_guessed_letters(game):
    '''
    Name: display_guessed_letters
    Parameters: the game list
    Return value: None
    '''
    print("guessed:", end=" ")
    for letter in game[0]:
        print(letter, end=" ")
    print()

def display_word(game):
    '''
    Name: display_word
    Parameters: the game list
    Return value: None
    '''
    for c in game[1]:
        if is_guessed(game, c):
            print(c, end=" ")
        else:
            print("_", end=" ")
    print()

def is_guessed(game, letter):
    '''
    Name: is_guessed
    Parameters: the game list, and a string with a single character
    Return value: True if the letter has been guessed, False otherwise
    '''
    guessed_letters = game[0]
    return letter in guessed_letters

def display_picture(game):
    '''
    Name: display_picture
    Parameters: the game list
    Return values: None
    '''
    misses = game[2]
    print()

    # Line one
    if misses > 0:
        print(" O ")

    # Line two
    if misses == 2:
        print(" | ")
    elif misses == 3:
        print("/| ")
    elif misses >= 4:
        print("/|\\")

    # Line three
    if misses == 5:
        print("/  ")
    elif misses >= 6:
        print("/ \\")
    print()

def main():
    another_game = True
    while another_game:
        ''' Simple Hangman game word game '''
        game = new_game() # all game data is stored in a list

        while not is_game_over(game): # keep guessing until game is over
            display_status(game) # output current game data
            guess = input("\nnext guess? ")
            if len(guess) > 0:
                guess_letter(game, guess[0]) # process a guess

        # output game result
        if not is_word_guessed(game): # did they guess the letter?
            print("\nYou lose.\nThe word is:", game[1])
        else:
            print("\nYou win!!")
            display_status(game)
        again = input("Play again? (y/n) ")
        if again.lower == "n" or again.lower == "no":
            another_game = False
    
    

if __name__ == "__main__":
    main()  # start the program by calling the main function
     