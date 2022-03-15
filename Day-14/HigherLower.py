from game_data import data
import art
from os import system
from random import choice

def information(account):
    name = account['name']
    decription = account['description']
    country = account['country']
    return f"{name}, a {decription}, from {country}"

def game():
    score = 0
    game_should_countinue = True
    system('cls')
    while game_should_countinue:
        # print logo
        print(art.logo)

        # Choose random account
        account_A = choice(data)
        account_B = choice(data)

        # Display
        print(f"Account A: {information(account_A)}.")
        print(art.vs)
        print(f"Account B: {information(account_B)}.")
        
        # User guess
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        # Check answer
        if account_A['follower_count'] > account_B['follower_count']:
            answer = 'a'
        else:
            answer = 'b'

        system('cls')
        # Continue and increase score if True, End if false
        if answer == guess:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            game_should_countinue = False
            print(f"Sorry, that's wrong. Final score: {score}")
            new_game = input("Do you want to play again? Type 'y' to play again, type another key to exit. ")
            system('cls')
            if new_game == 'y':
                game()
                
game()