from brain_games1.random import random_num

description = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(n):
    d = 2
    while n % d != 0:
        d += 1
    return d == n


def game_actions():
    question = random_num()
    right_answer = 'yes' if is_prime(question) is True else 'no'
    return question, right_answer
