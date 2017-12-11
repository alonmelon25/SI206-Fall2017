import calendar
import collections
import itertools
import json
import plotly
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
	request_data = requests.get(url).text
	data = json.loads(request_data)['data']
	user_id = posts[0]['user']['id']

	if user in CACHE_DICTION: #If the user is in CACHE_DICTION, run if loop. If not, runs the else loop.
		print("Using cached data...")
		instagram_results = CACHE_DICTION[user]
	else:
		print("Fetching data...")
		instagram_results = requests.get(url, params = unique_identifier)
		CACHE_DICTION[user] = instagram_results.text
		dumped_json_cache = json.dumps(CACHE_DICTION)
		f = open(CACHE_FNAME, 'w')
		f.write(dumped_json_cache)
		f.close()  #Close the open file
	return instagram_results

	# 	# lst = []
	# 	# for posts in data:
	# 	# 	time = dt.fromtimestamp(int(posts['time']))
	# 	# 	day_of_week = calendar.day[time.day_of_week()]
	# 	# 	lst.append((posts['user']['id'], posts['likes']['count'], day_of_week))
    #
	# try:
	# 	CACHE_DICTION[user_id] = json.dumps(lst)
	# 	dumped_json_cache = json.dumps(CACHE_DICTION)
	# 	f = open(CACHE_FNAME, 'w')
	# 	f.write(dumped_json_cache)
	# 	f.close()  #Close the open file
	# 	return CACHE_DICTION[user_id]
	# except:
	# 	print("Wasn't in cache")
	# 	return None

# Organize data by day of week
def weekly_interactions(data):
    user_id = data[0][0]
    day = {"Sunday": {"Posts": 0, "Likes": 0}, "Monday": {"Posts": 0, "Likes": 0},
	"Tuesday": {"Posts": 0, "Likes": 0}, "Wednesday": {"Posts": 0, "Likes": 0},
	"Thursday": {"Posts": 0, "Likes": 0}, "Friday": {"Posts": 0, "Likes": 0},
	"Saturday": {"Posts": 0, "Likes": 0}}

    for posts in data:
		if posts[2] == "Sunday":
            day["Sunday"]['Posts'] += 1
            day["Sunday"]['Likes'] += posts[1]
		elif posts[2] == "Monday":
            day["Monday"]['Posts'] += 1
            day["Monday"]['Likes'] += posts[1]
        elif posts[2] == "Tuesday":
            day["Tuesday"]['Posts'] += 1
            day["Tuesday"]['Likes'] += posts[1]
        elif posts[2] == "Wednesday":
            day["Wednesday"]['Posts'] += 1
            day["Wednesday"]['Likes'] += posts[1]
        elif posts[2] == "Thursday":
            day["Thursday"]['Posts'] += 1
            day["Thursday"]['Likes'] += posts[1]
        elif posts[2] == "Friday":
            day["Friday"]['Posts'] += 1
            day["Friday"]['Likes'] += posts[1]
        else:
            day["Saturday"]['Posts'] += 1
            day["Saturday"]['Likes'] += posts[1]


	lst = {}
    for i in day:
        if day[i]['posts'] != 0:
            lst[i] = (day[i]['likes'] / day[i]['posts'])
        else:
            lst[i] = day[i]['likes']
    lst["User ID"] = int(user_id)
    return lst

def get_user_id(list_of_data):
    return list_of_data[0][0]

user_id = get_user_id(get_data(user))

# Create database and loading data into database
conn = sqlite3.connect('instagram.sqlite')
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS Likes")
cur.execute("""CREATE TABLE Likes (user_id TEXT, Sunday INTEGER, Monday INTEGER, Tuesday INTEGER,
                    Wednesday INTEGER, Thursday INTEGER, Friday INTEGER, Saturday INTEGER)""")
tup = (weekly_data["User ID"], weekly_data['Monday'], weekly_data['Tuesday'], weekly_data['Wednesday'], weekly_data['Thursday'], weekly_data['Friday'], weekly_data['Saturday'], weekly_data['Sunday'])
cur.execute('INSERT OR IGNORE INTO Likes (user_id, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday) VALUES (?,?,?,?,?,?,?,?)', tup)

conn.commit()
cur.close()

# def sql_to_csv(sql_filename, csv_filename):
#     conn = sqlite3.connect(sql_filename)
#     cur = conn.cursor()
#     cur.execute('SELECT * FROM Insta_AvgLikes')
#
#     row = cur.fetchall()
#     with open(csv_filename, 'w', newline='') as fp:
#         data = csv.writer(fp, delimiter=',')
#         data.writerows(row)
#
#     cur.close()
