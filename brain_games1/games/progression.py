import random

description = 'What number is missing in the progression?'


def game_actions():
    start = random.randint(0, 20)
    difference = random.randint(1, 5)
    count = random.randint(5, 10)

    progression = list(range(start, start + difference * count, difference))

    num_idx = random.randint(0, count - 1)
    right_answer = str(progression[num_idx])
    progression[num_idx] = '..'

    question = ''
    for i in range(count):
        if i == num_idx:
            question += '.. '
        else:
            question += str(progression[i]) + ' '

    return question, right_answer
