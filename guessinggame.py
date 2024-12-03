import random

def guessing_game():
    # Generate a random number between 1 and 100
    random_number = random.randint(1, 100)
    user_guess = 0
    attempts = 0

    print("Welcome to the Guessing Game!")
    print("I have selected a number between 1 and 100. Try to guess it.")

    # Loop until the user guesses the correct number
    while user_guess != random_number:
        try:
            user_guess = int(input("Enter your guess: "))
            attempts += 1

            if user_guess < random_number:
                print("Too low! Try again.")
            elif user_guess > random_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the correct number {random_number}")
                print(f"It took you {attempts} attempts to win the game.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

# Run the game
guessing_game()
