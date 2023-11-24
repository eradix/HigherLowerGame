from art import logo, vs
from game_data import data
import random, os

def clean_screen():
    '''clear the console screen'''
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For macOS and Linux
    else:
        os.system('clear')

def get_highest_follower(choice1, choice2):
    if choice1['follower_count'] > choice2['follower_count']:
        return choice1
    return choice2

if __name__ == '__main__':
    clean_screen()
    game_over = False
    score = 0
    message=""
    # random data for letter a
    letter_a = random.choice(data)
    while not game_over:
        # logo
        print(logo)
        # message
        print(message)

        # filter the data must not contain the letter a
        filtered_data = [d for d in data if d != letter_a]
        # random data for letter b
        letter_b = random.choice(filtered_data)


        print(f"Compare A: {letter_a['name']}, {letter_a['description']}, from {letter_a['country']}")

        print(vs)

        print(f"Against B: {letter_b['name']}, {letter_b['description']}, from {letter_b['country']}")

        # ensures user enters the right input
        right_user_input = False
        while not right_user_input:
            user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
            if user_choice not in ['a', 'b']:
                print('Invalid input.')
            else:
                right_user_input = True

        # get the answer
        answer = get_highest_follower(letter_a, letter_b)
        # get user answer
        user_answer = letter_a if user_choice == 'a' else letter_b

        # check if user is correct
        if answer == user_answer:
            score += 1
            message = f"You're right!, Current score: {score}"
            letter_a = letter_b
            clean_screen()
        else:
            game_over = True

    print(f"Game over. Your score is {score}")
    




