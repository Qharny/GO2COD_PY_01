# Number Guessing Game 🎲🔢

## Overview

This is a simple, interactive Python Number Guessing Game where players try to guess a randomly generated number. The game provides real-time feedback and allows players to test their guessing skills.

## Features

- 🎯 Random number generation between 1 and 100
- 📊 Attempt tracking
- 🆘 Exit game option
- 🔁 Play multiple rounds
- 🛡️ Input validation
- 📝 Helpful feedback messages

## Requirements

- Python 3.x
- `random` module (included in Python standard library)

## How to Play

1. Run the script
2. The game will generate a random number between 1 and 100
3. Enter your guess
4. Receive feedback:
   - "Too low!" if your guess is smaller than the target
   - "Too high!" if your guess is larger than the target
   - "Congratulations!" when you guess correctly
5. See how many attempts it took you to guess the number
6. Choose to play again or exit

### Special Commands

- `exit`: Quit the current game at any time
- `yes/no`: Choose to play another round after completing a game

## Game Controls

- Enter numbers between 1 and 100
- Type `exit` to quit the current game
- Respond with `yes` to play again
- Respond with `no` to end the game

## Example Gameplay

```
Welcome to the Number Guessing Game!
Guess the number between 1 and 100.
Type 'exit' at any time to quit the game.

Enter your guess: 50
Too low! Try a higher number.
Enter your guess: 75
Too high! Try a lower number.
Enter your guess: 62
Congratulations! You've guessed the number 62 correctly!
It took you 3 attempts.

Do you want to play again? (yes/no): yes
```

## Installation

No special installation required. Ensure you have Python 3.x installed.

### Running the Game

```bash
python numberguess.py
```

## Error Handling

- Invalid numeric inputs are caught and prompt for re-entry
- Non-numeric inputs display a helpful message
- Mid-game exit is supported

## Customization

You can easily modify the code to:
- Change the number range
- Adjust difficulty
- Add more complex feedback mechanisms


## Author

Manasseh Kabutey Kwame

## Acknowledgments

- Python `random` module
- Simple console-based game design
- GO2COD