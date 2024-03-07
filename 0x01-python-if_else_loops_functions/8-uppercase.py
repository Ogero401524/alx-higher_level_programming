#!/usr/bin/python3
def uppercase(str):
    for chaee in str:
        if ord(chaee) >= 97 and ord(chaee) <= 122:
            chaee = chr(ord(chaee) - 32)
        print("{}".format(chaee), end="")
    print()
