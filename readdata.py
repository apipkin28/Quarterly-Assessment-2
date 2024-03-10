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

# Function to fetch all data from a specific table
def fetch_all_data(table_name):
    # Connect to the database
    conn = sqlite3.connect('QuizBowl.db')
    cr = conn.cursor()

    # Fetch all data from the table
    cr.execute(f"SELECT * FROM {table_name};")
    data = cr.fetchall()

    # Close the connection
    conn.close()

    return data