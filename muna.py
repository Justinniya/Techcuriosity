import sqlite3

# Connect to the SQLite database (or create it)
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Create a sample table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Age INTEGER NOT NULL
)
''')

# Insert sample data
cursor.execute("INSERT INTO users (Name, Age) VALUES ('Alice', 30)")
cursor.execute("INSERT INTO users (Name, Age) VALUES ('Bob', 25)")
cursor.execute("INSERT INTO users (Name, Age) VALUES ('Charlie', 35)")

conn.commit()
conn.close()
