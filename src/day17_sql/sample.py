import sqlite3

conn = sqlite3.connect("college.db")
cursor = conn.cursor()

# Fresh table
cursor.execute("DROP TABLE IF EXISTS students")

cursor.execute("""
CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    marks INTEGER
)
""")

# Insert data
cursor.execute("INSERT INTO students VALUES (1, 'Amit', 85)")
cursor.execute("INSERT INTO students VALUES (2, 'Riya', 92)")
cursor.execute("INSERT INTO students VALUES (3, 'John', 78)")

conn.commit()

# 🔹 Your new condition
cursor.execute("SELECT * FROM students WHERE marks > 80 AND name != 'John'")
rows = cursor.fetchall()

print("Filtered Students:")
for row in rows:
    print(row)

conn.close()