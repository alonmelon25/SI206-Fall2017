import datetime
import json
import plotly
import random
import requests
import sqlite3
import unittest

from datetime import datetime as dt
from instagram.client import InstagramAPI

# Set up Instagram access token
instagram_access_token = "59b747372459455b832178eeda37a1f9"

# Set up the caching pattern start -- the dictionary and the try/except statement.
CACHE_FNAME = "instagram_cache.json"  #Create json file

try:
	cache_file = open("cache_fname", 'r')  #Read file
	cache_contents = cache_file.read()
	CACHE_DICTION = json.loads(cache_contents)  #Add to dictionary
	cache_file.close()  #Close file
except:
	CACHE_DICTION = {}

# Function to get data
def get_instagram_data(user):
	unique_identifier = {"access_token": instagram_access_token}
	url = 'https://api.instagram.com/v1/users/self/media/recent/?access_token={}'.format(instagram_access_token)

	if user in CACHE_DICTION: #If the user is in CACHE_DICTION, run if loop. If not, runs the else loop.
		print("Using cached data...")
		instagram_results = CACHE_DICTION[user]
	else:
		print("Fetching data...")
		results = requests.get(url, params = unique_identifier)
		CACHE_DICTION[user] = json.loads(results.text)
		instagram_results = CACHE_DICTION[user]
		dumped_json_cache = json.dumps(CACHE_DICTION)
		f = open(CACHE_FNAME, 'w')
		f.write(dumped_json_cache)
		f.close()  #Close the open file
	return instagram_results

# Invocation
instagram_json = get_instagram_data("alonmelon25")

data = instagram_json['data']
info = []

# Connect database and load data into database
conn = sqlite3.connect('instagram.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Instagram')
cur.execute('CREATE TABLE Instagram (post VARCHAR, created_time DATETIME)')
for i in data:
    tup = (post['user']['full_name'], str(dt.strptime(i['created_time'][:-5], '%Y-%m-%dT%H:%M:%S')))
    info.append(dt.strptime(i['created_time'][:-5], '%Y-%m-%dT%H:%M:%S'))
    cur.execute('INSERT OR IGNORE INTO Instagram (post, created_time) VALUES (?, ?)', tup)

conn.commit()

# Create plotly graph
# Create empty lists for the days of the week
sun = []
mon = []
tue = []
wed = []
thu = []
fri = []
sat = []

for i in info:
    day_of_week = dt.date(i).weekday()

# Separating days of week
    if day_of_week == 0:
        sun.append(day_of_week)
    elif day_of_week == 1:
        mon.append(day_of_week)
    elif day_of_week == 2:
        tue.append(day_of_week)
    elif day_of_week == 3:
        wed.append(day_of_week)
    elif day_of_week == 4:
        thu.append(day_of_week)
    elif day_of_week == 5:
        fri.append(day_of_week)
    else:
        sat.append(day_of_week)

# Plotly API
plotly.tools.set_credentials_file(username = 'alonmelon25', api_key = 'PmSfJAhSMgo0KNMV7mWU')
plotly.tools.set_config_file(world_readable = True)

# Plot data for Darksky
instagram_info = [plotly.graph_objs.Bar(x=['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'],
y = [len(sun), len(mon), len(tue), len(wed), len(thu), len(fri), len(sat)])]
plotly.plotly.iplot(instagram_info, filename = 'Instagram Interactions')
