#!/usr/bin/python3
def write_file(filename="", textttts=""):
    with open(filename, "w", encoding="utf-8") as fil:
        uh = fil.write(textttts)
        return (uh)
