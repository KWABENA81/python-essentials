#   Q1.
#   Write a program to print the:
#   a.  Number of lowercase “a” and “o” in the following sentence.
#   b.  Number of uppercase “L” and “N” in the following sentence.
#   ‘Discover, Learning, withA, Edureka’
def q1():
    lcount = 0
    ucount = 0
    sentence = 'Discover, Learning, with, Edureka'

    for l in sentence:
        if l.islower() and (l == 'a' or l == 'o'):
            lcount += 1
        elif l.isupper() and (l == 'L' or l == 'N'):
            ucount += 1

    print('Number of lowercase “a” and “o” in the sentence: ', lcount)
    print('Number of uppercase “L” and “N” in the sentence: ', ucount)


if __name__ == '__main__':
    q1()
