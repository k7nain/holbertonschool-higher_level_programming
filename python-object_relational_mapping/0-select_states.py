#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Al arguments: username, password, database
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to MySQL on localhost:3306
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=password,
        db=database
    )

    cursor = db.cursor()
    # Execute query, order by id ascending
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Print each row
    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()
