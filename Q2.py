#  Q2.
#  Write a program to remove the following from:
#  www.edureka.in
#  a. Remove all w’s before and after .edureka.
#  b. Remove all lowercase letter before and after .edureka.
#  c. Remove all printable characters

def q():
    return 'www.edureka.in'


def q2a():
    web_addr = q()
    print('(a) ', web_addr.lstrip('w'))


def q2b():
    sentence = q()
    fn = sentence.index('.')
    ln = sentence.rindex('.')
    n = 0
    _sentence = ''
    for l in sentence:
        if n < fn:
            if l.isupper():
                _sentence += l
            else:
                _sentence += '#'
        elif n > ln:
            if l.isupper():
                _sentence += l
            else:
                _sentence += '#'
        else:
            _sentence += l
        n += 1
    sentence = _sentence.strip('#')
    print('(b) ', 'sentence: ', sentence)


def q2c():
    sentence = q()
    prt_sentence = ''
    for l in sentence:
        if l.isprintable():
            prt_sentence += l

    print('(c) ', 'printable sentence: ', prt_sentence)


if __name__ == '__main__':
    q2a()
    q2b()
    q2c()
