"""
Usage: python guessing_game.py
"""

TARGET      = 42 
UPPER_BOUND = 100  
LOWER_BOUND = 1

def guessing_game():
    while True:
        try:
            user_guess = int(input(f'Guess a number between {LOWER_BOUND} and {UPPER_BOUND}: '))
            if user_guess < LOWER_BOUND or user_guess > UPPER_BOUND:
                print(f'Input should be a number between {LOWER_BOUND} and {UPPER_BOUND}')
                continue
            if user_guess == TARGET:
                print('Correct')
                break
            else:
                print('Incorrect')
        except ValueError:
            print('Incorrect')

if __name__ == "__main__":
    guessing_game()