import sqlite3
import pandas as pd

conn = sqlite3.connect("internship.db")
cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS interns")
cursor.execute("""
CREATE TABLE interns (
    id INTEGER PRIMARY KEY,
    name TEXT,
    track TEXT,
    stipend INTEGER
)
""")
cursor.executemany("""
INSERT INTO interns VALUES (?, ?, ?, ?)
""", [
    (1, 'Amit', 'Data Science', 15000),
    (2, 'Sneha', 'Cybersecurity', 8000),
    (3, 'Rahul', 'Data Science', 4000),
    (4, 'Priya', 'Blockchain', 10000),
    (5, 'Arjun', 'Data Science', 7000),
    (6, 'Meera', 'Cybersecurity', 6000)
])
cursor.execute("DROP TABLE IF EXISTS mentors")
cursor.execute("""
CREATE TABLE mentors (
    mentor_id INTEGER PRIMARY KEY,
    mentor_name TEXT,
    track TEXT
)
""")
cursor.executemany("""
INSERT INTO mentors VALUES (?, ?, ?)
""", [
    (101, 'Dr. Sharma', 'Data Science'),
    (102, 'Mr. Iyer', 'Cybersecurity'),
    (103, 'Ms. Kapoor', 'Blockchain')
])
conn.commit()
join_query = """
SELECT interns.name AS intern_name,
       interns.track,
       mentors.mentor_name
FROM interns
INNER JOIN mentors
ON interns.track = mentors.track
"""
df = pd.read_sql_query(join_query, conn)

print("Interns with their Mentors:\n")
print(df)

conn.close()