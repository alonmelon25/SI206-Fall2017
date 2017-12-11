import requests
import json
from datetime import datetime as dt

base_url = 'https://api.darksky.net/forecast/'
api_key = 'fc81cbec4d2940e71ab13cf15e4d50ef'
lat_lng = '42.280841, -83.738115'
full_url = base_url + api_key + '/' + lat_lng

response = requests.get(full_url)
data = json.loads(response.text)
daily = data['daily']['data']
print(json.dumps(daily, indent=4))
print(data.keys())

for day in daily:
    time = dt.fromtimestamp(day['time'])
    summary = day['summary']
    high_temp = day['temperatureHigh']
    low_temp = day['temperatureLow']
    print("Time: {}".format(time) + "\t" + "Summary: {:60} Highest Temperature: {:10} Lowest Temperature: {:10}".format(summary, high_temp, low_temp))
