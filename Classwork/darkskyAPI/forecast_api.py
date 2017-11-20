import requests
import json
from datetime import datetime as dt

base_url = 'https://api.darksky.net/forecast/'
api_key = 'fc81cbec4d2940e71ab13cf15e4d50ef'
lat_lng = '42.280841, -83.738115'
full_url = base_url + api_key + '/' + lat_lng

response = requests.get(full_url)
data = json.loads(response.text)
hourly = data['hourly']['data']
print(json.dumps(hourly, indent=4))
print(data.keys())

for hour in hourly:
    time = dt.fromtimestamp(hour['time'])
    summary = hour['summary']
    temp = hour['temperature']
    # table_data
    # for row in table_data:
    print("Time: {}".format(time) + "\t" + "Summary: {:30} Temperature: {:10}".format(summary, temp))
