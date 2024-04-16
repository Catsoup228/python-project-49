from brain_games1.random import random_num
import random

description = 'What is the result of the expression?'


def game_actions():
    first_number = random_num()
    second_number = random_num()

    operators = ['+', '-', '*']
    operator = random.choice(operators)

    question = f'{first_number} {operator} {second_number}'
    answer = 0

    if operator == '+':
        answer = first_number + second_number
    elif operator == "-":
        answer = first_number - second_number
    elif operator == "*":
        answer = first_number * second_number
    right_answer = str(answer)

    return question, right_answer
