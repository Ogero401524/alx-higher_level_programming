#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    listes = list(a_dictionary.keys())

    for valuedic in listes:
        if value == a_dictionary.get(valuedic):
            del a_dictionary[valuedic]

    return (a_dictionary)
