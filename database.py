import sqlite3

# Database configuration
DATABASE_NAME = 'expenses.db'

# Create a connection to the SQLite database
conn = sqlite3.connect(DATABASE_NAME)

# Create a cursor object using the connection
cursor = conn.cursor()

# Example table creation (Uncomment to use)
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS expenses (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     description TEXT NOT NULL,
#     amount REAL NOT NULL,
#     date TEXT NOT NULL
# )
# ''')

# Commit the changes
# conn.commit()

# Close the connection
# conn.close()