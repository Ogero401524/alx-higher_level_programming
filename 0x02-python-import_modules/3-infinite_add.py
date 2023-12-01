#!/usr/bin/python3
# Prints the result of the addition of all arguments

if __name__ == "__main__":
    import sys

    # Extracting command-line argts excluding  name)
    arguments = sys.argv[1:]

    # Usi list comprehension to add integers
    result = sum(map(int, arguments))

    # Priting the result
    print(result)
