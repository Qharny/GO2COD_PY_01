import random

def number_guessing_game():
    # Generate a random number between 1 and 100
    target_number = random.randint(1, 100)
    
    # Initialize attempt counter
    attempts = 0
    
    print("Welcome to the Number Guessing Game!")
    print("Guess the number between 1 and 100.")
    print("Type 'exit' at any time to quit the game.")
    
    # Continue the game until the correct number is guessed
    while True:
        try:
            # Get user's guess
            user_input = input("Enter your guess: ")
            
            # Check for exit command
            if user_input.lower() == 'exit':
                print(f"\nGame ended. The number was {target_number}.")
                return
            
            # Convert input to integer
            user_guess = int(user_input)
            
            # Increment attempts
            attempts += 1
            
            # Check the guess and provide feedback
            if user_guess < target_number:
                print("Too low! Try a higher number.")
            elif user_guess > target_number:
                print("Too high! Try a lower number.")
            else:
                # Correct guess
                print(f"\nCongratulations! You've guessed the number {target_number} correctly!")
                print(f"It took you {attempts} attempts.")
                break
        
        except ValueError:
            # Handle invalid input
            print("Please enter a valid number or 'exit'!")

def main():
    while True:
        # Play the number guessing game
        number_guessing_game()
        
        # Ask if player wants to play again
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye.")
            break

# Run the game
if __name__ == "__main__":
    main()