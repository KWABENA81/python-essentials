from random import random, randrange

choice_prompt = 'Choose level (easy, intermediate, or hard): '
questions_prompt = 'Please give us the number of question you want to attempt: '
q_type = 'Specify the question type (multiplication:M, addition:A, subtraction:S, division:D): '
prompts = [choice_prompt, questions_prompt, q_type]
questions = []
tasks = {1: '', 2: '', 3: ''}


def divide(x, y):
    if x > y:
        return "What's " + str(x) + " divided by " + str(y) + "? "
    else:
        return "What's " + str(x) + " divided by " + str(y) + "? "


def multiply(x, y):
    return "What's " + str(x) + " multiply by " + str(y) + "? "


def add(x, y):
    return "What's " + str(x) + " plus " + str(y) + "? "


def substract(x, y):
    return "What's " + str(x) + " substract " + str(y) + "? "
# def questionaire_loop():
#     for n in range(len(prompts)):
#         tasks[n + 1] = input(prompts[n])
#
#     num = int(tasks[2])
#     for i in range(num):
#         print(randrange(11))
#         a = randrange(25)
#         b = randrange(19)
#         answer = input(substract(a, b))
#         print(answer)


if __name__ == '__main__':
    pass