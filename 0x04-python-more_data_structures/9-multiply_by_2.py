#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    newdic = a_dictionary.copy()
    list_keys = list(newdic.keys())

    for i in list_keys:
        newdic[i] *= 2

    return (newdic)
