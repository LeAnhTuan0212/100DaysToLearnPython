import random

should_continue = True

while should_continue:
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
    computer_number = random.randint(1, 101)

    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    life = 10
    if level == 'hard':
        life = 5
    you_win = False

    while life > 0:
        print(f"You have {life} attemps remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == computer_number:
            print(f"You got it! The answer was {computer_number}.")
            you_win = True
            break
        elif guess < computer_number:
            print("Too low.") 
        elif guess > computer_number:
            print("Too high.")
        life -= 1

    if you_win:
        print("You win!")
    else:
        print(f"The answer was {computer_number}.")
        print("You lose")

    if input("Do you want to play again? Type 'y' to continue, 'n' to exit. ") == 'n':
        should_continue = False

    