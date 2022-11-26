from random import randrange

from deep_dive.Q1_Ops import get_operation

choice_prompt = 'Choose level (easy, intermediate, or hard): '
questions_prompt = 'Please give us the number of question you want to attempt: '
q_type = 'Specify the question type (multiplication:M, addition:A, subtraction:S, division:D): '
prompts = [choice_prompt, questions_prompt, q_type]
questions = []
tasks = {1: '', 2: '', 3: ''}


def rand_num(param):
    _seed = 1
    if param == 'easy':
        _seed = 25
    elif param == 'intermediate':
        _seed = 75
    elif param == 'hard':
        _seed = 100
    else:
        print('\n\tInvalid difficulty mode entered\n')
    return _seed


def questionaire_loop():
    for n in range(len(prompts)):
        tasks[n + 1] = input(prompts[n])

    num = int(tasks[2])
    ran_range = rand_num(tasks[1])
    for i in range(num):
        a = randrange(ran_range)
        b = randrange(ran_range)
        _oper = tasks[3].upper()

        y =get_operation(_oper, a, b)
        answer_prompt = input(y['question'])
        if int(answer_prompt) == y['answer']:
            print('That\'s right -- well done')


if __name__ == '__main__':
    while True:
        questionaire_loop()
        response = input("Continue or exit (Continue: C, Exit: E): ")
        if response.upper() == 'C':
            continue
        else:
            break
