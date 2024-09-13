import random

results = []

def display_resultsboard():
    """Displays the prev-attempts"""
    if not results:
        print("No results yet.")
    else:
        print("\nResults Board:")
        for result in results:
            print(f"Player: {result['name']}, Difficulty: {result['difficulty']}, Remaining Attempts: {result['attempts']}")
    print()


def display_difficulty():
    """Prompts the user to select a difficult level."""
    while True:
        print("\nSelect difficulty level:")
        print("1. Easy (Range: 1-20, 7 attempts)")
        print("2. Medium (Range: 1-50, 5 attempts)")
        print("3. Hard (Range: 1-100, 3 attempts)")
        choice = input("Enter your choice (1, 2, or 3): ").strip()

        if choice == "1":
            return 'Easy', 1, 20, 7
        elif choice == "2":
            return 'Medium', 1, 50, 5
        elif choice == "3":
            return 'Hard', 1, 100, 3
        else:
            print("Invalid choice. Please try again.")


def play():
    "Play console"
    player_name = input("Enter your name: ").strip()
    difficulty, lower_bound, upper_bound, attempts = display_difficulty()

    random_number = random.randint(lower_bound, upper_bound)

    print(f"\nYou selected {difficulty} difficulty.")
    print(f"You have {attempts} attempts to guess the number between {lower_bound} and {upper_bound}.")

    remaining_attempts = attempts
    while remaining_attempts > 0:
        try:
            guess = int(input(f"\nEnter your guess ({lower_bound}-{upper_bound}): ").strip())
            if guess < lower_bound or guess > upper_bound:
                print(f"Please enter a number between {lower_bound} and {upper_bound}.")
                continue

            # Correct answer case
            if guess == random_number:
                print(f"Congratulations, {player_name}! You guessed the number correctly.")
                results.append({
                    'name': player_name,
                    'difficulty': difficulty,
                    'attempts': remaining_attempts
                })
                display_resultsboard()
                break

            # Incorrect answer case
            elif guess < random_number:
                print("Too low!")
            else:
                print("Too high!")

            remaining_attempts -= 1
            print(f"Remaining attempts: {remaining_attempts}")


        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Attempts run out case
    if remaining_attempts == 0:
        print(f"\nSorry, {player_name}. You ran out of attempts. The correct number was {random_number}.")


def main():
    """Main console"""
    while True:
        print("\nWelcome to the Game of Chance!")
        print("1. Play")
        print("2. View Results Board")
        print("3. Exit")
        choice = input("Enter your choice (1, 2, or 3): ").strip()

        if choice == "1":
            play()
        elif choice == "2":
            display_resultsboard()
        elif choice == "3":
            print("Thank you for playing! Goodbye.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

















