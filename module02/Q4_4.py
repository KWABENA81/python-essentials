alist = ['a', 'b', 'c', 'd']

dict = {}
for x, l in enumerate(alist, start=1):
    dict[l] = x

print(dict)

#   {'a': 1, 'b': 2, 'c': 3, 'd': 4}