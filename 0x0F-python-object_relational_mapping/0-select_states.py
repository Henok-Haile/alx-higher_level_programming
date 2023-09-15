#!/usr/bin/python3
# A script that lists all states from the database hbtn_0e_0_usa.

import sys
import MySQLdb

if __name__ == "__main__":
	db = MySQLdb.connect(user=sys.argv[1], paaswd=sys.argv[2], db=sys.argv[3])
	cur = db.cursor()
	cur.execute("SELECT * FROM states")
	for state in cur.fetchall():
		print(state)
