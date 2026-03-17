import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("Choose a difficulty level:")
    print("1. Easy   (Guess from 1 to 50, 10 chances)")
    print("2. Medium (Guess from 1 to 100, 7 chances)")
    print("3. Hard   (Guess from 1 to 200, 5 chances)")

    # Get the user's choice, 
    try:
        choice = input("Enter 1, 2, or 3: ")
    except EOFError:
        print("\n[Input unavailable: Auto-selecting Easy mode]")
        choice = '1'

    # Set the game rules based user chose
    if choice == '1':
        max_number = 50
        chances = 10
    elif choice == '2':
        max_number = 100
        chances = 7
    elif choice == '3':
        max_number = 200
        chances = 5
    else:
        # If they type something wrong, automatically pick Easy mode
        print("Invalid choice. We will start on Easy mode.")
        max_number = 50
        chances = 10

    # The computer picks a random 
    secret_number = random.randint(1, max_number)

    # Tell the player the rules 
    print(f"\nI am thinking of a number between 1 and {max_number}.")
    print(f"You have {chances} chances to guess it.\n")

    # Start a loop that gives the player a limited number of chances
    for attempt in range(chances):
        # Ask the player to type their guess, loop until they give a valid number
        while True:
            try:
                guess_text = input(f"Chance {attempt + 1} of {chances} - Enter your guess: ")
                guess = int(guess_text) 
                break 
            except ValueError:
                print("Please type a valid number! This won't cost you a chance.")
            except EOFError:
                print("\n[Input unavailable: Exiting game automatically.]")
                return 
        if guess == secret_number:
            print(f"Awesome! You guessed the number {secret_number} correctly!")
            print("You win!")
            return # Stop the game because the player won

        # If the guess is smaller than the secret number
        elif guess < secret_number:
            print("Too low! Try guessing a bigger number.")
            
        # If the guess is bigger than the secret number
        else:
            print("Too high! Try guessing a smaller number.")

    # If the loop finishes without returning, the player used all their chances
    print("\nGame Over! You ran out of chances.")
    print(f"The secret number was {secret_number}.")

# This is where the program actually starts running
if __name__ == "__main__":
    number_guessing_game()