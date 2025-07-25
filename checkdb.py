import sqlite3

conn = sqlite3.connect("excel_data.db")
cursor = conn.cursor()


cursor.execute("select * from mytable")
rows = cursor.fetchall()

for row in rows:
  print(row)