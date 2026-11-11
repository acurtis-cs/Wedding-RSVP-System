
import sqlite3
import os

# Locate the project's main folder
folder = os.path.dirname(__file__)

# Locate wedding.db
database = os.path.join(folder, "wedding.db")


# Retrieve information from the database
def fetch_data(query, parameters=()):
    # Open a connection to the SQLite database.
    connection = sqlite3.connect(database)

    try:
        # Create a cursor object to execute SQL commands.
        cursor = connection.cursor()
        # Execute the SQL query with the provided parameters.
        cursor.execute(query, parameters)
        # Fetch all rows from the query result.
        data = cursor.fetchall()
        # Return the fetched data.
        return data
    # Ensure the database connection is closed even if an error occurs.
    finally:
        connection.close()
