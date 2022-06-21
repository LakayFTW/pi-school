import mysql.connector
from datetime import datetime

connect = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="rasppi_test"
)

cursor = connect.cursor()

cursor.execute("SELECT days.datetime, temperatures.temp FROM days INNER JOIN temperatures ON days.ID = temperatures.ID")

result = cursor.fetchall()
print("Row Count: ", len(result))
for x in result:
    print(x[0])
    print(x[1])