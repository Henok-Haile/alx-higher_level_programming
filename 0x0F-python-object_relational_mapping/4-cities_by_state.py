#!/usr/bin/python3
""" A script that lists all cities from the database hbtn_0e_4_usa """

import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT c.id, c.name, s.name \
                From cities as c \
                INNER JOIN states as s \
                ON s.id=c.state_id")
    rows = cur.fetchall()
    for state in rows:
        print(state)
    cur.close()
    db.close()
