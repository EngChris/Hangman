import random


def print_word(word, guessed_letters):
    """
    Prints the word with underscores for unguessed letters and guessed letters revealed.

    Args:
        word (str): The secret word.
        guessed_letters (list): A list of guessed letters.

    Returns:
        str: The formatted word string.
    """

    result = ""
    for letter in word:
        if letter in guessed_letters:
            result += letter
        else:
            result += "_"
    return result

def check_guess(word, guessed_letters, guess):
    """
    Checks if the guessed letter is in the word.

    Args:
        word (str): The secret word.
        guessed_letters (list): A list of guessed letters.
        guess (str): The guessed letter.

    Returns:
        bool: True if the guess is correct, False otherwise.
    """

    if guess in guessed_letters:
        print("You've already guessed that letter.")
        return False
    elif guess in word:
        guessed_letters.append(guess)
        print("Correct guess!")
        return True
    else:
        print("Incorrect guess.")
        return False

def play_game():
    f = open("words.txt", "rt")
    #print(f.read())
    data = f.read()
    rand = data.split("\n")
    word= random.choice(rand)
    f.close()
    guessed_letters = [] 
    tries =7
    

    print("Welcome to Hangman!")
    print(print_word(word, guessed_letters))

    while tries > 0:
        guess = input("Enter a letter: ").lower()

        if check_guess(word, guessed_letters, guess):
            if all(letter in guessed_letters for letter in word):
                print("Congratulations! You won!")
                break
        else:
            tries -= 1
            print(f"You have {tries} tries left.")

        print(print_word(word, guessed_letters))

    if tries == 0:
        print("Sorry, you ran out of tries. The word was:", word)

play_game()

def print_random(file_name):
    f= open(file_name)
    data= f.read()
    word = data.split("\n")
    rand= random.choice(word)
    print(rand)