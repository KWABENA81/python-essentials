#   2.  Write a recursive function to compute x raised to the power of n.

def recusive_pow(base, exp):
    if exp == 0:
        return 1
    else:
        return base * recusive_pow(base, exp - 1)


if __name__ == '__main__':
    n = 9
    x = 2
    pw = recusive_pow(x, n)
    print('pow(', x, ', ', n, '): ', pw)
