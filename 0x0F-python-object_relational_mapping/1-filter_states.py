#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys


if __name__ == "__main__":
    dbase = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], dbase=sys.argv[3], port=3306)
    cursa = db.cursor()
    cursa.execute("""SELECT * FROM states WHERE name
                LIKE BINARY 'N%' ORDER BY states.id""")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cursa.close()
    dbase.close()
