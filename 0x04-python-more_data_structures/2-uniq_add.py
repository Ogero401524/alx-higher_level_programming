#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniqlist = set(my_list)
    numT = 0

    for i in uniqlist:
        numT += i

    return (numT)
