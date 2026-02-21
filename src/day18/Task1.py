import sqlite3

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
cursor.execute("INSERT INTO interns VALUES (1, 'Amit', 'Data Science', 15000)")
cursor.execute("INSERT INTO interns VALUES (2, 'Sneha', 'Cybersecurity', 8000)")
cursor.execute("INSERT INTO interns VALUES (3, 'Rahul', 'Data Science', 4000)")
cursor.execute("INSERT INTO interns VALUES (4, 'Priya', 'Blockchain', 10000)")
cursor.execute("INSERT INTO interns VALUES (5, 'Arjun', 'Data Science', 7000)")
cursor.execute("INSERT INTO interns VALUES (6, 'Meera', 'Cybersecurity', 6000)")

conn.commit()

print("Data Science interns with stipend > 5000:\n")

for row in cursor.execute("""
SELECT * FROM interns
WHERE track = 'Data Science'
AND stipend > 5000
"""):
    print(row)

print("\nAverage stipend by track:\n")

for row in cursor.execute("""
SELECT track, AVG(stipend)
FROM interns
GROUP BY track
"""):
    print(row)

print("\nTotal interns by track:\n")

for row in cursor.execute("""
SELECT track, COUNT(*)
FROM interns
GROUP BY track
"""):
    print(row)

conn.close()