import mysql.connector
from datetime import datetime

connect = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="rasppi_test"
)

cursor = connect.cursor()

cursor.execute("SELECT days.datetime AS datetime, temperatures.temp AS temp FROM days INNER JOIN temperatures ON days.ID = temperatures.ID")

result = cursor.fetchall()
for x in result:
    print(x)