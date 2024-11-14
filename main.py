import sqlite3
import datetime
import os

conn = sqlite3.connect('database.db')

cursor = conn.cursor()

# res = cursor.execute("CREATE TABLE lol (teammember_ID, name, hourly_wage, opening_closing, fulltime_parttime, hire_date)")

# res = cursor.execute("""INSERT INTO Primary_database VALUES (514926, "John Doe", 16.50, 0, 0, 2019)""")

res = cursor.execute('SELECT * FROM Primary_database')
# conn.commit()
# print(res)
print(res.fetchone())

# print(rows)

# conn.close()