#!/usr/bin/python3
'''Lists all states from a MySQL database.'''
import sys
import MySQLdb


if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=password, 
        db=db_name)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC;")
    for state in cur.fetchall():
        print(state)
