#!/usr/bin/python3

if __name__ == "__main__":
    import importlib

    try:
        hidden_4 = importlib.import_module("hidden_4")

        # Get all names defined in the module
        all_names = dir(hidden_4)

        # Filter names that do not start with '__' and print them in alphabetical order
        _names = sorted(name for name in all_names if not name.startswith('__'))
        for name in _names:
            print(name)

    except ImportError:
        print("Error: Module 'hidden_4' not found.")
