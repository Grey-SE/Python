import random
import art


def check_guess(guess, random_number):
    if guess < random_number:
        print("Too low.")
    elif guess > random_number:
        print("Too high.")
    else:
        print(f"You got it! The answer was {random_number}.")

is_running = True

while is_running:
    number_to_be_guessed = random.randint(1, 100)

    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    number_of_attempts = 10 if difficulty == "easy" else 5

    player_guess = None

    while player_guess != number_to_be_guessed:
        if number_of_attempts == 0:
            print("You've run out of guesses, you lose.")
            break

        print(f"You have {number_of_attempts} attempts remaining to guess the number.")
        try:
            player_guess = int(input("Make a guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        check_guess(player_guess, number_to_be_guessed)

        if player_guess == number_to_be_guessed:
            is_running = False
            break

        number_of_attempts -= 1
        if number_of_attempts > 0:
            print("Guess again.")


