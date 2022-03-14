import requests
import json
import os.path

class weathercall:
    
    url = 'https://community-open-weather-map.p.rapidapi.com/weather'

    querystring = {"q":"Leer,de","lat":"0","lon":"0","id":"2172797","lang":"de","units":"metric", "mode": "json"}

    headers ={
        'x-rapidapi-host': 'community-open-weather-map.p.rapidapi.com',
        'x-rapidapi-key': '72109e8162msh24c22aa9b2420a6p110363jsn93742e6d1779'
        }
    
    response = requests.request("GET", url, headers=headers, params=querystring)

    if (os.path.exists('testdata.json')):
        os.remove('testdata.json')  
    
    with open('testdata.json', 'w') as file:
        file.write(response.text) 

    file = open('testdata.json', 'r')
    file_load = json.load(file)

    def getWeatherDesc(self):
        weather = weathercall.file_load['weather'][0]['description']
        return weather