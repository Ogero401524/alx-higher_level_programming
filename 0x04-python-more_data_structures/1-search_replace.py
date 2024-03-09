#!/usr/bin/python3
def search_replace(my_list, search, replace):
    newwllist = list(map(lambda a: replace if a == search else a, my_list))
    return (newwllist)
