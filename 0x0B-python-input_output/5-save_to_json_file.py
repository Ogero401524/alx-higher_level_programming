import json

def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using its JSON representation.

    Parameters:
    - my_obj: The object to be serialized to JSON and saved to the file.
    - filename (str): The name of the file where the JSON representation will be saved.

    Returns:
    - None

"""
    with open(filename, "w", encoding="utf-8") as fil:
        json.dump(my_obj, fil)
