import mysql.connector
from datetime import datetime
import json
import os

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

json_obj = {}
json_obj['temperatures'] = []
data = []

counter = 0;
for x in result:
    date = str(x[0])
    temp = str(x[1])

    item = {}
    item[counter] ={'date': date, 'temp': temp}
    data.append(item)

    counter += 1
    

print(data)

if (os.path.exists('json/temperatures.json')):
    os.remove('json/temperatures.json')

with open('json/temperatures.json', 'w') as jsonfile:
    json.dump(data, jsonfile)