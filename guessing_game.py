"""
Usage: python main.py
"""

TARGET      = 42 
UPPER_BOUND = 100  
LOWER_BOUND = 1

def guessing_game():
    while True:
        try:
            user_guess = int(input('Guess a number between 1 and 100: '))
            if user_guess < LOWER_BOUND or user_guess > UPPER_BOUND:
                print('Input should be a number between 1 and 100')
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