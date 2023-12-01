#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    argument = sys.argv
    sizeArgument = len(argument) - 1

    if sizeArgument > 1:
        print("{} arguments:".format(sizeArgument))
        for i in range(1, sizeArgument + 1):
            print("{}: {}".format(i, argument[i]))

    elif sizeArgument == 0:
        print("{} arguments.".format(sizeArgument))

    else:
        print("{} argument:".format(sizeArgument))
        print("{}: {}".format(sizeArgument, argument[1]))
