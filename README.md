# Number Guessing Game

A fun, interactive command-line game written in Python. The computer randomly selects a secret number, and you have a limited number of chances to guess it correctly!

This project was built to practice Python logic, loops, and error handling.

## Features:

- **Three Difficulty Levels:**

    - **Easy:** Guess from 1 to 50 (10 chances)

    - **Medium:** Guess from 1 to 100 (7 chances)

    - **Hard:** Guess from 1 to 200 (5 chances)

- **Input Validation:** Automatically catches typos (like typing letters instead of numbers) and prompts the user again without wasting their turn.
- **Environment Safe:** Includes `EOFError` handling to gracefully exit and prevent crashes in non-interactive online IDEs or restricted terminals.

## How to Play:

1. Make sure you have [Python](https://www.python.org/downloads/ "null") installed on your computer.
2. Clone this repository or download the `guessing_game.py` file.
3. Open your terminal or command prompt.
4. Navigate to the folder where the file is saved.
5. Run the script using the following command:
    ```
    python guess.py
    ```
6. Follow the on-screen prompts to choose your difficulty and start guessing!

