#!/usr/bin/python3
"""List states whose names start with an uppercase N."""

import sys

import MySQLdb


if __name__ == "__main__":
    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
    )

    cursor = connection.cursor()
    cursor.execute(
        "SELECT id, name FROM states "
        "WHERE name LIKE BINARY 'N%' "
        "ORDER BY states.id ASC"
    )

    for state in cursor.fetchall():
        print(state)

    cursor.close()
    connection.close()
