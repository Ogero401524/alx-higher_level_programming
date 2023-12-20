#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    PRINTEL = 0
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end= " ")
            PRINTEL += 1
    except IndexError:
        pass
    print()
    return PRINTEL
