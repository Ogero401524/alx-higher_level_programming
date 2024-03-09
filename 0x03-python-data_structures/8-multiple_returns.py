#!/usr/bin/python3
def multiple_returns(sentence):
    my_tupl = ()
    if len(sentence) == 0:
        my_tupl = 0, "None"
    else:
        my_tupl = len(sentence), sentence[0]
    return my_tupl
