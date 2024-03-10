import sqlite3

# Function to get table names from the database
def getTableNames():
    # Connect to the database
    conn = sqlite3.connect('QuizBowl.db')
    cr = conn.cursor()

    # Fetch table names
    cr.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cr.fetchall()

    # Close the connection
    conn.close()

    # Extract table names from the result
    tableNames = [table[0] for table in tables]
    return tableNames