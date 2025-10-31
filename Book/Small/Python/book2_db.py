import sqlite3

# Connect to SQLite database (creates book.db if it doesn't exist)
conn = sqlite3.connect('book2.db')
cursor = conn.cursor()

# Create table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY,
        title TEXT,
        author TEXT
    )
''')

# INSERT a book
cursor.execute("INSERT INTO books (title, author) VALUES (?, ?)", ("Atomic Habits", "James Clear"))

# SELECT all books
cursor.execute("SELECT * FROM books")
print("Before update:")
for row in cursor.fetchall():
    print(row)

# UPDATE the author name
cursor.execute("UPDATE books SET author = ? WHERE title = ?", ("J. Clear", "Atomic Habits"))

# SELECT again to see changes
cursor.execute("SELECT * FROM books")
print("After update:")
for row in cursor.fetchall():
    print(row)

# Save and close
conn.commit()
conn.close()
