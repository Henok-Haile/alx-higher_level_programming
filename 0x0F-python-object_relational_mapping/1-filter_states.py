#!/usr/bin/python3
"""  A script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa """

import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("""SELECT * FROM states WHERE name
                REGEXP '^N' ORDER BY states.id""")
    rows = cur.fetchall()
    for state in rows:
        print(state)
    cur.close()
    db.close()
