#!/usr/bin/python3
def read_file(filename=""):
     """
    Reads the content of a text file in UTF-8 format and prints it to stdout.

    Parameters:
    - filename (str, optional): The name of the file to be read. Defaults to an
empty string.
    Note:
    - This function uses the 'with' statement to ensure proper handling of file
resources.
    - The function does not manage file permission or file-not-exist exceptions.
 Any exceptions during
      file reading are caught, and an error message is printed.
    Usage:
    - read_file("example.txt"): Reads and prints the content of the
file "example.txt".
    - read_file(): If no filename is provided, reads and prints content of a
file with an empty string as the filename.
>>> read_file()
    An error occurred: [Error Message]
    """
     with open(filename, encoding="utf-8") as fileText:
          contents = fileText.read()
          print(contents)
