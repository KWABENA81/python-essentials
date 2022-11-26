#    3.  Sort the list using lambda function mylist = [["john", 1, "a"], ["larry", 0, "b"]].
#    Sort the list by second item 1 and 0.

def run_sort():
    mylist = [["john", 1, "a"], ["larry", 0, "b"]]
    print('Original list before sorting: ', mylist)

    #   "sort list based on index"
    index = 1
    mylist.sort(key=lambda y: y[index])
    print('Sorted list based on index[', index, '] : ', mylist)

    index = 0
    mylist.sort(key=lambda y: y[index])
    print('Sorted list based on index[', index, '] : ', mylist)


if __name__ == '__main__':
    run_sort()
