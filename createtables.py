import sqlite3

# defining function to create tables
def tableCreation():
    # connecting to db
    conn = sqlite3.connect('QuizBowl.db')
    cr = conn.cursor()