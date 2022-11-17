# 4.    Write a program for String Formatting Operator % which should include
#   the following conversions:
#   a.  Character
#   b.  Signed decimal integer
#   c.  Octal integer
#   d.  Hexadecimal integer (UPPERcase letters)
#   e.  Floating point real number
#   f.  Exponential notation (with lowercase 'e')


def q4a():
    formatter = '%d %c '
    print('Print Characters: ')
    print('num -> char:', formatter % (128, 128))
    print('num -> char:', formatter % (91, 91))
    print('num -> char:', formatter % (219, 219))
    print('num -> char:', formatter % (119, 119))


def q4b():
    print('\nSigned decimal integer: {:+4.1f} '.format(128.09))
    print('Signed decimal integer: {:+4.1f} '.format(-128))


def q4c():
    print("\nOctal integer for 12: %o" % 12)
    print("Octal integer for 831: %o" % 831)


def q4d():
    print('\nHexadecimal integer (12809) %X: ' % 82909)
    print('Hexadecimal integer (999) %X: ' % 999)


def q4e():
    print('\nFloating point real number (128.90009): %6.2d ' % 128.90009)
    print('Floating point real number (99.49): %4.1d ' % 99.49)


def q4f():
    print('\nExponential notation  (128.90009): %6.2e ' % 128.90009)
    print('Exponential notation  (.009949): %4.1e ' % .009949)


if __name__ == '__main__':
    q4a()
    q4b()
    q4c()
    q4d()
    q4e()
    q4f()
