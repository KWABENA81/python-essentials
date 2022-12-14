#   4.  Sort the list using operator.itemgetter function mylist = [["john", 1, "a"], ["larry", 0, "b"]].
#   Sort the list by second item 1 and 0.
#
import operator


def run_sort():
    mylist = [["john", 1, "a"], ["larry", 0, "b"]]
    print('Original list before sorting: ', mylist)

    #   "sort list based on index"
    index = 1
    new_list = sorted(mylist, key=operator.itemgetter(index))
    print('Sorted list based on index[', index, '] : ', new_list)

    index = 0
    new_list = sorted(mylist, key=operator.itemgetter(index))
    print('Sorted list based on index[', index, '] : ', new_list)


if __name__ == '__main__':
    run_sort()
