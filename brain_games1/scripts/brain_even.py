from brain_games1.cli import welcome_user
import random
import prompt


def main():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    options = ['yes', 'no']
    for i in range(3):
        ran_num = random.randrange(0, 100)
        print(f'Question: {ran_num}')
        answer = prompt.string('Your answer: ')
        if answer in options:
            if (answer == options[ran_num % 2]):
                print('Correct!')
            else:
                print(f"'{answer}' is wrong answer ;(. Correct answer was '{options[ran_num % 2]}'.\nLet's try again, {name}!");
                return
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{options[ran_num % 2]}'.\nLet's try again, {name}!");
            return  
    print(f'Congratulations, {name}!')

