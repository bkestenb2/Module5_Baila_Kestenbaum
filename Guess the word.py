import random
"""
A word-guessing game where the player chooses a category and difficulty level.
The user chooses a letter and to try and guess word before tries run out.
"""

# Dictionary of word categories and their possible words
CATEGORIES = {
    "foods" : ["apple", "banana", "chicken", "licorice", "pizza",
               "fries", "strawberry", "chocolate", "steak", "bread"],
    "colors" : ["red", "orange", "yellow", "green", "blue",
                "purple", "pink", "turquoise", "teal", "white"],
    "shapes" : ["square", "circle", "triangle", "rectangle", "oval",
                "hexagon", "octagon", "pentagon", "rhombus", "trapezoid"]
}

# Number of tries per difficulty level
DIFFICULTY_LEVELS = {"easy" : 10, "medium" : 8, "hard" : 6}

def choose_word():
    """
    Prompts the user to choose a category.
    Selects radom word from the category listed in CATEGORIES.
    Return:
         str of randomly chosen word from CATEGORIES.
    """
    print("Welcome to Guess the Word!")
    print("\n CATEGORIES:")
    # Display available categories
    for cat in CATEGORIES:
        print(f" - {cat.title()}")

    # Ask to choose category until user provides a valid category
    while True:
        category = input("Choose a category: ").strip().lower()
        if category in CATEGORIES:
            break
        print("Invalid choice. Please choose a category.")

    # Select a random word from chosen category
    word = random.choice(CATEGORIES[category])
    return word

def choose_difficulty():
    """
    Prompts the user to choose a difficulty level.
    Return:
         int of the number of tries of that difficulty level.
    """
    print("\nDifficulty Levels(tries): easy (10), medium (8), hard (6)")

    while True:
        level = input("Choose a difficulty: ").strip().lower()
        if level in DIFFICULTY_LEVELS:
           return DIFFICULTY_LEVELS[level]
        print("Invalid choice. Please choose a difficulty level.")

def display_progress(secret_word, guessed_letters, guessed_word):
    """
    Updates the displayed word by displaying correctly guessed letters.
    Arguments:
        secret_word (str): The word the player is trying to guess.
        guessed_letters (str): The letters guessed by user.
        guessed_word (list): The current progress of the word (with underscores and letters).
    Returns:
        updated list showing the updated word
        by displaying correctly guessed letters in correct order/place.
    """
    # Loop through the word and replace underscores with the correctly guessed letter
    for index in range(len(secret_word)):
        if guessed_letters == secret_word[index] :
            guessed_word[index] = guessed_letters
    return guessed_word

def get_guess(guessed_letters):
    """
    Prompt the user to guess a letter. (Validate)
    Arguments:
        guessed_letters (list): Letters that have been guessed.
    Returns:
        str of the users guessed letters.
    """
    while True:
        guess = input("Guess a letter: ").strip().lower()

        # Check for invalid inputs
        if not guess:
            print("Can't accept blank input.")
            continue
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter between a-z.")
            continue
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        return guess

def play_round():
    """
    Play one full round of Guess the Word.
    Returns:
         bool True if player won, False otherwise.
    """
    # Choose word and set difficulty
    secret_word = choose_word()
    tries = choose_difficulty()

    # Variables for tracking guesses
    guessed_letters = set()  # Letters guessed so far
    correct_letters = set(secret_word)  # Letters in secret word
    guessed_word = ['_'] * len(secret_word)  # Display progress (underscores/letters where guessed)
    guess = ''

    # Game loop
    while tries > 0:
        print("\nWord:", display_progress(secret_word, guess, guessed_word))
        print(f"{tries} tries left")
        print("Guessed letters:", " ".join(sorted(guessed_letters)))

        # Get players guess
        guess = get_guess(guessed_letters)
        guessed_letters.add(guess)

        # Subtract a try with each guess
        tries -= 1

        # Check if guess is correct
        if guess in correct_letters:
            print("Good guess!")
            # Check if won (all letters guessed)
            if correct_letters.issubset(guessed_letters):
                print(f"Congrats! You guessed the word! {secret_word}")
                return True
        else:
            print("Sorry, wrong guess.")

    # Loop is over/ out of guesses
    print(f"You are out of guesses! The correct word was: {secret_word}")
    return False

def main():
    """
    Run game, track wins/losses, and plays/replays
    """
    wins = 0
    losses = 0

    print("---Welcome to Guess the Word!---")

    # Loop allows replaying
    while True:
        if play_round():
            wins += 1
        else:
            losses += 1

        # Display current score
        print(f"Score: {wins} win(s) / {losses} loss(es)")

        # Ask user if they want to play again
        again = input("Would you like to play again? (y/n): ").strip().lower()
        if again == "y":
            continue
        elif again == "n":
            break
        else:
            print("Invalid choice. Must enter 'y'/'n'. Please try again.")
            continue

    print("\nThank you for playing! Have a nice day!")



if __name__ == "__main__":
    main()