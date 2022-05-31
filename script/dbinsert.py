import mysql.connector
from datetime import datetime

connect = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="rasppi_test"
)

cursor = connect.cursor()
now = datetime.now()

temp = 20.0
print(now)

cursor.execute("INSERT INTO days (datetime) VALUES (%s)" , [now])
cursor.execute("INSERT INTO temperatures (temp) VALUES (%s)" , [temp])

connect.commit()

print(cursor.rowcount, "record inserted")