from brain_games1.random import random_num

description = 'Answer "yes" if the number is even, otherwise answer "no".'


def game_actions():
    question = random_num()
    right_answer = 'yes' if question % 2 == 0 else 'no'
    return question, right_answer
