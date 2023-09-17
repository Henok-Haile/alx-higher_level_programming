#!/usr/bin/python3
""" A script that takes in the name of a state as an argument and lists
all cities of that state, using the database hbtn_0e_4_usa """

import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT c.name \
                FROM cities c \
                INNER JOIN states s \
                    ON s.id=c.state_id \
                WHERE s.name=%s", (sys.argv[4],))
    rows = cur.fetchall()
    city_names = []
    for state in rows:
        city_names.append(state[0])
    print(*city_names, sep=", ")
    cur.close()
    db.close()
