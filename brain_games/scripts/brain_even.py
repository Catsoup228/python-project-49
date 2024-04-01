from ..cli import welcome_user
import random
import prompt


def main():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for i in range(3):
        ran_num = random.randrange(0, 100)
        print(f'Question: {ran_num}')
        answer = prompt.string('Your answer: ')
        if (int(ran_num % 2 == 0) & int(answer == 'yes')) | (int(ran_num % 2 != 0) & int(answer == 'no')):
            print('Correct!')
        elif (int(ran_num % 2 == 0) & int(answer == 'no')):
            return f"'{answer}' is wrong answer ;(. Correct answer was 'yes'.\nLet's try again, {name}!"
        elif (int(ran_num % 2 != 0) & int(answer == 'yes')):
            return f"'{answer}' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, {name}!"    
    print(f'Congratulations, {name}!')

    
    
