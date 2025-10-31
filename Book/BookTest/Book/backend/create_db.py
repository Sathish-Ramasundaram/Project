import sqlite3

conn = sqlite3.connect("book.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS pages (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT,
  content TEXT
)
""")

# Insert sample page
cursor.execute("INSERT INTO pages (title, content) VALUES (?, ?)", (
  "Be thankful for what you have",
  "Some people aren't as fortunate as you. Some people are missing organs that you have."
))

cursor.execute("INSERT INTO pages (title, content) VALUES (?, ?)", (
    "Health is Wealth", 
    "As long as your body is healthy, you have thousands of problems.\n" 
    "But the moment your body gets sick, you have only one problem.\n\n"
    "That's why, before tackling everything else or figuring out how to build your life, make sure your body stays healthy.\n"
    "So, respect, take care of, love, and nourish your body. Give your body top priority."))

# You can repeat this block for each of your 20 pages:
# cursor.execute("INSERT INTO pages (title, content) VALUES (?, ?)", ("Title", "Content"))

conn.commit()
conn.close()
print("book.db created successfully!")
