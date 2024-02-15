#!/usr/bin/python3
import sys

from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

def add_item_to_list():
    existing_items = load_from_json_file("add_item.json") or []
    new_items = sys.argv[1:]
    combined_list = existing_items + new_items
    ave_to_json_file(combined_list, "add_item.json")

if __name__ == "__main__":
    add_item_to_list()
