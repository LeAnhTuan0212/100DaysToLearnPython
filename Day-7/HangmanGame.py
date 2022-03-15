import hangman_words
import random 

# LOGO
print(hangman_words.logo)

# HANGMAN PICTURE
hangman_pics = hangman_words.hangman_pictures

# Randomly choose a word from the word_list
chosen_word = random.choice(hangman_words.word_list)
len_of_chosen_word = len(chosen_word)
print(f"The word has {len_of_chosen_word} words...")

# Create an blanks list called display.
display = ["_"] * len_of_chosen_word
print(display)

# Setting game
end_of_game = False
lives = 6
print(hangman_pics[6 - lives])

# START
while not end_of_game:
    
    # Ask the user to guess a letter.
    guess = input("Guess a letter: ").lower()
    num_of_guess = 0
    
    # Check guessed letter
    for position in range (len_of_chosen_word):
        letter = chosen_word[position]
        if (letter == guess):
            display[position] = letter
            num_of_guess += 1

    # Print the number of guessed letter in word.
    if num_of_guess > 1:
        print(f"There are {num_of_guess} letters in word.")
    elif num_of_guess:
        print("There is one letter in word.")
    else:
        lives -= 1
        print(f"The word doesn't have a letter '{guess}'.")
        print(hangman_pics[-1 - lives])
    
    # Print display
    print(display)
    
    # END GAME
    if "_" not in display:
        end_of_game = True
        print("YOU ARE WINNER!!!")
    elif lives == 0:
        end_of_game = True
        print(f"The word is {chosen_word}.\nYOU LOSE!")

