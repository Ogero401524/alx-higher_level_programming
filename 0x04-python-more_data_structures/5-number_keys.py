#!/usr/bin/python3
def number_keys(a_dictionary):
    numT = 0
    listOfkeys = list(a_dictionary.keys())

    for i in listOfkeys:
        numT += 1

    return (numT)
