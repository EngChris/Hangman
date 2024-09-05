'''
The program needs to pick a word
The program needs to count how many letters that word contains
replace letters with underscore
Keep track of amount of guesses

----
keep correct letters
keep wrong letters
and keep of when the word is complete

----
Accept user input
It needs to check user input
show correct and incorrect guessed letters

'''

tries=4
theword= 'john'


#Getting the lines-count 
def letter_count(theword):
    for x in theword:
        print('-', end='')
 
def match_found(word,user_input):
    for x in word:
        if(x == user_input):
            print('match found in',user_input)
            return True
            
        else:
            print('no match found in',user_input)
            return False
    
letter_count(theword)
#match_found(theword,user_input)

user_tries=5
print("Welcome to Hangman!")

while user_tries > 0:
    guess = input("Enter a letter: ").lower()
    
    if(match_found(theword,guess))== True:
        #user_tries +=1
        print('Proceed')
        
    else:
        tries -=1
        print(f"You have {user_tries} tries left.")
        
if user_tries ==0:
    print("Sorry, you ran out of tries. The word was:", theword)
    
    
    
'''   
tries = 5

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
        
'''