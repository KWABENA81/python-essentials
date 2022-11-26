
def divide(x, y):
    return "What's " + str(x) + " divided by " + str(y) + "? "


def multiply(x, y):
    return "What's " + str(x) + " multiply by " + str(y) + "? "


def add(x, y):
    return "What's " + str(x) + " plus " + str(y) + "? "


def substract(x, y):
    return "What's " + str(x) + " substract " + str(y) + "? "


def get_operation(_op, a, b):
    results = {'question': '', 'answer': 0}
    if _op == 'S':
        results['answer'] = a - b
        results['question'] = substract(a, b)
    if _op == 'M':
        results['answer'] = a * b
        results['question'] = multiply(a, b)
    if _op == 'D':
        #   rework values
        x = a + 1
        y = b + 1
        if x < y:
            tmp = y
            y = x
            x = tmp
        tmp = x % y
        if tmp > 0:
            x = x + (y - tmp)
        a = x
        b = y
        results['answer'] = a / b
        results['question'] = divide(a, b)
    if _op == 'A':
        results['answer'] = a - b
        results['question'] = add(a, b)
    return results


if __name__ == '__main__':
    pass
