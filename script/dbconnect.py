import sqlite3
import mysql.connector

conn = mysql.connector.connect(user="root", password="", host="localhost")

cursor = conn.cursor()

cursor.execute("SELECT * from lehrgang")
data = cursor.fetchone()
print(data)

conn.close();
