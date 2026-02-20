import sqlite3

conn=sqlite3.connect("internship.db")
cursor=conn.cursor()

cursor.execute("DROP TABLE IF EXISTS interns")

cursor.execute("""
               CREATE TABLE interns(
                   id INTEGER PRIMARY KEY,
                   name TEXT,
                   track TEXT,stipened INTEGER
                   )
               """)

cursor.execute("INSERT INTO interns VALUES (1, 'Amit', 'Data Science', 15000)")
cursor.execute("INSERT INTO interns VALUES (2, 'Riya', 'Web Dev', 12000)")
cursor.execute("INSERT INTO interns VALUES (3, 'John', 'Cybersecurity', 18000)")
cursor.execute("INSERT INTO interns VALUES (4, 'Sneha', 'Data Science', 16000)")
cursor.execute("INSERT INTO interns VALUES (5, 'Rahul', 'Web Dev', 11000)")

conn.commit()

cursor.execute("SELECT name,track FROM interns")
rows=cursor.fetchall()

print("Intern Names and Tracks : ")
for row in rows:
    print(row)
conn.close()