#!/usr/bin/python3
"""
Lists all states from hbtn_0e_0_usa
Usage: ./0-select_states.py <mysql username> \
                            <mysql password> \
                             <database name>
"""
import sys
import MySQLdb


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database)

        cursor = db.cursor()

        cursor.execute("SELECT * FROM states ORDER BY id ASC")

        for state in cursor.fetchall():
            print(state)

        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print("Error connecting to MySQL database: {}".format(e))
        exit(1)
