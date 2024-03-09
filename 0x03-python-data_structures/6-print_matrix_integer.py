#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for rw in matrixX:
        for cl in rw:
            print("{:d}".format(cl), end=" " if cl != rw[-1] else "")
        print()
