import sqlite3

conn = sqlite3.connect('studentss.db')
print("Opened database successfully")

conn.execute('CREATE TABLE customers (email VARCHAR, password VARCHAR)')
print("Table created successfully")
conn.close()