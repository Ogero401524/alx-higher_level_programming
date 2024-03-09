#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    listINord = list(a_dictionary.keys())
    listINord.sort()
    for i in listINord:
        print("{}: {}".format(i, a_dictionary.get(i)))
