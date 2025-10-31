import sqlite3

# step 1: Connect to the database (creates book.db if it doesn't exist)

conn = sqlite3.connect('book.db')

# Step 2: Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Step 3: Create a table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
               id INTEGER PRIMARY KEY, 
               title TEXT, 
               author TEXT
               )

''')


# Step 4: Insert a book
cursor.execute("INSERT INTO books (title, author) VALUES (?, ?)", ("Habits", "Sathish"))

# Step 5: Commit changes and close the connection
conn.commit()
conn.close()