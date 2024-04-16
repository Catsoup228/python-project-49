from brain_games1.random import random_num

description = 'Find the greatest common divisor of given numbers.'


def game_actions():
    first_number = random_num()
    second_number = random_num()
    question = f'{first_number} {second_number}'
    while first_number != 0 and second_number != 0:
        if first_number > second_number:
            first_number = first_number % second_number
        else:
            second_number = second_number % first_number
    right_answer = str(first_number + second_number)
    return question, right_answer
