#!/usr/bin/python3
"""list all states """
import MySQLdb
import sys

if __name__ == "__main__":
    listdb = MySQLdb.connect(host="localhost",
                             user=sys.argv[1], passwd=sys.argv[2],
                             listdb=sys.argv[3], port=3306)
    pointer = listdb.cursor()
    pointer.execute("SELECT * FROM states")
    r = pointer.fetchall()
    for rw in r:
        print(rw)
    pointer.close()
    listdb.close()
