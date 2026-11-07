
import sqlite3
import os

# Locate the project's main folder
folder = os.path.dirname(__file__)

# Locate wedding.db
database = os.path.join(folder, "wedding.db")


# Retrieve information from the database
def fetch_data(query, parameters=()):

    connection = sqlite3.connect(database)

    try:
        cursor = connection.cursor()

        cursor.execute(query, parameters)

        data = cursor.fetchall()

        return data

    finally:
        connection.close()
