#! C:\Users\Luca\AppData\Local\Programs\Python\Python310\python.exe
#! C:\Users\Milch\AppData\Local\Programs\Python\Python310\python.exe
# -*- coding: UTF-8 -*-

#enable debugging
import cgitb
cgitb.enable()

print('Content-type: text/html\r\n')
from myclass import myclass
# change the top most comment to current local python directory
from api.weathercall import weathercall

#region initiate/instantiate
p1 = myclass()
wetter = weathercall()
#endregion

print ('<!DOCTYPE HTML>')
print ('<html>\n')

print ('<head>')
print ('<title>Raspberry Wetterstation</title>')
print ('<link rel="stylesheet" href="../css/style.css" type="text/css">')
print ('<script src="../js/themeSwitcher.js"></script>')
print ('</head>')

print ('<body id="body" class="light-mode body">\n')

print ('<div class="header space-x justify-between">')
print ('<p>Wetterstation</p>')
print ('<button class="button" onclick="handleSwitchDarkLight()">DayNight</button>')
print ('</div name="header">')

print ('<div class="mainview">')
print ('<h1>Testing</h1>')

wetterbeschreibung = wetter.getWeatherDesc()
print("<h1>" + wetterbeschreibung + "</h1>")
print("<h1> Test ")

print('<h3>' + str(p1.x) + '</h3>')

print('</div>')

print ('</body>')
print ('<script>')
print ('window.onload = checkForCookies()')
print ('</script>')
print ('</html>')