#! C:\Users\Milch\AppData\Local\Programs\Python\Python310\python.exe
#! C:\Users\Luca\AppData\Local\Programs\Python\Python310\python.exe
# -*- coding: UTF-8 -*-

#enable debugging
import cgitb
cgitb.enable()

print('Content-type: text/html\r\n')
from myclass import myclass
# change the top most comment to current local python directory
from API.weathercall import weathercall

#region Header
print ('<!DOCTYPE HTML>')
print ('<html>\n')

print ('<head>')
print ('<title>Test</title>')
print ('<link rel="stylesheet" href="/css/style.css" type="text/css">')
print ('</head>')
#endregion

print ('<body>\n')

print ('<h1>Testing</h1>')

#region python code goes brrrr

p1 = myclass()
wetter = weathercall()
wetterbeschreibung = wetter.getWeatherDesc()
print("<h1>" + wetterbeschreibung + "</h1>")

print('<h3>' + str(p1.x) + '</h3>')

#endregion

print ('</body>')
print ('</html>')