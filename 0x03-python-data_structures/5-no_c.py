#!/usr/bin/python3
def no_c(my_string):
    new_stringsNew = my_string.translate({ord(i): None for i in 'cC'})
    return new_stringsNew
