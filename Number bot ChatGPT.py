def guess_number():
    while True:
        try:
            # Get the range from the user
            lower_bound = int(input("Enter the smaller number of the range: "))
            upper_bound = int(input("Enter the larger number of the range: "))

            # Validate the range
            if lower_bound >= upper_bound:
                print("Invalid range. The smaller number must be less than the larger number. Please try again.")
                continue

            # Get the number to guess from the user
            target_number = int(input(f"Enter the number you want the program to guess (between {lower_bound} and {upper_bound}): "))

            # Validate the target number
            if target_number < lower_bound or target_number > upper_bound:
                print(f"Invalid number. The number must be between {lower_bound} and {upper_bound}. Please try again.")
                continue

            # Get the number of attempts from the user
            attempts = int(input("Enter the number of attempts the program should make: "))

            # Validate the number of attempts
            if attempts <= 0:
                print("Invalid number of attempts. Please enter a positive number. Please try again.")
                continue

            break

        except ValueError:
            print("Invalid input. Please enter integer values. Please try again.")

    # Start guessing
    print("\nStarting the guessing game...\n")

    guess_count = 0
    for attempt in range(1, attempts + 1):
        # Guess the midpoint of the current range
        guess = (lower_bound + upper_bound) // 2
        guess_count += 1
        print(f"Attempt {attempt}: The program guesses {guess}")

        if guess == target_number:
            print(f"The program guessed the correct number in {guess_count} attempts!")
            return
        elif guess < target_number:
            lower_bound = guess + 1
        else:
            upper_bound = guess - 1

    print(f"The program did not guess the correct number within the given attempts. Total guesses made: {guess_count}")

# Run the guessing game
guess_number()