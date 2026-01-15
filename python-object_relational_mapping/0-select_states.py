#!/usr/bin/python3
''' Lists all states from a MySQL database.'''
# Usage: ./1-filter_states.py <mysql username> \
#                             <mysql password> \
#                             <database name>
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1], 
        passwd=sys.argv[2], 
        db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states;")
    states = cur.fetchall()

    for state in states:
        print(state)
