from brain_games1.cli import welcome_user
import prompt


def game_logic(game):
    name = welcome_user()
    print(f'{game.description}')
    for _ in range(3):
        question, right_answer = game.game_actions()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if user_answer == right_answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{right_answer}'."
                  f"\nLet's try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')
